import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('song_data_diolah.csv')

st.markdown(
    """
    <h1 style='text-align: center;'>APLIKASI MEMPREDIKSI POPULARITAS LAGU DENGAN MENGGUNAKAN ALGORITMA RANDOM FOREST</h1>
    """, 
    unsafe_allow_html=True
)
st.write('Literatur Pengertian Setiap Kolom')

lit = ['song_name', 'song_popularity', 'song_duration_min', 'danceability','energy','key','loudness','audio_mode','speechiness','time_signature','tempo_category_numeric']

literatur = st.selectbox('Pilih Literatur yang ingin anda ketahui', lit)
        
if literatur == 'song_name':
    st.header('Song Name')
    st.subheader('Song Name atau Judul Lagu')
    st.write('Judul Lagu merupakan nama atau sebutan yang diberikan kepada sebuah lagu untuk mengidentifikasinya. Judul ini sering mencerminkan tema, lirik, atau perasaan yang ingin disampaikan oleh pencipta lagu.')

elif literatur == 'song_popularity':
    st.header('Song Popularity')
    st.subheader('Song Popularity atau Popularitas sebuah Lagu')
    st.write('mengacu pada ukuran seberapa populer atau terkenal sebuah lagu. Popularitas ini biasanya dihitung berdasarkan berbagai faktor seperti jumlah pemutaran (streams) di platform musik digital, jumlah unduhan, jumlah like atau share, serta interaksi sosial lainnya (seperti komentar dan ulasan).')
    st.markdown('''Namun pada dataset kali ini,Popularitas sebuah lagu diukur dengan faktor yang berbeda,yakni :
- Durasi Lagu
- Dance Ability : Kemampuan sebuah lagu untuk membuat seseorang menari 
- Energy : Energy adalah Tingkat energi dari sebuah lagu
- Nada Dasar : merupakan nilai numerik yang mewakili nada dasar dari lagu, dengan skala 0 hingga 11 sesuai dengan nada pada tangga nada musik
- Loudness : menunjukkan volume rata-rata dari sebuah lagu.
- Audio Mode : Audio Mode merupakan jenis audio dari lagu tersebut apakah merupakan audio yang berjenis Mono atau Stereo
-Speechness : Tingkat ada tidaknya unsur vokal atau ucapan dalam sebuah lagu.
- Time Signature : Tanda birama dari sebuah lagu.
- Tempo Category Numeric : Tempo yang dikategorikan secara Numerik ''')

elif literatur == 'song_duration_min':
    st.header('Song Duration Min')
    st.subheader('Durasi Lagu dalam hitungan Menit')
    st.write('Fitur ini diukur dalam satuan waktu (menit) dan bisa berupa nilai desimal untuk menunjukkan durasi yang lebih tepat. Contohnya, 3.5 berarti lagu berdurasi 3 menit dan 30 detik.')
    st.markdown('''Dimana itu dihitung dengan cara berikut :
- Contoh: Durasi Lagu 3 Menit 20 Detik yang berarti (Menit: 3 Detik: 20)
- Konversikan Detik Menjadi menit :
    * Konversi detik menjadi menit : 20 / 60 = 0.3333
    * Gabungkan nilai menit dengan hasil konversi:
    * Durasi dalam desimal : 3 + 0.3333 = 3.3333
    * Jadi, 3 menit 20 detik dinotasikan dalam bentuk desimal sebagai 3.3333 menit.''')   

elif literatur == 'danceability':
    st.header('Dance Ability')
    st.subheader('Kemampuan lagu untuk membuat pendengar ingin menari.')
    st.markdown ('''Dalam konteks analisis musik, danceability sering kali digunakan untuk menilai seberapa baik sebuah lagu dapat membuat pendengar ingin bergerak atau menari berdasarkan beberapa karakteristik musik.
                Fitur danceability biasanya dihitung secara otomatis oleh algoritma di platform musik digital dan dinyatakan sebagai nilai numerik dalam rentang 0 hingga 1, di mana:
- 0 menunjukkan bahwa lagu tersebut tidak cocok untuk menari.
- 1 menunjukkan bahwa lagu tersebut sangat cocok untuk menari.''')

