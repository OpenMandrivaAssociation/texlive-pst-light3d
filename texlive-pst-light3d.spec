Name:		texlive-pst-light3d
Version:	15878
Release:	1
Summary:	3D lighting effects for pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-light3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A PSTricks package for three dimensional lighting effects on
characters and PSTricks graphics, like lines, curves, plots,
...

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-light3d/pst-light3d.pro
%{_texmfdistdir}/tex/generic/pst-light3d/pst-light3d.tex
%{_texmfdistdir}/tex/latex/pst-light3d/pst-light3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-light3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-light3d/README
%doc %{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-light3d/pst-light3d-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-light3d/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
