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
with current and master PLUMED versions.

|   date   |  # inputs | # fail current PLUMED | # fail master PLUMED |
| :------: |  :------:  |  :------:  | :------:  |
|  {{ date }} | {{ ninp }} | {{ nfail }} | {{ nfailm }} |


Table reporting eggs with failed tests.

{:#browse-table .display}
| plumID | Name | Contributor | # inputs | # fail current | # fail master |
| :------: |  :------:  |  :------: | :------: | :------:  | :------: |
{% for item in site.data.eggs %} {% if item.nfail > 0 or item.nfailm > 0 %} | [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. | {{ item.ninputs }} | {{ item.nfail }} | {{ item.nfailm }} | {% endif %} {% endfor %}

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
