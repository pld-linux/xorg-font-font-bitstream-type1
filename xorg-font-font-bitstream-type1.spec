# $Rev: 3203 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-bitstream-type1
Summary(pl):	font-bitstream-type1
Name:		xorg-font-font-bitstream-type1
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bitstream-type1-%{version}.tar.bz2
# Source0-md5:	04a9e7c622fd2b13d1a723c0ca0aee86
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-bitstream-type1-%{version}-root-%(id -u -n)

%description
font-bitstream-type1

%description -l pl
font-bitstream-type1


%prep
%setup -q -n font-bitstream-type1-%{version}


%build
%{__aclocal}
%{__autoconf}
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
%{_libdir}/X11/fonts/Type1/*
