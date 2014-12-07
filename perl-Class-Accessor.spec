%define upstream_name    Class-Accessor
%define upstream_version 0.34

Summary:	Automated accessor generation
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module automagically generates accessor/mutators for your class.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Class
%{_mandir}/man3/*

