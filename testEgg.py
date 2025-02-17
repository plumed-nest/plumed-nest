# this is using ruff==0.6.2 to check that the code won't explode badly
# pip install ruff==0.6.2
# ruff format testEgg.py
# ruff check testEgg.py


DEFAULT_PLUMED = "plumed"


class InvalidJSONError(Exception):
    """Raised when a json is not loaded correctly."""

    pass


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog="testEgg",
        description="""
Test the correctness, if the egg can be compiled on the nest.

%(prog)s needs plumed installed and runnable to work.

%(prog)s will check only if the egg can be compiled and could pass the GitHub workflow.
Note that %(prog)s will not find any rendering error due to wrong Markdown or HTML syntax.
""",
    )
    parser.add_argument(
        "eggPath",
        help="The path to the nest.yml file to test or to the directory containing it",
    )
    args = parser.parse_args()

    from nest import process_egg

    import subprocess
    import json

    eggPath = args.eggPath
    plumed_to_use = DEFAULT_PLUMED
    cmd = [plumed_to_use, "info", "--root"]
    plumed_info = subprocess.run(cmd, capture_output=True, text=True)
    keyfile = plumed_info.stdout.strip() + "/json/syntax.json"

    with open(keyfile) as f:
        try:
            plumed_syntax = json.load(f)
        except ValueError as ve:
            raise InvalidJSONError(ve)

    action_counts = {}
    plumed_version = (
        subprocess.check_output("plumed info --version", shell=True)
        .decode("utf-8")
        .strip()
    )
    for key in plumed_syntax:
        if key == "vimlink" or key == "replicalink" or key == "groups":
            continue
        action_counts[key] = 0
    if "nest.yml" in eggPath:
        eggPath = eggPath.replace("nest.yml", "")

    print("checking the egg: " + eggPath)
    print("plumed version:   " + plumed_version)
    print("plumed root:      " + plumed_info.stdout.strip())
    print("all the files will be stored in the egg directory\n")

    process_egg(eggPath, action_counts, plumed_syntax, plumeds=[plumed_to_use])
