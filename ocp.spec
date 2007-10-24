# TODO
# - check what is /usr/lib/ocp/autoload direcroty for
# - should we pack .so files in -devel package?
Summary:	A console music player
Summary(pl.UTF-8):	Konsolowy odtwarzacz muzyczny
Name:		ocp
Version:	0.1.14
Release:	0.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://stian.lunafish.org/ocp/%{name}-%{version}.tar.bz2
# Source0-md5:	97a4c79361938b0a0ec614c3851fa53e
Patch0:		%{name}-ini_file.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-Makefile.patch
URL:		http://stian.lunafish.org/project-ocp.php
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Cubic Player is a music player which can play a wide variety of
music formats.

%description -l pl.UTF-8
Open Cubic Player jest odtwarzaczem muzycznym, który potrafi
odtwarzać szeroką gamę formatów muzyki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__sed} -i 's@<curses.h>@<ncurses/curses.h>@' `grep -R '<curses.h>' * | cut -d":" -f1`

%build
%configure \
	--with-dir-suffix=""
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ocp.ini
%doc AUTHORS CREDITS Changelog README.Darwin SUID TODO doc/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/data
%{_desktopdir}/opencubicplayer.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/autoload
%{_libdir}/%{name}/*.so
%{_pixmapsdir}/opencubicplayer.xpm
