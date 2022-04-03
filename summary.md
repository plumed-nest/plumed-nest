Eggs overview
-----------------------------

{% assign ninp   = 0 %}
{% assign nfail  = 0 %}
{% assign nfailm = 0 %}
{% assign failed = ''  | split: ',' %}
{% assign missing = '' | split: ',' %}
{% assign date = "now" | date: "%Y-%m-%d %H:%M" %}

{% for item in site.data.eggs %}
   {% assign ninp   = ninp   | plus: item.ninputs %}
   {% assign nfail  = nfail  | plus: item.nfail %}
   {% assign nfailm = nfailm | plus: item.nfailm %}
   {% if item.nfail > 0 or item.nfailm > 0 %}
     {% assign failed = failed | push: item %}
   {% endif %}
   {% if item.doi == "" or item.doi == "unpublished" or item.reference == "unpublished" %}
     {% assign missing = missing | push: item %}
   {% endif %}
{% endfor %}

Total number of eggs and PLUMED input files deposited in PLUMED-NEST, along with number of failed tests
with current ({{ site.data.plumed.stable }}) and master PLUMED versions.

|   Date   |  # eggs | # inputs | ![current](https://img.shields.io/badge/current-failed-red.svg) | ![master](https://img.shields.io/badge/master-failed-red.svg) |
| :------: |  :------:  |  :------:  | :------:  | :------:  |
|  {{ date }} | {{ site.data.eggs.size }} | {{ ninp }} | {{ nfail }} | {{ nfailm }} |


__List of eggs with failed tests__

There are {{ failed.size }} eggs with failing tests.

{:#browse-table .display}
| plumID | Name | Contributor | # inputs | # current | # master |
| :------: |  :------:  |  :------: | :------: | :------:  | :------: |
{% for item in failed %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. | {{ item.ninputs }} | {{ item.nfail }} | {{ item.nfailm }} |
{% endfor %}

__List of eggs with missing reference paper__

There are {{ missing.size }} eggs with missing reference paper.

{:#browse-table2 .display}
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
   
<script>
$(document).ready(function() {
var table = $('#browse-table2').DataTable({
  "dom": '<"search"f><"top"il>rt<"bottom"Bp><"clear">',
  language: { search: '', searchPlaceholder: "Search project..." },
  buttons: [
        'copy', 'excel', 'pdf'
  ],
  "order": [[ 0, "desc" ]]
  });
$('#browse-table2-searchbar').keyup(function () {
  table.search( this.value ).draw();
  });
});
</script>
