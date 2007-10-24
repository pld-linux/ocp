Summary:	-
Summary(pl.UTF-8):	-
Name:		ocp
Version:	0.1.14
Release:	0.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://stian.lunafish.org/ocp/%{name}-%{version}.tar.bz2
# Source0-md5:	97a4c79361938b0a0ec614c3851fa53e
Patch0:		%{name}-ini_file.patch
URL:		http://stian.lunafish.org/project-ocp.php
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
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
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/autoload
%{_libdir}/%{name}/*.so
