#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package singularity-polkit-agent
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
%global 	commit      	856cf43feb91a84c008203cfeecbf81c2eb7b877
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

Name:           singularity-polkit-agent
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        Polkit agent for Singularity Desktop.
License:        LGPL-2.1-only
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(singularity-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(polkit-agent-1)

%description
A lightweight Polkit authentication agent for the Singularity Desktop Environment.

%prep

%autosetup -n %{name}-%{commit}

%build

%meson
%meson_build


%install

%meson_install

%files

#%license LICENSE     there is no license file in the root repo for now so....
%{_libexecdir}/singularity-polkit-agent
%{_libexecdir}/singularity-polkit-auth-helper


%changelog
