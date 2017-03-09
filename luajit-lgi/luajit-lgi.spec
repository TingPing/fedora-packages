%global luaver 5.1
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
%global luaincdir %{_includedir}/luajit-2.0

Name:		luajit-lgi
Version:	0.9.1
Release:	1%{?dist}
Summary:	Lua bindings to GObject libraries
License:	MIT
URL:		https://github.com/pavouk/lgi
Source0:	https://github.com/pavouk/lgi/archive/%{version}/lgi-%{version}.tar.gz

BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.10.8
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(luajit)

Requires:	luajit

%description
LGI is gobject-introspection based dynamic Lua binding to GObject
based libraries. It allows using GObject-based libraries directly from
Lua.

%prep
%setup -q -n lgi-%{version}


%build
%make_build LUA_INCDIR=%{luaincdir} LUA_CFLAGS="$(pkg-config --cflags luajit)"

%install
%make_install \
  "PREFIX=%{_prefix}" \
  "LUA_LIBDIR=%{lualibdir}" \
  "LUA_SHAREDIR=%{luapkgdir}"


%files
%license LICENSE
%{luapkgdir}/lgi.lua
%{luapkgdir}/lgi
%{lualibdir}/lgi


%changelog
* Thu Mar 9 2017 Patrick Griffis <tingping@fedoraproject.org> - 0.9.1-1
- Initial version based upon lua-lgi package