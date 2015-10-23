# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       nodejs

# >> macros
# << macros

Summary:    Evented I/O for V8 JavaScript
Version:    v4.2.1
Release:    1
Group:      Development/Languages
License:    MIT
URL:        http://www.nodejs.org
Source0:    %{name}-%{version}.tar.gz
Source100:  nodejs.yaml
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  curl
BuildRequires:  gcc-c++
BuildRequires:  procps
BuildRequires:  pkgconfig
BuildRequires:  python
Provides:   npm = %{version}

%description
Provides an easy way to build scalable network programs
http://nodejs.org


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
#./configure --prefix=%{_prefix} --shared-v8 --shared-openssl --shared-zlib --gdb
#./configure --prefix=%{_prefix} --shared-openssl --shared-zlib --gdb
./configure --prefix=%{_prefix} --shared-zlib --gdb
# << build pre


make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
#node-gyp needs common.gypi too
mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node

# << install post

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/node
%attr(755,root,root) %{_bindir}/npm
%{_mandir}/*/*
%{_datadir}/systemtap/tapset/node.stp
%{_datadir}/node
%{_libdir}/node_modules
%{_includedir}/node
%doc AUTHORS LICENSE
%exclude %{_libdir}/node_modules/npm/.npmignore
%exclude %{_libdir}/node_modules/npm/scripts/clean-old.sh
%exclude %{_libdir}/node_modules/npm/scripts/install.sh
%attr(755,root,root) %{_libdir}/node_modules/npm/scripts/clean-old.sh
%attr(755,root,root) %{_libdir}/node_modules/npm/scripts/install.sh
# >> files
# << files
