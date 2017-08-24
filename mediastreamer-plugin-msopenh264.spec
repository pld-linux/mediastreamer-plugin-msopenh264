Summary:	H.264 video codec for mediastreamer based on the openh264 library
Summary(pl.UTF-8):	Kodek obrazu H.264 dla mediastreamera oparty na bibliotece openh264
Name:		mediastreamer-plugin-msopenh264
Version:	1.1.1
Release:	4
License:	GPL v2+
Group:		Libraries
Source0:	http://linphone.org/releases/sources/plugins/msopenh264/msopenh264-%{version}.tar.gz
# Source0-md5:	7500abc43b1f3c935c97ea6a5c0d75ee
Patch0:		openh264-1.6.patch
URL:		http://www.linphone.org/technical-corner/mediastreamer2/overview
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mediastreamer-devel >= 2.7.0
BuildRequires:	openh264-devel >= 1.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	openh264 >= 1.4.0
Requires:	mediastreamer >= 2.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the H264 video
codec, based on openh264 library.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka obrazu H264,
opartą na bibliotece openh264.

%prep
%setup -q -n msopenh264-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmsopenh264.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsopenh264.so*
