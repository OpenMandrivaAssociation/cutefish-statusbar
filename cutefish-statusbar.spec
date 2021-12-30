%define _empty_manifest_terminate_build 0

%define oname statusbar

Name:           cutefish-statusbar
Version:        0.7
Release:        1
Summary:        Top status bar
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cutefishos/statusbar
Source:         https://github.com/cutefishos/statusbar/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)

%description
The status bar at the top displays the current status of the system, such
as time, system tray, etc.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
mkdir -p build
pushd ./build
# FIXME: you should use the %%cmake macros
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build
popd

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
