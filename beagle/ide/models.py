import os
import time

from django.db import models
from django.contrib.auth.models import User
import django.utils.simplejson as json

TEMA_ARAYUZ = (
    ('default', 'Default'),
    ('black', 'Black'),
    ('blueopal', 'Blue Opal'),
    ('metro', 'Metro'),
    ('silver', 'Silver')
)

TEMA_EDITOR = (
    ('textmate', 'TextMate'),
    ('eclipse', 'Eclipse'),
    ('dawn', 'Dawn'),
    ('idle_fingers', 'idleFingers'),
    ('pastel_on_dark', 'Pastel on dark'),
    ('twilight', 'Twilight'),
    ('clouds', 'Clouds'),
    ('clouds_midnight', 'Clouds Midnight'),
    ('crimson_editor', 'Crimson'),
    ('kr_theme', 'krTheme'),
    ('mono_industrial', 'Mono Industrial'),
    ('monokai', 'Monokai'),
    ('merbivore', 'Merbivore'),
    ('merbivore_soft', 'Merbivore Soft'),
    ('vibrant_ink', 'Vibrant Ink'),
    ('solarized_dark', 'Solarized Dark'),
    ('solarized_light', 'Solarized Light'),
)

BOYUT = (
    ('6px', '6px'),
    ('7px', '7px'),
    ('8px', '8px'),
    ('9px', '9px'),
    ('10px', '10px'),
    ('11px', '11px'),
    ('12px', '12px'),
    ('13px', '13px'),
    ('14px', '14px'),
    ('15px', '15px'),
    ('16px', '16px'),
    ('17px', '17px'),
    ('18px', '18px'),
    ('19px', '19px'),
    ('20px', '20px'),
    ('21px', '21px'),
    ('22px', '22px'),
    ('23px', '23px'),
    ('24px', '24px'),
)

TUSLAR = (
    ('ace', 'Ace'),
    ('vim', 'Vim'),
    ('emacs', 'Emacs')
)

WRAP = (
    ('off', 'Off'),
    ('40', '40 Chars'),
    ('80', '80 Chars'),
    ('free', 'Free')
)
  
class Preferences (models.Model):

    user = models.OneToOneField(User)

    idename = models.CharField('IDE Adi', max_length=255, default="Beagleboard IDE")
    basedir = models.CharField('Ana Dizin', max_length=255)
    uitheme = models.CharField('Arayuz Temasi', choices=TEMA_ARAYUZ, max_length=25, default='silver')
    theme = models.CharField('Editor Temasi', choices=TEMA_EDITOR, max_length=25, default='textmate')
    fontsize = models.CharField('Font Boyutu', choices=BOYUT, max_length=10, default='14px')
    keybind = models.CharField('Tus Secimi', choices=TUSLAR, max_length=10, default='ace')
    swrap = models.CharField('Satir Wrap', choices=WRAP, max_length=10, default='off')

    tabsize = models.IntegerField('Tab Boyutu', default=4)

    hactive = models.BooleanField('Aktif Satiri Belirt', default=True)
    hword = models.BooleanField('Aktif Kelimeyi Belirt', default=True)
    invisibles = models.BooleanField('Gizli Dosyalari Goster', default=False)
    gutter = models.BooleanField('Show Gutter', default=True)
    pmargin = models.BooleanField('Yazilabilir Alani Goster', default=True)
    softab = models.BooleanField('Hafif Tab Kullan', default=True)
    behave = models.BooleanField('Davranislar', default=True)
    splitterm = models.BooleanField('Split Terminal/IDE Ayiraci', default=True)
    save_session = models.BooleanField('Save Session', default=True)

    session = models.TextField(blank=True, null=True)

    bg = models.ImageField('Terminal Arkaplani', blank=True, null=True, upload_to='bg')

    font = models.CharField('Terminal Fontu', max_length=255, default='"Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace')
    tfontsize = models.CharField('Terminal Font Boyutu', max_length=25, default='16px')

    def last_session (self):
        if self.session:
            return json.dumps(self.session.split("\n"))
        return '[]';
    
    def valid_path (self, path):
        path = os.path.normpath(path)
        if path.startswith(self.basedir):
            return True
      
        return False

class TempFile (models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to='tmp')
  
class ExtFileRequest (models.Model):
    secret = models.CharField(max_length=255)
    path = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
