Summary:	A very fast and comfortable imageviewer
Name:		kuickshow
Version: 	0.10.0
Release: 	1
Source0: 	http://download.kde.org/stable/%{name}/%{version}/%name-%version.tar.xz
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kde.org
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5PrintSupport) cmake(Qt5X11Extras)
BuildRequires:	cmake(KF5DocTools) cmake(KF5I18n) cmake(KF5IconThemes) cmake(KF5Init) cmake(KF5KIO) cmake(KF5WindowSystem) cmake(KF5XmlGui)
BuildRequires:	imlib-devel
Obsoletes: 	kdegraphics-kuickshow < 1:3.5.10-3
Conflicts:	kde-l10n < 3.5.9-5

%description
KuickShow is a very fast and comfortable imageviewer.

%files -f build/%{name}.lang
%_kde5_bindir/*
%_kde5_libdir/*.so
%_kde5_datadir/applications/*.desktop
%_kde5_datadir/%name
%_kde5_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake_kde5
%ninja
%find_lang %{name} --with-kde

%install
%{ninja_install} -C build
