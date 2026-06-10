#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package singularity-demo
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
%global 	snapshot    	20260609
%global 	commit      	4b2aef6c9f8f30b6f73c2716d2c8e425766360ac
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

Name:           singularity-demo
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        Singularity Desktop demo application.
License:        GPL-3.0-or-later
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson >= 1.11.0
BuildRequires:  vala
BuildRequires:  gcc
BuildRequires:	vetro

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(singularity-1.0)

%description
Sample app for the Singularity Desktop, useful as a template and integration test.


%prep

%autosetup -n %{name}-%{commit}

%build

%meson
%meson_build


%install

%meson_install

%files

%license LICENSE
%{_bindir}/singularity-demo
%{_datadir}/applications/dev.sinty.demo.desktop
%{_datadir}/icons/hicolor/scalable/apps/dev.sinty.demo.svg

%changelog


