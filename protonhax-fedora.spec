Name:           Protonhax-fedora
Version:        1.0.5
Release:        1%{?dist}
Summary:        Protonhax packaged for fedora.

License:        BSD-3-CLAUSE
URL:            https://github.com/hamburgerghini1/protonhax-fedora
Source0:        protonhax-fedora.tar.gz

BuildArch:      noarch

%description
This package contains a simple script that does something cool.

%prep
%autosetup -n protonhax-fedora

%install
install -D -m 755 protonhax %{buildroot}/%{_bindir}/protonhax-fedora

%files
%{_bindir}/protonhax-fedora

%changelog
* Mon Jan 06 2025 Tommi Pöntinen <tommipontinen76@proton.me> - 1.0.5-1
- Initial RPM package
