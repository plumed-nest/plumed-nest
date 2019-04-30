The PLUMED consortium
-----------------------------
The PLUMED consortium is an open community composed of current and past PLUMED developers, contributors, 
and all those researchers whose work builds in part on PLUMED and at the same time drives 
the development and dissemination of PLUMED.
The mission of the consortium is to transform the way researchers communicate the 
protocols that are used in their MD simulations, in order to maximize the impact of 
new research and promote the highest possible standards of scientific reproducibility. 

More information about the PLUMED consortium can be found here:

The PLUMED consortium.
The PLUMED consortium: A community effort to promote openness, transparency and reproducibility in molecular simulations, Submitted

The coordinators of the PLUMED consortium are:

* [Max Bonomi](https://research.pasteur.fr/en/member/massimiliano-bonomi/) (Institut Pasteur - CNRS, France) 
* [Giovanni Bussi](http://people.sissa.it/%7Ebussi) (International School for Advanced Studies, Italy)
* [Carlo Camilloni](http://sites.unimi.it/camilloni) (University of Milan, Italy)
* [Gareth Tribello](http://titus.phy.qub.ac.uk/members/gareth/) (Queen's University Belfast, UK)

Currently, the consortium includes {{ site.data.members | size }} members
from {{ site.data.members | group_by:"affiliation" | size }} different institutions and
{{ site.data.members | group_by:"country" | size }} different countries, listed below:
{% for item in site.data.members %}
* {{ item.name }}, {{ item.affiliation }}, {{ item.city }}, {{ item.country }}{% endfor %}
