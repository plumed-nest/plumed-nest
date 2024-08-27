Browse the eggs in PLUMED-NEST
-----------------------------
PLUMED-NEST provides all the data needed to reproduce the results of a PLUMED-enhanced molecular dynamics simulation or analysis contained in a published paper. Furthermore, PLUMED-NEST monitors the compatibility of the provided PLUMED input files with the current and development versions of the code and integrates links from these files to the PLUMED manual.
  
Here is the list of projects already deposited in PLUMED-NEST, while a complete bibliography can be found [here](bibliography.md).
<!---
If you are a contributor, you can check if your eggs are still compatible with the current and master PLUMED versions [here](summary.md).
-->

{:#browse-table .display}
| plumID | Name | Category | Keywords | Contributor | Actions | Modules |
|:--------:|:--------:|:---------:|:---------:|:---------:|:---------:|:---------:|
{% for item in site.data.eggs %}| [{{ item.id }}]({{ item.path }}) | {{ item.name }} | {{ item.category }} | {{ item.keywords }} | {{ item.contributor }} | {{ item.actions }} | {{ item.modules }} |
{% endfor %}

<script>
$(document).ready(function() {
var table = $('#browse-table').DataTable({
  "dom": '<"search"f><"top"il>rt<"bottom"Bp><"clear">',
  language: { search: '', searchPlaceholder: "Search project..." },
  buttons: [
        'copy', 'excel', 'pdf'
  ],
  "columnDefs": [ 
     { "targets": 5, "visible": false },
     { "targets": 6, "visible": false }
  ],
  "order": [[ 0, "desc" ]]
  });
$('#browse-table-searchbar').keyup(function () {
  table.search( this.value ).draw();
  });
  hu = window.location.search.substring(1);
  searchfor = hu.split("=");
  if( searchfor[0]=="search" ) {
      table.search( searchfor[1] ).draw();
  }
});
</script>
