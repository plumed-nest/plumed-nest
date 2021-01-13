How to cite PLUMED-NEST
-----------------------------
All projects deposited in PLUMED-NEST are assigned a unique ID in the format plumID:XX.YYY.
If you have deposited your data in PLUMED-NEST before submitting your paper, we invite you to add the following sentence to the manuscript:

*"All the data and PLUMED input files required to reproduce the results reported in this paper are available on PLUMED-NEST (www.plumed-nest.org), 
the public repository of the PLUMED consortium [1], as plumID:XX.YYY"*.

**Bibliography**

[1] The PLUMED consortium.
_Promoting transparency and reproducibility in enhanced molecular simulations_,
[Nat. Methods 16, 670 (2019)](https://doi.org/10.1038/s41592-019-0506-8)

Download citation:

RIS format: <a id="risc">consortium as authors</a> | <a id="ris4">Plumed four + consortium as authors</a> | <a id="risa">full list of authors</a>

BibTeX format: <a id="bibc">consortium as authors</a> | <a id="bib4">Plumed four + consortium as authors</a> | <a id="biba">full list of authors</a>

<scirpt>
const downloadToFile = (content, filename, contentType) => {
  const a = document.createElement('a');
  const file = new Blob([content], {type: contentType});
  
  a.href= URL.createObjectURL(file);
  a.download = filename;
  a.click();
  
  URL.revokeObjectURL(a.href);
};

document.querySelector('#rics').addEventListener('click', () => {
  const text = "hovno";
  
  downloadToFile(text, 'my-new-file.txt', 'text/plain');
});
</script>
