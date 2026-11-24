
define r = Character('Rian')
define p = Character('Pak Seno')
define g = Character('Gadis Payung Merah')
define i = Character('Ibu')
define n = Character(None)
default melihat_foto = False
default mengingat_pekerjaan = False
default percaya_gadis = False
image stasiun_kenangan = "images/stasiun.png"
image peron_terakhir = "images/background/peron_terakhir.png"
image rumah_pagi = "images/background/rumah_pagi.png"
image ruang_tamu = "images/background/ruang_tamu.png"
image ibu = "images/character/ibu.png"

# Character Position
transform posisi_kiri:
    zoom 0.5
    xpos 230
    yalign 0.82

transform posisi_kanan:
    zoom 0.5
    xpos 1690
    xanchor 1.0
    yalign 0.82

# System Variables
default honesty = 0
default memory = 0
default father_bond = 0
default mother_bond = 0

# Chapter 1 Flags
default cek_papan = False
default cek_saku = False
default elak_jam = False

init python:
    def suara_ketik(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/Keyboard.mp3", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

define n = Character(None, callback=suara_ketik)
label start:

    scene black
    play sound "audio/telepon .mp3"
    n "Terdengar suara getar ponsel di atas permukaan meja kayu yang berulang tiga kali sebelum akhirnya diangkat."

    i "Halo, Yan? Maaf Ibu telepon malam malam. Kamu sudah istirahat?"

    r "Belum, Bu. Ini Rian masih beresin berkas kerjaan. Kenapa, Bu? Ada yang penting?"

    i "Nggak ada apa-apa, Nak. Ibu cuma kepikiran saja. Sudah hampir setahun kamu nggak pulang. Kapan kamu ada libur barang dua hari?"

    play sound "audio/Kertas_remuk.mp3"
    

    play sound "audio/Kertas_remuk.mp3"
    n "Terdengar suara kertas diremas pelan—amplop pemberitahuan kontrak kerja yang tidak diperpanjang."

    r "Bu, kan Rian sudah bilang bulan lalu. Di sini lagi masa penyesuaian proyek besar. Kalau Rian pulang sekarang tanpa bawa hasil apa-apa, mau ditaruh di mana muka Rian? Ibu tunggu saja sampai urusan di sini beres, jangan telepon terus nanyain kapan pulang."

    n "Hening selama tiga detik di seberang telepon. Hanya terdengar tarikan napas pelan."

    i "Iya, Yan. Maaf ganggu waktumu. Jangan lupa makan malam, ya."
    play sound "audio/telepon_terputus.mp3" 
    n "Sambungan telepon terputus. Suara dengung hening memenuhi ruangan. Terdengar langkah kaki tergesa-gesa, ritsleting koper ditarik cepat, lalu pintu kamar ditutup rapat."

    r "Sial... kenapa aku ngomong kayak gitu barusan."
    n "Rian langsung mengambil jaket dan tas nya, lalu bergegas menancap gas mobil menuju pintu tol untuk menuju ke rumah orang tua nya"
    n "Suara jalan tol perlahan menghilang, digantikan hembusan angin malam yang dingin dan dengung lampu neon stasiun."
    with dissolve

    scene stasiun_kenangan

    

    n "Tiba tiba rian terbangun di suatu tempat yang ia tidak kenali"

    n "Rian duduk menyandar di bangku besi panjang dengan jaket denim lusuh. Di samping kakinya tergeletak sebuah koper hitam."

    show boti at posisi_kiri onlayer characters
    
    "Jam dua lewat..."
    "Sebentar. Ini peron berapa? Kok sepi banget?"

    hide boti onlayer characters

    n "Rian berdiri dan meregangkan bahunya yang kaku. Sejauh mata memandang, ujung peron di sebelah kiri dan kanan tertutup kabut putih tipis."

    n "Satu-satunya penanda yang menempel di tiang besi hanyalah papan seng tua bertuliskan angka 0."

    show boti at posisi_kiri onlayer characters

    "Stasiun Nol. Bagus. Jangan-jangan tadi aku ketiduran di bus terus diturunin di terminal antah-berantah."

    hide boti onlayer characters

    n "Rian mengamati sekelilingnya. Tidak ada petugas, tidak ada penumpang lain, bahkan suara kereta pun tidak terdengar."

    show boti at posisi_kiri onlayer characters

    r "Oke... daripada berdiri di sini terus, mending cari tahu dulu tempat ini."

    hide boti onlayer characters

    menu:

        "Periksa papan jadwal keberangkatan di dekat tiang.":

            $ memory += 1
            $ cek_papan = True

            n "Rian berjalan mendekati papan jadwal manual yang tergantung di dekat tiang besi."

            n "Huruf-huruf plastiknya tampak miring dan sebagian sudah memudar."

            n "Hanya ada satu baris tulisan yang masih bisa dibaca."

            n "JALUR PULANG — MENUNGGU JADWAL"

            show boti at posisi_kiri onlayer characters

            r "Sistem informasi macam apa ini. Nggak ada jam keberangkatan, nggak ada nama kota tujuan."

            hide boti onlayer characters

        "Periksa saku jaket dan celana untuk mencari ponsel.":

            $ memory += 1
            $ cek_saku = True

            n "Rian merogoh saku jaket dan celananya."

            n "Namun, ponselnya tidak ditemukan. Jarinya justru menyentuh sesuatu yang terasa seperti kertas tebal."

            play sound "audio/Kertas_remuk.mp3"
            n "Ia mengeluarkan selembar tiket karton kusam tanpa tanggal dan nama stasiun asal."

            show boti at posisi_kiri onlayer characters

            r "Kapan aku beli tiket kertas model begini? Perasaan tadi nyetir sendiri..."

            hide boti onlayer characters

        "Langsung berjalan menuju pos loket di ujung cahaya.":

            n "Rian mengangkat koper hitamnya dan mulai berjalan menuju arah cahaya di ujung peron."

            show boti at posisi_kiri onlayer characters

            r "Mudah-mudahan ada petugas yang bisa ditanyain."

            hide boti onlayer characters

    n "Belum jauh Rian berjalan, terdengar suara langkah sepatu kulit yang teratur dari arah lorong."

    n "Seorang pria paruh baya berseragam petugas stasiun berwarna abu-abu tua berjalan menghampirinya sambil membawa papan klip kayu."

    show laki at posisi_kanan onlayer characters

    p "Selamat malam, Mas. Kalau mencari kereta ekspres ke arah kota, jalurnya sudah tutup sejak tadi."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Akhirnya ada orang."

    r "Pak, permisi mau tanya, ini daerah mana ya? Saya mau arah pulang ke kampung, tapi kayaknya salah ambil jalur."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Ini Stasiun 0. Transit sementara."

    hide laki onlayer characters

    n "Pak Seno melirik pergelangan tangan Rian yang sejak tadi beberapa kali diperiksa."

    show laki at posisi_kanan onlayer characters

    p "Ngomong-ngomong, dari tadi saya perhatikan Mas sering sekali melirik jam tangan. Sedang dikejar jadwal rapat?"

    hide laki onlayer characters

    menu:

        "Kebiasaan di Jakarta, Pak. Kalau telat sedikit saja rasanya sudah ketinggalan banyak hal.":

            $ honesty += 1
            $ father_bond += 1

            n "Pak Seno mengangguk kecil. Sudut bibirnya sedikit terangkat."

            show laki at posisi_kanan onlayer characters

            p "Orang kota memang selalu berlari, bahkan saat sedang duduk menunggu."

            p "Padahal keretanya saja belum tentu datang lebih cepat."

            hide laki onlayer characters

            show boti at posisi_kiri onlayer characters

            r "Hehe... iya juga, Pak."

            hide boti onlayer characters

        "Nggak juga, Pak. Cuma memastikan baterai jam saya masih jalan.":

            $ elak_jam = True

            n "Pak Seno memperhatikan jam tangan Rian sejenak sebelum kembali menatapnya."

            show laki at posisi_kanan onlayer characters

            p "Begitu. Silakan saja dicek, kalau memang masih bisa jalan."

            hide laki onlayer characters

            n "Setelah mengatakan itu, Pak Seno kembali memperhatikan papan klip kayunya."

            show boti at posisi_kiri onlayer characters

            r "Iya, Pak."

            hide boti onlayer characters

        "Bapak petugas shift malam di sini? Sepi sekali stasiunnya.":

            $ father_bond += 1

            show laki at posisi_kanan onlayer characters

            p "Memang tidak banyak penumpang yang turun di sini pada jam segini."

            hide laki onlayer characters

            show boti at posisi_kiri onlayer characters

            r "Pantas saja sepi banget."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Sudah biasa."

            hide laki onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Silakan tunggu di ruang tunggu dekat mesin minuman kalau kedinginan."

    p "Kabut malam di peron tidak bagus untuk badan yang sedang capek."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Oh, ada mesin minuman juga ternyata."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Ikuti lorong itu. Nanti juga terlihat."

    hide laki onlayer characters

    n "Pak Seno merapikan papan klip kayunya, kemudian berjalan perlahan menuju pos loket."

    n "Rian memperhatikan punggung pria itu sejenak sebelum kembali mengangkat kopernya."

    show boti at posisi_kiri onlayer characters

    r "Petugasnya agak aneh juga..."

    hide boti onlayer characters

    n "Dengan langkah perlahan, Rian mulai mengikuti arah lorong yang ditunjukkan Pak Seno."

    scene black with fade

    n "Suara langkah kaki Rian perlahan menghilang di antara dengung lampu neon."

    n "Di ujung lorong, sebuah cahaya kecil tampak menyala."

    jump bab_2

label bab_2:

    scene ruang_tunggu with fade

    n "Rian akhirnya sampai di ruang tunggu yang ditunjukkan Pak Seno."

    n "Ruangan itu tidak terlalu luas. Beberapa kursi besi tersusun menghadap sebuah mesin minuman otomatis."

    n "Lampu neon putih menerangi seluruh ruangan, tetapi suasananya tetap terasa dingin dan sepi."

    n "Tidak ada penumpang lain di sana."

    show boti at posisi_kiri onlayer characters

    r "Ruang tunggu, ya..."

    r "Setidaknya di sini lebih terang daripada peron tadi."

    hide boti onlayer characters

    n "Rian meletakkan kopernya di samping kursi, kemudian duduk untuk beristirahat."

    n "Ia kembali melihat jam tangannya."

    if elak_jam:

        show boti at posisi_kiri onlayer characters

        r "Dari tadi jam ini rasanya nggak berubah."

        hide boti onlayer characters

    else:

        show boti at posisi_kiri onlayer characters

        r "Jam dua lewat tujuh belas..."

        hide boti onlayer characters

    n "Jarum jam menunjukkan pukul 02.17."

    n "Rian mencoba memeriksa ponselnya, tetapi benda itu tidak ditemukan."

    show boti at posisi_kiri onlayer characters

    r "Ponsel juga nggak ada. Sebenarnya tadi aku bawa atau nggak, sih?"

    hide boti onlayer characters

    n "Ia kemudian memperhatikan mesin minuman yang berada di seberang kursi."

    menu:

        "Mencoba membeli minuman dari mesin.":

            n "Rian berdiri dan berjalan mendekati mesin minuman."

            n "Beberapa pilihan minuman terpampang di balik kaca."

            show boti at posisi_kiri onlayer characters

            r "Lumayan. Siapa tahu bisa buat menghangatkan badan."

            hide boti onlayer characters

            n "Rian mencoba memasukkan uang ke mesin tersebut."

            n "Namun, layar kecil di bagian depan justru menampilkan tulisan."

            n "\"SILAKAN MASUKKAN TIKET ANDA.\""

            show boti at posisi_kiri onlayer characters

            r "Tiket? Mesin minuman sekarang pakai tiket?"

            hide boti onlayer characters

        "Memeriksa koper dan barang bawaan.":

            n "Rian menarik kopernya mendekat dan membuka bagian atasnya."

            n "Ia memeriksa beberapa pakaian dan dokumen pekerjaan yang tersimpan di dalam."

            show boti at posisi_kiri onlayer characters

            r "Semua masih ada..."

            hide boti onlayer characters

            n "Di antara barang-barang tersebut, Rian menemukan sebuah foto lama."

            n "Foto dirinya bersama kedua orang tuanya."

            show boti at posisi_kiri onlayer characters

            r "Sudah lama banget..."

            hide boti onlayer characters

            $ memory += 1

        "Duduk dan mencoba beristirahat.":

            n "Rian menyandarkan punggungnya pada kursi besi."

            n "Ia memejamkan mata sejenak, berharap bisa mengumpulkan tenaga."

            show boti at posisi_kiri onlayer characters

            r "Sebentar saja. Badan gue capek banget."

            hide boti onlayer characters

            n "Namun, suara langkah kaki dari arah pintu membuatnya kembali membuka mata."

    n "Terdengar suara langkah kaki pelan dari arah pintu masuk."

    n "Rian menoleh."

    n "Seorang gadis berdiri di dekat pintu. Ia mengenakan pakaian sederhana dan membawa sebuah payung berwarna merah."

    show boti at posisi_kiri onlayer characters

    r "Eh... siapa lagi ini?"

    hide boti onlayer characters

    n "Gadis itu berjalan mendekati mesin minuman."

    n "Ia berdiri beberapa saat, kemudian menoleh ke arah Rian."

    g "Kamu sedang menunggu kereta?"

    show boti at posisi_kiri onlayer characters

    r "Iya. Memangnya ada kereta yang lewat di sini?"

    hide boti onlayer characters

    g "Ada."

    g "Tapi kereta itu tidak datang untuk semua orang."

    show boti at posisi_kiri onlayer characters

    r "Maksudnya gimana?"

    hide boti onlayer characters

    n "Gadis itu tidak langsung menjawab."

    n "Ia justru memperhatikan koper hitam di samping Rian."

    g "Kamu mau pulang?"

    show boti at posisi_kiri onlayer characters

    r "Iya. Kenapa?"

    hide boti onlayer characters

    g "Sudah lama?"

    n "Rian terdiam sejenak."

    menu:

        "Sudah hampir setahun.":

            $ honesty += 1

            show boti at posisi_kiri onlayer characters

            r "Hampir setahun."

            r "Aku memang belum sempat pulang."

            hide boti onlayer characters

            g "Pasti ada yang menunggu."

            show boti at posisi_kiri onlayer characters

            r "Mungkin."

            hide boti onlayer characters

        "Bukan urusan kamu.":

            n "Rian menjawab dengan nada sedikit ketus."

            g "Oh, begitu."

            n "Gadis itu tidak terlihat tersinggung."

            g "Kalau begitu, aku tidak akan bertanya lagi."

        "Kenapa kamu banyak bertanya?":

            show boti at posisi_kiri onlayer characters

            r "Dari tadi kamu nanya terus. Memangnya kenapa?"

            hide boti onlayer characters

            g "Tidak apa-apa."

            g "Aku hanya penasaran dengan orang yang datang membawa koper."

    n "Gadis itu kemudian duduk di kursi yang tidak jauh dari Rian."

    n "Payung merahnya diletakkan di samping kursi."

    g "Namaku tidak terlalu penting di tempat ini."

    show boti at posisi_kiri onlayer characters

    r "Terus aku harus manggil kamu apa?"

    hide boti onlayer characters

    g "Panggil saja aku Gadis Payung Merah."

    show boti at posisi_kiri onlayer characters

    r "Nama yang aneh."

    hide boti onlayer characters

    g "Mungkin."

    n "Keduanya terdiam beberapa saat."

    n "Suara dengung mesin minuman menjadi satu-satunya suara yang terdengar."

    g "Boleh aku bertanya satu hal lagi?"

    show boti at posisi_kiri onlayer characters

    r "Apa lagi?"

    hide boti onlayer characters

    g "Kalau kamu bisa kembali ke satu tempat, tempat mana yang ingin kamu datangi?"

    menu:

        "Rumah. Aku ingin bertemu Ibu.":

            $ mother_bond += 2

            n "Rian teringat percakapan teleponnya dengan Ibu sebelum perjalanan."

            show boti at posisi_kiri onlayer characters

            r "Rumah."

            r "Ada seseorang yang belum sempat aku temui."

            hide boti onlayer characters

            g "Seseorang yang sedang menunggumu?"

            show boti at posisi_kiri onlayer characters

            r "Iya."

            hide boti onlayer characters

            g "Kalau begitu, jangan membuatnya menunggu terlalu lama."

        "Aku ingin kembali ke masa lalu.":

            $ memory += 2

            show boti at posisi_kiri onlayer characters

            r "Mungkin aku ingin kembali ke masa ketika semuanya masih terasa sederhana."

            hide boti onlayer characters

            g "Apa kamu yakin semuanya lebih baik saat itu?"

            show boti at posisi_kiri onlayer characters

            r "Setidaknya aku nggak harus memikirkan banyak hal."

            hide boti onlayer characters

        "Tidak ada. Aku hanya ingin menyelesaikan urusanku.":

            $ honesty += 1

            show boti at posisi_kiri onlayer characters

            r "Nggak ada."

            r "Aku cuma ingin menyelesaikan urusanku, setelah itu semuanya selesai."

            hide boti onlayer characters

            g "Kamu terdengar sangat yakin."

            show boti at posisi_kiri onlayer characters

            r "Memang harus begitu."

            hide boti onlayer characters

    n "Gadis itu menatap jam dinding yang berada di atas mesin minuman."

    g "Waktunya hampir tiba."

    show boti at posisi_kiri onlayer characters

    r "Waktu untuk apa?"

    hide boti onlayer characters

    g "Kereta berikutnya."

    n "Tiba-tiba, mesin minuman mengeluarkan bunyi pendek."

    play sound "audio/Kertas_remuk.mp3"

    n "Sebuah tiket karton keluar dari lubang kecil di bagian bawah mesin."

    n "Gadis itu berdiri dan mengambil tiket tersebut."

    g "Sepertinya ini milikmu."

    n "Ia meletakkan tiket itu di atas kursi dekat Rian."

    show boti at posisi_kiri onlayer characters

    r "Tunggu. Aku nggak pesan apa-apa."

    hide boti onlayer characters

    g "Aku tahu."

    g "Tapi kamu tetap harus membawanya."

    n "Rian mengambil tiket tersebut dan memperhatikan tulisan yang tercetak di permukaannya."

    n "\"SATU KALI PERJALANAN\""

    n "\"TUJUAN DITENTUKAN OLEH PENUMPANG\""

    show boti at posisi_kiri onlayer characters

    r "Ini tiket apa sebenarnya?"

    hide boti onlayer characters

    g "Tiket untuk perjalananmu."

    n "Gadis itu mengambil payung merahnya."

    g "Kalau sudah siap, pergilah ke peron."

    show boti at posisi_kiri onlayer characters

    r "Tunggu! Aku masih punya banyak pertanyaan!"

    hide boti onlayer characters

    n "Gadis itu berjalan menuju pintu keluar."

    g "Kamu akan menemukan jawabannya nanti."

    n "Sebelum menghilang, gadis itu sempat menoleh."

    g "Dan satu hal lagi."

    g "Jangan lupa alasan kamu ingin pulang."

    n "Gadis itu menghilang di balik pintu."

    n "Rian kembali melihat tiket yang berada di tangannya."

    show boti at posisi_kiri onlayer characters

    r "Apa sebenarnya tempat ini..."

    hide boti onlayer characters

    n "Dari pengeras suara terdengar pengumuman."

    n "\"Kereta menuju jalur berikutnya akan segera tiba.\""

    n "Rian mengangkat kopernya dan berjalan menuju peron."

    scene black with fade

    n "Di tengah kegelapan, suara kereta mulai terdengar semakin dekat."

    n "Perjalanan Rian belum berakhir."

    n "Bahkan, mungkin perjalanan sebenarnya baru saja dimulai."

    jump bab_3
label bab_3:

    scene peron_kedua with fade

    n "Rian melangkah keluar dari lorong ruang tunggu."

    n "Suara kereta yang sebelumnya terdengar semakin dekat perlahan menghilang."

    n "Di hadapannya terbentang sebuah peron yang berbeda dari sebelumnya."

    n "Tidak ada kabut putih. Tidak ada papan seng bertuliskan angka nol."

    n "Hanya ada beberapa bangku kayu, lampu kuning redup, dan sebuah papan besar bertuliskan angka 1."

    show boti at posisi_kiri onlayer characters

    r "Peron satu..."

    r "Tadi aku masih di Stasiun 0, kan?"

    hide boti onlayer characters

    n "Rian memeriksa tiket yang diberikan Gadis Payung Merah."

    n "Tulisan pada tiket masih sama. Namun, sekarang terdapat angka kecil di bagian belakangnya."

    n "\"01\""

    show boti at posisi_kiri onlayer characters

    r "Angka satu lagi?"

    hide boti onlayer characters

    n "Tiba-tiba terdengar suara seseorang dari belakang."

    p "Akhirnya sampai juga, Mas."

    show laki at posisi_kanan onlayer characters

    p "Bagaimana? Sudah menemukan ruang tunggunya?"

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Pak Seno?"

    r "Bapak dari tadi ada di sini?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Saya memang bertugas di stasiun ini."

    p "Tapi sepertinya Mas masih punya banyak pertanyaan."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Jelas, Pak. Saya bahkan belum tahu sebenarnya tempat ini apa."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Tidak semua hal bisa dijelaskan sekaligus."

    p "Kadang seseorang harus melihat sendiri sebelum bisa memahami."

    hide laki onlayer characters

    n "Pak Seno menunjuk sebuah bangku kayu di dekat papan jadwal."

    p "Duduklah sebentar. Keretanya belum datang."

    show boti at posisi_kiri onlayer characters

    r "Bukannya tadi ada pengumuman kalau kereta segera tiba?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Segera bukan berarti sekarang."

    hide laki onlayer characters

    n "Rian akhirnya duduk."

    n "Di dekat bangku terdapat sebuah kotak kayu kecil dengan tiga benda di atasnya."

    n "Sebuah foto keluarga, map dokumen pekerjaan, dan jam tangan tua."

    menu:

        "Mengambil foto keluarga.":

            $ melihat_foto = True
            $ memory += 1

            play sound "audio/Kertas_remuk.mp3"

            n "Rian mengambil foto tersebut."

            n "Foto itu memperlihatkan dirinya ketika masih muda, berdiri di antara Ayah dan Ibu."

            show boti at posisi_kiri onlayer characters

            r "Foto ini..."

            r "Sudah lama sekali aku nggak melihatnya."

            hide boti onlayer characters

            if mother_bond >= 2:

                n "Rian memperhatikan wajah Ibu di dalam foto."

                n "Ia kembali teringat percakapan telepon mereka."

                show boti at posisi_kiri onlayer characters

                r "Ibu pasti masih menyimpan foto yang sama."

                hide boti onlayer characters

            else:

                n "Rian mengamati foto itu beberapa saat sebelum meletakkannya kembali."

        "Memeriksa map dokumen pekerjaan.":

            $ mengingat_pekerjaan = True

            n "Rian membuka map dokumen yang terletak di atas kotak."

            n "Di dalamnya terdapat beberapa lembar laporan proyek dan sebuah surat pemberitahuan."

            n "Tulisan pada surat itu membuat Rian terdiam."

            n "\"PEMBERITAHUAN BERAKHIRNYA MASA KONTRAK KERJA\""

            show boti at posisi_kiri onlayer characters

            r "Ini..."

            r "Surat yang tadi ada di kamar."

            hide boti onlayer characters

            n "Rian membaca surat itu sekali lagi."

            n "Tidak ada perubahan pada isi surat tersebut."

            n "Kontrak kerjanya memang tidak diperpanjang."

        "Mengambil jam tangan tua.":

            n "Rian mengambil jam tangan tua yang terletak di atas kotak."

            n "Bentuknya sederhana, dengan tali kulit yang sudah mulai mengelupas."

            show boti at posisi_kiri onlayer characters

            r "Jam tangan siapa ini?"

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Kadang benda yang sederhana justru menyimpan banyak cerita."

            hide laki onlayer characters

            n "Rian membalik jam tangan itu."

            n "Di bagian belakang terdapat ukiran kecil."

            n "\"Untuk Rian. Jangan lupa pulang.\""

            $ memory += 1

            show boti at posisi_kiri onlayer characters

            r "Tulisan ini..."

            hide boti onlayer characters

            n "Rian tidak bisa mengingat kapan terakhir kali melihat jam tangan tersebut."

    n "Pak Seno memperhatikan Rian dari kejauhan."

    show laki at posisi_kanan onlayer characters

    p "Menemukan sesuatu yang menarik?"

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Bapak sebenarnya tahu semua benda ini?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Saya hanya menjaga apa yang tertinggal."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Apa maksudnya sesuatu yang tertinggal?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Tidak semua penumpang datang ke sini dengan membawa barang."

    p "Ada yang membawa penyesalan, ada yang membawa harapan, dan ada juga yang membawa sesuatu yang belum sempat diselesaikan."

    hide laki onlayer characters

    n "Rian terdiam."

    n "Ucapan Pak Seno membuatnya kembali memikirkan alasan ia meninggalkan rumah."

    menu:

        "Menceritakan masalah pekerjaan kepada Pak Seno.":

            $ honesty += 1
            $ father_bond += 1

            show boti at posisi_kiri onlayer characters

            r "Sebenarnya kontrak kerja saya nggak diperpanjang, Pak."

            r "Saya cuma belum berani bilang ke Ibu."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Kenapa harus takut mengatakan sesuatu yang memang terjadi?"

            hide laki onlayer characters

            show boti at posisi_kiri onlayer characters

            r "Saya nggak mau mengecewakan mereka."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Terkadang kita terlalu sibuk menjaga harapan orang lain sampai lupa memahami diri sendiri."

            hide laki onlayer characters

        "Mengatakan bahwa semuanya baik-baik saja.":

            show boti at posisi_kiri onlayer characters

            r "Nggak ada masalah, Pak. Semuanya masih bisa saya atasi."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Begitu, ya."

            p "Semoga memang begitu."

            hide laki onlayer characters

        "Bertanya mengapa Pak Seno selalu membicarakan masa lalu.":

            show boti at posisi_kiri onlayer characters

            r "Kenapa Bapak selalu membicarakan hal-hal seperti ini?"

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Karena banyak orang datang ke sini dengan pertanyaan yang sama."

            p "Dan sebagian besar dari mereka sebenarnya sudah tahu jawabannya."

            hide laki onlayer characters

    n "Tiba-tiba, lampu di sepanjang peron berkedip."

    n "Suara pengumuman terdengar dari pengeras suara."

    n "\"Penumpang dengan tiket nomor satu, silakan bersiap.\""

    show boti at posisi_kiri onlayer characters

    r "Tiket nomor satu?"

    hide boti onlayer characters

    n "Rian memeriksa tiket karton yang dipegangnya."

    n "Angka 01 di bagian belakang tiket terlihat semakin jelas."

    show laki at posisi_kanan onlayer characters

    p "Sepertinya giliran Mas sudah tiba."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Pak, sebelum saya pergi, saya mau tanya sesuatu."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Silakan."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Apa saya bisa benar-benar pulang dari tempat ini?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Itu tergantung pada apa yang ingin Mas temukan."

    p "Jangan hanya mencari jalan pulang."

    p "Cobalah mengingat alasan Mas ingin kembali."

    hide laki onlayer characters

    n "Dari kejauhan, suara kereta mulai terdengar."

    n "Lampu di ujung peron menyala semakin terang."

    n "Rian berdiri sambil menggenggam tiketnya."

    show boti at posisi_kiri onlayer characters

    r "Baiklah..."

    r "Apa pun yang terjadi, saya harus tahu jawabannya."

    hide boti onlayer characters

    n "Sebuah kereta berhenti tepat di depan peron."

    n "Pintunya terbuka perlahan."

    n "Namun, tidak ada masinis maupun penumpang di dalamnya."

    n "Hanya ada satu kursi kosong di dekat jendela."

    scene black with fade

    n "Rian melangkah masuk."

    n "Pintu kereta mulai tertutup."

    n "Di balik kaca jendela, Pak Seno berdiri diam sambil memperhatikan kereta yang perlahan bergerak."

    n "Perjalanan menuju kenangan berikutnya dimulai."

    jump bab_4
label bab_4:

    scene gerbong_kereta with fade

    n "Suara roda kereta bergesekan dengan rel terdengar memenuhi gerbong."

    n "Rian duduk sendirian di dekat jendela. Koper hitamnya diletakkan di samping kursi."

    n "Di luar jendela, tidak terlihat pemandangan kota maupun bangunan."

    n "Hanya hamparan gelap dengan cahaya kecil yang sesekali melintas."

    show boti at posisi_kiri onlayer characters

    r "Kereta macam apa ini..."

    r "Dari tadi nggak kelihatan apa-apa di luar."

    hide boti onlayer characters

    n "Rian kembali memeriksa tiket yang berada di tangannya."

    n "Angka 01 masih tercetak jelas di bagian belakang."

    show boti at posisi_kiri onlayer characters

    r "Peron satu, tiket satu..."

    r "Sebenarnya perjalanan ini mau membawaku ke mana?"

    hide boti onlayer characters

    n "Tiba-tiba, lampu di dalam gerbong berkedip."

    play sound "audio/Kertas_remuk.mp3"

    n "Terdengar suara kertas bergesekan dari kursi di seberangnya."

    n "Rian menoleh."

    n "Sebuah amplop cokelat tergeletak di atas kursi kosong."

    show boti at posisi_kiri onlayer characters

    r "Amplop?"

    hide boti onlayer characters

    n "Rian mengambil amplop tersebut."

    n "Pada bagian depannya tertulis namanya sendiri."

    n "\"RIAN\""

    menu:

        "Membuka amplop tersebut.":

            $ memory += 1

            n "Rian perlahan membuka amplop itu."

            n "Di dalamnya terdapat selembar surat dengan tulisan tangan yang sudah tidak asing baginya."

            n "Ia mulai membaca setiap kalimatnya."

            n "\"Yan, jangan terlalu memaksakan diri. Kalau capek, pulanglah. Rumah selalu terbuka untukmu.\""

            n "Rian terdiam."

            show boti at posisi_kiri onlayer characters

            r "Tulisan Ibu..."

            hide boti onlayer characters

            $ mother_bond += 1

        "Menyimpan amplop tanpa membukanya.":

            n "Rian memperhatikan amplop tersebut beberapa saat."

            show boti at posisi_kiri onlayer characters

            r "Aku nggak tahu ini dari siapa."

            r "Lebih baik kusimpan dulu."

            hide boti onlayer characters

            n "Ia memasukkan amplop itu ke dalam tas."

        "Mencari tahu apakah ada penumpang lain.":

            n "Rian berdiri dan melihat ke arah gerbong berikutnya."

            n "Namun, tidak ada seorang pun yang terlihat."

            show boti at posisi_kiri onlayer characters

            r "Kosong semua?"

            hide boti onlayer characters

            n "Ketika kembali ke kursinya, Rian menyadari sebuah amplop cokelat tergeletak di sana."

            n "Pada bagian depannya tertulis namanya sendiri."

            $ memory += 1

    n "Suara kereta semakin pelan."

    n "Lampu gerbong kembali berkedip."

    n "Pemandangan di luar jendela perlahan berubah."

    n "Kegelapan mulai digantikan oleh pemandangan sebuah rumah sederhana."

    show boti at posisi_kiri onlayer characters

    r "Rumah...?"

    hide boti onlayer characters

    n "Rian mendekatkan wajahnya ke jendela."

    n "Ia mengenali halaman kecil, pagar besi, dan pohon yang berdiri di dekat teras."

    n "Tempat itu adalah rumahnya."

    n "Namun, rumah tersebut terlihat seperti beberapa tahun yang lalu."

    if melihat_foto:

        n "Rian teringat foto keluarga yang ditemukannya di peron sebelumnya."

        n "Pemandangan di luar jendela terasa semakin familiar."

    if mengingat_pekerjaan:

        n "Rian kembali teringat surat pemberitahuan kontrak kerja."

        n "Ia mencoba mengalihkan pandangannya dari rumah tersebut."

    n "Suara seorang perempuan terdengar dari kejauhan."

    i "Rian! Sudah pulang, Nak?"

    n "Rian membeku."

    show boti at posisi_kiri onlayer characters

    r "Ibu...?"

    hide boti onlayer characters

    n "Suara itu terdengar semakin jelas."

    i "Ayo masuk. Ibu sudah siapkan makan malam."

    n "Rian memperhatikan pemandangan di luar jendela."

    n "Ia melihat sosok Ibu berdiri di depan pintu rumah."

    show boti at posisi_kiri onlayer characters

    r "Bu..."

    hide boti onlayer characters

    n "Rian mencoba membuka pintu gerbong."

    n "Namun, pintu itu tidak bergerak."

    show boti at posisi_kiri onlayer characters

    r "Tunggu! Bu!"

    hide boti onlayer characters

    n "Kereta kembali bergerak semakin cepat."

    n "Pemandangan rumah perlahan menjauh."

    n "Suara Ibu semakin samar hingga akhirnya menghilang."

    scene black with fade

    n "Gerbong kembali gelap."

    n "Rian duduk dengan napas yang tidak teratur."

    show boti at posisi_kiri onlayer characters

    r "Kenapa..."

    r "Kenapa aku nggak bisa turun?"

    hide boti onlayer characters

    n "Tiba-tiba terdengar suara dari pengeras suara gerbong."

    n "\"Penumpang dimohon tetap berada di tempat duduk.\""

    n "\"Perjalanan menuju pemberhentian berikutnya akan segera dimulai.\""

    scene gerbong_kereta with fade

    n "Beberapa saat kemudian, lampu gerbong kembali menyala."

    n "Di kursi seberang Rian, kini duduk Gadis Payung Merah."

    show boti at posisi_kiri onlayer characters

    r "Kamu lagi?"

    hide boti onlayer characters

    g "Sepertinya kamu sudah melihat sesuatu."

    show boti at posisi_kiri onlayer characters

    r "Itu rumahku. Aku melihat Ibu."

    hide boti onlayer characters

    g "Lalu kenapa kamu tidak bisa turun?"

    menu:

        "Aku ingin pulang, tapi belum tahu caranya.":

            $ honesty += 1
            $ mother_bond += 1

            show boti at posisi_kiri onlayer characters

            r "Aku memang ingin pulang."

            r "Tapi aku nggak tahu bagaimana caranya keluar dari tempat ini."

            hide boti onlayer characters

            g "Mungkin karena kamu belum tahu apa yang sebenarnya ingin kamu selesaikan."

        "Aku masih punya urusan yang belum selesai.":

            $ memory += 1

            show boti at posisi_kiri onlayer characters

            r "Masih ada banyak hal yang harus aku selesaikan."

            r "Aku belum bisa pulang begitu saja."

            hide boti onlayer characters

            g "Apa semuanya memang harus selesai sebelum kamu kembali?"

        "Aku tidak ingin membicarakannya.":

            show boti at posisi_kiri onlayer characters

            r "Aku nggak mau membahasnya."

            hide boti onlayer characters

            g "Baiklah."

            n "Gadis itu mengalihkan pandangannya ke arah jendela."

    n "Gadis Payung Merah kemudian berdiri."

    g "Kita sebentar lagi sampai."

    show boti at posisi_kiri onlayer characters

    r "Sampai di mana?"

    hide boti onlayer characters

    g "Tempat yang mungkin selama ini kamu hindari."

    n "Gadis itu berjalan menuju pintu gerbong."

    n "Sebelum keluar, ia berhenti sejenak."

    g "Rian."

    show boti at posisi_kiri onlayer characters

    r "Ya?"

    hide boti onlayer characters

    g "Tidak semua orang yang pulang harus membawa keberhasilan."

    g "Terkadang, pulang adalah cara seseorang belajar menerima dirinya sendiri."

    n "Pintu gerbong terbuka."

    n "Cahaya putih masuk memenuhi ruangan."

    scene black with fade

    n "Suara kereta perlahan berhenti."

    n "Pengumuman terdengar dari pengeras suara."

    n "\"Kereta telah tiba di pemberhentian kedua.\""

    n "\"Selamat datang di Stasiun Kenangan.\""

    n "Rian berdiri dan mengambil kopernya."

    n "Ia melangkah keluar dari gerbong."

    n "Namun, kali ini ia tidak lagi berjalan sendirian."

    jump bab_5
label bab_5:

    scene stasiun_kenangan with fade

    n "Pintu gerbong tertutup perlahan. Suara kereta semakin menjauh, meninggalkan Rian seorang diri di sebuah peron yang terasa asing."

    n "Berbeda dengan Stasiun 0, tempat ini terlihat lebih hidup. Lampu-lampu kuning menerangi bangku kayu, sementara beberapa daun kering berserakan di sepanjang peron."

    show boti at posisi_kiri onlayer characters

    r "Stasiun Kenangan..."

    r "Tempat apalagi ini?"

    hide boti onlayer characters

    n "Rian mengamati papan nama stasiun. Di bawah tulisan tersebut terdapat sebuah kalimat kecil."

    n "'Tidak semua yang tertinggal harus dilupakan.'"

    show boti at posisi_kiri onlayer characters

    r "Apa maksudnya?"

    hide boti onlayer characters

    n "Di dekat bangku kayu, Rian melihat sebuah kotak kecil yang diletakkan di atas meja."

    menu:

        "Membuka kotak kecil di atas meja.":

            $ memory += 1

            n "Rian membuka kotak tersebut secara perlahan."

            n "Di dalamnya terdapat beberapa benda lama. Sebuah mobil-mobilan kecil, foto keluarga, dan kartu ucapan ulang tahun."

            show boti at posisi_kiri onlayer characters

            r "Tunggu..."

            r "Aku ingat benda-benda ini."

            hide boti onlayer characters

            if melihat_foto:

                n "Rian mengambil foto keluarga yang sebelumnya ia temukan di peron."

                n "Foto yang sama. Namun kali ini, ia mulai mengingat kejadian di balik foto tersebut."

                r "Waktu itu Ibu yang motret..."

            else:

                n "Rian memperhatikan foto keluarga yang terselip di antara benda-benda tersebut."

                n "Ada dirinya yang masih kecil, berdiri di samping seorang perempuan yang tersenyum."

                r "Ibu..."

            n "Sebuah kenangan perlahan muncul di pikirannya."

            n "Dulu, Rian pernah berjanji akan pulang sebelum ulang tahun ibunya."

        "Duduk di bangku kayu dan memperhatikan sekitar.":

            n "Rian meletakkan kopernya di samping bangku, lalu duduk untuk beristirahat."

            n "Suasana stasiun terasa begitu tenang. Tidak ada pengumuman keberangkatan, tidak ada suara kendaraan, hanya angin yang berembus pelan."

            show boti at posisi_kiri onlayer characters

            r "Aneh..."

            r "Kenapa tempat ini terasa familiar?"

            hide boti onlayer characters

            $ memory += 1

        "Berjalan menuju lorong di belakang peron.":

            n "Rian meninggalkan bangku kayu dan berjalan menuju lorong kecil di belakang peron."

            n "Di sepanjang dinding, terdapat beberapa bingkai foto yang tampak sudah lama terpasang."

            n "Salah satu foto memperlihatkan seorang anak laki-laki sedang memegang piala kecil."

            show boti at posisi_kiri onlayer characters

            r "Itu..."

            r "Foto waktu aku masih sekolah."

            hide boti onlayer characters

            $ memory += 1

    n "Tiba-tiba terdengar suara langkah kaki dari belakang."

    show laki at posisi_kanan onlayer characters

    p "Akhirnya sampai juga, Mas."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Pak Seno?"

    r "Bapak sebenarnya siapa, sih? Kenapa selalu muncul di tempat seperti ini?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Saya hanya petugas yang memastikan setiap penumpang menemukan jalannya."

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Jalan menuju mana?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Itu tergantung pada apa yang ingin Mas temukan."

    p "Ada orang yang mencari tempat untuk dituju. Ada juga yang sebenarnya hanya ingin memperbaiki sesuatu yang pernah ditinggalkan."

    hide laki onlayer characters

    n "Pak Seno kemudian menunjuk sebuah papan pengumuman di dekat lorong."

    show laki at posisi_kanan onlayer characters

    p "Coba Mas lihat papan itu."

    hide laki onlayer characters

    n "Rian mendekati papan pengumuman tersebut. Di sana terdapat beberapa lembar kertas dengan tulisan tangan yang berbeda-beda."

    n "Salah satu tulisan tampak sangat familiar."

    show boti at posisi_kiri onlayer characters

    r "Tulisan ini..."

    hide boti onlayer characters

    n "'Nak, kalau sudah selesai dengan urusanmu, rumah selalu punya tempat untukmu.'"

    n "Tidak ada nama pengirim di bawah kalimat tersebut."

    if mother_bond >= 2:

        show boti at posisi_kiri onlayer characters

        r "Ibu..."

        r "Kenapa aku baru sadar kalau selama ini Ibu cuma ingin aku pulang?"

        hide boti onlayer characters

    else:

        show boti at posisi_kiri onlayer characters

        r "Siapa yang menulis ini?"

        hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Ada sesuatu yang ingin Mas sampaikan kepada seseorang?"

    hide laki onlayer characters

    menu:

        "Aku ingin meminta maaf kepada Ibu.":

            $ honesty += 1
            $ mother_bond += 2

            show boti at posisi_kiri onlayer characters

            r "Aku terlalu sibuk memikirkan pekerjaan sampai lupa ada seseorang yang menunggu di rumah."

            r "Bahkan ketika Ibu cuma ingin tahu kabarku, aku malah membentaknya."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Kalau begitu, Mas sudah tahu apa yang harus dilakukan."

            hide laki onlayer characters

        "Aku ingin tahu kenapa aku bisa berada di tempat ini.":

            $ memory += 1

            show boti at posisi_kiri onlayer characters

            r "Aku bahkan nggak ingat bagaimana caranya sampai di sini."

            r "Apa semua ini cuma mimpi?"

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Terkadang, pertanyaan yang paling sulit bukan tentang bagaimana kita sampai di suatu tempat."

            p "Melainkan kenapa kita terus berada di sana."

            hide laki onlayer characters

        "Tidak ada. Aku cuma ingin segera pulang.":

            $ honesty += 1

            show boti at posisi_kiri onlayer characters

            r "Aku cuma ingin semuanya selesai."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Pulang bukan berarti semua masalah langsung selesai, Mas."

            p "Tapi setidaknya, Mas tidak harus menghadapinya sendirian."

            hide laki onlayer characters

    n "Tiba-tiba terdengar suara perempuan dari pengeras suara stasiun."

    n "Namun, suara itu bukan pengumuman keberangkatan."

    i "Rian..."

    n "Rian langsung terdiam."

    show boti at posisi_kiri onlayer characters

    r "Ibu?"

    hide boti onlayer characters

    i "Kalau kamu mendengar suara Ibu, berarti kamu masih ingat jalan pulang."

    n "Suara tersebut terdengar semakin pelan."

    i "Ibu nggak pernah meminta kamu menjadi orang hebat, Nak."

    i "Ibu cuma ingin kamu pulang dalam keadaan baik."

    show boti at posisi_kiri onlayer characters

    r "Bu, tunggu!"

    r "Rian mau pulang, Bu..."

    hide boti onlayer characters

    n "Rian berlari menuju pengeras suara, tetapi suaranya telah menghilang."

    n "Di tengah keheningan, Gadis Payung Merah muncul dari ujung peron."

    show boti at posisi_kiri onlayer characters

    r "Kamu lagi..."

    hide boti onlayer characters

    g "Kali ini kamu mendengarnya, kan?"

    show boti at posisi_kiri onlayer characters

    r "Itu suara ibuku."

    hide boti onlayer characters

    g "Lalu, apa yang ingin kamu katakan kepadanya?"

    menu:

        "Aku ingin pulang dan memperbaiki semuanya.":

            $ honesty += 1
            $ mother_bond += 1

            show boti at posisi_kiri onlayer characters

            r "Aku nggak tahu apakah semuanya masih bisa diperbaiki."

            r "Tapi aku ingin mencoba."

            hide boti onlayer characters

            g "Kalau begitu, jangan terus menunda."

        "Aku belum siap menghadapi semuanya.":

            $ memory += 1

            show boti at posisi_kiri onlayer characters

            r "Aku takut kalau ternyata semuanya sudah terlambat."

            hide boti onlayer characters

            g "Rasa takut tidak akan membuat waktu berhenti."

            g "Tapi kamu masih bisa menentukan apa yang akan kamu lakukan setelah ini."

        "Aku tidak tahu harus berkata apa.":

            show boti at posisi_kiri onlayer characters

            r "Aku benar-benar nggak tahu."

            hide boti onlayer characters

            g "Tidak apa-apa. Setidaknya sekarang kamu mulai mendengarkan."

    n "Gadis itu menunjuk sebuah pintu besar di ujung peron."

    n "Di atas pintu tersebut tertulis sebuah kalimat."

    n "'PERON TERAKHIR — TEMPAT MENENTUKAN TUJUAN'"

    show boti at posisi_kiri onlayer characters

    r "Peron terakhir?"

    hide boti onlayer characters

    g "Perjalananmu hampir selesai, Rian."

    g "Tapi sebelum itu, ada satu hal yang harus kamu ingat."

    show boti at posisi_kiri onlayer characters

    r "Apa?"

    hide boti onlayer characters

    g "Kamu tidak harus membawa pulang semua keberhasilanmu."

    g "Terkadang, cukup pulang sebagai dirimu sendiri."

    n "Rian menunduk. Tangannya menggenggam erat pegangan koper hitam."

    n "Untuk pertama kalinya, ia tidak memikirkan pekerjaan, target, ataupun hal-hal yang harus dibuktikan kepada orang lain."

    n "Ia hanya ingin pulang."

    scene black with fade

    n "Pintu besar di ujung peron perlahan terbuka."

    n "Cahaya putih memenuhi pandangan Rian."

    n "Perjalanan menuju peron terakhir pun dimulai."

    jump bab_6

label bab_6:

    scene peron_terakhir with fade

    n "Cahaya putih perlahan menghilang."

    n "Rian kini berdiri di sebuah peron yang jauh lebih luas dibandingkan stasiun sebelumnya."

    n "Tidak ada bangku, tidak ada loket, dan tidak ada papan jadwal."

    n "Hanya ada satu kereta yang berhenti tepat di hadapannya."

    show boti at posisi_kiri onlayer characters

    r "Jadi... ini peron terakhir?"

    hide boti onlayer characters

    n "Rian memperhatikan kereta tersebut. Pada bagian depan gerbong terdapat tulisan kecil."

    n "'TUJUAN: RUMAH'"

    show boti at posisi_kiri onlayer characters

    r "Rumah..."

    hide boti onlayer characters

    n "Di dekat pintu kereta, terdapat sebuah meja kecil dengan tiga benda di atasnya."

    n "Sebuah amplop, jam tangan, dan foto keluarga."

    n "Rian mengenali ketiganya."

    menu:

        "Mengambil amplop.":

            $ memory += 1

            n "Rian mengambil amplop tersebut."

            n "Di bagian depannya tertulis namanya sendiri."

            n "Ia membuka amplop itu dan menemukan selembar surat."

            if mother_bond >= 2:

                n "'Rian, Ibu tahu kamu sedang berusaha keras di sana. Jangan lupa, kesehatan dan kabarmu juga penting bagi Ibu.'"

                n "'Ibu selalu menunggu kamu pulang. Tidak perlu membawa apa-apa.'"

            else:

                n "'Rian, sudah lama Ibu tidak mendengar kabarmu. Ibu hanya ingin tahu kamu baik-baik saja.'"

                n "'Kalau ada waktu, telepon Ibu, ya.'"

            show boti at posisi_kiri onlayer characters

            r "Aku bahkan nggak pernah membalas pesan-pesan Ibu..."

            hide boti onlayer characters

            $ honesty += 1

        "Mengambil jam tangan.":

            n "Rian mengambil jam tangan yang tergeletak di atas meja."

            n "Jarumnya berhenti tepat pada pukul dua belas."

            show boti at posisi_kiri onlayer characters

            r "Jam ini..."

            r "Sejak tadi aku terus melihat waktu."

            r "Seolah-olah ada sesuatu yang harus aku kejar."

            hide boti onlayer characters

            n "Rian memasang kembali jam tangan itu."

            n "Namun, untuk pertama kalinya, ia tidak merasa perlu memeriksa jarumnya."

            $ memory += 1

        "Mengambil foto keluarga.":

            n "Rian mengambil foto keluarga yang tergeletak di atas meja."

            n "Dalam foto tersebut, ia berdiri di tengah kedua orang tuanya."

            n "Wajahnya terlihat bahagia, tanpa memikirkan pekerjaan atau masa depan."

            show boti at posisi_kiri onlayer characters

            r "Dulu semuanya terasa sederhana."

            r "Aku cuma perlu pulang ke rumah untuk merasa cukup."

            hide boti onlayer characters

            $ mother_bond += 1
            $ father_bond += 1

    n "Tiba-tiba terdengar suara langkah kaki dari belakang."

    show laki at posisi_kanan onlayer characters

    p "Sudah menemukan tujuanmu, Mas?"

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Pak Seno..."

    r "Bapak masih belum mau menjelaskan sebenarnya tempat ini apa?"

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Mungkin karena Mas sendiri belum siap mendengar jawabannya."

    p "Sejak pertama kali datang, Mas selalu memikirkan apa yang belum berhasil Mas capai."

    p "Tapi pernahkah Mas bertanya apa yang sudah Mas tinggalkan?"

    hide laki onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Aku cuma ingin berhasil, Pak."

    r "Aku ingin membuktikan kalau semua pengorbananku selama ini nggak sia-sia."

    hide boti onlayer characters

    show laki at posisi_kanan onlayer characters

    p "Tidak ada yang salah dengan keinginan untuk berhasil."

    p "Namun, jangan sampai Mas kehilangan alasan kenapa dulu Mas memulai semuanya."

    hide laki onlayer characters

    n "Rian terdiam."

    n "Perlahan, ingatannya kembali pada malam ketika ia menerima kabar bahwa kontrak kerjanya tidak diperpanjang."

    n "Ia mengingat telepon dari ibunya, koper yang disiapkan terburu-buru, dan perjalanan malam yang tidak pernah benar-benar ia selesaikan."

    show boti at posisi_kiri onlayer characters

    r "Jadi... malam itu..."

    hide boti onlayer characters

    p "Mas masih ingat?"

    show boti at posisi_kiri onlayer characters

    r "Aku kehilangan pekerjaan."

    r "Aku takut pulang tanpa membawa sesuatu yang bisa kubanggakan."

    r "Aku bahkan sampai marah kepada Ibu hanya karena beliau menanyakan kapan aku pulang."

    hide boti onlayer characters

    n "Pak Seno tidak langsung menjawab."

    n "Ia hanya memandang kereta yang sejak tadi menunggu."

    show laki at posisi_kanan onlayer characters

    p "Kadang, yang membuat perjalanan terasa jauh bukan jaraknya."

    p "Melainkan hal-hal yang tidak berani kita hadapi."

    hide laki onlayer characters

    n "Tiba-tiba suara perempuan terdengar dari arah pintu kereta."

    g "Rian."

    n "Gadis Payung Merah berdiri di dekat pintu gerbong."

    show boti at posisi_kiri onlayer characters

    r "Kamu..."

    hide boti onlayer characters

    g "Kamu sudah sampai sejauh ini."

    g "Sekarang, kamu harus menentukan sendiri ke mana kamu akan melangkah."

    n "Rian melihat ke arah kereta. Kemudian ia kembali menatap Pak Seno."

    menu:

        "Naik kereta dan pulang.":

            $ honesty += 2
            $ mother_bond += 1

            n "Rian menarik napas panjang."

            show boti at posisi_kiri onlayer characters

            r "Aku mau pulang."

            r "Aku nggak tahu apa yang akan terjadi setelah ini."

            r "Tapi aku nggak mau terus-terusan lari."

            hide boti onlayer characters

            show laki at posisi_kanan onlayer characters

            p "Kalau begitu, silakan naik, Mas."

            hide laki onlayer characters

            $ keputusan_akhir = "pulang"

        "Tetap berdiri dan meminta penjelasan.":

            $ memory += 1

            show boti at posisi_kiri onlayer characters

            r "Tunggu."

            r "Sebelum aku pergi, aku ingin tahu satu hal."

            r "Apakah semua ini benar-benar terjadi?"

            hide boti onlayer characters

            g "Tidak semua hal harus kamu pahami sekarang."

            g "Yang terpenting adalah apa yang akan kamu lakukan setelah mengingat semuanya."

            show boti at posisi_kiri onlayer characters

            r "Aku mengerti..."

            hide boti onlayer characters

            $ keputusan_akhir = "memahami"

        "Menolak naik karena merasa belum siap.":

            $ honesty += 1

            show boti at posisi_kiri onlayer characters

            r "Aku belum siap."

            r "Aku masih takut menghadapi semuanya."

            hide boti onlayer characters

            g "Tidak apa-apa merasa takut, Rian."

            g "Tapi jangan jadikan rasa takut sebagai alasan untuk terus menghindar."

            n "Rian menunduk cukup lama sebelum akhirnya kembali melihat kereta."

            $ keputusan_akhir = "ragu"

    n "Suara pengumuman terdengar dari pengeras suara."

    n "Kereta tujuan rumah akan segera diberangkatkan."

    if keputusan_akhir == "pulang":

        n "Rian melangkah masuk ke dalam gerbong."

        n "Sebelum pintu tertutup, ia sempat menoleh ke arah Pak Seno."

        show boti at posisi_kiri onlayer characters

        r "Terima kasih, Pak."

        hide boti onlayer characters

        show laki at posisi_kanan onlayer characters

        p "Hati-hati di perjalanan, Mas."

        hide laki onlayer characters

    elif keputusan_akhir == "memahami":

        n "Rian kembali melihat papan kecil di depan kereta."

        n "Tulisan tujuan rumah masih terlihat jelas."

        n "Setelah beberapa saat, ia akhirnya melangkah masuk."

    else:

        n "Rian masih berdiri di tempatnya."

        n "Namun, kali ini ia tidak lagi berjalan menjauh dari kereta."

        n "Ia mengangkat kopernya dan perlahan memasuki gerbong."

    scene black with fade

    n "Pintu kereta tertutup."

    n "Suara mesin mulai terdengar, disusul gerakan roda yang perlahan membawa kereta meninggalkan peron."

    n "Rian duduk di dekat jendela."

    n "Di luar, cahaya stasiun semakin jauh."

    n "Ia memejamkan mata."

    n "Untuk pertama kalinya setelah sekian lama, ia tidak memikirkan apa yang harus dibuktikan."

    n "Ia hanya ingin sampai di rumah."

    jump bab_7

label bab_7:

    scene black with fade

    n "Suara roda kereta perlahan melemah."

    n "Cahaya matahari mulai masuk melalui jendela gerbong."

    n "Rian membuka matanya."

    n "Di hadapannya, tidak ada lagi kabut atau lorong panjang yang asing."

    n "Hanya sebuah stasiun kecil yang pernah ia lewati dalam perjalanan pulang."

    show boti at posisi_kiri onlayer characters

    r "Akhirnya..."

    hide boti onlayer characters

    n "Rian mengambil koper hitamnya dan turun dari kereta."

    scene black with fade

    n "Beberapa saat kemudian, sebuah kendaraan mengantarnya menuju rumah."

    n "Jalanan yang dahulu terasa begitu jauh kini terlihat semakin familiar."

    n "Pepohonan di pinggir jalan, warung kecil di persimpangan, hingga pagar rumah yang mulai kusam."

    n "Semuanya masih ada."

    scene rumah_pagi with dissolve

    n "Rian berdiri di depan sebuah rumah sederhana."

    n "Rumah yang sudah hampir setahun tidak ia kunjungi."

    show boti at posisi_kiri onlayer characters

    r "Rumah..."

    hide boti onlayer characters

    n "Tangannya terangkat untuk mengetuk pintu, tetapi ia berhenti sejenak."

    n "Ada banyak hal yang ingin ia katakan."

    n "Namun, tidak satu pun terasa cukup untuk menggambarkan apa yang selama ini ia pendam."

    menu:

        "Mengetuk pintu dan memanggil Ibu.":

            $ honesty += 1
            $ mother_bond += 1

            n "Rian mengetuk pintu sebanyak tiga kali."

            show boti at posisi_kiri onlayer characters

            r "Bu..."

            r "Rian pulang."

            hide boti onlayer characters

        "Menunggu di depan rumah beberapa saat.":

            n "Rian meletakkan kopernya di samping kaki."

            n "Ia memperhatikan rumah tersebut cukup lama."

            show boti at posisi_kiri onlayer characters

            r "Sudah lama sekali..."

            hide boti onlayer characters

            n "Setelah menarik napas panjang, Rian akhirnya mengetuk pintu."

            $ memory += 1

        "Menelepon Ibu terlebih dahulu.":

            n "Rian mengambil ponselnya dan mencari nomor Ibu."

            n "Jarinya sempat berhenti sebelum menekan tombol panggil."

            show boti at posisi_kiri onlayer characters

            r "Bu, ini Rian."

            r "Rian sudah di depan rumah."

            hide boti onlayer characters

            $ mother_bond += 1

    n "Tidak lama kemudian, pintu rumah terbuka."

    show ibu at posisi_kanan onlayer characters

    i "Rian...?"

    hide ibu onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Iya, Bu."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Kamu benar-benar pulang?"

    hide ibu onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Maaf, Bu."

    r "Rian terlalu lama pergi."

    hide boti onlayer characters

    n "Ibu terdiam sejenak. Matanya memperhatikan wajah Rian, seolah memastikan bahwa anaknya benar-benar berdiri di hadapannya."

    show ibu at posisi_kanan onlayer characters

    i "Sudah makan, Nak?"

    hide ibu onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Belum, Bu."

    hide boti onlayer characters

    n "Ibu menghela napas kecil."

    show ibu at posisi_kanan onlayer characters

    i "Ya sudah, masuk dulu. Ibu masakkan sesuatu."

    hide ibu onlayer characters

    n "Rian menunduk. Pertanyaan sederhana itu membuatnya teringat pada malam ketika ia justru membentak ibunya melalui telepon."

    show boti at posisi_kiri onlayer characters

    r "Bu..."

    r "Rian mau cerita sesuatu."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Nanti saja, Nak. Sekarang istirahat dulu."

    hide ibu onlayer characters

    n "Rian masuk ke dalam rumah."

    scene ruang_tamu with dissolve

    n "Tidak banyak yang berubah. Jam dinding masih tergantung di tempat yang sama. Foto keluarga masih tersusun di atas lemari."

    n "Namun, ada satu hal yang baru ia sadari."

    n "Selama ini, ia terlalu sibuk mencari tempat untuk membuktikan dirinya sampai lupa bahwa ada tempat yang selalu menerimanya."

    if keputusan_akhir == "pulang" and mother_bond >= 3 and honesty >= 2:

        jump ending_1

    elif mother_bond >= 2 or honesty >= 2:

        jump ending_2

    else:

        jump ending_3


label ending_1:

    scene ruang_tamu with fade

    n "Malam harinya, Rian duduk bersama ibunya di ruang tamu."

    n "Untuk pertama kalinya setelah sekian lama, ia menceritakan semuanya."

    show boti at posisi_kiri onlayer characters

    r "Bu, sebenarnya kontrak kerja Rian sudah nggak diperpanjang sejak malam itu."

    r "Rian takut pulang karena merasa gagal."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Kenapa harus takut, Nak?"

    i "Kamu pikir Ibu hanya akan bangga kalau kamu membawa keberhasilan?"

    hide ibu onlayer characters

    show boti at posisi_kiri onlayer characters

    r "Rian cuma nggak mau mengecewakan Ibu."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Ibu lebih kecewa kalau kamu merasa harus menghadapi semuanya sendirian."

    hide ibu onlayer characters

    n "Rian terdiam. Tidak ada jawaban yang bisa ia berikan."

    n "Ia hanya menunduk dan mendengarkan."

    show boti at posisi_kiri onlayer characters

    r "Maaf, Bu."

    r "Mulai sekarang Rian akan lebih sering pulang."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Iya, Nak. Kita jalani pelan-pelan."

    hide ibu onlayer characters

    scene black with fade

    n "Malam itu tidak mengubah semua masalah yang dimiliki Rian."

    n "Pekerjaannya masih harus ia pikirkan. Masa depannya masih belum pasti."

    n "Namun, ada satu hal yang akhirnya ia pahami."

    n "Kegagalan bukan alasan untuk menjauh dari orang-orang yang menyayanginya."

    n "Dan pulang bukan berarti menyerah."

    n "Terkadang, pulang adalah langkah pertama untuk memulai kembali."

    centered "{size=45}ENDING 1{/size}"

    centered "{size=32}AKHIR DARI SEBUAH PERJALANAN{/size}"

    return


label ending_2:

    scene ruang_tamu with fade

    n "Malam itu, Rian duduk di ruang tamu bersama ibunya."

    n "Mereka tidak banyak berbicara."

    n "Ada beberapa hal yang masih sulit Rian ungkapkan."

    show boti at posisi_kiri onlayer characters

    r "Bu, Rian belum tahu harus mulai dari mana."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Tidak perlu terburu-buru, Nak."

    i "Kamu bisa cerita kapan saja."

    hide ibu onlayer characters

    n "Rian mengangguk pelan."

    n "Ia belum sepenuhnya berdamai dengan dirinya sendiri."

    n "Namun, setidaknya kali ini ia tidak lagi berusaha menyembunyikan semuanya."

    show boti at posisi_kiri onlayer characters

    r "Terima kasih sudah menunggu, Bu."

    hide boti onlayer characters

    show ibu at posisi_kanan onlayer characters

    i "Ibu selalu punya waktu untuk kamu."

    hide ibu onlayer characters

    scene black with fade

    n "Tidak semua luka dapat selesai dalam satu malam."

    n "Tidak semua kesalahan dapat diperbaiki dengan satu permintaan maaf."

    n "Namun, Rian akhirnya memahami bahwa perubahan tidak harus dimulai dengan sesuatu yang besar."

    n "Kadang, perubahan dimulai dari keberanian untuk kembali."

    centered "{size=45}ENDING 2{/size}"

    centered "{size=32}RUMAH YANG MENUNGGU{/size}"

    return


label ending_3:

    scene ruang_tamu with fade

    n "Rian duduk sendirian di ruang tamu."

    n "Ibunya sudah masuk ke kamar untuk beristirahat."

    n "Di atas meja terdapat foto keluarga yang sejak tadi menarik perhatiannya."

    show boti at posisi_kiri onlayer characters

    r "Aku sudah pulang..."

    r "Tapi kenapa rasanya masih ada sesuatu yang belum selesai?"

    hide boti onlayer characters

    n "Rian mengambil foto tersebut dan memperhatikannya cukup lama."

    n "Ia menyadari bahwa perjalanan panjangnya tidak serta-merta menghilangkan rasa takut yang selama ini ia miliki."

    n "Masih ada banyak hal yang harus ia hadapi."

    n "Namun, setidaknya sekarang ia sudah berada di rumah."

    scene black with fade

    n "Di luar rumah, malam semakin larut."

    n "Rian belum menemukan semua jawaban."

    n "Tetapi mungkin, perjalanan yang sebenarnya memang baru saja dimulai."

    centered "{size=45}ENDING 3{/size}"

    centered "{size=32}PERJALANAN YANG BELUM SELESAI{/size}"

    return