%undefine _hardened_build
Name:                libgdiplus
Version:             5.6
Release:             4
Summary:             An Open Source implementation of the GDI+ API
License:             MIT and MPL-1.1 and GPL-3.0+
URL:                 http://www.mono-project.com/Main_Page
Source0:             http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Patch1:              libgdiplus-2.10.9-format.patch

BuildRequires:       gcc freetype-devel glib2-devel libjpeg-devel libtiff-devel
BuildRequires:       libpng-devel fontconfig-devel cairo-devel giflib-devel libexif-devel zlib-devel

%description
An Open Source implementation of the GDI+ API, it is part of the Mono Project.

%package devel
Summary:             Development files for libgdiplus
Requires:            %{name} = %{version}-%{release}

%description devel
Development files for libgdiplus

%prep
%setup -q
%patch1 -p1 -b .format
CFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"
CXXFLAGS="$RPM_OPT_FLAGS -Wl,-z,lazy"
export CFLAGS
export CXXFLAGS

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS README TODO AUTHORS ChangeLog
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
* Thu Jan 21 2021 Ge Wang <wangge20@huawei.com> - 5.6-4
- Modify license information.

* Thu Jul 9 2020 leiju <leiju4@huawei.com> - 5.6-3
- Package init
