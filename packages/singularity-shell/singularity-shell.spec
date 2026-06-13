#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package singularity-shell
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
%global 	snapshot    	20260614
%global 	commit      	5d3fe39090bf772495f9934876a6a9d44266a050
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

Name:           singularity-shell
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        The desktop shell for the Singularity Desktop Environment.
License:        GPL-3.0-only
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:		fix-wayland-headers.patch	

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc
BuildRequires:	vetro

BuildRequires:  pkgconfig(singularity-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libpng)
BuildRequires:	pkgconfig(gnome-desktop-4.0)
BuildRequires:	mpv-devel
BuildRequires:	pam-devel
BuildRequires:	gettext-devel
BuildRequires:	libdecor-devel
BuildRequires:	systemd-devel
BuildRequires:	gstreamer-devel
%if	0%{?fedora}
BuildRequires:	pixman-devel
%else
BuildRequires:	libpixman-1-0-devel


Requires:       singularity-polkit-agent
Requires:	libsingularity
Requires:	labwc-sinty
Requires:	xdg-desktop-portal-singularity
Requires:	singularity-desktop-session
Requires:	bluez
Requires:	NetworkManager-libnm
Requires:	wl-clipboard
Requires:	cliphist
Requires:	upower
Requires:	mpv
Requires:	gnome-online-accounts
Requires:	pipewire-pulseaudio

Recommends:     ibus




%description
The desktop shell for the Singularity Desktop Environment.

%prep

%autosetup -n %{name}-%{commit} -p1

%build

%meson
%meson_build


%install

%meson_install

%files

%license LICENSE
%config(noreplace) /etc/pam.d/singularity-lockscreen

%{_bindir}/singularity-desktop
%{_bindir}/singularity-keyboard-reset
%{_bindir}/singularity-lockscreen
%{_bindir}/singularity-region-picker
%{_bindir}/singularity-screenshot

%{_datadir}/glib-2.0/schemas/dev.sinty.lockscreen.gschema.xml

%changelog
