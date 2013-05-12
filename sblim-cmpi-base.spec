Summary:	SBLIM CMPI Base Instrumentation package
Summary(pl.UTF-8):	Pakiet podstawowych pomiarów SBLIM CMPI
Name:		sblim-cmpi-base
Version:	1.6.1
Release:	2
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	fca81c5a5e88856d30d818a3132790ea
URL:		http://sblim.sourceforge.net/
BuildRequires:	sblim-cmpi-devel
BuildRequires:	sblim-indication_helper-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SBLIM CMPI Base Instrumentation allows you to get the very base
system information via CIMOM technology/infrastructure.

%description -l pl.UTF-8
Pakiet SBLIM CMPI Base Instrumentation (podstawowych pomiarów SBLIM
CMPI) umożliwia łatwe pobieranie podstawowych informacji o systemie
poprzez infrastrukturę CIMOM.

%package libs
Summary:	SBLIM cmpiOSBase library
Summary(pl.UTF-8):	Biblioteka SBLIM cmpiOSBase
Group:		Libraries

%description libs
SBLIM cmpiOSBase library.

%description libs -l pl.UTF-8
Biblioteka SBLIM cmpiOSBase.

%package devel
Summary:	Header files for SBLIM cmpiOSBase library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SBLIM cmpiOSBase
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	sblim-cmpi-devel

%description devel
Header files for cmpiOSBase library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SBLIM cmpiOSBase.

%package static
Summary:	Static SBLIM cmpiOSBase library
Summary(pl.UTF-8):	Statyczna biblioteka SBLIM cmpiOSBase
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SBLIM cmpiOSBase library.

%description static -l pl.UTF-8
Statyczna biblioteka SBLIM cmpiOSBase.

%prep
%setup -q

%build
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmpi/libcmpiOSBase_*Provider.{la,a}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DEBUG NEWS README*
%dir %{_libdir}/cmpi
%attr(755,root,root) %{_libdir}/cmpi/libcmpiOSBase_*Provider.so
%dir %{_datadir}/sblim-cmpi-base
%{_datadir}/sblim-cmpi-base/Linux_Base*.mof
%{_datadir}/sblim-cmpi-base/Linux_BaseIndication.registration
%attr(755,root,root) %{_datadir}/sblim-cmpi-base/provider-register.sh

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiOSBase_Common.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmpiOSBase_Common.so.0
%attr(755,root,root) %{_libdir}/libdmiinfo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdmiinfo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiOSBase_Common.so
%attr(755,root,root) %{_libdir}/libdmiinfo.so
%{_libdir}/libcmpiOSBase_Common.la
%{_libdir}/libdmiinfo.la
# XXX: shared dir
%dir %{_includedir}/sblim
%{_includedir}/sblim/OSBase_*.h
%{_includedir}/sblim/cmpiOSBase_*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcmpiOSBase_Common.a
%{_libdir}/libdmiinfo.a
