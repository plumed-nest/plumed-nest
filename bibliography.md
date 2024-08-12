Bibliography
-----------------------------
  
Here is the complete list of the published papers connected to the eggs deposited in PLUMED-NEST:

{% assign sorted_eggs = site.data.eggs | sort: "id" | reverse %}

{% for item in sorted_eggs %}
  {% if item.reference != 'unpublished' and item.reference != 'submitted' and item.reference != 'DOI not found' %}
   [[plumID:{{ item.id }}]({{ item.path }})] [{{ item.reference }}]({{ item.ref_url }})
 {% endif %}
{% endfor %}
