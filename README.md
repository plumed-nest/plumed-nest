[![Build Status](https://travis-ci.org/plumed-nest/plumed-nest.svg?branch=master)](https://travis-ci.org/plumed-nest/plumed-nest)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/plumed-nest/plumed-nest.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/plumed-nest/plumed-nest/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/plumed-nest/plumed-nest.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/plumed-nest/plumed-nest/context:python)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/plumed-nest/plumed-nest.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/plumed-nest/plumed-nest/context:javascript)

# PLUMED-NEST
This repository contains all the sources and scripts required to build the website located at www.plumed-nest.org.

Documentation is still partial and will be improved. Meanwhile, you can find some note here.

Each "project" uploaded through the [web form](https://www.plumed-nest.org/contribute.html) will result is a single directory
in this repository, with a name corresponding to the ID associated to the project. Each ID is a unique progressive number. Each directory contains a single `nest.yml` file with some metadata. The reason why we use a full directory per project, rather than a single file, is that in the future we might add the possibility to upload small additional files related to your project on this repository. However, the bulk of your material is expected to be located elsewhere. This data is routinely analyzed by a script that runs on [Travis-CI](https://travis-ci.org/plumed-nest/plumed-nest) and that builds the real website.

The most important information is the URL of the zip file containing your material. This zip file is **not hosted on the PLUMED-NEST**. It could be included as a Supporting Material of a paper, it could be on a service such as [materials cloud](https://www.materialscloud.org/), on [arXiv](https://arxiv.org/), etc. In case you want to move your zip file elsewhere, you should modify the URL stored in the `nest.yml` file (or ask the maintainers to do it for you) so that at the next round the script will be able to find your data again. We currently only support zip files, but it would be easy to add more formats. Please open an issue if you would like us to do so!

In principle, we would like to be able to detect as many information as possible automatically from the content of zip file. However, for some information we need to rely on the contributors filling the proper fields in the web form, or providing a yml file with the relevant data.

You might want to have a look at the nest.py script in this repository, which does all the processing. If you look in the [issues](https://github.com/plumed-nest/plumed-nest/issues) tab of this repository, you will find comments on the current limitations and a features that we plan to implement in the future.

**Contributions to this repository, both as new projects and as improvements to our analysis scripts are welcome! Please open a new [issue](https://github.com/plumed-nest/plumed-nest/issues/new) or [pull request](https://github.com/plumed-nest/plumed-nest/compare) if you have comments or ideas to share.**

## Testing the appearance of the PLUMED-NEST site

If you push a commit on branch `test`, the result will appear on www.plumed-nest.org/test-site. Use this to double check changes to the layout before committing to master branch. Feel free to force push this branch (with `git push -f origin yourbranch:test`), this branch is just used for testing.

## Instructions for filling the yml file

The yml file should contain a number of fields. Please use existing yml files as a template and report if you think the documentation below is outdated.

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

**doi**: DOI to the related publication. If not available, write either `unpublished` or `submitted`
````
doi: 10.1038/nphys1170
````

**history**: This field should be either a list of pairs including date and message or a dictionary of messages using dates as keys:
````
history:
  - [2019-04-20,"Changed something"]
  - [2019-04-22,"Changed something else"]
````
or
````
history:
  2019-04-20: Changed something
  2019-04-22: Changed something else
````

### Optional fields

**md5**: The MD5 checksum of your zip file. In case the md5 sum of the downloaded zip files does not match this one, the build will fail. The checksum can be obtained a priori using the command line tool `md5`, or it can be seen in the travis log upon failures. Example
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

**plumed_version**: The plumed version originally used to produce this work. Added for documentation purpose only.

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

## Where should the zip files be hosted

We have no preference on the place where the zip files will be hosted. The only crucial point is that they should
be accessible with an URL, so that while we generate the webpages we will be able to download them. Existing projects can
be used for inspiration. Here are some possibilities.

**MaterialsCloud**: [MaterialsCloud](www.materialscloud.org) allows users to upload files in their [archive](https://archive.materialscloud.org/). Files are guaranteed to be retained for 10 years and are accessible with an URL.
There are a number of fields that you should fill in order to upload our files on MaterialsCloud. However, notice that there is a significant overlap between what is requested when uploading information on PLUMED-NEST and on MaterialsCloud. Moreover, this would be a very convenient path if you want to simultaneously exploit the analysis capabilities of MaterialsCloud and of PLUMED-NEST.

**GitHub**: [GitHub](http://github.com) provides convenient space to archive your data for free if they are open source. Notice that GitHub is designed for source code rather than for binary files, so it is expected to work well only if you upload small files. You would typically have two ways to use GitHub to store your zip files:
1. Generate the zip files on your computer and then upload them to a designated GitHub repository. The zip file will then be reachable at an URL such as `https://github.com/USER/REPOSITORY/raw/TAG/DIR/FILE.zip`. The advantage of this approach is that it allows you to use a single repository for all your projects (of course, only if the data files are small enough to fit).
2. Use a whole repository for each project. In this case, GitHub can generate the zip for you at an URL such as `https://github.com/USER/PROJECT/archive/TAG.zip`. The advantage of this approach is that it will make your files directly browseable from GitHub (at `https://github.com/USER/PROJECT`).

In both these cases, `TAG` represents the git snapshot corresponding to your file. If you use `master` for instance, we will always download the latest version of your file (this however has the drawback of making the build possibly not reproducible). Alternatively, you could use a specific git hash to indentify exactly the version of your file.

**arXiv** [ArXiv](http://arxiv.org) allows you to include supporting information by uploading "ancillary files" in a `anc` directory. These files are accessible at an URL such as `https://arxiv.org/src/ID/anc/FILENAME.zip` If you include a zip file there we would be able to reach it.
