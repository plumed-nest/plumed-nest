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
const text = "
TY  - JOUR
AU  - The PLUMED consortium,
PY  - 2019
DA  - 2019/08/01
TI  - Promoting transparency and reproducibility in enhanced molecular simulations
JO  - Nature Methods
SP  - 670
EP  - 673
VL  - 16
IS  - 8
AB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analys is of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.
SN  - 1548-7105
UR  - https://doi.org/10.1038/s41592-019-0506-8
DO  - 10.1038/s41592-019-0506-8
ID  - Bonomi2019
ER  - 
";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
document.querySelector('#ris4').addEventListener('click', () => {
const text = "
TY  - JOUR
AU  - Bonomi, Massimiliano
AU  - Bussi, Giovanni
AU  - Camilloni, Carlo
AU  - Tribello, Gareth A.
AU  - The PLUMED consortium,
PY  - 2019
DA  - 2019/08/01
TI  - Promoting transparency and reproducibility in enhanced molecular simulations
JO  - Nature Methods
SP  - 670
EP  - 673
VL  - 16
IS  - 8
AB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.
SN  - 1548-7105
UR  - https://doi.org/10.1038/s41592-019-0506-8
DO  - 10.1038/s41592-019-0506-8
ID  - Bonomi2019
ER  - 
";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
document.querySelector('#risa').addEventListener('click', () => {
const text = "
TY  - JOUR
AU  - Bonomi, Massimiliano
AU  - Bussi, Giovanni
AU  - Camilloni, Carlo
AU  - Tribello, Gareth A.
AU  - Banáš, Pavel
AU  - Barducci, Alessandro
AU  - Bernetti, Mattia
AU  - Bolhuis, Peter G.
AU  - Bottaro, Sandro
AU  - Branduardi, Davide
AU  - Capelli, Riccardo
AU  - Carloni, Paolo
AU  - Ceriotti, Michele
AU  - Cesari, Andrea
AU  - Chen, Haochuan
AU  - Chen, Wei
AU  - Colizzi, Francesco
AU  - De, Sandip
AU  - De La Pierre, Marco
AU  - Donadio, Davide
AU  - Drobot, Viktor
AU  - Ensing, Bernd
AU  - Ferguson, Andrew L.
AU  - Filizola, Marta
AU  - Fraser, James S.
AU  - Fu, Haohao
AU  - Gasparotto, Piero
AU  - Gervasio, Francesco Luigi
AU  - Giberti, Federico
AU  - Gil-Ley, Alejandro
AU  - Giorgino, Toni
AU  - Heller, Gabriella T.
AU  - Hocky, Glen M.
AU  - Iannuzzi, Marcella
AU  - Invernizzi, Michele
AU  - Jelfs, Kim E.
AU  - Jussupow, Alexander
AU  - Kirilin, Evgeny
AU  - Laio, Alessandro
AU  - Limongelli, Vittorio
AU  - Lindorff-Larsen, Kresten
AU  - Löhr, Thomas
AU  - Marinelli, Fabrizio
AU  - Martin-Samos, Layla
AU  - Masetti, Matteo
AU  - Meyer, Ralf
AU  - Michaelides, Angelos
AU  - Molteni, Carla
AU  - Morishita, Tetsuya
AU  - Nava, Marco
AU  - Paissoni, Cristina
AU  - Papaleo, Elena
AU  - Parrinello, Michele
AU  - Pfaendtner, Jim
AU  - Piaggi, Pablo
AU  - Piccini, GiovanniMaria
AU  - Pietropaolo, Adriana
AU  - Pietrucci, Fabio
AU  - Pipolo, Silvio
AU  - Provasi, Davide
AU  - Quigley, David
AU  - Raiteri, Paolo
AU  - Raniolo, Stefano
AU  - Rydzewski, Jakub
AU  - Salvalaglio, Matteo
AU  - Sosso, Gabriele Cesare
AU  - Spiwok, Vojtěch
AU  - Šponer, Jiří
AU  - Swenson, David W. H.
AU  - Tiwary, Pratyush
AU  - Valsson, Omar
AU  - Vendruscolo, Michele
AU  - Voth, Gregory A.
AU  - White, Andrew
PY  - 2019
DA  - 2019/08/01
TI  - Promoting transparency and reproducibility in enhanced molecular simulations
JO  - Nature Methods
SP  - 670
EP  - 673
VL  - 16
IS  - 8
AB  - The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.
SN  - 1548-7105
UR  - https://doi.org/10.1038/s41592-019-0506-8
DO  - 10.1038/s41592-019-0506-8
ID  - Bonomi2019
ER  - 
";
downloadToFile(text, 'plumed.ris', 'text/plain');
});
document.querySelector('#bibc').addEventListener('click', () => {
const text = "
@Article{Bonomi2019,
author={{The PLUMED consortium}},
title={Promoting transparency and reproducibility in enhanced molecular simulations},
journal={Nature Methods},
year={2019},
month={Aug},
day={01},
volume={16},
number={8},
pages={670-673},
abstract={The PLUMED consortium unifies developers and contributors to PLUMED, an open-source library for enhanced-sampling, free-energy calculations and the analysis of molecular dynamics simulations. Here, we outline our efforts to promote transparency and reproducibility by disseminating protocols for enhanced-sampling molecular simulations.},
issn={1548-7105},
doi={10.1038/s41592-019-0506-8},
url={https://doi.org/10.1038/s41592-019-0506-8}
}
";
</script>
