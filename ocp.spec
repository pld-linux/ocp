Summary:	A console music player
Summary(pl.UTF-8):	Konsolowy odtwarzacz muzyczny
Name:		ocp
Version:	0.1.19
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://stian.cubic.org/ocp/%{name}-%{version}.tar.bz2
# Source0-md5:	b7879e7d284f0e0c92bbb3cea2e364f0
Patch0:		%{name}-ini_file.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-Makefile.patch
Patch3:		%{name}-link.patch
URL:		http://stian.cubic.org/project-ocp.php
BuildRequires:	SDL-devel
BuildRequires:	adplug-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	flac-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libsidplay-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Cubic Player is a music player which can play a wide variety of
music formats.

%description -l pl.UTF-8
Open Cubic Player jest odtwarzaczem muzycznym, który potrafi odtwarzać
szeroką gamę formatów muzyki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i 's,curses\.h,ncurses/curses\.h,' \
	configure playsid/sidpplay.cpp

%build
%configure \
	--with-dir-suffix="" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
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
%dir %{_libdir}/%{name}/autoload
%{_libdir}/%{name}/autoload/*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_pixmapsdir}/opencubicplayer.xpm