elif literatur == 'energy':
    st.header('Energy')
    st.subheader('ukuran intensitas dan aktivitas dari sebuah lagu')
    st.markdown ('''Fitur ini digunakan untuk mengukur seberapa energik sebuah lagu terdengar berdasarkan beberapa karakteristik audio. Seperti danceability, energy juga dinyatakan dalam bentuk nilai numerik yang berkisar dari 0 hingga 1, di mana:
- 0 menunjukkan bahwa lagu tersebut memiliki energi yang sangat rendah.
- 1 menunjukkan bahwa lagu tersebut memiliki energi yang sangat tinggi.''')

elif literatur == 'key':
    st.header('Key')
    st.subheader('Nada Dasar dari Sebuah Lagu')
    st.write ('key (nada dasar) sering dikategorikan secara numerik untuk memudahkan pemrosesan data. Dalam musik Barat, ada 12 nada utama dalam skala kromatik, dan ini biasanya diwakili oleh angka 0 hingga 11.')
    st.markdown('''Berikut adalah pembagian numerik untuk masing-masing nada dasar (key) :
- 0 (C): Nada dasar C Major.
- 1 (C#/Db): Nada dasar C# Major atau Db Major.
- 2 (D): Nada dasar D Major.
- 3 (D#/Eb): Nada dasar D# Major atau Eb Major.
- 4 (E): Nada dasar E Major.
- 5 (F): Nada dasar F Major.
- 6 (F#/Gb): Nada dasar F# Major atau Gb Major.
- 7 (G): Nada dasar G Major.
- 8 (G#/Ab): Nada dasar G# Major atau Ab Major.
- 9 (A): Nada dasar A Major.
- 10 (A#/Bb): Nada dasar A# Major atau Bb Major.
- 11 (B): Nada dasar B Major.

Berikut adalah literasi singkat tentang jenis jenis key diatas''')
    
    litkey = ['0','1','2','3','4','5','6','7','8','9','10','11']
    literaturkey = st.selectbox('Pilih literatur kategori numerik key yang ingin anda ketahui : ', litkey)
    
    if literaturkey == '0':
        st.header('0 (C)')
        st.subheader('Nada dasar C Major')
        st.write('C Major Tidak memiliki tanda kres (#) atau mol (b). Dikenal sebagai nada dasar yang memiliki sifat netral dan cerah.')
    
    elif literaturkey == '1':
        st.header('1 (C#/Db)')
        st.subheader('Nada Dasar C# Major / Db Major')
        st.write('C# Major memiliki 7 kres (#), sedangkan Db Major memiliki 5 mol (b). Memberikan karakteristik yang tajam dan cemerlang.')
        
    elif literaturkey == '2':
        st.header('2 (D)')
        st.subheader('Nada dasar D Major')
        st.write('D Major: Memiliki 2 kres (#) (F# dan C#).Oleh karena itu musik yang bernada dasar D Major terasa energik dan ceria.')
    
    elif literaturkey == '3':
        st.header('3 (D#/Eb)')
        st.subheader('Nada Dasar Nada dasar D# Major atau Eb Major')
        st.write('D# Major / Eb Major: D# Major memiliki 6 kres (#), sementara Eb Major memiliki 3 mol (b).Maka dari itu musik yang bernada dasar D# Major terdengar kaya dan terkadang megah.')
    
    elif literaturkey == '4':
        st.header('4 (E)')
        st.subheader('Nada Dasar E Major')
        st.write('E Major: Memiliki 4 kres (#) (F#, C#, G#, dan D#).Nada dasar berikut memiliki karakteristik yang terdengar cerah dan bersemangat.')     
    
    elif literaturkey == '5':
        st.header('5 (F)')
        st.subheader('Nada dasar F Major')
        st.write('F Major: Memiliki 1 mol (b) (Bb).Karakteristik lagu yang memiliki nada dasar ini adalah Terasa hangat dan penuh pengharapan.')

    elif literaturkey == '6':
        st.header('6 (F#/Gb)')
        st.subheader('Nada dasar F# Major atau Gb Major')
        st.write('F# Major / Gb Major: F# Major memiliki 6 kres (#), sementara Gb Major memiliki 6 mol (b).Karakteristik lagu yang memiliki nada dasar ini adalah Terdengar kompleks dan sedikit eksotis.')

    elif literaturkey == '7':
        st.header('7 (G)')
        st.subheader('Nada dasar G Major')
        st.write('G Major: Memiliki 1 kres (#) (F#).Kunci ini apabila diimplementasikan ke dalam sebuah lagu Sering dianggap memiliki karakteristik riang dan optimis')

    elif literaturkey == '8':
        st.header('8 (G#/Ab)')
        st.subheader('Nada dasar G# Major atau Ab Major')
        st.write('G# Major / Ab Major: G# Major memiliki 5 kres (#), sementara Ab Major memiliki 4 mol (b). Dengan nada dasar ini diimplementasikan dalam sebuah lagu maka akan memberikan perasaan yang elegan dan misterius.')

    elif literaturkey == '9':
        st.header('9 (A)')
        st.subheader('Nada dasar A Major')
        st.write('A Major: Memiliki 3 kres (#) (F#, C#, dan G#).Lagu yang memiliki nada dasar ini, memiliki aura yang kuat dan percaya diri.')
    
    elif literaturkey == '10':
        st.header('10 (A#/Bb)')
        st.subheader('Nada dasar A# Major atau Bb Major')
        st.write('A# Major / Bb Major: A# Major memiliki 7 kres (#), sementara Bb Major memiliki 2 mol (b). Nada dasar ini memiliki karakteristik yang Terdengar hangat nan kaya.')

    elif literaturkey == '11':
        st.header('11 (B)')
        st.subheader('Nada dasar B Major')
        st.write('B Major: Memiliki 5 kres (#) (F#, C#, G#, D#, dan A#). implementasi lagu yang memiliki nada dasar ini Terdengar memiliki karakteristik yang kuat dan penuh energi.')
        
    else:
        st.write('pilih Kategorikal Key di atas')

