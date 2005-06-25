# TODO:
# - add categories to .desktop file

Summary:	KGuitar - a KDE tabulature editor
Summary(pl):	KGuitar - edytor tabulatur dla KDE
Name:		kguitar
Version:	0.5
Release:	0.99
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/kguitar/%{name}-%{version}.tar.bz2
# Source0-md5:	4b259961a8a9aef9e56826f4725fb33d
Patch0:		%{name}-doc.patch
URL:		http://kguitar.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	tse3-devel >= 0.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KGuitar is basically a guitar tabulature editor for K Desktop
Environment. It's much more than just a tab editor. Its features are:
- Free GPLed program;
- K Desktop Environment GUI;
- Powerful and convenient tabulature editing, including many effects
  and classical note score editing for classic instrument players;
- Full and very customizable MIDI to tabulature import and export;
- Support of extra data formats, such as ASCII tabulatures or popular
  programs' format, such as Guitar Pro's or TablEdit;
- Chord fingering construction tools - chord finder & chord analyzer;
- Highly customizable to suit a lot of possible instruments (not only
  6-stringed guitars, and even not only guitars), including drum
  tracks, lyrics and other MIDI events.

%description -l pl
KGuitar to w uproszczeniu edytor tabulatur gitarowych dla ¶rodowiska
KDE. Jednak jest to nieco wiêcej ni¿ edytor tabulatur. Jego cechy to:
- wolnodostêpno¶æ na zasadach GPL
- graficzny interfejs KDE
- potê¿na i wygodna edycja tabulatur, wraz z wieloma efektami i
  klasycznym zapisem warto¶ci nut
- pe³ny i wysoce konfigurowalny import i eksport tabulatur do/z MIDI
- obs³uga dodatkowych formatów danych, takich jak tabulatury ASCII czy
  formaty popularnych programów, takich jak Guitar Pro czy TablEdit
- narzêdzia do tworzenia uk³adów palców dla akordów (chord finder i
  chord analyzer)
- wysoka konfigurowalno¶æ, aby pasowaæ do wielu instrumentów (nie
  tylko 6-strunowych gitar, a nawet nie tylko gitar), w³±czaj±c
  ¶cie¿ki bêbnów, teksty i inne zdarzenia MIDI.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	TEXMF=/usr/share/texmf \
	kde_appsdir=%{_desktopdir} \
	kde_htmldir=%{_kdedocdir}

# en/kguitar but kguitar-%{version}.mo
%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
# "KDE library"
%{_libdir}/
%{_datadir}/apps/kguitar
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*.desktop
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}
