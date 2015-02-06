
%define _includedir	/usr/share/lynis/include
%define _pluginsdir	/usr/share/lynis/plugins
%define _dbdir		/usr/share/lynis/db
%define _bindir		/usr/bin

Summary:		Security and system auditing tool
Name:			lynis
Version:		1.2.9
Release:		2
License:		GPL
Group:			System/Configuration/Other
Source:			lynis-%{version}.tar.gz
BuildRoot:		 %{_tmppath}/%{name}-%{version}-build  
URL:			http://www.rootkit.nl/
BuildArch:		noarch
%if 0%{?mandriva_version}
BuildRequires: spec-helper
%endif

%description
Lynis is a security and system auditing tool. It scans a system on the


most interesting parts useful for audits, like:
     - Security enhancements
     - Logging and auditing options
     - Banner identification
     - Software availability

Lynis is released as a GPL licensed project and free for everyone to use.

See http://www.rootkit.nl for a full description and documentation.

%prep


# Make directory with our name, instead of with version
%setup -q



%build

%install
# Install profile
install -d ${RPM_BUILD_ROOT}/etc/lynis
install default.prf ${RPM_BUILD_ROOT}/etc/lynis
# Install binary
install -d ${RPM_BUILD_ROOT}/%{_bindir}
install lynis ${RPM_BUILD_ROOT}/%{_bindir}
# Install man page
install -d ${RPM_BUILD_ROOT}/%{_mandir}/man8
install lynis.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
# Install functions/includes
install -d ${RPM_BUILD_ROOT}%{_includedir}
install include/* ${RPM_BUILD_ROOT}%{_includedir}
# Install plugins
install -d ${RPM_BUILD_ROOT}%{_pluginsdir}
install plugins/* ${RPM_BUILD_ROOT}%{_pluginsdir}
# Install database files
install -d ${RPM_BUILD_ROOT}%{_dbdir}
install db/* ${RPM_BUILD_ROOT}%{_dbdir}


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
# Binaries

%{_bindir}/lynis
# Man page and docs
%doc CHANGELOG FAQ LICENSE README
%doc %{_mandir}/man8/lynis.8.*
/etc/lynis/default.prf
%{_dbdir}/*
%{_includedir}/*
%{_pluginsdir}/*
%dir /etc/lynis
%dir /usr/share/lynis
%dir /usr/share/lynis/db
%dir /usr/share/lynis/include
%dir /usr/share/lynis/plugins



%changelog
* Mon Oct 04 2010 Zombie Ryushu <ryushu@mandriva.org> 1.2.9-1mdv2011.0
+ Revision: 582920
- Fix group
- Fix group
- import lynis



* Wed Oct 08 2008 -n mrdocs at opensuse.org
- change the files listing to pacify rpmlint
* Tue Aug 26 2008 -n mrdocs at opensuse.org
- 1.2.1 release
* Tue Aug 26 2008 -n mrdocs at opensuse.org
- 1.2.0 release
* Sun Aug 10 2008 -n mrdocs at opensuse.org
- New test: AppArmor framework check [MACF-6204]
- New test: FreeBSD boot loader test [BOOT-5124]
- New test: PHP option register_globals [PHP-2368]
- New test: Promiscuous network interfaces (Linux) [NETW-3015]
- Report option 'bootloader' added to several tests
- Added readlink binary check
- Extended file check (IsWorldWritable) for symlinks
- Added /usr/local/etc to sudoers test [AUTH-9250]
- Improved FreeBSD banner output [BANN-7113]
- Removed incorrect line at promiscuous interface test [NETW-3014]
- Fix: Show only once the GRUB test output [BOOT-5121]
- Fix: Typo in NTP test [TIME-3104]
- Fix: Skip NTP test in /etc/cron.d if empty [TIME-3104]
- Fix: Initialize values when performing an update check without connection
- Fix: Solaris id function has been fixed
- Disabled FreeBSD double packages tests, due minor issues [PKGS-7303]
- Changed LDAP/MySQL running states [LDAP-2219] [DBS-1804]
- Replaced ifconfig calls with IFCONFIGBINARY
- Renamed tests_auditing to tests_mac_frameworks
- Several tests improved with extended logging

* Thu Jul 17 2008 -n mrdocs at opensuse.org
- several improved tests for networking, php, LDAP, NTP, and MySQL
- extended support for Mac OS X and Solaris
- updated documentation on the Web site, profile, and FAQ. 
* Sun Jun 29 2008 -n mrdocs at opensuse.org
- It also fixes several incorrect messages, has improved logging, SuSE Linux detection
- and a better way of collecting the warning messages
* Fri Jun 20 2008 -n mrdocs at opensuse.org
- This release adds a big amount of new tests including syslog
- Solaris zones, LDAP authentication, iptables, sudoers files
- and home directories. 
- improved warning/error messages, improved logging, ID reassignments
- few small bugfixes. 

* Wed Jun 11 2008 -n mrdocs at opensuse.org
- new version 
* Sun Jun 01 2008 -n mrdocs at opensuse.org
- first build server package

