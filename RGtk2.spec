%global packname  	RGtk2

Name:            R-%{packname}
Version:          2.20.31
Release:          1%{?dist}
Source0:        ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{version}.tar.gz
License:          GPLv2+
URL:              http://cran.r-project.org/src/contrib
Group:            Applications/Engineering
Summary:          Adds foo functionality for R
BuildRequires:    R-devel, tex(latex)
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-core
#BuildArch: noarch

%description
R Interface to foo, enables bar!

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/demo/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/examples/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/CITATION
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/images/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/include/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/include/RGtk2/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/ui/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library/%{packname}/libs/

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

%check
#%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/demo/alphaSlider.R
%{_libdir}/R/library/%{packname}/demo/alphaSliderClass.R
%{_libdir}/R/library/%{packname}/demo/appWindow.R
%{_libdir}/R/library/%{packname}/demo/assistant.R
%{_libdir}/R/library/%{packname}/demo/builder.R
%{_libdir}/R/library/%{packname}/demo/buttonBoxes.R
%{_libdir}/R/library/%{packname}/demo/clipboard.R
%{_libdir}/R/library/%{packname}/demo/colorSelector.R
%{_libdir}/R/library/%{packname}/demo/compositeplot.R
%{_libdir}/R/library/%{packname}/demo/dnd.R
%{_libdir}/R/library/%{packname}/demo/drawingArea.R
%{_libdir}/R/library/%{packname}/demo/editableCells.R
%{_libdir}/R/library/%{packname}/demo/entryCompletion.R
%{_libdir}/R/library/%{packname}/demo/expander.R
%{_libdir}/R/library/%{packname}/demo/fileCopier.R
%{_libdir}/R/library/%{packname}/demo/iconView.R
%{_libdir}/R/library/%{packname}/demo/iconviewdnd.R
%{_libdir}/R/library/%{packname}/demo/images.R
%{_libdir}/R/library/%{packname}/demo/messageDialog.R
%{_libdir}/R/library/%{packname}/demo/multipleViews.R
%{_libdir}/R/library/%{packname}/demo/pangoCairo.R
%{_libdir}/R/library/%{packname}/demo/pixbufs.R
%{_libdir}/R/library/%{packname}/demo/printing.R
%{_libdir}/R/library/%{packname}/demo/rgtkplot.R
%{_libdir}/R/library/%{packname}/demo/rotatedText.R
%{_libdir}/R/library/%{packname}/demo/searchentry.R
%{_libdir}/R/library/%{packname}/demo/sizeGroups.R
%{_libdir}/R/library/%{packname}/demo/slide.R
%{_libdir}/R/library/%{packname}/demo/spinner.R
%{_libdir}/R/library/%{packname}/demo/svgspacewar.R
%{_libdir}/R/library/%{packname}/demo/text-scroll.R
%{_libdir}/R/library/%{packname}/demo/tooltips.R
%{_libdir}/R/library/%{packname}/demo/treeStore.R
%{_libdir}/R/library/%{packname}/examples/GAppInfo.R
%{_libdir}/R/library/%{packname}/examples/GAsyncResult.R
%{_libdir}/R/library/%{packname}/examples/GCancellable.R
%{_libdir}/R/library/%{packname}/examples/GMemoryOutputStream.R
%{_libdir}/R/library/%{packname}/examples/GSocketConnectable.R
%{_libdir}/R/library/%{packname}/examples/GThemedIcon-1.R
%{_libdir}/R/library/%{packname}/examples/GThemedIcon-2.R
%{_libdir}/R/library/%{packname}/examples/GVolume-1.R
%{_libdir}/R/library/%{packname}/examples/GVolume-2.R
%{_libdir}/R/library/%{packname}/examples/GtkAboutDialog-1.R
%{_libdir}/R/library/%{packname}/examples/GtkAboutDialog-2.R
%{_libdir}/R/library/%{packname}/examples/GtkAboutDialog-3.R
%{_libdir}/R/library/%{packname}/examples/GtkAccelLabel.R
%{_libdir}/R/library/%{packname}/examples/GtkActivatable.R
%{_libdir}/R/library/%{packname}/examples/GtkCellRenderer.R
%{_libdir}/R/library/%{packname}/examples/GtkCombo-1.R
%{_libdir}/R/library/%{packname}/examples/GtkCombo-2.R
%{_libdir}/R/library/%{packname}/examples/GtkDialog-1.R
%{_libdir}/R/library/%{packname}/examples/GtkDialog-3.R
%{_libdir}/R/library/%{packname}/examples/GtkDialog-4.R
%{_libdir}/R/library/%{packname}/examples/GtkDialog-5.R
%{_libdir}/R/library/%{packname}/examples/GtkDrawingArea.R
%{_libdir}/R/library/%{packname}/examples/GtkEditable.R
%{_libdir}/R/library/%{packname}/examples/GtkExpander.R
%{_libdir}/R/library/%{packname}/examples/GtkFileChooser-1.R
%{_libdir}/R/library/%{packname}/examples/GtkFileChooser-2.R
%{_libdir}/R/library/%{packname}/examples/GtkFileChooserButton.R
%{_libdir}/R/library/%{packname}/examples/GtkFileChooserDialog.R
%{_libdir}/R/library/%{packname}/examples/GtkFileSelection.R
%{_libdir}/R/library/%{packname}/examples/GtkIconTheme.R
%{_libdir}/R/library/%{packname}/examples/GtkIconView.R
%{_libdir}/R/library/%{packname}/examples/GtkImage-1.R
%{_libdir}/R/library/%{packname}/examples/GtkImage-2.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-2.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-3.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-4.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-5.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-6.R
%{_libdir}/R/library/%{packname}/examples/GtkLabel-7.R
%{_libdir}/R/library/%{packname}/examples/GtkListStore-1.R
%{_libdir}/R/library/%{packname}/examples/GtkListStore-3.R
%{_libdir}/R/library/%{packname}/examples/GtkMenu-1.R
%{_libdir}/R/library/%{packname}/examples/GtkMenu-2.R
%{_libdir}/R/library/%{packname}/examples/GtkMessageDialog-1.R
%{_libdir}/R/library/%{packname}/examples/GtkMessageDialog-2.R
%{_libdir}/R/library/%{packname}/examples/GtkMessageDialog-3.R
%{_libdir}/R/library/%{packname}/examples/GtkMessageDialog-4.R
%{_libdir}/R/library/%{packname}/examples/GtkNotebook-2.R
%{_libdir}/R/library/%{packname}/examples/GtkPageSetup.R
%{_libdir}/R/library/%{packname}/examples/GtkPaned.R
%{_libdir}/R/library/%{packname}/examples/GtkPrintContext.R
%{_libdir}/R/library/%{packname}/examples/GtkRadioAction.R
%{_libdir}/R/library/%{packname}/examples/GtkRadioButton.R
%{_libdir}/R/library/%{packname}/examples/GtkRadioMenuItem.R
%{_libdir}/R/library/%{packname}/examples/GtkRecentChooserDialog.R
%{_libdir}/R/library/%{packname}/examples/GtkRecentFilter.R
%{_libdir}/R/library/%{packname}/examples/GtkRecentManager-1.R
%{_libdir}/R/library/%{packname}/examples/GtkRecentManager-2.R
%{_libdir}/R/library/%{packname}/examples/GtkScale.R
%{_libdir}/R/library/%{packname}/examples/GtkSocket.R
%{_libdir}/R/library/%{packname}/examples/GtkSpinButton-1.R
%{_libdir}/R/library/%{packname}/examples/GtkSpinButton-2.R
%{_libdir}/R/library/%{packname}/examples/GtkToggleButton.R
%{_libdir}/R/library/%{packname}/examples/GtkTooltips.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeModel-1.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeModel-2.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeModelFilter.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeModelSort-1.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeModelSort-2.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeSelection.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeStore-2.R
%{_libdir}/R/library/%{packname}/examples/GtkTreeViewColumn.R
%{_libdir}/R/library/%{packname}/examples/GtkUIManager-3.R
%{_libdir}/R/library/%{packname}/examples/GtkWidget-3.R
%{_libdir}/R/library/%{packname}/examples/GtkWidget-4.R
%{_libdir}/R/library/%{packname}/examples/GtkWidget-5.R
%{_libdir}/R/library/%{packname}/examples/GtkWidget-6.R
%{_libdir}/R/library/%{packname}/examples/GtkWidget-7.R
%{_libdir}/R/library/%{packname}/examples/cairo-Patterns-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-Patterns-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-cairo-t-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-cairo-t-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-context-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-context-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-image-surface.R
%{_libdir}/R/library/%{packname}/examples/cairo-paths-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-paths-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-paths-3.R
%{_libdir}/R/library/%{packname}/examples/cairo-pattern-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-pattern-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-ps-surface.R
%{_libdir}/R/library/%{packname}/examples/cairo-scaled-font-1.R
%{_libdir}/R/library/%{packname}/examples/cairo-scaled-font-2.R
%{_libdir}/R/library/%{packname}/examples/cairo-scaled-font-3.R
%{_libdir}/R/library/%{packname}/examples/cairo-version-info-3.R
%{_libdir}/R/library/%{packname}/examples/cairo-version-info-4.R
%{_libdir}/R/library/%{packname}/examples/cairo-version-info-5.R
%{_libdir}/R/library/%{packname}/examples/gdk-Cursors.R
%{_libdir}/R/library/%{packname}/examples/gdk-GdkRGB.R
%{_libdir}/R/library/%{packname}/examples/gdk-Keyboard-Handling-2.R
%{_libdir}/R/library/%{packname}/examples/gdk-Windows-1.R
%{_libdir}/R/library/%{packname}/examples/gdk-Windows-2.R
%{_libdir}/R/library/%{packname}/examples/gdk-pixbuf-File-saving-1.R
%{_libdir}/R/library/%{packname}/examples/gdk-pixbuf-File-saving-2.R
%{_libdir}/R/library/%{packname}/examples/gdk-pixbuf-File-saving-3.R
%{_libdir}/R/library/%{packname}/examples/gdk-pixbuf-scaling.R
%{_libdir}/R/library/%{packname}/examples/gio-Extension-Points-1.R
%{_libdir}/R/library/%{packname}/examples/gio-Extension-Points-2.R
%{_libdir}/R/library/%{packname}/examples/gtk-High-level-Printing-API-1.R
%{_libdir}/R/library/%{packname}/examples/gtk-High-level-Printing-API-2.R
%{_libdir}/R/library/%{packname}/examples/gtk-High-level-Printing-API-3.R
%{_libdir}/R/library/%{packname}/examples/gtk-Resource-Files-12.R
%{_libdir}/R/library/%{packname}/examples/gtk-gtkfilefilter.R
%{_libdir}/R/library/%{packname}/examples/pango-Cairo-Rendering.R
%{_libdir}/R/library/%{packname}/examples/pango-PangoRenderer.R
%{_libdir}/R/library/%{packname}/examples/pango-Scripts-and-Languages.R
%{_libdir}/R/library/%{packname}/examples/pango-pango-renderer.R
%{_libdir}/R/library/%{packname}/examples/gdk-Application-launching.R
%{_libdir}/R/library/%{packname}/examples/gdk-Events.R
%{_libdir}/R/library/%{packname}/examples/gdk-Keyboard-Handling-1.R
%{_libdir}/R/library/%{packname}/examples/gdk-Pango-Interaction.R
%{_libdir}/R/library/%{packname}/images/alphatest.png
%{_libdir}/R/library/%{packname}/images/apple-red.png
%{_libdir}/R/library/%{packname}/images/background.jpg
%{_libdir}/R/library/%{packname}/images/floppybuddy.gif
%{_libdir}/R/library/%{packname}/images/gnome-applets.png
%{_libdir}/R/library/%{packname}/images/gnome-calendar.png
%{_libdir}/R/library/%{packname}/images/gnome-foot.png
%{_libdir}/R/library/%{packname}/images/gnome-fs-directory.png
%{_libdir}/R/library/%{packname}/images/gnome-fs-regular.png
%{_libdir}/R/library/%{packname}/images/gnome-gimp.png
%{_libdir}/R/library/%{packname}/images/gnome-gmush.png
%{_libdir}/R/library/%{packname}/images/gnome-gsame.png
%{_libdir}/R/library/%{packname}/images/gnu-keys.png
%{_libdir}/R/library/%{packname}/images/gtk-logo-rgb.gif
%{_libdir}/R/library/%{packname}/images/rgtk-logo.gif
%{_libdir}/R/library/%{packname}/include/RGtk2/RSCommon.h
%{_libdir}/R/library/%{packname}/include/RGtk2/atk.h
%{_libdir}/R/library/%{packname}/include/RGtk2/atkClassImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/atkClasses.h
%{_libdir}/R/library/%{packname}/include/RGtk2/atkImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/atkUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/atkUserFuncs.h
%{_libdir}/R/library/%{packname}/include/RGtk2/cairo-enums.h
%{_libdir}/R/library/%{packname}/include/RGtk2/cairo.h
%{_libdir}/R/library/%{packname}/include/RGtk2/cairoImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/cairoUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/cairoUserFuncs.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gdk.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gdkClassImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gdkClasses.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gdkImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gdkUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gdkUserFuncs.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gio.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gioClassImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gioClasses.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gioImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gioUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gioUserFuncs.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gobject.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gobjectImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gtk.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gtkClassImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gtkClasses.h
%{_libdir}/R/library/%{packname}/include/RGtk2/gtkImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gtkUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/gtkUserFuncs.h
%{_libdir}/R/library/%{packname}/include/RGtk2/pango.h
%{_libdir}/R/library/%{packname}/include/RGtk2/pangoClassImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/pangoClasses.h
%{_libdir}/R/library/%{packname}/include/RGtk2/pangoImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/pangoUserFuncImports.c
%{_libdir}/R/library/%{packname}/include/RGtk2/pangoUserFuncs.h
%{_libdir}/R/library/%{packname}/libs/RGtk2.so
%{_libdir}/R/library/%{packname}/ui/demo.ui


%changelog
* Sat Jan 23 2016 konstantinjch <konstantinjch@yandex.ru> 1.0-1
- Initial package creation
