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

RIS format: | <a id="risc">consortium as authors</a> | <a id="ris4">Plumed four + consortium as authors</a> | <a id="risa">full list of authors</a>
BibTeX format: | <a id="bibc">consortium as authors</a> | <a id="bib4">Plumed four + consortium as authors</a> | <a id="biba">full list of authors</a>

<script>
const downloadToFile = (content, filename, contentType) => {
const a = document.createElement('a');
const file = new Blob([content], {type: contentType});
a.href= URL.createObjectURL(file);
a.download = filename;
a.click();
URL.revokeObjectURL(a.href);
};
document.querySelector('#risc').addEventListener('click', () => {
const text = "TY  - JOUR\nAU  - The PLUMED consortium,\nPY  - 2019\nDA  - 2019/08/01\nTI  - Promoting transparency and reproducibility in enhanced molecular simulations\nJO  - Nature Methods\nSP  - 670\nEP  - 673\nVL  - 16\nIS  - 8\nAB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.\nSN  - 1548-7105\nUR  - https://doi.org/10.1038/s41592-019-0506-8\nDO  - 10.1038/s41592-019-0506-8\nID  - Bonomi2019\nER  -";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
document.querySelector('#ris4').addEventListener('click', () => {
const text = "TY  - JOUR\nAU  - Bonomi, Massimiliano\nAU  - Bussi, Giovanni\nAU  - Camilloni, Carlo\nAU  - Tribello, Gareth A.\nAU  - The PLUMED consortium,\nPY  - 2019\nDA  - 2019/08/01\nTI  - Promoting transparency and reproducibility in enhanced molecular simulations\nJO  - Nature Methods\nSP  - 670\nEP  - 673\nVL  - 16\nIS  - 8\nAB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.\nSN  - 1548-7105\nUR  - https://doi.org/10.1038/s41592-019-0506-8\nDO  - 10.1038/s41592-019-0506-8\nID  - Bonomi2019\nER  - ";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
document.querySelector('#risa').addEventListener('click', () => {
const text = "TY  - JOUR\nAU  - Bonomi, Massimiliano\nAU  - Bussi, Giovanni\nAU  - Camilloni, Carlo\nAU  - Tribello, Gareth A.\nAU  - Banáš, Pavel\nAU  - Barducci, Alessandro\nAU  - Bernetti, Mattia\nAU  - Bolhuis, Peter G.\nAU  - Bottaro, Sandro\nAU  - Branduardi, Davide\nAU  - Capelli, Riccardo\nAU  - Carloni, Paolo\nAU  - Ceriotti, Michele\nAU  - Cesari, Andrea\nAU  - Chen, Haochuan\nAU  - Chen, Wei\nAU  - Colizzi, Francesco\nAU  - De, Sandip\nAU  - De La Pierre, Marco\nAU  - Donadio, Davide\nAU  - Drobot, Viktor\nAU  - Ensing, Bernd\nAU  - Ferguson, Andrew L.\nAU  - Filizola, Marta\nAU  - Fraser, James S.\nAU  - Fu, Haohao\nAU  - Gasparotto, Piero\nAU  - Gervasio, Francesco Luigi\nAU  - Giberti, Federico\nAU  - Gil-Ley, Alejandro\nAU  - Giorgino, Toni\nAU  - Heller, Gabriella T.\nAU  - Hocky, Glen M.\nAU  - Iannuzzi, Marcella\nAU  - Invernizzi, Michele\nAU  - Jelfs, Kim E.\nAU  - Jussupow, Alexander\nAU  - Kirilin, Evgeny\nAU  - Laio, Alessandro\nAU  - Limongelli, Vittorio\nAU  - Lindorff-Larsen, Kresten\nAU  - Löhr, Thomas\nAU  - Marinelli, Fabrizio\nAU  - Martin-Samos, Layla\nAU  - Masetti, Matteo\nAU  - Meyer, Ralf\nAU  - Michaelides, Angelos\nAU  - Molteni, Carla\nAU  - Morishita, Tetsuya\nAU  - Nava, Marco\nAU  - Paissoni, Cristina\nAU  - Papaleo, Elena\nAU  - Parrinello, Michele\nAU  - Pfaendtner, Jim\nAU  - Piaggi, Pablo\nAU  - Piccini, GiovanniMaria\nAU  - Pietropaolo, Adriana\nAU  - Pietrucci, Fabio\nAU  - Pipolo, Silvio\nAU  - Provasi, Davide\nAU  - Quigley, David\nAU  - Raiteri, Paolo\nAU  - Raniolo, Stefano\nAU  - Rydzewski, Jakub\nAU  - Salvalaglio, Matteo\nAU  - Sosso, Gabriele Cesare\nAU  - Spiwok, Vojtěch\nAU  - Šponer, Jiří\nAU  - Swenson, David W. H.\nAU  - Tiwary, Pratyush\nAU  - Valsson, Omar\nAU  - Vendruscolo, Michele\nAU  - Voth, Gregory A.\nAU  - White, Andrew\nPY  - 2019\nDA  - 2019/08/01\nTI  - Promoting transparency and reproducibility in enhanced molecular simulations\nJO  - Nature Methods\nSP  - 670\nEP  - 673\nVL  - 16\nIS  - 8\nAB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.\nSN  - 1548-7105\nUR  - https://doi.org/10.1038/s41592-019-0506-8\nDO  - 10.1038/s41592-019-0506-8\nID  - Bonomi2019\nER  - ";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
</script>
