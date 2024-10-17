%define name udev-browse
%define version 0.0.0
%define git 20100131
%define rel 2

%define release %mkrel 0.%{git}.%{rel}

%define git_url git://git.0pointer.de/udev-browse.git

Summary: A simple GUI to browse udev/sysfs tree
Name:    %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
# (cg) Guess at license until I find out properly
License: GPLv2+
Group:   Development/Other
URL:     https://0pointer.de/blog/projects/udev-browse.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

BuildRequires: udev-devel
BuildRequires: vala-devel
BuildRequires: libgee-devel
BuildRequires: libgudev-devel
BuildRequires: gtk2-devel
BuildRequires: pango-devel


%description
A simple GUI to browse udev/sysfs tree


%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -a %{name} %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%{_bindir}/udev-browse
