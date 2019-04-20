#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Handler-Trees
Version  : 0.02
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/E/EB/EBOHLMAN/XML-Handler-Trees-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EB/EBOHLMAN/XML-Handler-Trees-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-handler-trees-perl/libxml-handler-trees-perl_0.02-7.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-XML-Handler-Trees-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
XML::Handler::Trees - PerlSAX handlers for building tree structures
SYNOPSIS
use XML::Handler::Trees;
use XML::Parser::PerlSAX;

%package dev
Summary: dev components for the perl-XML-Handler-Trees package.
Group: Development
Provides: perl-XML-Handler-Trees-devel = %{version}-%{release}

%description dev
dev components for the perl-XML-Handler-Trees package.


%package license
Summary: license components for the perl-XML-Handler-Trees package.
Group: Default

%description license
license components for the perl-XML-Handler-Trees package.


%prep
%setup -q -n XML-Handler-Trees-0.02
cd ..
%setup -q -T -D -n XML-Handler-Trees-0.02 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-Handler-Trees-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Handler-Trees
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-XML-Handler-Trees/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/XML/Handler/Trees.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Handler::Trees.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Handler-Trees/deblicense_copyright
