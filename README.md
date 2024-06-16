# tushuguan

`tushuguan` is a template repository to create a personal (or shared) ${\mathrm{B{\scriptstyle{IB}} T_{\displaystyle E} X}}$ library.

## Usage

### Create a new library

Click [Use this template](https://github.com/new?template_name=tushuguan&template_owner=njzjz) button to create a new library.

### Add new references

#### Add a `.bib` file via a pull request

Add a ${\mathrm{B{\scriptstyle{IB}} T_{\displaystyle E} X}}$ file with items via a pull request.
The items with the `@aricle` type are expected to have a `<LastName>_<Year>_<JournalAbbr>_v<Volume>_p<Page>` key, for example, [`Zeng_JChemPhys_2023_v159_p054801`](./article/JChemPhys/Zeng_JChemPhys_2023_v159_p054801.bib).
The pre-commit will run to automatically fix the format of the ${\mathrm{B{\scriptstyle{IB}} T_{\displaystyle E} X}}$ file.

> [!NOTE]
> GitHub Actions runs will [not be triggered](https://github.com/orgs/community/discussions/25702) with the autofix commit. In this case, one can close and reopen the PR to manually trigger the GitHub Actions runs.

#### Add a reference from an identifier

> [!NOTE]
> Go to `Settings` > `Actions` > `General` > `Workflow permissions` and click `Allow GitHub Actions to create and approve pull requests`.

Open a new issue with the title `/new <DOI>`, such as `/new 10.1063/5.0155600`.
Powered by [`wenxian`](https://github.com/njzjz/wenxian), a pull request will be automatically created.

> [!NOTE]
> GitHub Actions runs will [not be triggered](https://github.com/orgs/community/discussions/25702) with a PR created by the GitHub Actions itself. In this case, one can close and reopen the PR to manually trigger the GitHub Actions runs.

### Use the merged `.bib` file

#### Download

Click the `Deployments` > `bibtex` on the right side to download the merged ${\mathrm{B{\scriptstyle{IB}} T_{\displaystyle E} X}}$ file.

#### Use in an external LaTeX project on GitHub

Use the library as a GitHub Actions step in an external $\LaTeX$ project.

> [!NOTE]
> If the library is private, go to `Settings` > `Actions` > `General` > `Access` to make it Accessible from other repositories.

```yml
# replace with your own library!
- name: Fetching the references
  uses: njzjz/tushuguan@master
  with:
    output: references.bib
# compile the latex project...
```

#### Use in Overleaf

1. Go to [nightly.link](https://nightly.link/) and click `Install and select your repositories` and `Authorize to see your repositories` buttons.
   Choose your library and fill the URL of [`.github/workflows/combine.yaml`](.github/workflows/combine.yaml).
   Copy the URL shown on the screen, for example, [https://nightly.link/njzjz/tushuguan/workflows/combine.yaml/master/dist-combined-bib.zip](https://nightly.link/njzjz/tushuguan/workflows/combine.yaml/master/dist-combined-bib.zip).
2. In the Overleaf, [upload a file using the copied URL](https://www.overleaf.com/learn/how-to/How_to_upload_a_file_using_an_external_URL).
   The default filename is `dist-combined-bib.zip`.
   When you need to update that file, click that file and then click `refresh`.
3. At the top of the $\LaTeX$ file, add the following code:
```tex
\usepackage[backend=biber]{biblatex}
\usepackage{shellesc}
% uncompress the zip file before each compilation
\ShellEscape{unzip dist-combined-bib.zip}
\addbibresource{combined.bib}
```

Then you can add `\cite` and `printbibliography` to cite the reference you need.
For example,
```tex
This sentence is an example of using the reference from \texttt{tushuguan}\cite{Zeng_JChemPhys_2023_v159_p054801}.

\printbibliography
```

An example Overleaf project is given [here](https://www.overleaf.com/read/dgfyfktsggcd#54f062).

### Search the references

Use the GitHub to search references, or use `grep` on the local.
