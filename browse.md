Browse the nest
-----------------------------
PLUMED-NEST provides all the data needed to reproduce the results of a PLUMED-enhanced molecular dynamics simulation or analysis contained in a published paper. Furthermore, PLUMED-NEST monitors the compatibility of the provided PLUMED input files with the current and development versions of the code and integrates links from these files to the PLUMED manual.
  
Here is the list of projects already deposited in PLUMED-NEST, while a complete bibliography can be found [here](bibliography.md).

{:#browse-table .display}
| plumID | Name | Category | Keywords | Contributor |
|:--------:|:--------:|:---------:|:---------:|:---------:|
{% for item in site.data.eggs %}| [{{ item.id }}]({{ item.path }}) | {{ item.shortname }} | {{ item.category }} | {{ item.shortkeywords }} | {{ item.contributor }} |
{% endfor %}

<script>
$(document).ready(function() {
var table = $('#browse-table').DataTable({
  "dom": '<"search"f><"top"il>rt<"bottom"p><"clear">',
  language: { search: '', searchPlaceholder: "Search project..." }
  });
$('#browse-table-searchbar').keyup(function () {
  table.search( this.value ).draw();
  });
});
</script>
