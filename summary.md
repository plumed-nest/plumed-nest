Eggs overview
-----------------------------

{% assign ninp   = 0 %}
{% assign nfail  = 0 %}
{% assign nfailm = 0 %}
{% assign date = "now" | date: "%Y-%m-%d %H:%M" %}

{% for item in site.data.eggs %}
   {% assign ninp   = ninp   | plus: item.ninputs %}
   {% assign nfail  = nfail  | plus: item.nfail %}
   {% assign nfailm = nfailm | plus: item.nfailm %}
{% endfor %}

Total number of PLUMED input files deposited in PLUMED-NEST, along with number of failed tests
with current ({{ site.data.plumed.stable }}) and master PLUMED versions.

|   date   |  # inputs | ![current](https://img.shields.io/badge/current-failed-red.svg) | ![master](https://img.shields.io/badge/master-failed-red.svg) |
| :------: |  :------:  |  :------:  | :------:  |
|  {{ date }} | {{ ninp }} | {{ nfail }} | {{ nfailm }} |


__List of eggs with failed tests__

{% assign failed = '' | split: ',' %}
{% for item in site.data.eggs %}
  {% if item.nfail > 0 or item.nfailm > 0 %}
     {% assign failed = failed | push: item %}
  {% endif %}
{% endfor %}

{:#browse-table .display}
| plumID | Name | Contributor | inputs | current | master |
| :------: |  :------:  |  :------: | :------: | :------:  | :------: |
{% for item in failed %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. | {{ item.ninputs }} | {{ item.nfail }} | {{ item.nfailm }} |
{% endfor %}

__List of eggs with unpublished reference paper__

{% assign missing = '' | split: ',' %}
{% for item in site.data.eggs %}
  {% if item.doi == "" or item.doi == "unpublished" or item.reference == "unpublished" %}
     {% assign missing = missing | push: item %}
  {% endif %}
{% endfor %}

| plumID | Name | Contributor |
| :------: |  :------:  |  :------: |
{% for item in missing %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. |
{% endfor %}

<script>
$(document).ready(function() {
var table = $('#browse-table').DataTable({
  "dom": '<"search"f><"top"il>rt<"bottom"Bp><"clear">',
  language: { search: '', searchPlaceholder: "Search project..." },
  buttons: [
        'copy', 'excel', 'pdf'
  ],
  "order": [[ 0, "desc" ]]
  });
$('#browse-table-searchbar').keyup(function () {
  table.search( this.value ).draw();
  });
});
</script>
