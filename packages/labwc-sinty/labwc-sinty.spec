#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package labwc-sinty
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

%global 	debug_package	%{nil}
%global 	snapshot	20260609
%global 	commit		77ec8147176af5de118357c418418b9d0695eaab
%global 	shortcommit	%(c=%{commit}; echo ${c:0:7})

%global		oname		labwc

Name:		%{oname}-sinty
Version:	0.9.5~git.%{snapshot}.%{shortcommit}
Release:	1%{?dist}
Summary:	Fork of LabWC used by the Sinty Desktop

License:	GPL-2.0-only
URL:		https://github.com/singularityos-lab/%{oname}
Source0:	%{URL}/archive/%{commit}/%{oname}-%{shortcommit}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:	git
BuildRequires: 	systemd
%if		0%{?suse_version}
BuildRequires:  ninja
%else
BuildRequires:	ninja-build
%endif
BuildRequires:	hicolor-icon-theme

BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xwaylandproto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libseat)
BuildRequires:	pkgconfig(libsfdo-basedir)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(scdoc)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wlroots-0.20)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xwayland)

%if		0%{?suse_version}
Requires:	Mesa-dri
%else
Requires:	mesa-dri-drivers
%endif
Requires:	xdg-desktop-portal-wlr
Recommends:	grim
Recommends:	alacritty
Recommends:	%{name}-session

# i have no will to try and make both work at the same time.
Provides:	%{oname}
Obsoletes:	%{oname}
Conflicts:	%{oname}

%description
This is fork of the original labWC project made with certain patches in mind to allow compatibility with the Sinty Desktop enviroment.

%prep
%autosetup -n %{oname}-%{commit}

%build
%meson \
    -Dman-pages=enabled \
    -Dxwayland=enabled \
    -Dnls=enabled \
    %{nil}
%meson_build

%install

%meson_install
%find_lang %{oname}

%files

%license LICENSE

%{_bindir}/%{oname}
%{_bindir}/lab-sensible-terminal
%{_bindir}/labnag

%{_datadir}/xdg-desktop-portal/%{oname}-portals.conf
%{_userunitdir}/%{oname}-session.target

%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/doc/%{oname}/*



%package lang
Summary: Translations for labwc-sinty
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description lang
Translations for labwc-sinty.

%files lang -f %{oname}.lang


%package	session
Summary:	base-labwc session
Requires:	%{name} = %{version}-%{release}
Requires:	hicolor-icon-theme


Conflicts:	%{oname}-session
Obsoletes:	%{oname}-session

BuildArch:	noarch

%description session
This package provides the labwc session files to run labwc as a
standalone environment.

%files session
%{_datadir}/wayland-sessions/%{oname}.desktop
%{_datadir}/icons/hicolor/*/*/%{oname}*.svg

%changelog


