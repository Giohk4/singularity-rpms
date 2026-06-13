#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package singularity-desktop-session
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

%global         debug_package       %{nil}


Name:           singularity-desktop-session
Version:        0.1.0
Release:        1%{?dist}
Summary:        Singularity Desktop Environment Session.
License:        GPL-3.0-or-later
URL:            https://github.com/Giohk4/singularity-desktop-session
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  hicolor-icon-theme
BuildRequires:	adwaita-icon-theme

Requires:       singularity-shell
Requires:       labwc-sinty
Requires:       hicolor-icon-theme
Requires:       adwaita-icon-theme


%description
Desktop Session for the Singularity Desktop Environment.


%prep

%autosetup -n %{name}-%{version}

%build

%meson
%meson_build


%install

%meson_install

%files
%license LICENSE

%{_bindir}/singularity-session
%{_bindir}/singularity-start

%{_datadir}/wayland-sessions/singularity.desktop
%{_datadir}/xdg-desktop-portal/portals/singularity.portal
%{_datadir}/accountsservice/interfaces/com.singularity.Desktop.xml
%{_datadir}/glib-2.0/schemas/dev.sinty.desktop.gschema.xml


%{_datadir}/icons/Singularity/index.theme
%{_datadir}/icons/hicolor/scalable/apps/emblem-singularity.svg
%{_datadir}/icons/hicolor/scalable/apps/dev.sinty.workspaces.svg
%{_datadir}/singularity/labwc/rc.xml
%{_datadir}/singularity/labwc/themerc


%{_userunitdir}/singularity-polkit-agent.service
%{_userunitdir}/xdg-desktop-portal-singularity.service
%{_userunitdir}/xdg-desktop-portal-fix.service


%changelog
