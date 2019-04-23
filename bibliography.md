Bibliography
-----------------------------
  
Here is the complete list of the published papers connected to the projects deposited in PLUMED-NEST:

{% for item in site.data.eggs %}
  {% if item.reference != 'unpublished' and item.reference != 'submitted' and item.reference != 'DOI not found' %}
   [[plumID:{{ item.id }}]({{ item.path }})] [{{ item.reference }}](http://dx.doi.org/{{ item.doi }})
 {% endif %}
{% endfor %}
