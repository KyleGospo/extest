# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate wayland-sys

Name:           rust-wayland-sys
Version:        0.31.1
Release:        %autorelease
Summary:        FFI bindings to the various libwayland-*.so libraries

License:        MIT
URL:            https://crates.io/crates/wayland-sys
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
FFI bindings to the various libwayland-*.so libraries. You should only
need this crate if you are working on custom wayland protocol
extensions. Look at the crate wayland-client for usable bindings.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cursor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cursor-devel %{_description}

This package contains library source intended for building other packages which
use the "cursor" feature of the "%{crate}" crate.

%files       -n %{name}+cursor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dlopen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dlopen-devel %{_description}

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

%files       -n %{name}+dlopen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+egl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+egl-devel %{_description}

This package contains library source intended for building other packages which
use the "egl" feature of the "%{crate}" crate.

%files       -n %{name}+egl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memoffset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memoffset-devel %{_description}

This package contains library source intended for building other packages which
use the "memoffset" feature of the "%{crate}" crate.

%files       -n %{name}+memoffset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+once_cell-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+once_cell-devel %{_description}

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%files       -n %{name}+once_cell-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%files       -n %{name}+server-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%changelog
%autochangelog
