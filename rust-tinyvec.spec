# check disabled to avoid circular dependency (criterion)
%bcond_with check
%global debug_package %{nil}

%global crate tinyvec

Name:           rust-%{crate}
Version:        1.1.1
Release:        2
Summary:        `tinyvec` provides 100% safe vec-like data structures

# Upstream license specification: Zlib OR Apache-2.0 OR MIT
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/tinyvec
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
%if %{with check}
BuildRequires:  (crate(criterion/default) >= 0.3.0 with crate(criterion/default) < 0.4.0)
BuildRequires:  (crate(serde_test/default) >= 1.0.0 with crate(serde_test/default) < 2.0.0)
%endif
%endif

%global _description %{expand:
`tinyvec` provides 100% safe vec-like data structures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec) = 1.1.1
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/default) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/alloc) = 1.1.1
Requires:       cargo
Requires:       (crate(tinyvec_macros/default) >= 0.1.0 with crate(tinyvec_macros/default) < 0.2.0)
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+experimental_write_impl-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/experimental_write_impl) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+experimental_write_impl-devel %{_description}

This package contains library source intended for building other packages
which use "experimental_write_impl" feature of "%{crate}" crate.

%files       -n %{name}+experimental_write_impl-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+grab_spare_slice-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/grab_spare_slice) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+grab_spare_slice-devel %{_description}

This package contains library source intended for building other packages
which use "grab_spare_slice" feature of "%{crate}" crate.

%files       -n %{name}+grab_spare_slice-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly_const_generics-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/nightly_const_generics) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+nightly_const_generics-devel %{_description}

This package contains library source intended for building other packages
which use "nightly_const_generics" feature of "%{crate}" crate.

%files       -n %{name}+nightly_const_generics-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly_slice_partition_dedup-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/nightly_slice_partition_dedup) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+nightly_slice_partition_dedup-devel %{_description}

This package contains library source intended for building other packages
which use "nightly_slice_partition_dedup" feature of "%{crate}" crate.

%files       -n %{name}+nightly_slice_partition_dedup-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc_1_40-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/rustc_1_40) = 1.1.1
Requires:       cargo
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+rustc_1_40-devel %{_description}

This package contains library source intended for building other packages
which use "rustc_1_40" feature of "%{crate}" crate.

%files       -n %{name}+rustc_1_40-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/serde) = 1.1.1
Requires:       cargo
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tinyvec_macros-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec/tinyvec_macros) = 1.1.1
Requires:       cargo
Requires:       (crate(tinyvec_macros/default) >= 0.1.0 with crate(tinyvec_macros/default) < 0.2.0)
Requires:       crate(tinyvec) = 1.1.1

%description -n %{name}+tinyvec_macros-devel %{_description}

This package contains library source intended for building other packages
which use "tinyvec_macros" feature of "%{crate}" crate.

%files       -n %{name}+tinyvec_macros-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
