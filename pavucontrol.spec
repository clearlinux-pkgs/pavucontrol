#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pavucontrol
Version  : 3.0
Release  : 3
URL      : http://freedesktop.org/software/pulseaudio/pavucontrol/pavucontrol-3.0.tar.xz
Source0  : http://freedesktop.org/software/pulseaudio/pavucontrol/pavucontrol-3.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pavucontrol-bin
Requires: pavucontrol-data
Requires: pavucontrol-doc
Requires: pavucontrol-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : libsigc++-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(sigc++-2.0)

%description
PulseAudio Volume Control 3.0
<mzcnihpbageby (at) 0pointer (dot) de>
* [1]License
* [2]News
* [3]Overview
* [4]Current Status
* [5]Documentation
* [6]Requirements
* [7]Installation
* [8]Acknowledgements
* [9]Download

%package bin
Summary: bin components for the pavucontrol package.
Group: Binaries
Requires: pavucontrol-data

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


%package locales
Summary: locales components for the pavucontrol package.
Group: Default

%description locales
locales components for the pavucontrol package.


%prep
%setup -q -n pavucontrol-3.0

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
%doc /usr/share/doc/pavucontrol/*

%files locales -f pavucontrol.lang 
%defattr(-,root,root,-)

