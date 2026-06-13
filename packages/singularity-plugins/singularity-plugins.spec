#
# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2026 Giohk404
#
# spec file for package singularity-plugins
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
%global 	commit      	798e2df99a0902f299ae5742f3e86cbccaee8447
%global 	shortcommit 	%(c=%{commit}; echo ${c:0:7})

%global		sinplug		%{_libdir}/singularity/plugins

Name:           singularity-plugins
Version:        0.1.0~git.%{snapshot}.%{shortcommit}
Release:        1%{?dist}
Summary:        metapackage for all the official Sinty Desktop plugins.
License:        GPL-3.0-only
URL:            https://github.com/singularityos-lab/%{name}

Source0:        %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(singularity-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)

Recommends:	%{name}-caffeine
Recommends:	%{name}-clipboard-history
Recommends:	%{name}-color-picker
Recommends:	%{name}-disk-usage
Recommends:	%{name}-downloads-dock
Recommends:	%{name}-emoji-search
Recommends:	%{name}-launcher-entry-dock
Recommends:	%{name}-media-controls
Recommends:	%{name}-mpris-dock
Recommends:	%{name}-pomodoro
Recommends:	%{name}-quick-notes
Recommends:	%{name}-status-monitor
Recommends:	%{name}-tailscale
Recommends:	%{name}-message-dock
Recommends:	%{name}-tray-icons
Recommends:	%{name}-weather
Recommends:	%{name}-workspace-indice
Recommends:	%{name}-exe-icon

Suggests:	%{name}-notification-test
Suggests:	%{name}-example-dock


Requires:	singularity-shell

%description
All of the official plugins for the Singularity Desktop shell.


%prep

%autosetup -n %{name}-%{commit}

%build

%meson
%meson_build


%install

%meson_install

%files
%license LICENSE





%package	caffeine
Summary:	Caffeine plugin for Singularity Desktop
Requires:	singularity-shell

%description	caffeine
Prevents the screen from sleeping or blanking.

%files		caffeine
%{sinplug}/caffeine/caffeine.plugin
%{sinplug}/caffeine/libcaffeine.so




%package	clipboard-history
Summary:	Clipboard History plugin for Singularity Desktop.
Requires:	singularity-shell

%description	clipboard-history
Keeps a history of clipboard entries accessible from the panel

%files		clipboard-history
%{sinplug}/clipboard-history/clipboard-history.plugin
%{sinplug}/clipboard-history/libclipboard-history.so




%package	color-picker
Summary:	ColorPicker plugin for Singularity Desktop.
Requires:	singularity-shell

%description	color-picker
Pick a color from the screen and copy its hex code to the clipboard.

%files		color-picker
%{sinplug}/color-picker/color-picker.plugin
%{sinplug}/color-picker/libcolor-picker.so




%package	disk-usage
Summary:	Disk Usgae monitor plugin for Singularity Desktop.
Requires:	singularity-shell

%description	disk-usage
Shows disk usage for key mount points in the sidebar

%files		disk-usage
%{sinplug}/disk-usage/disk-usage.plugin
%{sinplug}/disk-usage/libdisk-usage.so




%package	downloads-dock
Summary:	Dock download watcher plugin for Singularity Desktop.
Requires:	singularity-shell

%description	downloads-dock
Shows active browser downloads (Chrome, Chromium, Brave, Firefox, ...) as bubbles next to the browser icon in the dock.

%files		downloads-dock
%{sinplug}/downloads-dock/downloads-dock.plugin
%{sinplug}/downloads-dock/libdownloads-dock.so




%package	emoji-search
Summary:	Emoji seaarch providor plugin for Singularity Desktop.
Requires:	singularity-shell

%description	emoji-search
Adds an "emoji" search provider - type :smile, :fire, :rocket… and pick an emoji to copy to the clipboard.

%files		emoji-search
%{sinplug}/emoji-search/emoji-search.plugin
%{sinplug}/emoji-search/libemoji-search.so




%package	example-dock
Summary:	example alternative dock plugin for Singularity Desktop.
Requires:	singularity-shell

%description	example-dock
Demonstrates the ShellSurfaceProvider API by replacing the built-in dock with a minimal own-surface launcher. Enable to see the shell yield the bottom layer to a plugin.

%files		example-dock
%{sinplug}/example-dock/example-dock.plugin
%{sinplug}/example-dock/libexample-dock.so




%package	launcher-entry-dock
Summary:	Dock entries watcher plugin for Singularity Desktop
Requires:	singularity-shell

