Name:		texlive-chemobabel
Version:	64778
Release:	2
Summary:	Convert chemical structures from ChemDraw, MDL molfile or SMILES using Open Babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chemobabel
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a way to convert and include chemical
structure graphics from various chemical formats, such as
ChemDraw files, MDL molfile or SMILES notations using Open
Babel. To use this LaTeX package, it is necessary to enable
execution of the following external commands via latex
-shell-escape. obabel (Open Babel) inkscape or rsvg-convert
(for SVG -> PDF/EPS conversion) pdfcrop or ps2eps (optional;
for cropping large margins of PDF/EPS)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/chemobabel
%{_texmfdistdir}/tex/latex/chemobabel
%doc %{_texmfdistdir}/doc/latex/chemobabel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
