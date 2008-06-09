%define major_version 1.1
%define minor_version 1

%define dsname fedora-ds
%define shortname fedora-admin
%define pkgname dirsrv

Summary:	Fedora Admin Server Management Console
Name:		fedora-admin-console
Version:	%{major_version}.%{minor_version}
Release:	1
License:	GPL v2
Group:		Applications/System
BuildArch:	noarch
Source0:	http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	e0f16a5a426a2c2bceefb5cfb99ea9c7
URL:		http://directory.fedoraproject.org
BuildRequires:	ant >= 1.6.2
BuildRequires:	idm-console-framework
BuildRequires:  jpackage-utils
BuildRequires:	ldapsdk
BuildRequires:  rpmbuild(macros) >= 1.300
Requires:	%{dsname}-admin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora Admin
Server.

%prep
%setup -q

%build
%ant \
	-Dconsole.location=%{_javadir} \
	-Dbuilt.dir=`pwd`/built

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
install built/package/%{shortname}* $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
install -d $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/admin/help
install help/en/*.html $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/admin
install help/en/tokens.map $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/admin
install help/en/help/*.html $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/manual/en/admin/help

# create symlinks
cd $RPM_BUILD_ROOT%{_datadir}/%{pkgname}/html/java
ln -s %{shortname}-%{version}.jar %{shortname}-%{major_version}.jar
ln -s %{shortname}-%{version}.jar %{shortname}.jar
ln -s %{shortname}-%{version}_en.jar %{shortname}-%{major_version}_en.jar
ln -s %{shortname}-%{version}_en.jar %{shortname}_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{version}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{major_version}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{version}_en.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}-%{major_version}_en.jar
%{_datadir}/%{pkgname}/html/java/%{shortname}_en.jar
%dir %{_datadir}/%{pkgname}/manual/en/admin
%{_datadir}/%{pkgname}/manual/en/admin/tokens.map
%doc %{_datadir}/%{pkgname}/manual/en/admin/*.html
%doc %{_datadir}/%{pkgname}/manual/en/admin/help/*.html
