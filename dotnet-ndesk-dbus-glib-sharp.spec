#
%include	/usr/lib/rpm/macros.mono
#

%define module ndesk-dbus-glib

Summary:	.NET library for using D-BUS message bus (Glib integration)
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS
Name:		dbus-ndesk-dbus-glib-sharp
Version:	0.4.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	7faf8770b214956fa9de009def550826
URL:		http://www.ndesk.org/DBusSharp
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	dotnet-ndesk-dbus-sharp
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS (glib integration).

%description -l pl.UTF-8
Biblioteka .NET do używania D-BUS.

%prep
%setup -q -n %{module}-%{version}

%build
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
%{_libdir}/mono/ndesk-dbus-glib-1.0
%{_libdir}/mono/gac/NDesk*
%{_pkgconfigdir}/ndesk-dbus-glib-1.0.pc
