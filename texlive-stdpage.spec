Name:		texlive-stdpage
Version:	15878
Release:	1
Summary:	Standard pages with n lines of at most m characters each
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stdpage
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For translations, proofreading, journal contributions etc.
standard pages are used. Those standard pages consist of a
fixed number of lines and characters per line. This package
produces pages with n lines of at most m characters each. For
instance the German "Normseite": 60 lines of 30 characters
each.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stdpage/stdpage.sty
%doc %{_texmfdistdir}/doc/latex/stdpage/README
%doc %{_texmfdistdir}/doc/latex/stdpage/stdpage-test.tex
%doc %{_texmfdistdir}/doc/latex/stdpage/stdpage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/stdpage/stdpage.dtx
%doc %{_texmfdistdir}/source/latex/stdpage/stdpage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