elif literatur == 'loudness':
    st.header('Loudness')
    st.subheader('Kenyaringan')
    st.write('Ukuran persepsi kekuatan atau intensitas suara yang terdengar dalam suatu lagu atau rekaman audio. Loudness mencerminkan seberapa keras atau lembut suatu suara terdengar bagi pendengar dan bukan hanya sekadar ukuran teknis dari amplitudo gelombang suara. Dalam konteks musik digital dan analisis audio, loudness diukur dalam unit desibel (dB), yang merupakan ukuran logaritmik dari intensitas suara.')

elif literatur == 'audio_mode':
    st.header('Audio Mode')
    st.subheader('Pengkategorian Mode Audio')
    st.write('Dalam konteks analisis musik mengacu pada modus atau skala musik yang digunakan dalam suatu lagu atau komposisi. Secara umum, audio mode dapat dibagi menjadi dua kategori utama: mayor (major) dan minor. Modus ini menentukan karakter tonal dan suasana dari lagu tersebut.')
    st.markdown(''' Biasanya, nilai-nilai ini adalah:
- 0 = Menandakan minor mode.
- 1 = Menandakan major mode. ''')

    litmode = ['0','1']
    literaturmode = st.selectbox('Pilih literatur kategori numerik key yang ingin anda ketahui : ', litmode)
    
    if literaturmode == '0':
        st.header('0 (Minor Mode)')
        st.subheader('Minor Mode')
        st.markdown(''' Minor Mode
- Mode minor sering dikaitkan dengan suasana yang lebih melankolis, sedih, atau serius. Lagu-lagu dalam modus minor cenderung memiliki nuansa emosional yang lebih dalam atau dramatis.
- Skala minor memiliki pola interval berbeda dari skala mayor: tone (T), semitone (S), tone (T), tone (T), semitone (S), tone (T), tone (T). Contoh: skala A minor terdiri dari nada A-B-C-D-E-F-G-A.''')
        st.markdown('''Pengaruhnya Mode Minor dalam Karakteristik Lagu :
- Karakteristik Suara dan Suasana : 
    * Lagu dalam mode minor terdengar lebih gelap, melankolis, dan sering kali penuh emosi. Skala minor memiliki interval yang memberikan kualitas suara yang lebih rendah dan lebih dalam dibandingkan dengan skala mayor.
    * Mode minor digunakan untuk mengekspresikan perasaan sedih, introspektif, misterius, atau bahkan dramatis. Banyak balada, lagu-lagu yang emosional, atau lagu dengan tema yang lebih serius sering kali ditulis dalam modus minor.
- Dlam Komposisi Musik :
    * Dalam skala minor, progresi akor sering kali melibatkan pola seperti i-iv-V (misalnya, Am-Dm-Em dalam A minor), yang menekankan suasana ketegangan dan resolusi yang lebih mendalam dan emosional.
    * Melodi dalam modus minor sering kali menggunakan interval yang lebih kecil dan motif yang berulang, menciptakan nuansa yang lebih reflektif atau bahkan dramatis. Modus minor juga cenderung memiliki lebih banyak variasi ritmis dan melodi untuk menambah kompleksitas emosional.''')
    
    elif literaturmode == '1':
        st.header('1 (C#/Db)')
        st.subheader('Nada Dasar C# Major / Db Major')
        st.markdown(''' Major Mode
- Mode mayor sering dikaitkan dengan suasana yang ceria, bahagia, optimis, dan terang. Lagu-lagu dalam modus mayor cenderung terdengar lebih riang dan penuh energi.
- Skala mayor memiliki pola interval khusus (jarak antar nada) yang terdiri dari: tone (T), tone (T), semitone (S), tone (T), tone (T), tone (T), semitone (S). Contoh: skala C mayor terdiri dari nada C-D-E-F-G-A-B-C.''')
        st.markdown('''Pengaruhnya Mode Major dalam Karakteristik Lagu :
- Karakteristik Suara dan Suasana : 
    * Lagu dalam mode mayor umumnya terdengar ceria, optimis, dan penuh energi. Nada-nada dalam skala mayor memiliki interval yang menghasilkan harmoni yang terang dan positif.
    * Modus mayor sering digunakan untuk menciptakan perasaan bahagia, semangat, atau kemenangan. Musik pop, lagu-lagu dansa, dan banyak lagu anak-anak biasanya ditulis dalam modus mayor untuk menciptakan suasana yang menyenangkan dan energik.
- Dlam Komposisi Musik :
    * Dalam skala mayor, progresi akor sering kali mengikuti pola I-IV-V (misalnya, C-F-G dalam C mayor), yang memberikan kesan stabil dan menyenangkan. Ini karena ketegangan dan resolusi yang diciptakan oleh progresi ini cenderung mengarah pada perasaan penutupan atau kepuasan.
    * Melodi dalam modus mayor cenderung bergerak dalam pola yang lebih naik-turun dengan interval yang lebih besar, menciptakan kesan kegembiraan dan dinamisme.''')
    else:
        st.write('pilih Kategorikal Mode Audio di atas')

