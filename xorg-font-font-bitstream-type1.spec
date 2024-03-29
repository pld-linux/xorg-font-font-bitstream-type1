Summary:	Bitstream Type1 fonts
Summary(pl.UTF-8):	Fonty Type1 Bitstream
Name:		xorg-font-font-bitstream-type1
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-bitstream-type1-%{version}.tar.xz
# Source0-md5:	3974a3e7f15ed7de19e45b4139d1468c
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bitstream Charter and Courier fonts in Type1 format.

%description -l pl.UTF-8
Fonty Bitstream Charter i Courier w formacie Type1.

%prep
%setup -q -n font-bitstream-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
%{__mv} *.afm afm
sed -e '1d' fonts.scale > fonts.scale.bitstream
%{__rm} fonts.scale fonts.dir

cat > Fontmap.bitstream <<EOF
/Courier10PitchBT-Roman                  (c0419bt_.pfb) ;
/Courier10PitchBT-Italic                 (c0582bt_.pfb) ;
/Courier10PitchBT-Bold                   (c0583bt_.pfb) ;
/Courier10PitchBT-BoldItalic             (c0611bt_.pfb) ;
/CharterBT-Bold                          (c0632bt_.pfb) ;
/CharterBT-BoldItalic                    (c0633bt_.pfb) ;
/CharterBT-Roman                         (c0648bt_.pfb) ;
/CharterBT-Italic                        (c0649bt_.pfb) ;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/Type1/c0*.pfb
%{_fontsdir}/Type1/afm/c0*.afm
%{_fontsdir}/Type1/fonts.scale.bitstream
%{_fontsdir}/Type1/Fontmap.bitstream
