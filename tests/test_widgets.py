#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prettyqt` package."""

import pytest

from prettyqt import widgets, core

app = widgets.Application.create_default_app()


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return widgets.Callout()


def test_action():
    action = widgets.Action()
    action.set_tooltip("test")
    action.set_enabled()
    action.set_disabled()
    action.set_icon("mdi.timer")
    action.set_shortcut("Ctrl+A")
    return True


def test_application():
    app.set_icon("mdi.timer")
    app.set_metadata(app_name="test",
                     app_version="1.0.0",
                     org_name="test",
                     org_domain="test")
    app.get_mainwindow()
    return True


def test_boxlayout():
    layout = widgets.BoxLayout("horizontal")
    widget = widgets.Widget()
    layout.addWidget(widget)
    layout.set_size_mode("maximum")
    assert(len(layout) == 1)
    return True


def test_buttongroup():
    group = widgets.ButtonGroup()
    btn = widgets.RadioButton("test")
    group.addButton(btn)
    return group


def test_checkbox():
    chk = widgets.CheckBox()
    chk.show()
    chk.close()


def test_colordialog():
    dlg = widgets.ColorDialog()
    dlg.show()
    dlg.close()


def test_combobox():
    box = widgets.ComboBox()
    box.set_disabled()
    box.set_enabled()
    box.add_item("test", data="data", icon="mdi.timer")
    box.set_insert_policy("bottom")
    box.set_size_policy("first_show")
    box.set_icon_size(10)
    box.set_min_char_length(10)
    box.show()
    box.close()


def test_desktopwidget():
    widgets.DesktopWidget()


def test_dialog():
    dlg = widgets.Dialog(layout="horizontal")
    dlg.set_modality()
    dlg.delete_on_close()
    dlg.add_widget(widgets.Widget())
    dlg.set_icon("mdi.timer")
    dlg.add_buttonbox()
    dlg.show()
    dlg.close()


def test_dialogbuttonbox():
    box = widgets.DialogButtonBox()
    box.set_horizontal()
    box.set_vertical()
    box.add_buttons(["apply"])
    box.show()
    box.close()


def test_dockwidget():
    widget = widgets.DockWidget()
    widget.setup_title_bar()
    widget.maximise()
    widget.show()
    widget.close()


def test_doublespinbox():
    widget = widgets.DoubleSpinBox()
    widget.show()
    widget.close()


def test_filedialog():
    dlg = widgets.FileDialog()
    dlg.set_label_text("accept", "test")
    dlg.set_accept_mode("open")
    dlg.set_accept_mode("save")
    dlg.set_filter(dict(a=[".csv"]))
    dlg.show()
    dlg.close()


def test_filesystemmodel():
    model = widgets.FileSystemModel()
    idx = model.index(0, 0)
    data = model.data(idx, model.DATA_ROLE)
    print(data)
    model.yield_child_indexes(idx)
    # qtmodeltester.check(model, force_py=True)


def test_fontdialog():
    dlg = widgets.FontDialog()
    dlg.show()
    dlg.close()


def test_formlayout():
    widget = widgets.FormLayout()
    widget.set_size_mode("maximum")
    widget.set_label_widget(0, "test")
    widget.set_label_widget(0, widgets.Widget())
    widget.set_field_widget(0, "test")
    widget.set_field_widget(0, widgets.Widget())
    widget.set_spanning_widget(0, "test")
    widget.set_spanning_widget(0, widgets.Widget())
    widget = widgets.FormLayout.from_dict({"2": "4"})
    assert(len(widget) == 2)
    return True


def test_frame():
    widget = widgets.Frame()
    widget.show()
    widget.close()


def test_gridlayout():
    layout = widgets.GridLayout()
    widget = widgets.Widget()
    layout[0:1, 0:3] = widget
    layout.set_size_mode("maximum")
    layout.set_alignment("left")
    assert len(layout) == len(list(layout)) == 1


def test_groupbox():
    widget = widgets.GroupBox()
    widget.show()
    widget.close()


