%define svn 1060448

Summary:	A very fast and comfortable imageviewer
Name:		kuickshow
Version: 	0.9.2
Release: 	%mkrel 0.%svn.2
Source0: 	http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%name-%version.%svn.tar.bz2
Patch1:     kuickshow-0.9.2-fix-imlib-init.patch
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

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/*
%_kde_libdir/*.so
%_kde_datadir/applications/kde4/*.desktop
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -qn %name
%patch1 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
