# $Rev: 3339 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	beforelight application
Summary(pl):	Aplikacja beforelight
Name:		xorg-app-beforelight
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/beforelight-%{version}.tar.bz2
# Source0-md5:	d967a9155ee3da48b9c916b0d652009f
Patch0:		beforelight-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/beforelight-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
beforelight application.

%description -l pl
Aplikacja beforelight.


%prep
%setup -q -n beforelight-%{version}
%patch0 -p1


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
%{_sysconfdir}/X11/app-defaults/B4light
%attr(755,root,wheel) %{_bindir}/beforelight
%{_mandir}/man1/*.1*