%description	launcher-entry-dock
istens to the Unity LauncherEntry DBus API (com.canonical.Unity.LauncherEntry) and surfaces per-app progress + badge counts in the dock. Out of the box this works for Nautilus, Files, Thunderbird, Steam, Mailspring and any other app that emits the standard signal.

%files		launcher-entry-dock
%{sinplug}/launcher-entry-dock/launcher-entry-dock.plugin
%{sinplug}/launcher-entry-dock/liblauncher-entry-dock.so




%package	media-controls
Summary:	Media controls panel plugin for Singularity Desktop
Requires:	singularity-shell

%description	media-controls
Shows MPRIS2 media player controls (prev, play/pause, next) in the panel

%files		media-controls
%{sinplug}/media-controls/libmedia-controls.so
%{sinplug}/media-controls/media-controls.plugin




%package	mpris-dock
Summary:	Media controls dock plugin for Singularity Desktop
Requires:	singularity-shell

%description	mpris-dock
Replaces the dock icon of any MPRIS-capable player (Spotify, Rhythmbox, etc.) with the album art, and shows prev/play/next controls next to it.

%files		mpris-dock
%{sinplug}/mpris-dock/libmpris-dock.so
%{sinplug}/mpris-dock/mpris-dock.plugin




%package	notification-test
Summary:	Example notification plugin for Singularity Desktop
Requires:	singularity-shell

%description	notification-test
Sends a test notification on startup

%files		notification-test
%{sinplug}/notification-test/libnotification-test.so
%{sinplug}/notification-test/notification-test.plugin




%package	pomodoro
Summary:	Pomodoro plugin for Singularity Desktop.
Requires:	singularity-shell

%description	pomodoro
Pomodoro timer in the panel with work/break cycle and notifications

%files		pomodoro
%{sinplug}/pomodoro/libpomodoro.so
%{sinplug}/pomodoro/pomodoro.plugin




%package	quick-notes
Summary:	Quick notes plugin for Singularity Desktop.
Requires:	singularity-shell

%description	quick-notes
Small sticky notes widget in the sidebar that auto-saves

%files		quick-notes
%{sinplug}/quick-notes/libquick-notes.so
%{sinplug}/quick-notes/quick-notes.plugin




%package	status-monitor
Summary:	Status monitor plugin for Singularity Desktop.
Requires:	singularity-shell

%description	status-monitor
Displays CPU usage in the panel

%files		status-monitor
%{sinplug}/status-monitor/libstatus-monitor.so
%{sinplug}/status-monitor/status-monitor.plugin




%package	tailscale
Summary:	Tailscale monitor plugin for Singularity Desktop.
Requires:	singularity-shell

%description	tailscale
Manage your Tailscale connection from Network settings

%files		tailscale
%{sinplug}/tailscale/libtailscale.so
%{sinplug}/tailscale/tailscale.plugin




%package	message-dock
Summary:	Messaging integration plugin for Singularity Desktop.
Requires:	singularity-shell

%description	message-dock
Shows unread chats from any messaging app (Telegram, Signal, Element, Slack, ...) as round avatar bubbles next to the app's dock icon. Auto-detects messaging apps via their .desktop Categories (InstantMessaging / Chat / IRCClient). Driven by desktop notifications - no login required.


%files		message-dock
%{sinplug}/telegram-dock/libtelegram-dock.so
%{sinplug}/telegram-dock/telegram-dock.plugin




%package	tray-icons
Summary:	System tray plugin for Singularity Desktop.
Requires:	singularity-shell

%description	tray-icons
Shows system tray icons from other applications


%files		tray-icons
%{sinplug}/tray-icons/libtray-icons.so
%{sinplug}/tray-icons/tray-icons.plugin




%package	weather
Summary:	Weather plugin for singularity Desktop.
Requires:	singularity-shell

%description	weather
Shows current weather in the panel fetched from wttr.in

%files		weather
%{sinplug}/weather/libweather.so
%{sinplug}/weather/weather.plugin




%package	workspace-indice
Summary:	Workspace indicator plugin for Singularity Desktop.
Requires:	singularity-shell

%description	workspace-indice
Shows workspace dots in the panel for quick navigation

%files		workspace-indice
%{sinplug}/workspaces-indicator/libworkspaces-indicator.so
%{sinplug}/workspaces-indicator/workspaces-indicator.plugin



%package	exe-icon
Summary:	Windows Executable Icons
Requires:	singularity-shell

%description	exe-icon
Show the embedded icon of Windows .exe files in the file manager.

%files		exe-icon
%{sinplug}/exe-icon/exe-icon.plugin
%{sinplug}/exe-icon/libexe-icon.so



%changelog
