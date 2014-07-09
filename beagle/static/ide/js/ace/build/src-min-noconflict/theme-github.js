ace.define("ace/theme/github",["require","exports","module","ace/lib/dom"],function(a,b,c){b.isDark=!0,b.cssClass="ace-github",b.cssText="/* CSS style content from github's default pygments highlighter template.   Cursor and selection styles from textmate.css. */.ace-github .ace_editor {  color: #333;  background-color: #F8F8F8;  border: 1px solid #CCC;  font: 13px 'Bitstream Vera Sans Mono', Courier, monospace !important;  line-height: 19px !important;  overflow: auto;  padding: 6px 10px;  border-radius: 3px;  position: relative;  margin-bottom: 15px;}.ace-github .ace_keyword {  font-weight: bold;}.ace-github .ace_string {  color: #D14;}.ace-github .ace_variable.ace_class {  color: teal;}.ace-github .ace_constant.ace_numeric {  color: #099;}.ace-github .ace_comment {  color: #998;  font-style: italic;}.ace-github .ace_variable.ace_language  {  color: #0086B3;}.ace-github .ace_paren.ace_lparen,.ace-github .ace_paren.ace_rparen {  font-weight: bold;}.ace-github .ace_constant.ace_language.ace_boolean {  font-weight: bold;}.ace-github .ace_string.ace_regexp {  color: #009926;  font-weight: normal;}.ace-github .ace_variable.ace_instancce {  color: teal;}.ace-github .ace_constant.ace_language {  font-weight: bold;}.ace-github .ace_text-layer {  cursor: text;}.ace-github .ace_cursor {  border-left: 2px solid black;}.ace-github .ace_cursor.ace_overwrite {  border-left: 0px;  border-bottom: 1px solid black;}.ace-github .ace_marker-layer .ace_selection {  background: rgb(181, 213, 255);}.ace-github.multiselect .ace_selection.start {  box-shadow: 0 0 3px 0px white;  border-radius: 2px;}";var d=a("../lib/dom");d.importCssString(b.cssText,b.cssClass)})