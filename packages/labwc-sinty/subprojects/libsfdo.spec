#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package libsfdo
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


Name:           libsfdo
Version:        0.1.4
Release:        1
Summary:        A collection of libraries implementing freedesktop.org specifications

License:        BSD-2-Clause
URL:            https://gitlab.freedesktop.org/vyivel/libsfdo


Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_libdir}/libsfdo-*.so.0

%files devel
%{_includedir}/sfdo-*.h
%{_libdir}/libsfdo-*.so
%{_libdir}/pkgconfig/libsfdo-*.pc
