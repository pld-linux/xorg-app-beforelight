Summary:	beforelight application - screen saver
Summary(pl.UTF-8):	Aplikacja beforelight - wygaszacz ekranu
Name:		xorg-app-beforelight
Version:	1.0.5
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/beforelight-%{version}.tar.bz2
# Source0-md5:	d587e2e64d63d0a33e7e911727f9ebd4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The beforelight program is a sample implementation of a screen saver
for X servers supporting the MIT-SCREEN-SAVER extension.

%description -l pl.UTF-8
Program beforelight to prosta implementacja wygaszacza ekranu dla
serwerów X obsługujących rozszerzenie MIT-SCREEN-SAVER.

%prep
%setup -q -n beforelight-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/beforelight
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.1*
