%define libname %mklibname KF6Notifications
%define devname %mklibname KF6Notifications -d
%define git 20230513

Name: kf6-knotifications
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/knotifications/-/archive/master/knotifications-master.tar.bz2#/knotifications-%{git}.tar.bz2
Summary: KNotification is used to notify the user of an event
URL: https://invent.kde.org/frameworks/knotifications
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
Requires: %{libname} = %{EVRD}

%description
KNotification is used to notify the user of an event.

%package -n %{libname}
Summary: KNotification is used to notify the user of an event
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KNotification is used to notify the user of an event.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KNotification is used to notify the user of an event.

%prep
%autosetup -p1 -n knotifications-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/knotifications.*
%{_datadir}/dbus-1/interfaces/*.xml

%files -n %{devname}
%{_includedir}/KF6/KNotifications
%{_libdir}/cmake/KF6Notifications
%{_qtdir}/mkspecs/modules/qt_KNotifications.pri
%{_qtdir}/doc/KF6Notifications.*

%files -n %{libname}
%{_libdir}/libKF6Notifications.so*
%{_qtdir}/qml/org/kde/notification
