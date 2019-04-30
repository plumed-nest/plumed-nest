How to contribute to PLUMED-NEST
--------------------------------
Contributing to PLUMED-NEST is free and easy. It is enough to provide the following
information in the form at the bottom of this page. All fields are required, unless otherwise specified.

* __plumID:__ please select *"new"* for a new submission, or your plumID in case of resubmission/update of an existing project
* __Project name:__ the name of your project
* __URL:__ the location of the zipped archive containing all the files needed to reproduce your PLUMED-enhanced simulation or analysis
* __PLUMED input files (optional):__ list of non-standard PLUMED input file names, i.e. different from `plumed*.dat`
* __Category:__ the category that best defines the project
* __Keywords:__ keywords describing the project
* __Instructions:__ list of software used and instructions to execute the simulation(s)/analysis
* __PLUMED version:__ the version of the code used in this project
* __Contributor:__ project contributor (a single name or name of the research group)
* __Publication:__ the DOI identifying the paper related to this project. If the work is still unpublished and not available on a preprint server, please type *"unpublished"*
* __Contact:__ the name of a contact person to communicate with the coordinators of the PLUMED consortium
* __Contact email:__ the email of the contact person
* __Comments (optional):__ comments related to the submission, e.g. list of changes in case of resubmission

__Please note that:__

* The name and email of the contact person will not appear on the PLUMED-NEST website.
* All contributions are curated and manually uploaded by the coordinators of the PLUMED consortium. Therefore, a delay between submission and online publication should be expected.
* If necessary, you will be able to edit the information on [GitHub](https://github.com/plumed-nest/plumed-nest) later or send us a revised version of the form. In the latter case, please specify a list of changes in the "Comments" field.
* PLUMED-NEST will not host your archive, so make sure the indicated URL remains accessible.
* PLUMED-NEST will not test your execution scripts, but only the compatibility of the PLUMED input files provided.

<center>
<p><b>Questions related to the submission to PLUMED-NEST can be directed to:</b></p>
<p><b><a href="mailto:plumed.nest@gmail.com">plumed.nest@gmail.com</a></b></p>
</center>

Fields marked with "<sup>*</sup>" are optional  

<form class="wj-contact" method="POST" action="https://formspree.io/plumed.nest@gmail.com">
  <table>
    <tr>
      <td><label for="id">plumID</label></td>
      <td width="600"><select id="id" type="texy" name="plumID"><option>new (plumID to be assigned)</option>{% for item in site.data.eggs %}<option>{{ item.id }}:{{ item.shortname }}</option>{% endfor %} required</select> </td>
    </tr>
    <tr>  
      <td><label for="name">Project name</label></td>
      <td width="600"><input id="name" type="text" name="projectname" required> </td>
    </tr>
    <tr>
      <td><label for="url">URL</label></td>
      <td width="600"><input id="url" type="text" name="url" required> </td>
    </tr>  
    <tr>
      <td><label for="pinput">PLUMED input files<sup>*</sup></label></td>
      <td width="600"><input id="pinput" type="text" name="plumedinput" placeholder="examples: colvar.dat, bias.dat, ..."> </td>
    </tr>
    <tr>
      <td><label for="category">Category</label></td>
      <td width="600"><select id="category" type="texy" name="category"><option>bio</option><option>chemistry</option><option>materials</option><option>methods</option><option>other</option></select> </td>
    </tr>
    <tr>
      <td><label for="keywords">Keywords</label></td>
      <td width="600"><input id="keywords" type="text" name="keywords" placeholder="examples: metadynamics, RNA, protein folding, small molecules, ..." required></td>
    </tr>
    <tr>
      <td height="200"><label for="instructions">Instructions</label></td>
      <td width="600" height="200"><textarea id="instructions" name="message" type="text" placeholder="Please explain how to use the deposited input files and provide a list of other software used (i.e. GROMACS) along with the specific version (i.e. 2018.6)" required></textarea></td>
    </tr>
    <tr>
      <td><label for="version">PLUMED version</label></td>
      <td width="600"><input id="version" type="text" name="version" placeholder="examples: 2.4, 2.5-dev" required></td>
    </tr>
    <tr>
      <td><label for="contributor">Contributor</label></td>
      <td width="600"><input id="contributor" type="text" name="contributor" required></td>
    </tr>
    <tr>
      <td><label for="publication">Publication</label></td>
      <td width="600"><input id="publication" type="text" name="publication" placeholder="examples: 10.1016/j.cpc.2013.09.018, unpublished" required></td>
    </tr>
    <tr>
      <td><label for="contact">Contact</label></td>
      <td width="600"><input id="contact" type="text" name="contact" required></td>
    </tr>
    <tr>
      <td><label for="email">Contact email</label></td>
      <td width="600"><input id="email" type="email" name="email" required></td>
    </tr>  
    <tr>
      <td><label for="comments">Comments<sup>*</sup></label></td>
      <td width="600"><input id="comments" type="text" name="comments"></td>
    </tr>
  </table>
  <input type="text" name="_gotcha" style="display:none"> <br>
  <button type="submit">Submit</button>
  <input type="hidden" name="_subject" id="_subject" value="PLUMED-NEST submission"> <br>
</form>

<style>
form.wj-contact input[type="text"], form.wj-contact textarea[type="text"], form.wj-contact input[type="email"]{
    width: 100%;
    height: 100%;
    vertical-align: middle;
    padding: 0.25em;
    font-family: monospace, sans-serif;
    font-weight: lighter;
    border-style: solid;
    border-color: #444;
    outline-color: #2e83e6;
    border-width: 1px;
    border-radius: 3px;
    transition: box-shadow .2s ease;
    margin-top: auto;
    margin-bottom: auto;
    margin-left: auto;
    margin-right: auto
    box-sizing: border-box;
}
</style>
    
