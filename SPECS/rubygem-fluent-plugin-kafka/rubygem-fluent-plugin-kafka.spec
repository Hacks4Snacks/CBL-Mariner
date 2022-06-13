%global debug_package %{nil}
%global gem_name fluent-plugin-kafka
Summary:        Kafka input and output plugin for Fluentd
Name:           rubygem-fluent-plugin-kafka
Version:        0.17.5
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/fluent/fluent-plugin-kafka
Source0:        https://github.com/fluent/fluent-plugin-kafka/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby
Requires:       rubygem-fluentd
Requires:       rubygem-ltsv
Requires:       rubygem-ruby-kafka < 2
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
A fluentd plugin to both consume and produce data for Apache Kafka.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add LICENSE file to buildroot from Source0
cp LICENSE %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 0.13.0-1
- License verified
- Original version for CBL-Mariner
