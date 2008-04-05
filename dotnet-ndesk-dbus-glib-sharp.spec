%include	/usr/lib/rpm/macros.mono
%define	module	ndesk-dbus-glib

Summary:	.NET library for using D-BUS message bus (GLib integration)
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS z GLib
Name:		dotnet-ndesk-dbus-glib-sharp
Version:	0.4.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	7faf8770b214956fa9de009def550826
Patch0:		%{name}-monodir.patch
URL:		http://www.ndesk.org/DBusSharp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	dotnet-ndesk-dbus-sharp-devel >= 0.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
# DllImport, not detected by monoautodeps
%ifarch %{x8664} ia64 ppc64 s390x
Requires:	libglib-2.0.so.0()(64bit)
%else
Requires:	libglib-2.0.so.0
%endif
Obsoletes:	ndesk-dbus-glib
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS with GLib.

This code provides GLib main loop integration for Managed D-Bus.

%description -l pl.UTF-8
Biblioteka .NET do używania D-BUS wraz z GLib.

Ten kod udostępnia integrację głównej pętli GLib z Managed D-Bus.

%package devel
Summary:	Development files for ndesk D-BUS GLib .NET library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET ndesk D-BUS GLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-ndesk-dbus-sharp-devel >= 0.4

%description devel
Development files for ndesk D-BUS GLib .NET library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET ndesk D-BUS GLib.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
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
%doc AUTHORS COPYING README
%{_prefix}/lib/mono/gac/NDesk.DBus.GLib
# .mdb to -debug?

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/ndesk-dbus-glib-1.0
%{_pkgconfigdir}/ndesk-dbus-glib-1.0.pc
