#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package xdg-desktop-portal-singularity
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
#

%global 	debug_package 	%{nil}
%global 	snapshot    	20260610
%global 	commit      	1bf818c3697168a709daf2e159a04a3f23bc6ece
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

Name:           xdg-desktop-portal-singularity
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        Singularity Desktop xdg-desktop-portal.
License:        LGPL-2.1-only
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc
BuildRequires:	vetro
BuildRequires:	pkg-config

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(gtk4-unix-print)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(gtk4-layer-shell-0)
BuildRequires:	pkgconfig(singularity-1.0)
BuildRequires:	pkgconfig(libpipewire-0.3)


%description
backend implementation for xdg-desktop-portal for the Singularity Desktop Environment.


%prep

%autosetup -n %{name}-%{commit}

%build

%meson
%meson_build


%install

%meson_install

%files

%license LICENSE
%{_bindir}/singularity-screencast-chooser
%{_libexecdir}/xdg-desktop-portal-singularity

%changelog


