%global debug_package %{nil}
%global gem_name semantic_puppet

Summary:        Useful tools for working with Semantic Versions
Name:           rubygem-%{gem_name}
Version:        1.0.4
Release:        3%{?dist}
Group:          Development/Languages
License:        MIT
Vendor:         Microsoft Corporation
Distribution:	Mariner
URL:            https://github.com/puppetlabs/semantic_puppet
Source0:        https://github.com/puppetlabs/semantic_puppet/archive/refs/tags/%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
Tools used by Puppet to parse, validate, and compare Semantic Versions and
Version Ranges and to query and resolve module dependencies.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add LICENSE file to buildroot from Source0
cp LICENSE %{buildroot}%{gem_instdir}/
#add lib folder to buildroot from Source0
cp -r lib/ %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gem_instdir}/lib
%{gemdir}

%changelog
* Tue May 03 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 1.0.4-3
- Add lib/ from source.

* Tue Mar 22 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 1.0.4-2
- Build from .tar.gz source.

* Tue Oct 19 2021 Suresh Babu Chalamalasetty <schalam@microsoft.com> - 1.0.4-1
- Original version for CBL-Mariner
- License verified
