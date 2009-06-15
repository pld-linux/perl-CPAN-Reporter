#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CPAN
%define	pnam	Reporter
Summary:	CPAN::Reporter - Adds CPAN Testers reporting to CPAN.pm
#Summary(pl.UTF-8):	
Name:		perl-CPAN-Reporter
Version:	1.1708
Release:	1
License:	Apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68e38ac6a4ad4404da66d8c828b59e63
URL:		http://search.cpan.org/dist/CPAN-Reporter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::pushd) >= 0.32
BuildRequires:	perl(IO::CaptureOutput) >= 1.03
BuildRequires:	perl(Probe::Perl)
BuildRequires:	perl(Tee) >= 0.13
BuildRequires:	perl-Config-Tiny >= 2.08
BuildRequires:	perl-CPAN >= 1.9203
BuildRequires:	perl-File-Copy-Recursive >= 0.35
BuildRequires:	perl-File-HomeDir >= 0.58
BuildRequires:	perl-Test-Reporter >= 1.34
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CPAN Testers project captures and analyses detailed results from building
and testing CPAN distributions on multiple operating systems and multiple
versions of Perl.  This provides valuable feedback to module authors and
potential users to identify bugs or platform compatibility issues and improves
the overall quality and value of CPAN.

One way individuals can contribute is to send a report for each module that
they test or install.  CPAN::Reporter is an add-on for the CPAN.pm module to
send the results of building and testing modules to the CPAN Testers project.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/CPAN/*.pm
%{perl_vendorlib}/CPAN/Reporter
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
