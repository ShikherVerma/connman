#
# spec file for package connman
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define systemd_present		(0%{?suse_version} != 1110)
%define	openconnect_present	(0%{?suse_version} != 1110 && 0%{?suse_version} != 1315)

# hh2serial and tist is not building correctly on PPC and I don't intend to fix that
%ifarch ppc ppc64
%define hh2serial_working	0
%define tist_working		0
%else
%define hh2serial_working	1
%define tist_working		1
%endif

Name:           connman
Version:        1.30
Release:        0
Summary:        Connection Manager
License:        GPL-2.0
Group:          System/Daemons
Url:            http://www.moblin.org/
Source0:        http://www.kernel.org/pub/linux/network/connman/connman-%{version}.tar.gz
Source1:        http://www.kernel.org/pub/linux/network/connman/connman-%{version}.tar.sign
Source2:        %{name}.keyring
Source3:        connman-rpmlintrc
BuildRequires:  dhcp
BuildRequires:  openvpn
BuildRequires:  readline-devel
BuildRequires:  wpa_supplicant
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(xtables)
#Docs do not build! Omit for now
#BuildRequires: gtk-doc
#Requires: glib2 >= 2.22
#Requires: dbus-1 >= 1.0
Requires:       bluez
Requires:       dhcp >= 3.0.2
Requires:       iptables
Requires:       wpa_supplicant
%if %{systemd_present}
BuildRequires:  systemd
%if 0%{?suse_version} >= 1210
%{?systemd_requires}
%else
Requires:       systemd
%endif
%endif #systemd_present

%description
Connection Manager provides a daemon for managing Internet connections
within embedded devices running the Linux operating system.

%package devel
Summary:        Development files for Connection Manager
Group:          Development/Libraries/C and C++
Requires:       %{name} >= %{version}

%description devel
connman-devel contains development files for use with connman.

%package doc
Summary:        Connman reference man pages
License:        GPL-2.0
Group:          Documentation/Man

%description doc
Documentation in form of man pages for connman

##############################
#Plugins
##############################

%if %{hh2serial_working}
%package plugin-hh2serial-gps
Summary:        HH2Serial GPS plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-hh2serial-gps
Provides HH2Serial GPS device support for Connman (Connection Manager).
%endif
#-------------------------------------

%if %{openconnect_present}
%package plugin-openconnect
Summary:        OpenConnect plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  pkgconfig(openconnect)
Requires:       %{name} >= %{version}
Requires:       dbus-1 >= 1.0
Requires:       openconnect

%description plugin-openconnect
Provides OpenConnect support for Connman (Connection Manager).
OpenConnect is an open client for Cisco(TM) AnyConnect(TM) VPN.
#-------------------------------------
%endif #openconnect_present

%package plugin-vpnc
Summary:        VPNC plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  vpnc
Requires:       %{name} >= %{version}
Requires:       vpnc

%description plugin-vpnc
Provides VPNC support for Connman (Connection Manager).
#-------------------------------------

%package plugin-openvpn
Summary:        OpenVPN plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  openvpn
Requires:       %{name} >= %{version}
Requires:       openvpn

%description plugin-openvpn
Provides OpenVPN support for Connman (Connection Manager).
#-------------------------------------

%package plugin-pptp
Summary:        PPTP plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  vpnc
Requires:       %{name} >= %{version}
Requires:       vpnc

%description plugin-pptp
Provides PPTP support for Connman (Connection Manager).
#-------------------------------------

%if %{tist_working}
%package plugin-tist
Summary:        TIST plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-tist
Provides TI Shared Transport support for Connman (Connection Manager).
%endif # tist_working
#-------------------------------------

%package plugin-l2tp
Summary:        L2TP plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description plugin-l2tp
Provides L2TP (Layer 2 Tunneling Protocol) support for Connman (Connection Manager).
#-------------------------------------

%package plugin-iospm
Summary:        Intel OSPM plugin for connman (Connection Manager)
Group:          System/Daemons
BuildRequires:  ppp-devel
Requires:       %{name} >= %{version}
Requires:       ppp

%description plugin-iospm
Provides Intel OSPM support for Connman (Connection Manager).
#-------------------------------------

%package test
Summary:        Test and example scripts for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description test
Provides test and example scripts for Connman (Connection Manager).
#-------------------------------------

%package nmcompat
Summary:        NetworkManager compatibility for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description nmcompat
Provides NetworkManager compatibility for Connman (Connection Manager).
#-------------------------------------

%package plugin-polkit
Summary:        PolicyKit plugin for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}
Requires:       dbus-1 >= 1.0
Requires:       polkit

%description plugin-polkit
Provides PolicyKit support for Connman (Connection Manager).
#-------------------------------------

%package client
Summary:        Client script for connman (Connection Manager)
Group:          System/Daemons
Requires:       %{name} >= %{version}

%description client
Provides client interface for Connman (Connection Manager).
#-------------------------------------
#%package session_policy
#
#Summary:        Session policy for connman (Connection Manager)
#Group:          System/Daemons
#Requires:       %{name} >= %{version}
#
#%description session_policy
#Provides client interface for Connman (Connection Manager).
#-------------------------------------

%prep
%setup -q -n connman-%{version}

%build

