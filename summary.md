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
{% for item in failed %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. | {{ item.ninputs }} | {{ item.nfail }} | {{ item.nfailm }} |
{% endfor %}

__List of eggs with preprint reference__

There are {{ preprint.size }} eggs with preprint reference (arXiv, bioRxiv, Research Square, medRxiv, or ChemRxiv).

{:#browse-table2 .display}
| plumID | Name | Contributor |
| :------: |  :------:  |  :------: |
{% for item in preprint %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. |
{% endfor %}

__List of eggs without reference paper__

There are {{ missing.size }} eggs without reference paper, marked as unpublished or submitted.

{:#browse-table3 .display}
| plumID | Name | Contributor |
| :------: |  :------:  |  :------: |
{% for item in missing %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.contributor | split: " " | last}} {{ item.contributor | split: " " | first | slice: 0}}. |
{% endfor %}

__Action Usage Chart__

{% assign actionlist = site.data.actioncount0 | map: "name" %}
{% assign actionno = site.data.actioncount0 | map: "number" %}
{% assign actionno1 = site.data.actioncount1 | map: "number" %}
{% assign actionno2 = site.data.actioncount2 | map: "number" %}
{% assign actionno3 = site.data.actioncount3 | map: "number" %}
{% assign actionno4 = site.data.actioncount4 | map: "number" %}
{% assign actionno5 = site.data.actioncount5 | map: "number" %}
{% assign actionno6 = site.data.actioncount6 | map: "number" %}
{% assign actionno7 = site.data.actioncount7 | map: "number" %}
{% assign actionno8 = site.data.actioncount8 | map: "number" %}
{% assign actionno9 = site.data.actioncount9 | map: "number" %}
{% assign nactions=actionno.size %}

{% assign astr="" %}
{% assign ano=actionno[0] | plus: actionno1[i] %}
{% assign astr=astr | append: ano %}
{% for i in (1..nactions) %}
   {% assign ano=actionno[i] | plus: actionno1[i] | plus: actionno2[i] | plus: actionno3[i] | plus: actionno4[i] | plus: actionno5[i] | plus: actionno6[i] | plus: actionno7[i] | plus: actionno8[i] | plus: actionno9[i] %}
   {% assign astr=astr | append: ", " | append: ano %}
{% endfor %}

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
var yValues = [ {{ astr }} ];
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
