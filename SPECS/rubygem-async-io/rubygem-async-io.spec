%global debug_package %{nil}
%global gem_name async-io
Summary:        Concurrent wrappers for native Ruby IO & Sockets
Name:           rubygem-%{gem_name}
Version:        1.33.0
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/socketry/async-io
Source0:        https://github.com/socketry/async-io/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  ruby
Requires:       rubygem-async
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
Async::IO provides builds on async and provides asynchronous
wrappers for IO, Socket, and related classes.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 1.30.1-1
- License verified
- Original version for CBL-Mariner
