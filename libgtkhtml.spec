Summary:	GTK HTML widget 2
Summary(pl):	Widget GTK HTML dla GNOME2
Name:		libgtkhtml
Version:	2.6.3
Release:	1
License:	GPL/LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgtkhtml/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	c77789241d725e189ffc0391eda94361
URL:		http://gtkhtml2.codefactory.se/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gail-devel >= 1.8.2
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	pkgconfig
Requires:	gail >= 1.8.2
Requires:	libxml2 >= 1:2.6.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK HTML Widget for the GNOME 2 platform.

%description -l pl
Widget GTK HTML dla platformy GNOME2.

%package devel
Summary:	Header files for GTK HTML 2
Summary(pl):	Pliki nag��wkowe GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gail-devel >= 1.8.2
Requires:	libxml2-devel >= 1:2.6.19

%description devel
Header files for GTK HTML 2.

%description devel -l pl
Pliki nag��wkowe dla GTK HTML 2.

%package static
Summary:	Static GTK HTML 2 library
Summary(pl):	Statyczna biblioteka GTK HTML 2
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of GTK HTML 2 library.

%description static -l pl
Statyczna wersja biblioteki GTK HTML 2.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO README NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/gtkhtml-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
