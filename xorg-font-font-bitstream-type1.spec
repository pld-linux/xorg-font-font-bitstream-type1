Summary:	Bitstream Type1 fonts
Summary(pl.UTF-8):	Fonty Type1 Bitstream
Name:		xorg-font-font-bitstream-type1
Version:	1.0.0
Release:	2
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-bitstream-type1-%{version}.tar.bz2
# Source0-md5:	6610475e2e231242f8f2122a709c3695
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
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
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
mv -f *.afm afm
sed -e '1d' fonts.scale > fonts.scale.bitstream
rm -f fonts.scale fonts.dir fonts.cache-1

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
%doc COPYING ChangeLog
%{_fontsdir}/Type1/*.pfb
%{_fontsdir}/Type1/afm/*.afm
%{_fontsdir}/Type1/fonts.scale.bitstream
%{_fontsdir}/Type1/Fontmap.bitstream