elif literatur == 'speechiness':
    st.header('Speechiness')
    st.subheader('Speechiness atau Elemen Vokal')
    st.write('fitur audio yang digunakan dalam analisis musik dan pemrosesan audio untuk mengukur sejauh mana suatu trek atau lagu mengandung elemen vokal yang menyerupai ucapan atau pembicaraan.')

elif literatur == 'time_signature':
    st.header('Time Signature')
    st.subheader('Time Signature atau Birama')
    st.write ('Time signature (tanda waktu) adalah elemen penting dalam notasi musik yang menentukan bagaimana ritme sebuah lagu atau komposisi diatur. Time signature memberi tahu pemain musik berapa banyak ketukan dalam setiap bar (ukur) dan jenis notasi yang mewakili satu ketukan.')
    st.markdown('''Berikut adalah pembagian numerik untuk masing-masing Time Signature :

- Kategori 1 (1/4).
- Kategori 2 (2/4).
- Kategori 3 (3/4).
- Kategori 4 (4/4).
- Kategori 5 (5/4).

Berikut adalah literasi singkat tentang jenis jenis Time Signature diatas''')
    
    littime = ['1','2','3','4','5']
    literaturtime = st.selectbox('Pilih literatur kategori numerik Time Signature yang ingin anda ketahui : ', littime)
    
    if literaturtime == '1':
        st.header('Kategori 1 (1/4)')
        st.subheader('Birama 1/4')
        st.write('Time signature 1/4 adalah sangat tidak umum dalam musik Barat. Ini akan berarti hanya ada satu ketukan per bar, dan setiap ketukan diwakili oleh not seperempat. Biasanya, ini tidak digunakan sebagai time signature standar dalam komposisi musik.')
    
    elif literaturtime == '2':
        st.header('Kategori 2 (2/4)')
        st.subheader('Birama 2/4')
        st.write('Time signature ini memiliki dua ketukan per bar dan sering ditemukan dalam musik march dan polka. Biasanya memberikan kesan ritme yang cepat dan bersemangat.')
        
    elif literaturkey == '3':
        st.header('Kategori 3 (3/4)')
        st.subheader('Birama 3/4')
        st.write('Dikenal sebagai "waltz time," time signature ini memiliki tiga ketukan per bar dan sering digunakan dalam musik waltz dan beberapa jenis musik folk.')
    
    elif literaturkey == '4':
        st.header('Kategori 4 (4/4)')
        st.subheader('Birama 4/4')
        st.write('time signature paling umum dalam musik Barat, juga dikenal sebagai "common time." Banyak genre musik, termasuk pop, rock, dan klasik, menggunakan time signature ini karena kestabilan dan kesederhanaannya.')
    
    elif literaturkey == '5':
        st.header('Kategori 5 (5/4)')
        st.subheader('Birama 5/4')
        st.write('Time signature 5/4 memiliki lima ketukan dalam satu bar dan setiap ketukan diwakili oleh not seperempat. Ini adalah time signature yang relatif jarang digunakan dan biasanya muncul dalam musik yang ingin menciptakan rasa ketidakrataan atau keunikan ritmik.')
    else:
        st.write('pilih Kategorikal Time Signature di atas')

