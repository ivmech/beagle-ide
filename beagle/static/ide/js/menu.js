
function about () {
  alert('Caner Durmusoglu - cnr437@gmail.com\n\nwww.ivmech.com\n\nLicense: GNU/GPL');
  hide_menu();
}

function show_menu () {
  var offset = $("#menu_button").offset();
  $("#main_menu").css('display', 'block');
  $("#main_menu").offset({top: offset.top + 30, left: offset.left});
  return false;
}

function hide_menu () {
  $("#main_menu").css('display', 'none');
  return true;
}

var pref_win;
var save_win;

$(document).ready(function () {
  pref_win = $("#editor_pref").kendoWindow({title: 'Editor Ayarlari', modal: true, width: "600px"}).data("kendoWindow");
  save_win = $("#saveall").kendoWindow({title: 'Kaydet', modal: true, width: "400px", height: '200px', actions: false, animation: false}).data("kendoWindow");
  
  //$(this).parent().children().children('.ui-dialog-titlebar-close').hide();
  
});

function show_pref () {
  hide_menu();
  pref_win.center();
  pref_win.open();
  $("#editor_pref iframe").attr('src', '/editor_pref/');
}

function update_prefs (new_prefs) {
  pref_win.close();
  pref = new_prefs;
  set_all_pref();
}

function CloseAll () {
  if (confirm('Tum dosyalari kapatmak istediginizden emin misiniz?')) {
    $('#tabs span.ui-icon-close').click();
  }
}

function SaveAll () {
  save_win.center();
  save_win.open();
  $("#saveall").css('display', 'block');
  $("#saveall").empty();
  for (dp in tab_paths) {
    $("#saveall").append('<p id="saveall_' + tab_paths[dp].uid + '">Kaydediliyor... ' + tab_paths[dp].filename + ' ...</p>');
  }
  setTimeout(function () { doSaveAll(); }, 500);
}

function doSaveAll () {
  for (dp in tab_paths) {
    var contents = tab_paths[dp].session.getValue();
    
    $.ajax({
      type: 'POST',
      url: '/filesave/',
      context: dp,
      data: {'path': dp, 'contents': contents},
      success: function (data, textStatus, jqXHR) {
        $("#saveall_" + data.uid).remove();
        if (data.result == 'bad') {
          alert(data.error);
        }
        
        if ($('#saveall').children().size() == 0) {
          save_win.close();
        }
      },
      error: function (jqXHR, textStatus, errorThrown) {
        alert('Kayit Hatasi ' + this);
        $("#status").html('');
        $("#saveall_" + tab_paths[this].uid).remove();
        if ($('#saveall').children().size() == 0) {
          save_win.close();
        }
      },
    });
  }
}

function set_editor_mode(mode) {
  var sess = editor_global.getSession();
  var Mode = require("ace/mode/" + mode).Mode;
  sess.setMode(new Mode());
}
