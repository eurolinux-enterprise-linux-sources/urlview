%global gitdate 20121210
%global gitrev 6cfcad
Name:           urlview
Version:        0.9
Release:        13.%{gitdate}git%{gitrev}%{?dist}
Summary:        URL extractor/launcher

Group:          Applications/Internet
License:        GPLv2+
URL:            https://github.com/sigpipe/urlview
# git clone git://github.com/sigpipe/urlview.git; cd urlview
# git archive --prefix=urlview/ %{gitrev} | xz > urlview-%{gitdate}git%{gitrev}.tar.xz
Source0:        %{name}-%{gitdate}git%{gitrev}.tar.xz

BuildRequires:  ncurses-devel

# mutt packages before 5:1.5.16-2 included urlview
Conflicts:      mutt < 5:1.5.16-2

Patch1:         urlview-default.patch

%description
urlview is a screen oriented program for extracting URLs from text
files and displaying a menu from which you may launch a command to
view a specific item.

%prep
%setup -q -n %{name}
%patch1 -p1 -b .default

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man{1,5}}
install -p -m644 urlview.conf.suse $RPM_BUILD_ROOT%{_sysconfdir}/urlview.conf
install -p urlview url_handler.sh $RPM_BUILD_ROOT%{_bindir}
install -p -m644 urlview.man $RPM_BUILD_ROOT%{_mandir}/man1/urlview.1
echo '.so man1/urlview.1' > $RPM_BUILD_ROOT%{_mandir}/man5/urlview.conf.5
echo '.so man1/urlview.1' > $RPM_BUILD_ROOT%{_mandir}/man1/url_handler.sh.1

%files
%doc AUTHORS ChangeLog COPYING README sample.urlview
%config(noreplace) %{_sysconfdir}/urlview.conf
%{_bindir}/urlview
%{_bindir}/url_handler.sh
%{_mandir}/man1/urlview.1*
%{_mandir}/man1/url_handler.sh.1*
%{_mandir}/man5/urlview.conf.5*

%changelog
* Fri May 24 2013 Miroslav Lichvar <mlichvar@redhat.com> 0.9-13.20121210git6cfcad
- add man page link for url_handler.sh
- fix default paths in man page

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12.20121210git6cfcad
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 14 2012 Miroslav Lichvar <mlichvar@redhat.com> 0.9-11.20121210git6cfcad
- update to 20121210git6cfcad
- remove obsolete macros

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Miroslav Lichvar <mlichvar@redhat.com> 0.9-7
- add man page link for urlview.conf (#526162)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9-3
- update license tag

* Fri Jun 29 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9-2
- add conflict with mutt, fix URL (#245951)

* Wed Jun 27 2007 Miroslav Lichvar <mlichvar@redhat.com> 0.9-1
- split from mutt package
