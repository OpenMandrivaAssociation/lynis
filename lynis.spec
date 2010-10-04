
%define _includedir	/usr/share/lynis/include
%define _pluginsdir	/usr/share/lynis/plugins
%define _dbdir	        /usr/share/lynis/db
%define _bindir		/usr/bin

Summary:		Security and system auditing tool
Name:			lynis
Version:		1.2.9
Release:		%mkrel 1
License:		GPL
Group:			Applications/System
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
%setup 



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

