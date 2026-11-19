
## File ini berisi opsi yang dapat diubah untuk mengkustomisasi game.
## Baris yang diawali dua tanda '#' adalah komentar.
## Kamu dapat mengaktifkan opsi tertentu dengan menghapus satu tanda '#'.

## Dasar #######################################################################

define config.name = _("LANGKAH TERAKHIR")

define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "LANGKAHTERAKHIR"


## Layer #######################################################################

## Layer characters berada di bawah screens agar karakter tidak menutupi UI dialog.

define config.layers = [
    "master",
    "transient",
    "characters",
    "screens",
    "overlay"
]


## Suara #######################################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## Contoh pengaturan suara:
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"
# define config.main_menu_music = "main-menu-theme.ogg"


## Transisi ####################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None


## Jendela Dialog ##############################################################

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preferensi ##################################################################

## Kecepatan teks dialog: 40 karakter per detik.

default preferences.text_cps = 40

default preferences.afm_time = 15


## Penyimpanan #################################################################

define config.save_directory = "LANGKAHTERAKHIR-1795045200"


## Ikon ########################################################################

define config.window_icon = "gui/window_icon.png"


## Build #######################################################################

init python:

    ## File yang tidak perlu dimasukkan ke dalam distribusi game.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Contoh untuk memisahkan aset dari distribusi utama.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Dokumentasi yang disertakan dalam distribusi.

    build.documentation('*.html')
    build.documentation('*.txt')


## Google Play #################################################################

## Masukkan kunci Google Play jika game akan dirilis di Google Play.

# define build.google_play_key = "..."


## itch.io #####################################################################

## Masukkan nama proyek itch.io jika diperlukan.

# define build.itch_project = "renpyt/test-project"
