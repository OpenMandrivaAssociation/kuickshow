Summary:	A very fast and comfortable imageviewer
Name:		kuickshow
Version: 	0.9.1
Release: 	%mkrel 2
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version-kde4.2.4.tar.bz2
Patch0:		kuickshow-0.9.1-doc-install.patch
License: 	GPLv2+
Group: 		Graphics
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	imlib-devel
Obsoletes: 	kdegraphics-kuickshow < 1:3.5.10-3
Conflicts:	kde-l10n < 3.5.9-5

%description
KuickShow is a very fast and comfortable imageviewer.

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -qn %name-%version-kde4.2.4
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