elif literatur == 'tempo_category_numeric':
    st.header('Tempo')
    st.subheader('Tempo dikategorikan dengan notasi numerik')
    st.write ('kecepatan atau laju di mana sebuah musik dimainkan, yang diukur dalam beats per minute (BPM) atau ketukan per menit.')
    st.markdown('''Berikut adalah pembagian numerik untuk masing-masing Tempo :

- Kategori 0 (Largo).
- Kategori 1 (Adagio).
- Kategori 2 (Andante).
- Kategori 3 (Moderato).
- Kategori 4 (Allegro).
- Kategori 5 (Presto).

Berikut adalah literasi singkat tentang jenis jenis Kategori Tempo diatas''')
    
    littempo = ['0','1','2','3','4','5','6']
    literaturtempo = st.selectbox('Pilih literatur kategori numerik key yang ingin anda ketahui : ', littempo)
    
    if literaturtempo == '0':
        st.header('Kategori 0 (Largo)')
        st.subheader('Rentang BPM: 40–60 BPM')
        st.write('Time signature 1/4 adalah sangat tidak umum dalam musik Barat. Ini akan berarti hanya ada satu ketukan per bar, dan setiap ketukan diwakili oleh not seperempat. Biasanya, ini tidak digunakan sebagai time signature standar dalam komposisi musik.')
    
    elif literaturtempo == '1':
        st.header('Kategori 1 (Adagio)')
        st.subheader('Rentang BPM: 66–76 BPM')
        st.write('Lambat dan penuh perasaan, sedikit lebih cepat dari Largo. Sering digunakan dalam musik yang melankolis atau romantis.')
        
    elif literaturtempo == '2':
        st.header('Kategori 2 (Andante)')
        st.subheader('Rentang BPM: 76–108 BPM')
        st.write('Kecepatan sedang yang tenang; sering diterjemahkan sebagai "kecepatan berjalan." Digunakan untuk bagian musik yang stabil dan tidak terlalu lambat atau cepat.')
    
    elif literaturtempo == '3':
        st.header('Kategori 3 (Moderato)')
        st.subheader('Rentang BPM: 108–120 BPM')
        st.write('Kecepatan sedang; lebih cepat dari Andante, tetapi tidak secepat Allegro. Digunakan untuk musik yang energik tetapi tetap tenang.')
    
    elif literaturtempo == '4':
        st.header('Kategori 4 (Allegro)')
        st.subheader('Rentang BPM: 120–168 BPM')
        st.write('Cepat, hidup, dan ceria. Sering digunakan dalam bagian musik yang dinamis dan bersemangat.')

    elif literaturtempo == '5':
        st.header('Kategori 5 (Presto)')
        st.subheader('Rentang BPM: 168–200 BPM')
        st.write('Sangat cepat dan bersemangat. Sering digunakan untuk bagian musik yang intens dan memerlukan kecepatan tinggi.')
        
    elif literaturtempo == '6':
        st.header('Kategori 6 (Prestissimo)')
        st.subheader('Rentang BPM: >200 BPM')
        st.write('Ekstrem cepat; lebih cepat dari Presto. Jarang digunakan kecuali untuk efek dramatis atau untuk menunjukkan keterampilan teknis musisi.')
    else:
        st.write('pilih Kategorikal Tempo di atas')

else:
    st.subheader('Pilih literatur yang ingin anda ketahui ')
