%define real_name Startup

Summary:	Startup module for perl 
Name:		perl-%{real_name}
Version:	0.103
Release:	8
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWARTZ/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Startup module for perl

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/replace
%{perl_vendorlib}/Startup.pm
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.103-6mdv2010.0
+ Revision: 430543
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.103-5mdv2009.0
+ Revision: 258383
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.103-4mdv2009.0
+ Revision: 246445
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.103-2mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.103-2mdv2008.0
+ Revision: 86901
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.103-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.103-1mdk
- initial Mandriva package