# Using i586 repository, so explicitly forward it to CC.
# Necesary, because i386 will fail due to:
# undefined reference to `__sync_add_and_fetch_4'
# Restrict to Fedora right for now.
%if 0%{?fedora}
%ifarch i386 i486 i586
CFLAGS='-O2 -g -march=i586 -mtune=i686'
export CFLAGS
CXXFLAGS='-O2 -g -march=i586 -mtune=i686'
export CXXFLAGS
FFLAGS='-O2 -g -march=i586 -mtune=i686'
export FFLAGS
%endif
%endif

%configure --enable-shared \
%if %{systemd_present}
           --with-systemdunitdir=%{_unitdir} \
%endif
           --disable-gtk-doc \
           --disable-debug \
           --enable-pie \
           --enable-threads \
%if %{hh2serial_working}	   
           --enable-hh2serial-gps \
%endif
%if %{openconnect_present}
           --enable-openconnect \
%endif
           --enable-openvpn \
           --enable-vpnc \
           --enable-l2tp \
           --enable-pptp \
           --disable-iwmx \
           --enable-iospm \
%if %{tist_working}
           --enable-tist \
%endif
           --enable-session-policy \
           --enable-test \
           --enable-nmcompat \
           --enable-polkit \
           --enable-loopback \
           --enable-ethernet \
           --enable-wifi \
           --enable-bluetooth \
           --enable-ofono \
           --enable-dundee \
           --enable-pacrunner \
           --enable-wispr \
           --enable-client \
           --enable-tools \
           --enable-datafiles


make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}/%{_bindir}
install -m755 client/connmanctl %{buildroot}/%{_bindir}/connmanctl
find %{buildroot} -type f -name "*.la" -delete -print
%if ! %{openconnect_present}
rm %{buildroot}%{_libdir}/%{name}/scripts/openconnect-script
%endif

%if 0%{?suse_version} >= 1210
%pre
%service_add_pre connman.service
%service_add_pre connman-vpn.service
%endif

%post
/sbin/ldconfig
%if 0%{?suse_version} >= 1210
%service_add_post connman.service
%service_add_post connman-vpn.service
%endif

%if 0%{?suse_version} >= 1210
%preun
%service_del_preun connman.service
%service_del_preun connman-vpn.service
%endif

%postun
/sbin/ldconfig
%if 0%{?suse_version} >= 1210
%service_del_postun connman.service
%service_del_postun connman-vpn.service
%endif

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%if %{hh2serial_working}
%post plugin-hh2serial-gps -p /sbin/ldconfig
%postun plugin-hh2serial-gps -p /sbin/ldconfig
%endif

%if %{openconnect_present}
%post plugin-openconnect -p /sbin/ldconfig
%postun plugin-openconnect -p /sbin/ldconfig
%endif

%post plugin-vpnc -p /sbin/ldconfig
%postun plugin-vpnc -p /sbin/ldconfig

%post plugin-iospm -p /sbin/ldconfig
%postun plugin-iospm -p /sbin/ldconfig

%post plugin-l2tp -p /sbin/ldconfig
%postun plugin-l2tp -p /sbin/ldconfig

%post plugin-openvpn -p /sbin/ldconfig
%postun plugin-openvpn -p /sbin/ldconfig

%post plugin-pptp -p /sbin/ldconfig
%postun plugin-pptp -p /sbin/ldconfig

%if %{tist_working}
%post plugin-tist -p /sbin/ldconfig
%postun plugin-tist -p /sbin/ldconfig
%endif

#%%post session_policy -p /sbin/ldconfig
#%%postun session_policy -p /sbin/ldconfig

# enable service automaticly
# Currently disabled as per http://en.opensuse.org/openSUSE:Systemd_packaging_guidelines
# enable connman.service

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_sbindir}/connmand
%{_sbindir}/connman-vpnd
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins-vpn
%config %{_sysconfdir}/dbus-1/system.d/connman.conf
%config %{_sysconfdir}/dbus-1/system.d/connman-vpn-dbus.conf
%{_datadir}/dbus-1/system-services/net.connman.vpn.service
%if %{systemd_present}
%{_unitdir}/connman.service
%{_unitdir}/connman-vpn.service
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-, root, root)
%{_mandir}/*/*

#plugins

%if %{hh2serial_working}
%files plugin-hh2serial-gps
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/hh2serial-gps.so
%endif

%if %{openconnect_present}
%files plugin-openconnect
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins-vpn/openconnect.so
%{_libdir}/%{name}/scripts/openconnect-script
%endif

%files plugin-vpnc
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins-vpn/vpnc.so

%files plugin-iospm
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/iospm.so

%files plugin-l2tp
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins-vpn/l2tp.so
%{_libdir}/%{name}/scripts/libppp-plugin.so*

%files plugin-openvpn
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins-vpn/openvpn.so
%{_libdir}/%{name}/scripts/openvpn-script

%files plugin-pptp
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins-vpn/pptp.so

%if %{tist_working}
%files plugin-tist
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/tist.so
%endif

%files test
%defattr(-,root,root,-)
%{_libdir}/%{name}/test

%files nmcompat
%defattr(-,root,root,-)
%config %{_sysconfdir}/dbus-1/system.d/connman-nmcompat.conf

%files plugin-polkit
%defattr(-,root,root,-)
%{_datadir}/polkit-1/actions/net.connman.policy
%{_datadir}/polkit-1/actions/net.connman.vpn.policy

%files client
%defattr(-,root,root,-)
%{_bindir}/connmanctl

#%%files session_policy
#%%defattr(-,root,root,-)
#%%{_libdir}/connman/plugins/session_policy.so

%changelog
