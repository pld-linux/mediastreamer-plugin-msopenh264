Summary:	H.264 video codec for mediastreamer based on the openh264 library
Summary(pl.UTF-8):	Kodek obrazu H.264 dla mediastreamera oparty na bibliotece openh264
Name:		mediastreamer-plugin-msopenh264
Version:	5.2.0
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/msopenh264/-/tags
Source0:	https://gitlab.linphone.org/BC/public/msopenh264/-/archive/%{version}/msopenh264-%{version}.tar.bz2
# Source0-md5:	f854bfa3db3244b388571c2359a895ee
Patch0:		msopenh264-b64-refactor.patch
URL:		https://www.linphone.org/technical-corner/mediastreamer2-ortp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mediastreamer-devel >= 5
BuildRequires:	openh264-devel >= 1.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	openh264 >= 1.4.0
Requires:	mediastreamer >= 5
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
%{__autoheader}
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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmsopenh264.so*
