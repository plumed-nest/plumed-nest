[![Homepage](https://img.shields.io/badge/Home-plumed--nest.org-green.svg)](http://www.plumed-nest.org)
[![CI](https://github.com/plumed-nest/plumed-nest/actions/workflows/main.yml/badge.svg)](https://github.com/plumed-nest/plumed-nest/actions/workflows/main.yml)


# PLUMED-NEST
This repository contains all the sources and scripts required to build the website located at www.plumed-nest.org.

Documentation is still partial and will be improved. Meanwhile, you can find some note here.

Each "project" uploaded through the [web form](https://www.plumed-nest.org/contribute.html) will result is a single directory
in this repository, with a name corresponding to the ID associated to the project. Each ID is a unique progressive number. Each directory contains a single `nest.yml` file with some metadata. The reason why we use a full directory per project, rather than a single file, is that in the future we might add the possibility to upload small additional files related to your project on this repository. However, the bulk of your material is expected to be located elsewhere. This data is routinely analyzed by a script that runs on [GitHub Actions](https://github.com/plumed-nest/plumed-nest/actions/workflows/main.yml) and that builds the real website.

The most important information is the URL of the zip file containing your material. This zip file is **not hosted on the PLUMED-NEST**. It could be included as a Supporting Material of a paper, it could be on a service such as [materials cloud](https://www.materialscloud.org/), on [arXiv](https://arxiv.org/), etc. In case you want to move your zip file elsewhere, you should modify the URL stored in the `nest.yml` file (or ask the maintainers to do it for you) so that at the next round the script will be able to find your data again. We currently only support zip files, but it would be easy to add more formats. Please open an issue if you would like us to do so!

In principle, we would like to be able to detect as many information as possible automatically from the content of zip file. However, for some information we need to rely on the contributors filling the proper fields in the web form, or providing a yml file with the relevant data.

You might want to have a look at the nest.py script in this repository, which does all the processing. If you look in the [issues](https://github.com/plumed-nest/plumed-nest/issues) tab of this repository, you will find comments on the current limitations and features that we plan to implement in the future.

**Contributions to this repository, both as new projects and as improvements to our analysis scripts are welcome! Please open a new [issue](https://github.com/plumed-nest/plumed-nest/issues/new) or [pull request](https://github.com/plumed-nest/plumed-nest/compare) if you have comments or ideas to share.**

## Adding data to the PLUMED-NEST site using a pull request

If you would prefer to submit your data to the PLUMED nest using a pull request on GitHub you can.  Please follow the instructions below:

* Make a fork of this repository and clone it to your local machine.
* Collect the files you used in your calculations.  Please test the validity of the PLUMED input files you are submitting before you upload.  The tests that are run by the nest use the command `plumed driver --natoms 100000 --parse-only --kt 2.49 --plumed plumed.dat`
* Create and upload a zip file containing all your inputs.  Info about where to host your zip file can be found [here](https://github.com/plumed-nest/plumed-nest/blob/master/README.md#zip-info).
* Create the yml file that containing the information on your submission by following the instructions in the next but one section. 
* Test the yml you have written using an [online tester](http://www.yamllint.com).
* Push your changes to your fork and setup the pull request on the upstream branch using GitHub.

Do not worry about following the instructions in the section immediately after this one about testing the appearance of your page before setting up the pull request.  This is only possible if you are working on the plumed-nest/plumed-nest repository directly.  When working on your fork you can work on the master branch of your fork directly.   Tests on the setup of the site will be done automatically when you setup the pull request.  You can check the appearance of your pages once the pull request is merged. 

## Testing the appearance of the PLUMED-NEST site

If you push a commit on branch `test`, the result will appear on www.plumed-nest.org/test-site. Use this to double check changes to the layout before committing to master branch. Feel free to force push this branch (with `git push -f origin yourbranch:test`), this branch is just used for testing.

If the nest pages appear to be taking a long time to update you can check the progress of your build by looking at the [GitHub Actions page](https://github.com/plumed-nest/plumed-nest/actions/workflows/main.yml) and the progress of the [upload](https://github.com/plumed-nest/test-site/commits/master).

## Instructions for filling the yml file

The yml file should contain a number of fields. Please use existing yml files as a template and report if you think the documentation below is outdated.  Also note that you can test that your file contains valid yml using online testers such as [this one](http://www.yamllint.com)

### Compulsory fields

**url**: URL to a zip file with your material
````
url: http://path.to/file.zip
````

**pname**: Short name for your project
````
pname: ALA2
````

**category**: Main category for your project
````
category: methods
````

**keyw**: Keywords for your project.
````
keyw: metadynamics, RNA
````

**contributor**: Name of the contributor
````
contributor: Ludwig Boltzmann
````
Make sure to provide it as `Name Surname` because it will be abbreviated as `Surname N.` in the summary table.

**doi**: DOI to the related publication. If not available, write either `unpublished` or `submitted`
````
doi: 10.1038/nphys1170
````
The DOI will be used to retrieve the full citation to the paper.

**history**: This field should be either a list of pairs including date and message:
````
history:
  - [2019-04-20,"Changed something"]
  - [2019-04-22,"Changed something else"]
````
or a dictionary of messages using dates as keys:
````
history:
  2019-04-20: Changed something
  2019-04-22: Changed something else
````
The former syntax is more redundant but is the only one that would allow having more than one change on the same date.

### Optional fields

**md5**: The MD5 checksum of your zip file. In case the md5 sum of the downloaded zip files does not match this one, the build will fail. The checksum can be obtained a priori using the command line tool `md5`, or it can be seen in the GitHub actions log upon failures. Example
````
url: https://github.com/srnas/shape-md/archive/476e47196772e5dc109018bc4c2447c5dc234381.zip
# optional checksum to avoid stealth updates
md5: 12877107e2d86627750c4461eae5ac38
````
This field might become compulsory in the future in order to allow for reproducible builds.


**instructions**: A string containing instructions about your project. This could be long, so it is recommended to split it on multiple lines
````
instructions: >
  This is a long text.
  Can be split in multiple lines using YAML rules.
````

**natoms**: This field can be used to specify how many atoms plumed should think you are using when running tests.
````
natoms: 200000
````
If not provided, we assume there are 100000 atoms (should accomodate most cases).

**nreplicas**: In case your input require multiple replicas in order to run, specify the number of replicas needed.
````
nreplicas: 4
````
Avoid using too many replicas since this could slow down things! Often two replicas are sufficient to check the syntax of your input.

**plumed_version**: The plumed version originally used to produce this work. It is used to decide the color of the badge associated to each run. In particular, when indicating a version name that ends with `-mod` (e.g. `v2.5-mod`) the badges will appear as yellow irrespectively of the result, to indicate that the user should install a modified version of PLUMED in order to reproduce the results.

**plumed_input**: This field should contain a list of input files that will be tested. If this field is not provided, we will use some heuristic to find our which are the correct input files. For instance:
````
plumed_input:
  - dir1/plumed.dat
  - dir2/test.dat
````
For each input file you can also specify some instructions related to how this input should be executed. In this case, the input should be a dictionary. The value with key `path` will correspond to the path of the file:
````
plumed_input:
  - dir1/plumed.dat
  - path: dir2/test.dat
    natoms: 200000
    nreplicas: 2
````
Notice that the first input could have been equivalently indicated with
````
plumed_input:
  - path: dir1/plumed.dat
````

The global keys that you can override at single input level are `natoms`, `nreplicas`, and `plumed_version`.

**acknowledgement**: This field can be used to add acknowledgements to funding connected to the data deposited in the nest.

<a name="zip-info"></a>
## Where should the zip files be hosted 

We have no preference on the place where the zip files will be hosted. The crucial points are:
* they should be accessible with an URL, so that while we generate the webpages we will be able to download them;
* the PLUMED input files are not contained in a tar or zip file within the main zip file. 

Existing projects can be used for inspiration. Below are some possibilities. Notice that Dropbox or Google Driver links seem difficult to manage since the URLs do not refer to the zip file but rather to an intermediate html file.

**Zenodo**: [Zenodo](https://zenodo.org) stores archives in CERN’s Data Centre. Every upload is assigned a Digital Object Identifier (DOI), to make them citable and trackable. Uploads are made available online as soon as you hit publish, and your DOI is registered within seconds. Datasets can be updated using a versioning feature. We have created a PLUMED consortium community on Zenodo. We invite contributors to use the *New upload* button on [this page](https://zenodo.org/communities/plumed-consortium/) to make sure that their upload appears in this community.

**GitHub**: [GitHub](http://github.com) provides convenient space to archive your data for free if they are open source. Notice that GitHub is designed for source code rather than for binary files, so it is expected to work well only if you upload small files. You would typically have two ways to use GitHub to store your zip files:
1. Generate the zip files on your computer and then upload them to a designated GitHub repository. The zip file will then be reachable at an URL such as `https://github.com/USER/REPOSITORY/raw/TAG/DIR/FILE.zip`. The advantage of this approach is that it allows you to use a single repository for all your projects (of course, only if the data files are small enough to fit).
2. Use a whole repository for each project. In this case, GitHub can generate the zip for you at an URL such as `https://github.com/USER/PROJECT/archive/TAG.zip`. The advantage of this approach is that it will make your files directly browseable from GitHub (at `https://github.com/USER/PROJECT`).

In both these cases, `TAG` represents the git snapshot corresponding to your file. If you use `master` for instance, we will always download the latest version of your file (this however has the drawback of making the build possibly not reproducible). Alternatively, you could use a specific git hash to indentify exactly the version of your file.

**MaterialsCloud**: [MaterialsCloud](https://www.materialscloud.org) allows users to upload files in their [archive](https://archive.materialscloud.org/). Files are guaranteed to be retained for 10 years and are accessible with an URL.
There are a number of fields that you should fill in order to upload our files on MaterialsCloud. However, notice that there is a significant overlap between what is requested when uploading information on PLUMED-NEST and on MaterialsCloud. Moreover, this would be a very convenient path if you want to simultaneously exploit the analysis capabilities of MaterialsCloud and of PLUMED-NEST.

**ArXiv**: [ArXiv](http://arxiv.org) allows you to include supporting information by uploading "ancillary files" in a `anc` directory. These files are accessible at an URL such as `https://arxiv.org/src/ID/anc/FILENAME.zip`. If you include a zip file there we would be able to reach it.

**Supporting Information**: Some publishers (e.g., [ACS](https://pubs.acs.org/)) allow you to upload Supporting Information that is then available free of charge. If these files are accessible at an URL (for ACS it would be something like  `https://pubs.acs.org/doi/suppl/DOI/suppl_file/FILENAME.zip`) we should be able to reach them.

**Open Science Foundation**: [Open Science Foundation](http://osf.io) (OSF) also provides long term storage for simulation files. We have no example yet on this line, but if you can point us to a zip file stored at OSF with an URL we should be able to reach it.
