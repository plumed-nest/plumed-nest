Eggs overview
-----------------------------

{% assign ninp   = 0 %}
{% assign nfail  = 0 %}
{% assign nfailm = 0 %}
{% assign failed = ''  | split: ',' %}
{% assign missing = '' | split: ',' %}
{% assign preprint = '' | split: ',' %}
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
   {% if item.preprint > 0 %}
     {% assign preprint = preprint | push: item %}
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
{% for item in failed %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor }} | {{ item.ninputs }} | {{ item.nfail }} | {{ item.nfailm }} |
{% endfor %}

__List of eggs with preprint reference__

There are {{ preprint.size }} eggs with preprint reference (arXiv, bioRxiv, Research Square, medRxiv, or ChemRxiv).

{:#browse-table2 .display}
| plumID | Name | Contributor |
| :------: |  :------:  |  :------: |
{% for item in preprint %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor }} |
{% endfor %}

__List of eggs without reference paper__

There are {{ missing.size }} eggs without reference paper, marked as unpublished or submitted.

{:#browse-table3 .display}
| plumID | Name | Contributor |
| :------: |  :------:  |  :------: |
{% for item in missing %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor }} |
{% endfor %}

__Action Usage Chart__

{% assign actionlist = site.data.actioncount_sum | map: "name" %}
{% assign actionno = site.data.actioncount_sum | map: "number" %}

The chart below shows how many eggs make use of each of the available actions in PLUMED (it will look clearer if you resize the window).

<canvas id="myChart" style="width:100%;"></canvas>

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

<script>
$(document).ready(function() {
var table = $('#browse-table3').DataTable({
  "dom": '<"search"f><"top"il>rt<"bottom"Bp><"clear">',
  language: { search: '', searchPlaceholder: "Search project..." },
  buttons: [
        'copy', 'excel', 'pdf'
  ],
  "order": [[ 0, "desc" ]]
  });
$('#browse-table3-searchbar').keyup(function () {
  table.search( this.value ).draw();
  });
});
</script>

<script>
var xValues = [ {{ actionlist | join: '", "' | prepend: '"' | append: '"' }} ];
var yValues = [ {{ actionno   | join: ', '}} ];
// do sorting in descending order based on yValues
//1) combine the arrays:
var list = [];
for (var j = 0; j < xValues.length; j++) 
    list.push({'x': xValues[j], 'y': yValues[j]});
//2) sort:
list.sort(function(a, b) {
    return ((a.y > b.y) ? -1 : ((a.y == b.y) ? 0 : 1));
});
//3) separate them back out:
for (var k = 0; k < list.length; k++) {
    xValues[k] = list[k].x;
    yValues[k] = list[k].y;
}   
var barColors = "green";

new Chart("myChart", {
  type: "horizontalBar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    maintainAspectRatio: false,
    legend: {display: false},
    title: {
      display: true,
      text: "Number of eggs using this action"
    }
  }
});
</script>
