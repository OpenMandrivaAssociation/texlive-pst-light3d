# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-light3d
# catalog-date 2007-03-11 16:56:01 +0100
# catalog-license lppl
# catalog-version 0.12
Name:		texlive-pst-light3d
Version:	0.12
Release:	1
Summary:	3D lighting effects for pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-light3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-light3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A PSTricks package for three dimensional lighting effects on
characters and PSTricks graphics, like lines, curves, plots,
...

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}