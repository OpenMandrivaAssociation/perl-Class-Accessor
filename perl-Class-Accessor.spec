%define upstream_name    Class-Accessor
%define upstream_version 0.34

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        4

Summary:        Automated accessor generation
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module automagically generates accessor/mutators for your class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.340.0-3mdv2011.0
+ Revision: 680775
- mass rebuild

* Wed Apr 07 2010 Antoine Ginies <aginies@mandriva.com> 0.340.0-2mdv2011.0
+ Revision: 532666
- rebuild

* Wed Sep 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2010.0
+ Revision: 443471
- update to 0.34

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 401708
- rebuild using %%perl_convert_version
- fixed license field

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2010.0
+ Revision: 372088
- update to new version 0.33

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.31-3mdv2009.0
+ Revision: 255838
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.31-1mdv2008.1
+ Revision: 136680
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2008.0
+ Revision: 52484
- update to new version 0.31


* Tue Mar 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2007.1
+ Revision: 142370
- new version
- Import perl-Class-Accessor

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2007.0
- New version 0.27
- fic directory ownership
- better sumary

* Sat Apr 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.25-1mdk
- 0.25
- Add tests

* Sat Apr 01 2006 Buchan Milne <bgmilne@mandriva.org> 0.22-2mdk
- Rebuild
- use mkrel

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdk
- New release 0.22

* Tue Nov 16 2004 Oden Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.19-1mdk
- initial contrib.

