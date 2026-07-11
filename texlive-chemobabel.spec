%global tl_name chemobabel
%global tl_revision 64778

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9l
Release:	%{tl_revision}.1
Summary:	Convert chemical structures from ChemDraw, MDL molfile or SMILES using Open B...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/chemobabel
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemobabel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a way to convert and include chemical structure
graphics from various chemical formats, such as ChemDraw files, MDL
molfile or SMILES notations using Open Babel. To use this LaTeX package,
it is necessary to enable execution of the following external commands
via latex -shell-escape. obabel (Open Babel) inkscape or rsvg-convert
(for SVG -> PDF/EPS conversion) pdfcrop or ps2eps (optional; for
cropping large margins of PDF/EPS)

