%global tl_name pst-light3d
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.12
Release:	%{tl_revision}.1
Summary:	Three dimensional lighting effects (PSTricks)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-light3d
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A PSTricks package for three dimensional lighting effects on characters
and PSTricks graphics, like lines, curves, plots, ...

