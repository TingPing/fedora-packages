Name:           libsexy3
Version:        1.1.0
Release:        1%{?dist}
Summary:        Custom Gtk3 widgets

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://tingping.github.io/libsexy3/
Source0:        https://github.com/TingPing/libsexy3/releases/download/v%{version}/libsexy3-%{version}.tar.xz

BuildRequires:  pkgconfig(gtk+-3.0) pkgconfig(enchant) pkgconfig(iso-codes)
BuildRequires:  vala-tools intltool gtk-doc gobject-introspection-devel


%description
A "continuation" of the libsexy library which contains custom widgets. Currently containing
only a GtkEntry with spell-checking added.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%configure --disable-static --enable-gtk-doc --enable-vala
%make


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Sexy-3.0.typelib


%files devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Sexy-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/%{name}.*
%dir %{_datadir}/glade/
%dir %{_datadir}/glade/catalogs/
%{_datadir}/glade/catalogs/sexy-catalog.xml



%changelog
* Mon Sep 21 2015 TingPing <tingping@tingping.se> - 1.1.0-1
- Initial package


