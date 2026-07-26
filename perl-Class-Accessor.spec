%define upstream_name    Class-Accessor
Summary:	Automated accessor generation
Name:		perl-%{upstream_name}
Version:	0.51
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Class-Accessor
Source0:	https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module automagically generates accessor/mutators for your class.

%prep
%setup -qn %{upstream_name}-%{version}

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

