#Library
import streamlit as st
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu
from PIL import Image
import webbrowser


#Header
kolom1, kolom2, kolom3 = st.columns(3)
with kolom2:
    logo1 = Image.open('AKABOGOR-NEW.png')
    st.image(logo1, caption=None, width=150, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

st.title("Politeknik AKA Bogor")
st.header("Kalkulator Analisis Fisika")

tab1, tab2, tabx, tab3, tab4 = st.tabs(["Beranda", "Profil", "Materi", "Kalkulator","Kontak"])

with tab1:
    st.header((('''
    Selamat Datang di Aplikasi Kalkulator Analisis Fisika dari Kelompok 5 Kelas 1B
    Aplikasi ini dibuat untuk mempermudah dalam pengolahan perhitungan data analisis fisika yang dimana terdapat banyak data yang harus dihitung dalam waktu singkat dengan tepat dan akurat. 
    Tersedia 8 macam perhitungan percobaan Analisis Fisika, yaitu:
    1. Hubungan Kerapatan dan Kepekatan Larutan
    2. Penetapan Kerapatan (Curah, Absolut, dan Relatif)
    3. Penetapan Kekentalan Metode Laju Alir (Ostwald)
    4. Penetapan Kekentalan Metode Silinder Berputar (Brookfield)
    5. Penetapan Kekentalan Metode Laju Alir (Engler)
    6. Penetapan Titik Leleh 
    7. Penetapan Koefisien Pemuaian Air/Alkohol
    8. Penetapan Kuat Tekan
    
    Dengan memanfaatkan aplikasi perhitungan maka mahasiswa dapat lebih mudah dan cepat untuk mendapat dan mengolah data perhitungan.
    ''')))
    
with tab2:
    st.title('Ini Merupakan Tim Kami')
    st.write('---')
    first_column, second_column, third_column, fourth_column = st.columns(4)
    with first_column:
        profile1 = Image.open('ani.jpg')
        st.image(profile1)
        st.write('Cahyaning Fitriani Lestari')
        st.write('2219048')

    with second_column:
        profile2 = Image.open('cindy.jpg')
        st.image(profile2)
        st.write('Cindy Shella Aprilia')
        st.write('2219054')
        
    with third_column:
        profile3 = Image.open('Goodwill1.jpg')
        st.image(profile3)
        st.write('Goodwill Christian Sitinjak')
        st.write('2219079')
        
    with fourth_column:  
        profile4 = Image.open('hanif1.jpg')
        st.image(profile4)
        st.write('Hanif Ibrohim Sedyotomo')
        st.write('2219080')
with tabx:
    st.subheader("Ini adalah materi Praktikum Analisis Fisika")
    st.write('bisa di baca sebelum masuk laboratorium')
    with st.expander("Percobaan 1"):
        st.title("Hubungan Kerapatan dan Kepekatan Larutan")
        st.write('Kerapatan adalah perbandingan jumlah massa per satuan volume, sedangkan kepekatan adalah satuan relatif yang diperoleh dari perbandingan jumlah bahan terlarut per jumlah larutan. Hubungan antara kerapatan dan konsentrasi larutan, dapat diketahui dengan cara menetapkan kerapatan suatu larutan yang telah diketehui konsentrasinya secara kuantitatif melalui pembuatan larutan deret dengan konsentrasi tertentu. Kerapatan dapat ditentukan dengan cara membandingkan bobot larutan dengan volume larutan.')
        
    with st.expander("Percobaan 2"): 
        st.title("Penetapan Kerapatan (Curah, Absolut, dan Relatif)")
        st.write('Pada benda berbentuk butiran, dapat dibedakan antara kerapatan curah dan kerapatan absolut. Kerapatan curah adalah bobot bahan padat berbentuk butiran dibagi volume curah (volume bahan dalam bentuk tercurah). Kerapatan absolut adalah bobot bahan dibagi volume nyata bahan (volume curah dikurangi volume udara diantara butiran – butiran bahan). Sedangkan, kerapatan relatif adalah perbandingan kerapatan bahan dengan kerapatan air pada temperatur dan tekanan yang sama. Kerapatan dapat ditentukan dengan cara membandingkan bobot larutan dengan volume larutan.')
        
    with st.expander("Percobaan 3"): 
        st.title("Penetapan Kekentalan Metode Laju Alir (Ostwald)")
        st.write('Viskositas adalah sifat suatu fluida untuk menghambat pengaliran jika pada fluida diberikan gaya. Pada praktikum ini difokuskan dengan mengukur waktu alir yang dibutuhkan suatu fluida dalam konsentrasi tertentu menggunakanviskometer ostwald. Cairan dihisap melalui lubang pipa yang lain hingga mencapai garis atas. Selanjutnya, cairan dibiarkan mengalir dari garis atas hingga garis bawah dengan diperhatikan waktu alirnya. Semakin kental cairan, maka semakin lambat waktu yang diperlukan agar cairan mengalir.')
        
    with st.expander("Percobaan 4"):
        st.title("Penetapan Kekentalan Metode Silinder Berputar (Brookfield)")
        st.write('Viskositas adalah sifat suatu fluida untuk menghambat pengaliran jika pada fluida diberikan suatu gaya.  Dengan alat Viskometer Brookfield nilai viskositasnya didapatkan dengan mengukur gaya puntir sebuah rotor silinder (spindle) yang dicelupkan ke dalam fluida. Viskometer Brookfield memungkinkan untuk mengukur viskositas dengan menggunakan Teknik dalam viscometry. Untuk mengukur viskositas, bahan harus diam dalam wadah sementara itu poros bergerak sambil direndam dalam dalam fluida.')
        
    with st.expander("Percobaan 5"):
        st.title("Penetapan Kekentalan Metode Laju Alir (Engler)")
        st.write('Viskositas adalah sifat fluida untuk menghambat pengaliran jika pada fluida dikenakan suatu gaya. Cairan dengan nilai kekentalan yang tinggi akan sukar mengalir sedangkan cairan dengan nilai kekentalan rendah akan mudah mengalir. Sejumlah cairan akan dialirkan dalam waktu tertentu yang terukur tercatat. Kekentalan cairan dihitung melalui perbandigan kekentalannya dengan blanko atau air')
    
    with st.expander("Percobaan 6"):
        st.title("Penetapan Titik Leleh")
        st.write('Titik leleh adalah suatu rentang temperatur dimana zat padat berubah wujud menjadi zat cair pada tekanan 1 atm. Perbedaan titik leleh antar sampel dipengaruhi oleh beberapa hal, diantaranya adalah perbedaan kuatnya ikatan yang dibentuk antar unsur dalam sampel tersebut. Dengan mengetahui titik leleh suatu zat, maka kita dapat mengetahui kemurnian suatu zat')
        
    with st.expander("Percobaan 7"):
        st.title("Penetapan Koefisien Pemuaian Air/Alkohol")
        st.write('Benda/zat jika dipanaskan pada suhu tertentu dapat mengalami pemuaian, kecepatan muai suatu zat tergantung dari koefisien muainya. Pemuaian dari zat cair dapat diukur dengan mengukur perubahan volume berdasarkan perubahan suhunya. Pada pengukuran muai panjang cair ditambahkan faktor koreksi dari muai ruang bahan tersebut')
        
    with st.expander("Percobaan 8"):
        st.title("Penetapan Kuat Tekan")
        st.write('Kekerasan merupakan kemampuan benda padat untuk menahan perubahan bentuk di permukaan. Pada dasarnya, benda dengan kekerasan yang lebih rendah bisa digores oleh benda dengan kekerasan yang lebih tinggi atau benda yang lebih keras tidak bisa digores oleh benda yang lebih lunak. Digunakan salah satu metode yaitu metode tekan digunakan untuk mengukur kekerasan bahan yang bersifat homogen (dari luar ke dalam memiliki kekerasan yang relatif sama) dan kaku')
        
        
        
with tab3:
                    
                tab = stx.tab_bar(data=[
                    stx.TabBarItemData(id="Percobaan 1", description="", title="Hubungan Kerapatan dan Kepekatan Larutan"),
                    stx.TabBarItemData(id="Percobaan 2", description="", title="Penetapan Kerapatan Curah, Absolut, dan Relatif"),
                    stx.TabBarItemData(id="Percobaan 3", description="", title="Penentuan Kekentalan Metode Laju Alir Ostwald"),
                    stx.TabBarItemData(id="Percobaan 4", description="", title="Penentuan Kekentalan Metode Silinder Berputar Brookfield"),
                    stx.TabBarItemData(id="Percobaan 5", description="", title="Penentuan Kekentalan Metode Laju Alir Engler"),
                    stx.TabBarItemData(id="Percobaan 6", description="", title="Penetapan Titik Leleh"),
                    stx.TabBarItemData(id="Percobaan 7", description="", title="Penetapan Koefisien Muai Air dan Alkohol"),
                    stx.TabBarItemData(id="Percobaan 8", description="", title="Penetapan Kuat Tekan")
                ])

                if tab == "Percobaan 1":
                    tab_1 = stx.tab_bar(data=[
                    stx.TabBarItemData(id="Kerapatan Air", description="", title="Kerapatan Air"),
                    stx.TabBarItemData(id="Kerapatan Deret Larutan Standar Garam", description="", title="Kerapatan Deret Larutan Standar Garam"),
                    ])

                    if tab_1 == "Kerapatan Air":
                        Bobot_Sampel_Perc_1 = st.number_input('Masukkan Nilai Bobot Sampel Pertama', key='first_tab_Masukkan_Bobot_Sa1', format='%f')
                        Bobot_Kosong_Perc_1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_Bobot_Ka1', format='%f')
                        Bobot_Sampel_Perc_2 = st.number_input('Masukkan Nilai Bobot Sampel Ke dua', key='first_tab_Masukkan_Bobot_Sa2', format='%f')
                        Bobot_Kosong_Perc_2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_Bobot_Ka2', format='%f')
                        Volume_Air_Perc_1 =  st.number_input('Masukkan Nilai Volume Air', key='first_tab_Masukkan_VolumeAir', format='%f')

                        Tombol = st.button ('Hitung')
                        if Tombol: 
                            BoSam1 = (Bobot_Sampel_Perc_1 - Bobot_Kosong_Perc_1) / Volume_Air_Perc_1
                            st.success(f'Kerapatan Air Pertama adalah {BoSam1} g/mL')
                            BoSam2 = (Bobot_Sampel_Perc_2 - Bobot_Kosong_Perc_2) / Volume_Air_Perc_1
                            st.success(f'Kerapatan Air Ke dua adalah {BoSam2} g/mL')

                    elif tab_1 == "Kerapatan Deret Larutan Standar Garam":
                        BobotTotalSatuPersen = st.number_input('Masukkan Nilai Bobot Larutan 1 %', key='first_tab_Masukkan_BT1%', format='%f')
                        BobotKosongSatuPersen = st.number_input('Masukkan Nilai Bobot Kosong 1 %', key='first_tab_Masukkan_BK1%', format='%f')
                        BobotTotalLimaPersen = st.number_input('Masukkan Nilai Bobot Larutan 5 %', key='first_tab_Masukkan_BT5%', format='%f')
                        BobotKosongLimaPersen = st.number_input('Masukkan Nilai Bobot Kosong 5 %', key='first_tab_Masukkan_BK5%', format='%f')
                        BobotTotalSepuluhPersen = st.number_input('Masukkan Nilai Bobot Larutan 10 %', key='first_tab_Masukkan_BT10%', format='%f')
                        BobotKosongSepuluhPersen = st.number_input('Masukkan Nilai Bobot Kosong 10 %', key='first_tab_Masukkan_BK10%', format='%f')
                        BobotTotalLimaBelasPersen = st.number_input('Masukkan Nilai Bobot Larutan 15 %', key='first_tab_Masukkan_BT15%', format='%f')
                        BobotKosongLimaBelasPersen = st.number_input('Masukkan Nilai Bobot Kosong 15 %', key='first_tab_Masukkan_BK15%', format='%f')
                        Volume_Deret_Standar = st.number_input('Masukkan Volume', key='first_tab_Masukkan_Volume', format='%f')

                        Tombol = st.button ('Hitung')
                        if Tombol: 
                            Kerapatan_Deret_Standar_1 = (BobotTotalSatuPersen - BobotKosongSatuPersen) / Volume_Deret_Standar
                            st.success(f'Kerapatan Larutan Garam 1% adalah {Kerapatan_Deret_Standar_1} g/mL')
                            Kerapatan_Deret_Standar_2 = (BobotTotalLimaPersen - BobotKosongLimaPersen) / Volume_Deret_Standar
                            st.success(f'Kerapatan Larutan Garam 5% adalah {Kerapatan_Deret_Standar_2} g/mL')
                            Kerapatan_Deret_Standar_3 = (BobotTotalSepuluhPersen - BobotKosongSepuluhPersen) / Volume_Deret_Standar
                            st.success(f'Kerapatan Larutan Garam 10% adalah {Kerapatan_Deret_Standar_3} g/mL')
                            Kerapatan_Deret_Standar_4 = (BobotTotalLimaBelasPersen - BobotKosongLimaBelasPersen) / Volume_Deret_Standar
                            st.success(f'Kerapatan Larutan Garam 15% adalah {Kerapatan_Deret_Standar_4} g/mL')

                    else: 
                        hasil = "Pilihlah yang Ada"

                elif tab == "Percobaan 2":
                    #Bobot & Volume Sampel Curah
                    st.write('Masukkan Nilai untuk Kerapatan Curah')
                    BobotSampel1 = st.number_input('Masukkan Nilai Bobot Sampel Pertama', key='first_tab_Masukkan_BobotSampel1', format='%f')
                    BobotKosong1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BobotKosong1', format='%f')
                    VolumeSampel1 = st.number_input('Masukkan Nilai Volume Sampel Pertama', key='first_tab_Masukkan_VolumeSampel1', format='%f')
                    BobotSampel2 = st.number_input('Masukkan Nilai Bobot Sampel Ke dua', key='first_tab_Masukkan_BobotSampel2', format='%f')
                    BobotKosong2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_BobotKosong2', format='%f')
                    VolumeSampel2 = st.number_input('Masukkan Nilai Volume Sampel Ke dua', key='first_tab_Masukkan_VolumeSampel2', format='%f')
                    BobotSampel3 = st.number_input('Masukkan Nilai Bobot Sampel Ke tiga', key='first_tab_Masukkan_BobotSampel3', format='%f')
                    BobotKosong3 = st.number_input('Masukkan Nilai Bobot Kosong Ke tiga', key='first_tab_Masukkan_BobotKosong3', format='%f')
                    VolumeSampel3 = st.number_input('Masukkan Nilai Volume Sampel Ke tiga', key='first_tab_Masukkan_VolumeSampel3', format='%f')
                    BobotSampel4 = st.number_input('Masukkan Nilai Bobot Sampel Ke empat', key='first_tab_Masukkan_BobotSampel4', format='%f')
                    BobotKosong4 = st.number_input('Masukkan Nilai Bobot Kosong Ke empat', key='first_tab_Masukkan_BobotKosong4', format='%f')
                    VolumeSampel4 = st.number_input('Masukkan Nilai Volume Sampel Ke empat', key='first_tab_Masukkan_VolumeSampel4', format='%f')
                    BobotSampel5 = st.number_input('Masukkan Nilai Bobot Sampel Ke lima', key='first_tab_Masukkan_BobotSampel5', format='%f')
                    BobotKosong5 = st.number_input('Masukkan Nilai Bobot Kosong Ke lima', key='first_tab_Masukkan_BobotKosong5', format='%f')
                    VolumeSampel5 = st.number_input('Masukkan Nilai Volume Sampel Ke lima', key='first_tab_Masukkan_VolumeSampel5', format='%f')

                    #Bobot & Volume Sampel Absolut
                    st.write('Masukkan Nilai untuk Kerapatan Absolut')
                    BobotS1 = st.number_input('Masukkan Nilai Bobot Sampel Pertama', key='first_tab_Masukkan_BobotS1', format='%f')
                    BobotK1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BobotK1', format='%f')
                    VolumeS1 = st.number_input('Masukkan Nilai Volume Sampel Pertama', key='first_tab_Masukkan_VolumeS1', format='%f')
                    BobotS2 = st.number_input('Masukkan Nilai Bobot Sampel Ke dua', key='first_tab_Masukkan_BobotS2', format='%f')
                    BobotK2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_BobotK2', format='%f')
                    VolumeS2 = st.number_input('Masukkan Nilai Volume Sampel Ke dua', key='first_tab_Masukkan_VolumeS2', format='%f')
                    BobotS3 = st.number_input('Masukkan Nilai Bobot Sampel Ke tiga', key='first_tab_Masukkan_BobotS3', format='%f')
                    BobotK3 = st.number_input('Masukkan Nilai Bobot Kosong Ke tiga', key='first_tab_Masukkan_BobotK3', format='%f')
                    VolumeS3 = st.number_input('Masukkan Nilai Volume Sampel Ke tiga', key='first_tab_Masukkan_VolumeS3', format='%f')
                    BobotS4 = st.number_input('Masukkan Nilai Bobot Sampel Ke empat', key='first_tab_Masukkan_BobotS4', format='%f')
                    BobotK4 = st.number_input('Masukkan Nilai Bobot Kosong Ke empat', key='first_tab_Masukkan_BobotK4', format='%f')
                    VolumeS4 = st.number_input('Masukkan Nilai Volume Sampel Ke empat', key='first_tab_Masukkan_VolumeS4', format='%f')
                    BobotS5 = st.number_input('Masukkan Nilai Bobot Sampel Ke lima', key='first_tab_Masukkan_BobotS5', format='%f')
                    BobotK5 = st.number_input('Masukkan Nilai Bobot Kosong Ke lima', key='first_tab_Masukkan_BobotK5', format='%f')
                    VolumeS5 = st.number_input('Masukkan Nilai Volume Sampel Ke lima', key='first_tab_Masukkan_VolumeS5', format='%f')

                    #Kerapatan Absolut
                    Kerapatan_Air = st.number_input('Masukkan Nilai Kerapatan Air', key='first_tab_Masukkan_Kerapatan Air', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        #Kalkulator Curah
                        KC1 = (BobotSampel1 - BobotKosong1) / VolumeSampel1
                        st.success(f'Kerapatan Curah Pertama adalah {KC1} g/mL')
                        KC2 = (BobotSampel2 - BobotKosong2) / VolumeSampel2
                        st.success(f'Kerapatan Curah Ke dua adalah {KC2} g/mL')
                        KC3 = (BobotSampel3 - BobotKosong3) / VolumeSampel3
                        st.success(f'Kerapatan Curah Ke tiga adalah {KC3} g/mL')
                        KC4 = (BobotSampel4 - BobotKosong4) / VolumeSampel4
                        st.success(f'Kerapatan Curah Ke empat adalah {KC4} g/mL')
                        KC5 = (BobotSampel5 - BobotKosong5) / VolumeSampel5
                        st.success(f'Kerapatan Curah Ke lima adalah {KC5} g/mL')

                        #Kalkulator Absolut
                        KA1 = (BobotS1 - BobotK1) / VolumeS1
                        st.success(f'Kerapatan Absolut Pertama adalah {KA1} g/mL')
                        KA2 = (BobotS2 - BobotK2) / VolumeS2
                        st.success(f'Kerapatan Absolut Ke dua adalah {KA2} g/mL')
                        KA3 = (BobotS3 - BobotK3) / VolumeS3
                        st.success(f'Kerapatan Absolut Ke tiga adalah {KA3} g/mL')
                        KA4 = (BobotS4 - BobotK4) / VolumeS4
                        st.success(f'Kerapatan Absolut Ke empat adalah {KA4} g/mL')
                        KA5 = (BobotS5 - BobotK5) / VolumeS5
                        st.success(f'Kerapatan Absolut Ke lima adalah {KA5} g/mL')

                        #Kalkulator Relatif
                        KR1 = KA1 / Kerapatan_Air
                        st.success(f'Kerapatan Absolut Pertama adalah {KR1} g/mL')
                        KR2 = KA2 / Kerapatan_Air
                        st.success(f'Kerapatan Absolut Pertama adalah {KR2} g/mL')
                        KR3 = KA3 / Kerapatan_Air
                        st.success(f'Kerapatan Absolut Pertama adalah {KR3} g/mL')
                        KR4 = KA4 / Kerapatan_Air
                        st.success(f'Kerapatan Absolut Pertama adalah {KR4} g/mL')
                        KR5 = KA5 / Kerapatan_Air
                        st.success(f'Kerapatan Absolut Pertama adalah {KR5} g/mL')

                        Ratarata = (KC1+KC2+KC3+KC4+KC5)/5
                        st.success(f'Rata-Rata Kerapatan Curah adalah {Ratarata} g/mL')
                        RataratA = (KA1+KA2+KA3+KA4+KA5)/5
                        st.success(f'Rata-Rata Kerapatan Absolut adalah {RataratA} g/mL')
                        RataRata = (KR1+KR2+KR3+KR4+KR5)/5
                        st.success(f'Rata-Rata Kerapatan Relatif adalah {RataRata}')

                elif tab == "Percobaan 3":
                    #Massa Air Suling
                    massa_k_1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK1', format='%f')
                    massa_air_1 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Pertama', key='first_tab_Masukkan_BT1', format='%f')
                    massa_k_2 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK2', format='%f')
                    massa_air_2 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke dua', key='first_tab_Masukkan_BT2', format='%f')
                    massa_k_3 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK3', format='%f')
                    massa_air_3 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke tiga', key='first_tab_Masukkan_BT3', format='%f')
                    massa_k_4 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK4', format='%f')
                    massa_air_4 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke empat', key='first_tab_Masukkan_BT4', format='%f')
                    massa_k_5 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK5', format='%f')
                    massa_air_5 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke lima', key='first_tab_Masukkan_BT5', format='%f')
                    volume_air = st.number_input('Masukkan Volume Air Suling', key='first_tab_Masukkan_Volume_AirSampel', format='%f')

                    #Massa Sampel
                    massa_ko_1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BKo1', format='%f')
                    massa_sampel_1 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Sampel Pertama', key='first_tab_Masukkan_BTo1', format='%f')
                    massa_ko_2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_BKo2', format='%f')
                    massa_sampel_2 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Sampel Ke dua', key='first_tab_Masukkan_BTo2', format='%f')
                    massa_ko_3 = st.number_input('Masukkan Nilai Bobot Kosong Ke tiga', key='first_tab_Masukkan_BKo3', format='%f')
                    massa_sampel_3 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Sampel Ke tiga', key='first_tab_Masukkan_BTo3', format='%f')
                    massa_ko_4 = st.number_input('Masukkan Nilai Bobot Kosong Ke empat', key='first_tab_Masukkan_BKo4', format='%f')
                    massa_sampel_4 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Sampel Ke empat', key='first_tab_Masukkan_BTo4', format='%f')
                    massa_ko_5 = st.number_input('Masukkan Nilai Bobot Kosong Ke lima', key='first_tab_Masukkan_BKo5', format='%f')
                    massa_sampel_5 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Sampel Ke lima', key='first_tab_Masukkan_BTo5', format='%f')
                    volume_sampel_ostwald = st.number_input('Masukkan Volume Air Suling', key='first_tab_Masukkan_VS', format='%f')

                    #Kekentalan 
                    kekentalan_air_1 = st.number_input('Masukkan Nilai Kekentalan Air pada Suhu yang Tertera di Termometer (dilihat di Literatur)', key='first_tab_Masukkan_KAS_Pertama', format='%f')

                    #Waktu Turun
                    waktu_ostwald_A1 = st.number_input('Masukkan Lama Waktu Air Turun Pertama', key='first_tab_Masukkan_WTo_Pertama', format='%f')
                    waktu_ostwald_A2 = st.number_input('Masukkan Lama Waktu Air Turun Ke dua', key='first_tab_Masukkan_WTo_Ke dua', format='%f')
                    waktu_ostwald_A3 = st.number_input('Masukkan Lama Waktu Air Turun Ke tiga', key='first_tab_Masukkan_WTo_Ke tiga', format='%f')
                    waktu_ostwald_A4 = st.number_input('Masukkan Lama Waktu Air Turun Ke empat', key='first_tab_Masukkan_WTo_Ke empat', format='%f')
                    waktu_ostwald_A5 = st.number_input('Masukkan Lama Waktu Air Turun Ke lima ', key='first_tab_Masukkan_WTo_Ke lima', format='%f')

                    #Waktu Turun Sampel
                    waktu_ostwald_S1 = st.number_input('Masukkan Lama Waktu Sabun Turun Pertama', key='first_tab_Masukkan_WTs_Pertama', format='%f')
                    waktu_ostwald_S2 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke dua', key='first_tab_Masukkan_WTs_Ke dua', format='%f')
                    waktu_ostwald_S3 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke tiga', key='first_tab_Masukkan_WTs_Ke tiga', format='%f')
                    waktu_ostwald_S4 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke empat', key='first_tab_Masukkan_WTs_Ke empat', format='%f')
                    waktu_ostwald_S5 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke lima ', key='first_tab_Masukkan_WTs_Ke lima', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        #Kerapatan Aquadest
                        Kerapatan_Aquadest_Ostwald1 = (massa_air_1 - massa_k_1) / volume_air
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest_Ostwald1} g/mL')
                        Kerapatan_Aquadest_Ostwald2 = (massa_air_2 - massa_k_2) / volume_air
                        st.success(f'Kerapatan Aquadest Ke dua adalah {Kerapatan_Aquadest_Ostwald2} g/mL')
                        Kerapatan_Aquadest_Ostwald3 = (massa_air_3 - massa_k_3) / volume_air
                        st.success(f'Kerapatan Aquadest Ke tiga adalah {Kerapatan_Aquadest_Ostwald3} g/mL')
                        Kerapatan_Aquadest_Ostwald4 = (massa_air_4 - massa_k_4) / volume_air
                        st.success(f'Kerapatan Aquadest Ke empat adalah {Kerapatan_Aquadest_Ostwald4} g/mL')
                        Kerapatan_Aquadest_Ostwald5 = (massa_air_5 - massa_k_5) / volume_air
                        st.success(f'Kerapatan Aquadest Ke lima adalah {Kerapatan_Aquadest_Ostwald5} g/mL')

                        #Kerapatan Sampel
                        Kerapatan_Sampel_Ostwald1 = (massa_sampel_1 - massa_ko_1) / volume_sampel_ostwald
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Sampel_Ostwald1} g/mL')
                        Kerapatan_Sampel_Ostwald2 = (massa_sampel_2 - massa_ko_2) / volume_sampel_ostwald
                        st.success(f'Kerapatan Aquadest Ke dua adalah {Kerapatan_Sampel_Ostwald2} g/mL')
                        Kerapatan_Sampel_Ostwald3 = (massa_sampel_3 - massa_ko_3) / volume_sampel_ostwald
                        st.success(f'Kerapatan Aquadest Ke tiga adalah {Kerapatan_Sampel_Ostwald3} g/mL')
                        Kerapatan_Sampel_Ostwald4 = (massa_sampel_4 - massa_ko_4) / volume_sampel_ostwald
                        st.success(f'Kerapatan Aquadest Ke empat adalah {Kerapatan_Sampel_Ostwald4} g/mL')
                        Kerapatan_Sampel_Ostwald5 = (massa_sampel_5 - massa_ko_5) / volume_sampel_ostwald
                        st.success(f'Kerapatan Aquadest Ke lima adalah {Kerapatan_Sampel_Ostwald5} g/mL')

                        #Viskositas Sampel
                        Viskositas_Sampel_Ostwald1 = (waktu_ostwald_S1 * Kerapatan_Sampel_Ostwald1 * kekentalan_air_1) / (waktu_ostwald_A1*Kerapatan_Aquadest_Ostwald1)
                        st.success(f'Kekentalan Sampel Pertama adalah {Viskositas_Sampel_Ostwald1} m²/s')
                        Viskositas_Sampel_Ostwald2 = (waktu_ostwald_S2 * Kerapatan_Sampel_Ostwald2 * kekentalan_air_1) / (waktu_ostwald_A2*Kerapatan_Aquadest_Ostwald2)
                        st.success(f'Kekentalan Sampel Pertama adalah {Viskositas_Sampel_Ostwald1} m²/s')
                        Viskositas_Sampel_Ostwald3 = (waktu_ostwald_S3 * Kerapatan_Sampel_Ostwald3 * kekentalan_air_1) / (waktu_ostwald_A3*Kerapatan_Aquadest_Ostwald3)
                        st.success(f'Kekentalan Sampel Ke tiga adalah {Viskositas_Sampel_Ostwald3} m²/s')
                        Viskositas_Sampel_Ostwald4 = (waktu_ostwald_S4 * Kerapatan_Sampel_Ostwald4 * kekentalan_air_1) / (waktu_ostwald_A4*Kerapatan_Aquadest_Ostwald4)
                        st.success(f'Kekentalan Sampel Ke empat adalah {Viskositas_Sampel_Ostwald4} m²/s')
                        Viskositas_Sampel_Ostwald5 = (waktu_ostwald_S5 * Kerapatan_Sampel_Ostwald5 * kekentalan_air_1) / (waktu_ostwald_A5*Kerapatan_Aquadest_Ostwald5)
                        st.success(f'Kekentalan Sampel Ke lima adalah {Viskositas_Sampel_Ostwald5} m²/s')


                elif tab == "Percobaan 4":
                    Viskositas_1 = st.number_input('Masukkan Nilai Perulangan Pertama', key='first_tab_Masukkan_Perulangan Pertama', format='%f')
                    Viskositas_2 = st.number_input('Masukkan Nilai Perulangan Ke dua', key='first_tab_Masukkan_Perulangan Ke dua', format='%f')
                    Viskositas_3 = st.number_input('Masukkan Nilai Perulangan Ke tiga', key='first_tab_Masukkan_Perulangan Ke tiga', format='%f')
                    Viskositas_4 = st.number_input('Masukkan Nilai Perulangan Ke empat', key='first_tab_Masukkan_Perulangan Ke empat', format='%f')
                    Viskositas_5 = st.number_input('Masukkan Nilai Perulangan Ke lima', key='first_tab_Masukkan_Perulangan Ke lima', format='%f')
                    Jumlah_Perulangan = st.number_input('Masukkan Jumlah Pengulangan', key='first_tab_Masukkan_Jumlah Pengulangan', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        Rerata = (Viskositas_1+Viskositas_2+Viskositas_3+Viskositas_4+Viskositas_5)/Jumlah_Perulangan
                        st.success(f'Rata-Ratanya adalah {Rerata}')

                elif tab == "Percobaan 5":
                    #Massa Air Aquadest
                    massa_kosong_1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BK_Pertama', format='%f')
                    massa_air_suling_1 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Pertama', key='first_tab_Masukkan_BT_Pertama', format='%f')
                    massa_kosong_2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_BK_Ke dua', format='%f')
                    massa_air_suling_2 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke dua', key='first_tab_Masukkan_BT_Ke dua', format='%f')
                    massa_kosong_3 = st.number_input('Masukkan Nilai Bobot Kosong Ke tiga', key='first_tab_Masukkan_BK_Ke tiga', format='%f')
                    massa_air_suling_3 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke tiga', key='first_tab_Masukkan_BT_Ke tiga', format='%f')
                    massa_kosong_4 = st.number_input('Masukkan Nilai Bobot Kosong Ke empat', key='first_tab_Masukkan_BK_Ke empat', format='%f')
                    massa_air_suling_4 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke empat', key='first_tab_Masukkan_BT_Ke empat', format='%f')
                    massa_kosong_5 = st.number_input('Masukkan Nilai Bobot Kosong Ke lima', key='first_tab_Masukkan_BK_Ke lima', format='%f')
                    massa_air_suling_5 = st.number_input('Masukkan Nilai Bobot Total Penimbangan Air Ke lima', key='first_tab_Masukkan_BT_Ke lima', format='%f')
                    volume_air_suling = st.number_input('Masukkan Volume Air Suling', key='first_tab_Masukkan_Volume_Air_Suling', format='%f')

                    #Massa Air Sabun
                    massa_1 = st.number_input('Masukkan Nilai Bobot Kosong Pertama', key='first_tab_Masukkan_BKS_Pertama', format='%f')
                    massa_air_sabun_1 = st.number_input('Masukkan Nilai Bobot Sampel Total Pertama', key='first_tab_Masukkan_BTS_Pertama', format='%f')
                    massa_2 = st.number_input('Masukkan Nilai Bobot Kosong Ke dua', key='first_tab_Masukkan_BKS_Ke dua', format='%f')
                    massa_air_sabun_2 = st.number_input('Masukkan Nilai Bobot Sampel Total Ke dua', key='first_tab_Masukkan_BTS_Ke dua', format='%f')
                    massa_3 = st.number_input('Masukkan Nilai Bobot Kosong Ke tiga', key='first_tab_Masukkan_BKS_Ke tiga', format='%f')
                    massa_air_sabun_3 = st.number_input('Masukkan Nilai Bobot Sampel Total Ke tiga', key='first_tab_Masukkan_BTS_Ke tiga', format='%f')
                    massa_4 = st.number_input('Masukkan Nilai Bobot Kosong Ke empat', key='first_tab_Masukkan_BKS_Ke empat', format='%f')
                    massa_air_sabun_4 = st.number_input('Masukkan Nilai Bobot Sampel Total Ke empat', key='first_tab_Masukkan_BTS_Ke empat', format='%f')
                    massa_5 = st.number_input('Masukkan Nilai Bobot Kosong Ke lima', key='first_tab_Masukkan_BKS_Ke lima', format='%f')
                    massa_air_sabun_5 = st.number_input('Masukkan Nilai Bobot Sampel Total Ke lima', key='first_tab_Masukkan_BTS_Ke lima', format='%f')
                    volume_air_sabun = st.number_input('Masukkan Volume Sampel ', key='first_tab_Masukkan_Volume_Sampel', format='%f')

                    #Waktu Turun Air
                    waktu_engler_A1 = st.number_input('Masukkan Lama Waktu Air Turun Pertama', key='first_tab_Masukkan_WTA_Pertama', format='%f')
                    waktu_engler_A2 = st.number_input('Masukkan Lama Waktu Air Turun Ke dua', key='first_tab_Masukkan_WTA_Ke dua', format='%f')
                    waktu_engler_A3 = st.number_input('Masukkan Lama Waktu Air Turun Ke tiga', key='first_tab_Masukkan_WTA_Ke tiga', format='%f')
                    waktu_engler_A4 = st.number_input('Masukkan Lama Waktu Air Turun Ke empat', key='first_tab_Masukkan_WTA_Ke empat', format='%f')
                    waktu_engler_A5 = st.number_input('Masukkan Lama Waktu Air Turun Ke lima', key='first_tab_Masukkan_WTA_Ke lima', format='%f')

                    #Waktu Turun Sabun
                    waktu_engler_S1 = st.number_input('Masukkan Lama Waktu Sabun Turun Pertama', key='first_tab_Masukkan_WTS_Pertama', format='%f')
                    waktu_engler_S2 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke dua', key='first_tab_Masukkan_WTS_Ke dua', format='%f')
                    waktu_engler_S3 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke tiga', key='first_tab_Masukkan_WTS_Ke tiga', format='%f')
                    waktu_engler_S4 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke empat', key='first_tab_Masukkan_WTS_Ke empat', format='%f')
                    waktu_engler_S5 = st.number_input('Masukkan Lama Waktu Sabun Turun Ke lima', key='first_tab_Masukkan_WTS_Ke lima', format='%f')

                    #Kekentalan 
                    kekentalan_air_aquadest = st.number_input('Masukkan Nilai Kekentalan Air pada Suhu yang Tertera di Termometer (dilihat di Literatur)', key='first_tab_Masukkan_KAA_Pertama', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        #Kerapatan Aquadest
                        Kerapatan_Aquadest1 = (massa_air_suling_1 - massa_kosong_1) / volume_air_suling
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest1} g/mL')
                        Kerapatan_Aquadest2 = (massa_air_suling_2 - massa_kosong_2) / volume_air_suling
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest2} g/mL')
                        Kerapatan_Aquadest3 = (massa_air_suling_3 - massa_kosong_3) / volume_air_suling
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest3} g/mL')
                        Kerapatan_Aquadest4 = (massa_air_suling_4 - massa_kosong_4) / volume_air_suling
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest4} g/mL')
                        Kerapatan_Aquadest5 = (massa_air_suling_5 - massa_kosong_5) / volume_air_suling
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Aquadest5} g/mL')

                        #Kerapatan Sampel
                        Kerapatan_Sampel1 = (massa_air_sabun_1 - massa_1) / volume_air_sabun
                        st.success(f'Kerapatan Aquadest Pertama adalah {Kerapatan_Sampel1} g/mL')
                        Kerapatan_Sampel2 = (massa_air_sabun_2 - massa_2) / volume_air_sabun
                        st.success(f'Kerapatan Aquadest Ke dua adalah {Kerapatan_Sampel2} g/mL')
                        Kerapatan_Sampel3 = (massa_air_sabun_3 - massa_3) / volume_air_sabun
                        st.success(f'Kerapatan Aquadest Ke tiga adalah {Kerapatan_Sampel3} g/mL')         
                        Kerapatan_Sampel4 = (massa_air_sabun_4 - massa_4) / volume_air_sabun
                        st.success(f'Kerapatan Aquadest Ke empat adalah {Kerapatan_Sampel4} g/mL')
                        Kerapatan_Sampel5 = (massa_air_sabun_5 - massa_5) / volume_air_sabun
                        st.success(f'Kerapatan Aquadest Ke lima adalah {Kerapatan_Sampel5} g/mL')

                        #Viskositas Sampel
                        Viskositas_Sampel1 = (waktu_engler_S1 * Kerapatan_Sampel1 * kekentalan_air_aquadest) / (waktu_engler_A1*Kerapatan_Aquadest1)
                        st.success(f'Kekentalan Sampel Pertama adalah {Viskositas_Sampel1} m²/s')
                        Viskositas_Sampel2 = (waktu_engler_S2 * Kerapatan_Sampel2 * kekentalan_air_aquadest) / (waktu_engler_A2*Kerapatan_Aquadest2)
                        st.success(f'Kekentalan Sampel Ke dua adalah {Viskositas_Sampel2} m²/s')
                        Viskositas_Sampel3 = (waktu_engler_S3 * Kerapatan_Sampel3 * kekentalan_air_aquadest) / (waktu_engler_A3*Kerapatan_Aquadest3)
                        st.success(f'Kekentalan Sampel Ke tiga adalah {Viskositas_Sampel3} m²/s')
                        Viskositas_Sampel4 = (waktu_engler_S4 * Kerapatan_Sampel4 * kekentalan_air_aquadest) / (waktu_engler_A4*Kerapatan_Aquadest4)
                        st.success(f'Kekentalan Sampel Ke empat adalah {Viskositas_Sampel4} m²/s')
                        Viskositas_Sampel5 = (waktu_engler_S5 * Kerapatan_Sampel5 * kekentalan_air_aquadest) / (waktu_engler_A5*Kerapatan_Aquadest5)
                        st.success(f'Kekentalan Sampel Ke lima adalah {Viskositas_Sampel5} m²/s')

                elif tab == "Percobaan 6":
                    FMelt = st.number_input('Masukkan Nilai Finish Melt', key='first_tab_Masukkan_Finish Melt', format='%f')
                    SMelt = st.number_input('Masukkan Nilai Start Melt', key='first_tab_Masukkan_Start Melt', format='%f')
                    Tombol = st.button ('Hitung')
                    if Tombol :
                        Rentang_Leleh = FMelt-SMelt
                        st.success(f'Rentang Melelehnya ialah {Rentang_Leleh} °C')

                elif tab == "Percobaan 7":
                    Pertambahan_Vol = st.number_input('Masukkan Nilai Pertambahan Volume', key='first_tab_Masukkan_Pertambahan Volume', format='%f')
                    Pertambahan_Suhu = st.number_input('Masukkan Nilai Kenaikan Suhu', key='first_tab_Masukkan_Kenaikan Suhu', format='%f')
                    Vol_Awal = st.number_input('Masukkan Volume Awal', key='first_tab_Masukkan_Volume Awal', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        Rata_Rata = Pertambahan_Vol / (Pertambahan_Suhu*Vol_Awal)
                        st.success(f'Hasil Pemuaiannya adalah {Rata_Rata}/℃')

                elif tab == "Percobaan 8":
                    st.subheader('''Masukkan Panjang dan Lebar dalam satuan cm''')
                    Panjang1 = st.number_input('Masukkan Panjang Ulangan 1', key='first_tab_Masukkan_Panjang 1', format='%f')
                    Lebar1 = st.number_input('Masukkan Lebar Ulangan 1', key='first_tab_Masukkan_Lebar 1', format='%f')
                    Panjang2 = st.number_input('Masukkan Panjang Ulangan 2', key='first_tab_Masukkan_Panjang 2', format='%f')
                    Lebar2 = st.number_input('Masukkan Lebar Ulangan 2', key='first_tab_Masukkan_Lebar 2', format='%f')
                    Panjang3 = st.number_input('Masukkan Panjang Ulangan 3', key='first_tab_Masukkan_Panjang 3', format='%f')
                    Lebar3 = st.number_input('Masukkan Lebar Ulangan 3', key='first_tab_Masukkan_Lebar 3', format='%f')
                    Panjang4 = st.number_input('Masukkan Panjang Ulangan 4', key='first_tab_Masukkan_Panjang 4', format='%f')
                    Lebar4 = st.number_input('Masukkan Lebar Ulangan 4', key='first_tab_Masukkan_Lebar 4', format='%f')
                    Panjang5 = st.number_input('Masukkan Panjang Ulangan 5', key='first_tab_Masukkan_Panjang 5', format='%f')
                    Lebar5 = st.number_input('Masukkan Lebar Ulangan 5', key='first_tab_Masukkan_Lebar 5', format='%f')

                    Berat_Tekan1 = st.number_input('Masukkan Nilai Berat Tekan Pertama (kg)', key='first_tab_Masukkan_Berat Tekan1', format='%f')
                    Berat_Tekan2 = st.number_input('Masukkan Nilai Berat Tekan Ke dua (kg)', key='first_tab_Masukkan_Berat Tekan2', format='%f')
                    Berat_Tekan3 = st.number_input('Masukkan Nilai Berat Tekan Ke tiga (kg)', key='first_tab_Masukkan_Berat Tekan3', format='%f')
                    Berat_Tekan4 = st.number_input('Masukkan Nilai Berat Tekan Ke empat (kg)', key='first_tab_Masukkan_Berat Tekan4', format='%f')
                    Berat_Tekan5 = st.number_input('Masukkan Nilai Berat Tekan Ke lima (kg)', key='first_tab_Masukkan_Berat Tekan5', format='%f')
                    Gaya_Gravitasi = st.number_input('Masukkan Tetapan Gaya Gravitasi (m/s²)', key='first_tab_Masukkan_Gaya Gaya Gravitasi', format='%f')

                    Tombol = st.button ('Hitung')
                    if Tombol :
                        Luas1 = Panjang1 / Lebar1
                        st.success(f'Luas Pertama adalah {Luas1} m²')
                        Luas2 = Panjang2 / Lebar2
                        st.success(f'Luas Ke dua adalah {Luas2} m²')
                        Luas3 = Panjang3 / Lebar3
                        st.success(f'Luas Ke tiga adalah {Luas3} m²')
                        Luas4 = Panjang4 / Lebar4
                        st.success(f'Luas Ke empat adalah {Luas4} m²')
                        Luas5 = Panjang5 / Lebar5
                        st.success(f'Luas Ke lima adalah {Luas4} m²')

                        Gaya_Tekan1 = Berat_Tekan1 * Gaya_Gravitasi
                        st.success(f'Gaya Tekan Pertama adalah {Gaya_Tekan1} N')
                        Gaya_Tekan2 = Berat_Tekan2 * Gaya_Gravitasi
                        st.success(f'Gaya Tekan Ke dua adalah {Gaya_Tekan2} N')
                        Gaya_Tekan3 = Berat_Tekan3 * Gaya_Gravitasi
                        st.success(f'Gaya Tekan Ke tiga adalah {Gaya_Tekan3} N')
                        Gaya_Tekan4 = Berat_Tekan4 * Gaya_Gravitasi
                        st.success(f'Gaya Tekan Ke empat adalah {Gaya_Tekan4} N')
                        Gaya_Tekan5 = Berat_Tekan5 * Gaya_Gravitasi
                        st.success(f'Gaya Tekan Ke lima adalah {Gaya_Tekan5} N')

                        Kuat_Tekan1 = Gaya_Tekan1 / Luas1
                        st.success(f'Gaya Tekan Pertama adalah {Kuat_Tekan1} N/m²')
                        Kuat_Tekan2 = Gaya_Tekan2 / Luas2
                        st.success(f'Gaya Tekan Ke dua adalah {Kuat_Tekan2} N/m²')
                        Kuat_Tekan3 = Gaya_Tekan3 / Luas3
                        st.success(f'Gaya Tekan Ke tiga adalah {Kuat_Tekan3} N/m²')
                        Kuat_Tekan4 = Gaya_Tekan4 / Luas4
                        st.success(f'Gaya Tekan Ke empat adalah {Kuat_Tekan4} N/m²')
                        Kuat_Tekan5 = Gaya_Tekan5 / Luas5
                        st.success(f'Gaya Tekan Ke lima adalah {Kuat_Tekan5} N/m²')

                        RErata = (Gaya_Tekan1+Gaya_Tekan2+Gaya_Tekan3+Gaya_Tekan4+Gaya_Tekan5) / 5
                        st.success(f'Rata-Rata Gaya Tekan adalah {RErata} N')

                        ReRata = (Kuat_Tekan1+Kuat_Tekan2+Kuat_Tekan3+Kuat_Tekan4+Kuat_Tekan5) / 5
                        st.success(f'Rata-Rata Kuat Tekan adalah {ReRata} N/m²')

                else:
                    result="Pilihlah Opsi yang ada"



with tab4:
    st.write('instagram.com/euthernally')
    st.write('instagram.com/cndyshl')
    st.write('instagram.com/goodwillchristian')
    st.write('instagram.com/hibrohims')