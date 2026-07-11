%global tl_name stdpage
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Standard pages with n lines of at most m characters each
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stdpage
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdpage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For translations, proofreading, journal contributions etc. standard
pages are used. Those standard pages consist of a fixed number of lines
and characters per line. This package produces pages with n lines of at
most m characters each. For instance the German "Normseite": 60 lines of
30 characters each.

