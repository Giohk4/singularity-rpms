#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package libsingularity
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions, and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# This file is provided "as is", without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.

%global 	debug_package 	%{nil}
%global 	snapshot    	20260610
%global 	commit      	ccfdf4661b0d3c80349435c209ec6855ba37db82
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

Name:           libsingularity
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        Singularity Desktop application framework library
License:        LGPL-2.1-only
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc
BuildRequires:	python3
BuildRequires:	sassc

BuildRequires:  pkgconfig(gtk4)                >= 4.6
BuildRequires:  pkgconfig(gtk4-layer-shell-0)  >= 0.7
BuildRequires:  pkgconfig(gee-0.8)             >= 0.20
BuildRequires:  pkgconfig(json-glib-1.0)       >= 1.6
BuildRequires:  pkgconfig(libpeas-2)           >= 2.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


# runtime

Requires:	%{name}-typelib

%description
A GTK4 application and widget framework for the Singularity Desktop Environment.

# devel package

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}
Requires:	%{name}-typelib

%description    devel
Development files for %{name}

# typelib package

%package        typelib
Summary:        GObject introspection typelib files for %{name}
Requires:       %{name}

%description    typelib
GObject introspection typelib.


%prep

%autosetup -n %{name}-%{commit}
sed -i "s/'--output', '@OUTPUT@',/'--output', '@OUTPUT@',\n      '--shared-library=libsingularity.so.0',/" meson.build


%build

%meson \
    -Dintrospection=true
%meson_build


%install

%meson_install

%files
%license LICENSE

%{_libdir}/libsingularity.so
%{_libdir}/libsingularity.so.*

%{_datadir}/themes/Singularity/index.theme
%{_datadir}/themes/Singularity/gtk-3.0/*
%{_datadir}/themes/Singularity/gtk-4.0/*

%files devel
%{_includedir}/singularity.h
%{_libdir}/pkgconfig/singularity-1.0.pc
%{_datadir}/gir-1.0/Singularity-1.0.gir
%{_datadir}/vala/vapi/singularity-1.0.deps
%{_datadir}/vala/vapi/singularity-1.0.vapi

%files typelib
%{_libdir}/girepository-1.0/Singularity-1.0.typelib


%changelog
