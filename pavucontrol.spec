#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pavucontrol
Version  : 4.0
Release  : 9
URL      : http://freedesktop.org/software/pulseaudio/pavucontrol/pavucontrol-4.0.tar.xz
Source0  : http://freedesktop.org/software/pulseaudio/pavucontrol/pavucontrol-4.0.tar.xz
Summary  : PulseAudio Volume Control
Group    : Development/Tools
License  : GPL-2.0
Requires: pavucontrol-bin = %{version}-%{release}
Requires: pavucontrol-data = %{version}-%{release}
Requires: pavucontrol-license = %{version}-%{release}
Requires: pavucontrol-locales = %{version}-%{release}
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : libsigc++-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libpulse-mainloop-glib)
BuildRequires : pkgconfig(sigc++-2.0)

%description
PulseAudio Volume Control 4.0
* [1]License
* [2]News
* [3]Overview
* [4]Current Status
* [5]Documentation
* [6]Requirements
* [7]Installation
* [8]Download
* [9]Bug Reports
* [10]Contributing Code

%package bin
Summary: bin components for the pavucontrol package.
Group: Binaries
Requires: pavucontrol-data = %{version}-%{release}
Requires: pavucontrol-license = %{version}-%{release}

%description bin
bin components for the pavucontrol package.


%package data
Summary: data components for the pavucontrol package.
Group: Data

%description data
data components for the pavucontrol package.


%package doc
Summary: doc components for the pavucontrol package.
Group: Documentation

%description doc
doc components for the pavucontrol package.


%package license
Summary: license components for the pavucontrol package.
Group: Default

%description license
license components for the pavucontrol package.


%package locales
Summary: locales components for the pavucontrol package.
Group: Default

%description locales
locales components for the pavucontrol package.


%prep
%setup -q -n pavucontrol-4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557096907
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557096907
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pavucontrol
cp LICENSE %{buildroot}/usr/share/package-licenses/pavucontrol/LICENSE
%make_install
%find_lang pavucontrol

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pavucontrol

%files data
%defattr(-,root,root,-)
/usr/share/applications/pavucontrol.desktop
/usr/share/pavucontrol/pavucontrol.glade

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/pavucontrol/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pavucontrol/LICENSE

%files locales -f pavucontrol.lang
%defattr(-,root,root,-)