def test_headerview():

    def test():
        pass

    table = widgets.HeaderView(parent=None)
    table = widgets.TableView()
    model = widgets.FileSystemModel()
    table.setModel(model)
    header = widgets.HeaderView(parent=table)
    header.resize_mode("interactive")
    header.resize_mode("interactive", col=0)
    header.resize_sections("interactive")
    header.set_custom_menu(test)
    header.set_sizes([100])
    label = header.section_labels()
    print(label)
    table.setHorizontalHeader(header)
    table.show()
    table.close()


def test_label():
    label = widgets.Label()
    label.set_image("")
    label.set_alignment(horizontal="left", vertical="top")
    label.show()
    label.close()


def test_lineedit():
    widget = widgets.LineEdit("Test")
    widget.set_regex_validator("[0-9]")
    widget.set_font("Consolas")
    widget.setText("0")
    widget.append("a")
    widget.show()
    widget.close()


def test_listview():
    widget = widgets.ListView()
    widget.show()
    widget.close()


def test_mainwindow():
    window = widgets.MainWindow()
    window.set_icon("mdi.timer")
    window.add_dockwidget("test", "Test")
    window.toggle_fullscreen()
    window.show()
    window.close()


def test_menu():
    menu = widgets.Menu("1")

    def test():
        pass

    menu.add_action("test", test, icon="mdi.timer", shortcut="Ctrl+A", checkable=True)
    menu._separator("test")
    menu.show()


def test_menubar():
    menu = widgets.MenuBar()
    menu.show()


def test_messagebox():
    widget = widgets.MessageBox()
    widget.show()


def test_plaintextedit():
    widget = widgets.PlainTextEdit()
    widget.set_text("hallo")
    widget.show()


def test_progressbar():
    widget = widgets.ProgressBar()
    widget.show()


def test_progressdialog():
    widget = widgets.ProgressDialog()
    widget.show()


def test_pushbutton():
    widget = widgets.PushButton("Test")
    widget.show()


def test_radiobutton():
    widget = widgets.RadioButton("Test")
    widget.set_icon("mdi.timer")
    widget.set_enabled()
    widget.set_disabled()
    widget.show()


def test_slider():
    widget = widgets.Slider()
    widget.show()


def test_spinbox():
    widget = widgets.SpinBox()
    widget.show()


def test_splitter():
    widget = widgets.Splitter("vertical")
    widget.show()


def test_tabwidget():
    widget = widgets.TabWidget()
    widget.add_tab(widgets.Widget(), "mdi.timer")
    widget.insert_tab(0, widgets.Widget(), "test", "mdi.timer")
    widget.detach_tab(0, core.Point())
    widget.remove_tab(0)
    widget.show()
    widget.close()
    assert True


def test_textbrowser():
    reader = widgets.TextBrowser()
    reader.show()
    reader.close()
    assert True


def test_textedit():
    widget = widgets.TextEdit()
    widget.set_text("test")
    widget.append(" this")
    assert(widget.text() == "test\n this")
    widget.set_font("Consolas")
    widget.set_enabled()
    widget.set_read_only()
    widget.scroll_to_end()
    widget.set_disabled()
    widget.show()


def test_toolbar():
    widget = widgets.Toolbar()
    widget.add_menu_button("test,", "mdi.timer", menu=widgets.Menu())
    widget.set_style("icon")

    def test():
        pass

    widget.add_action("test", "mdi.timer", test, checkable=True)
    widget.show()


def test_treeview():
    widget = widgets.TreeView()
    widget.show()


def test_widget():
    widget = widgets.Widget()
    with widget.block_signals():
        pass
    widget.set_enabled()
    widget.set_disabled()


def test_widgetaction():
    action = widgets.Action()
    widgetaction = widgets.WidgetAction(action)
    widgetaction.set_tooltip("test")
    widgetaction.set_enabled()
    widgetaction.set_disabled()
    widgetaction.set_icon("mdi.timer")
    widgetaction.set_shortcut("Ctrl+A")
    return True
