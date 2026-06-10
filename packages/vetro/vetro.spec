#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package vetro
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

Name:           vetro
Version:        1.0.0
Release:        1%{?dist}
Summary:        GTK4 UI transpiler.
License:        MIT
URL:            https://github.com/singularityos-lab/vetro

Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Vetro is a declarative GTK4 UI transpiler with a built-in Language Server Protocol (LSP) server.

%prep

%autosetup -n %{name}-%{version}

%build

go build -o vetro .

%install

install -Dm755 vetro %{buildroot}%{_bindir}/vetro

%files

%license LICENSE
%{_bindir}/vetro


%changelog


