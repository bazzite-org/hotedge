%global uuid hotedge@jonathan.jdoda.ca

Name:          gnome-shell-extension-hotedge
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       A GNOME Shell extension that replaces the top-left hot corner with a bottom hot edge.

Group:         User Interface/Desktops
License:       GPLv2
URL:           https://github.com/KyleGospo/hotedge
Source0:       %{url}/archive/refs/heads/main.tar.gz
BuildArch:     noarch

BuildRequires: make
BuildRequires: unzip
BuildRequires: gettext
BuildRequires: gnome-shell

Requires:    gnome-shell >= 3.12
%description
A GNOME Shell extension that adds a hot edge that activates the overview to the bottom of the screen. This minimizes the pointer travel required to access the dash when using the new GNOME Shell 40 overview layout.

%prep
%autosetup -n hotedge-main

%install
make install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip build/%{uuid}.shell-extension.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
