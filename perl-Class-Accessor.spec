%define upstream_name    Class-Accessor
%define upstream_version 0.51

Summary:	Automated accessor generation
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Class-Accessor
Source0:	https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
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

