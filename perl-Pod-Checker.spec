%{?scl:%scl_package perl-Pod-Checker}

Name:           %{?scl_prefix}perl-Pod-Checker
# Compete with perl.spec
Epoch:          4
Version:        1.73
Release:        451%{?dist}
Summary:        Check POD documents for syntax errors
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Pod-Checker
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAREKR/Pod-Checker-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  %{?scl_prefix}perl(Pod::Simple) >= 3.28
BuildRequires:  %{?scl_prefix}perl(Pod::Simple::Methody)
# Pod::Usage not used at tests
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(FileHandle)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(vars)
# VMS::Filespec not used
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Pod::Simple) >= 3.28

%description
Module and tools to verify POD documentation contents for compliance with the
Plain Old Documentation format specifications.

%prep
%setup -q -n Pod-Checker-%{version}
for F in CHANGES README; do
    sed -i -e 's/\r//' "$F"
done

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.73-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.73-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.73-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.73-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 Petr Pisar <ppisar@redhat.com> - 4:1.73-1
- 1.73 bump

* Tue May 24 2016 Petr Pisar <ppisar@redhat.com> - 4:1.72-1
- 1.72 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.71-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4:1.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:1.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4:1.71-4
- Perl 5.22 rebuild

* Thu Nov 13 2014 Petr Pisar <ppisar@redhat.com> - 4:1.71-3
- Compete with perl.spec's epoch (bug #1163490)

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.71-2
- Perl 5.20 rebuild

* Mon Jun 23 2014 Petr Pisar <ppisar@redhat.com> - 1.71-1
- 1.71 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Petr Pisar <ppisar@redhat.com> - 1.70-1
- 1.70 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.60-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1.60-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.60-2
- Perl 5.18 rebuild

* Mon Feb 04 2013 Petr Pisar <ppisar@redhat.com> 1.60-1
- Specfile autogenerated by cpanspec 1.78.
