%define debug_package %{nil}

Summary:	Nagios plugin - check_crond
Name:		nagios-plugins-crond
Version:	1.3
Release:	4.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		http://thesharp.ru/nagios-plugins/
Source0:	http://thesharp.ru/nagios-plugins/crond/nagios-plugins-crond-%{version}.tar.gz
Requires:	nagios-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A plugin for nagios that will check crond.

%prep
%setup -q -n nagios-plugins-crond-%{version}
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" check_crond

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 check_crond %{buildroot}%{_libdir}/nagios/plugins/check_crond

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog
%{_libdir}/nagios/plugins/check_crond

%changelog
* Sun Sep 22 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.3-4.vortex
- Change summary.

* Sun Sep 18 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.3-3.vortex
- Remove dot from summary.

* Thu Sep 08 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.3-2.vortex
- Vortex rebranding.

* Tue Jul 26 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.3-1
- New upstream release.
- Internal ChangeLog file was added to docs.

* Tue Jul 26 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.2-1
- New upstream release.

* Mon Jul 25 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-1
- New upstream release.

* Tue Apr  5 2011  Ilya A. Otyutskiy <otyutskiy@wiw.ru> - 1.0-1
- Initial packaging for CentOS.

