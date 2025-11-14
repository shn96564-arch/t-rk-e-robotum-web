import streamlit as st

# Uygulamanın Başlığı ve Açıklaması
st.title("🤖 Türkçe Robotum - Yusuf Efe Şahin Yapay Zeka Dersi")
st.write("Bu Streamlit uygulaması, 7. Sınıf Türkçe konuları üzerine uzmanlaşmış bir robottur.")

# Kullanıcıdan Girdi Alma
user_input = st.text_area("Lütfen robotunuza bir soru sorun (Örnek: 'Sözcükte Anlam nedir?' veya 'Fiiller konusunu anlat'):", height=150)

# Cevap Üretme Butonu
if st.button("Cevap Üret"):
    if user_input:
        
        # Kullanıcı girdisini küçük harfe çeviriyoruz
        girdi = user_input.lower()
        response = ""
        
        # --- 7. SINIF TÜRKÇE KONULARI VE UZUN ANLATIMLARI ---

        if "sözcükte anlam" in girdi or "sözcük" in girdi:
            response = """
            ### 📖 Sözcükte Anlam
            Sözcükte anlam, kelimelerin tek başına taşıdığı veya cümle içinde kazandığı anlamlardır. Üç temel başlıkta incelenir:
            
            1.  **Gerçek (Temel) Anlam:** Bir kelimenin söylendiğinde akla gelen ilk anlamıdır. Sözlükteki ilk karşılığıdır. 
                *Örnek:* "Ayşe, yemeğin **sıcak** olduğunu söyledi." (Temel anlam)
            2.  **Mecaz Anlam:** Bir kelimenin gerçek anlamından tamamen uzaklaşarak kazandığı yeni anlamdır. 
                *Örnek:* "Arkadaşının söyledikleri ona **ağır** geldi." (Mecaz anlam)
            3.  **Terim Anlam:** Bir bilim, sanat, spor dalı veya meslekle ilgili özel kavramları karşılayan kelimelerdir. 
                *Örnek:* Müzikte "**nota**," matematikte "**kök**," futbolda "**taç**."
            """
        
        elif "cümlede anlam" in girdi or "cümle" in girdi:
            response = """
            ### 💬 Cümlede Anlam
            Cümlede anlam, iki veya daha fazla sözcüğün bir araya gelerek bir duygu, düşünce, haber veya isteği tam olarak ifade etmesidir. 
            Başlıca konuları şunlardır:
            
            1.  **Neden-Sonuç (Sebep-Sonuç) Cümleleri:** Bir eylemin hangi sebeple yapıldığını belirtir. (Çünkü, -den dolayı)
                *Örnek:* "Yağmur yağdığı **için** maçı ertelediler."
            2.  **Amaç-Sonuç Cümleleri:** Bir eylemin hangi amaca yönelik yapıldığını belirtir. (Amacıyla, diye, için)
                *Örnek:* "Sınavı kazanmak **için** çok çalıştı."
            3.  **Karşılaştırma Cümleleri:** İki varlık, kavram veya durumun benzerliklerini ya da farklılıklarını ortaya koyar. (Daha, kadar, en)
                *Örnek:* "Ali, Mehmet'ten **daha** hızlı koşar."
            """

        elif "parçada anlam" in girdi or "parça" in girdi or "ana fikir" in girdi:
            response = """
            ### 📝 Parçada Anlam
            Parçada anlam, bir metnin bütününü kavrama, metnin ana düşüncesini, yardımcı düşüncelerini, başlığını, konusunu ve anahtar sözcüklerini bulma becerisidir.
            
            * **Ana Düşünce (Ana Fikir):** Yazarın okuyucuya asıl vermek istediği mesajdır. Parçanın yazılma amacıdır.
            * **Konu:** Parçada üzerinde durulan, bahsedilen genel kavramdır. "Bu metin ne anlatıyor?" sorusunun cevabıdır.
            * **Başlık:** Konuyla ve ana düşünceyle en ilgili olan, metni özetleyen kelime veya kelime grubudur.
            """

        elif "tablo" in girdi or "grafik" in girdi or "görsel yorumlama" in girdi:
            response = """
            ### 📊 Tablo, Grafik ve Görsel Yorumlama
            Bu beceri, sayısal verileri içeren tabloları, çubuk/daire grafikleri ve diğer görselleri doğru okuma ve bu verilerden mantıklı çıkarımlar yapmayı içerir.
            
            * **Tablo:** Verilerin düzenli bir biçimde satır ve sütunlarda gösterilmesidir.
            * **Grafik:** Verilerin görsel olarak karşılaştırılmasını sağlayan şekillerdir (en çok artan, en azalan gibi).
            * **Yorumlama:** Verilere bakarak "kesinlikle söylenebilir" veya "ulaşılamaz" gibi yargılara ulaşma sürecidir.
            """
        
        elif "metin türleri" in girdi or "metin türü" in girdi:
            response = """
            ### 🎭 Metin Türleri
            Metinler; anlatım biçimlerine, yazılış amaçlarına ve konularına göre farklı türlere ayrılır. Başlıca türler:
            
            1.  **Olay Yazıları (Anlatmaya Bağlı):** Roman, Hikaye (Öykü), Masal, Fabl.
            2.  **Düşünce Yazıları (Öğretici):** Makale, Deneme, Fıkra, Söyleşi (Mülakat), Biyografi, Otobiyografi.
            3.  **Bildirmeye Bağlı Metinler:** Tiyatro, Gezi Yazısı.
            """
            
        elif "söz sanatları" in girdi or "söz sanatı" in girdi:
            response = """
            ### ✨ Söz Sanatları (Edebi Sanatlar)
            Anlatımı daha etkili, güzel ve çarpıcı hale getirmek için sözcüklere yeni anlamlar yükleme sanatıdır. 7. Sınıf konuları:
            
            1.  **Benzetme (Teşbih):** Zayıf olanı güçlü olana benzetme (Aslan gibi güçlü adam).
            2.  **Kişileştirme (Teşhis):** İnsan dışındaki varlıklara insana ait özellikler verme (Rüzgar usulca fısıldadı).
            3.  **Konuşturma (İntak):** Kişileştirilen varlıkları konuşturma.
            4.  **Abartma (Mübalağa):** Bir şeyi olduğundan çok daha büyük veya küçük gösterme (Bir ah çeksem dağı taşı eritir).
            """

        elif "fiiller" in girdi or "fiil" in girdi:
            response = """
            ### 🏃 Fiiller (Eylemler)
            Varlıkların yaptıkları işi, hareketi, oluşu veya durumu anlatan kelimelerdir. Fiiller, zaman ve kişi ekleriyle çekimlenir.
            
            * **Anlamlarına Göre Fiiller:**
                1.  **İş (Kılış) Fiilleri:** Nesne alabilen fiillerdir. (Neyi? Kimi? sorularına cevap verir.) *Örnek:* Okumak, kırmak.
                2.  **Durum Fiilleri:** Nesne alamayan, öznenin içinde bulunduğu durumu anlatan fiillerdir. *Örnek:* Uyudu, oturdu.
                3.  **Oluş Fiilleri:** Öznenin iradesi dışındaki değişimleri anlatan fiillerdir (Zamanla kendiliğinden olan). *Örnek:* Büyümek, paslanmak.
            """

        elif "ek fiil" in girdi or "ekfiil" in girdi:
            response = """
            ### 🔄 Ek Fiil (-idi, -imiş, -ise, -dir)
            Ek fiilin iki temel görevi vardır:
            
            1.  **İsim Soylu Sözcüklere Gelerek Onları Yüklem Yapmak:** *Örnek:* "Hava bugün **güneşliydi**." (Güneşli ismini yüklem yaptı.)
            2.  **Basit Zamanlı Fiillere Gelerek Onları Bileşik Zamanlı Yapmak:**
                *Örnek:* "Geliyor **imiş**." (Şimdiki zamanın rivayeti)
            
            Ek fiilin olumsuzu "değil" kelimesiyle yapılır.
            """
            
        elif "zarflar" in girdi or "zarf" in girdi:
            response = """
            ### 🌬️ Zarflar (Belirteçler)
            Fiilleri, fiilimsileri, sıfatları ve bazen de kendi türünden kelimeleri (zarfları) anlam yönünden etkileyen kelimelerdir. 5 temel türü vardır:
            
            1.  **Durum (Hal) Zarfları:** Eylemin nasıl yapıldığını bildirir. (Nasıl?) *Örnek:* **Güzel** konuştu.
            2.  **Zaman Zarfları:** Eylemin ne zaman yapıldığını bildirir. (Ne zaman?) *Örnek:* **Yarın** gelecek.
            3.  **Yer-Yön Zarfları:** Eylemin yönünü belirtir. (-e, -de eki almaz.) (Nereye?) *Örnek:* **Dışarı** çıktı.
            4.  **Miktar (Azlık-Çokluk) Zarfları:** Eylemin ne kadar yapıldığını belirtir. (Ne kadar?) *Örnek:* **Çok** yorgun.
            5.  **Soru Zarfları:** Eylemi soru yoluyla belirtir. *Örnek:* **Neden** gülüyor?
            """
            
        elif "anlatım bozuklukları" in girdi or "anlatım" in girdi:
            response = """
            ### 🤯 Anlatım Bozuklukları
            Cümlelerin anlam ve yapı bakımından taşıması gereken kurallara uymamasıdır. İki ana başlıkta incelenir:
            
            1.  **Anlamsal Bozukluklar:** Gereksiz sözcük kullanımı, anlamca çelişen sözcüklerin bir arada kullanılması, sözcüğün yanlış anlamda kullanılması gibi hatalardır.
            2.  **Yapısal Bozukluklar:** Özne-yüklem uyumsuzluğu, tamlama yanlışları, ek yanlışları, çatı uyumsuzluğu gibi dil bilgisel kurallara aykırılıklardır.
            """

        elif "yazım kuralları" in girdi or "yazım" in girdi:
            response = """
            ### ✍️ Yazım Kuralları
            Türkçede kelimelerin doğru yazılması için belirlenmiş kurallardır. Başlıca kurallar:
            
            * **Büyük Harflerin Kullanımı:** Cümle başları, özel isimler, unvanlar, belli bir tarihi belirten ay ve gün adları büyük harfle başlar.
            * **Kısaltmalar:** Kurum adları büyük harfle yapılır (T.B.M.M.).
            * **De, ki, mi'nin Yazımı:** Bağlaç olan 'de/ki' ayrı, ek olanlar bitişik yazılır. 'Mi' soru eki her zaman ayrı yazılır.
            """
            
        elif "noktalama işaretleri" in girdi or "noktalama" in girdi:
            response = """
            ### 📌 Noktalama İşaretleri
            Yazıda okumayı kolaylaştırmak, anlam karışıklığını gidermek ve vurguyu belirtmek için kullanılan işaretlerdir. Temel görevleri:
            
            * **Nokta (.):** Cümlenin bittiğini, bazı kısaltmaları ve sıra sayılarını belirtir.
            * **Virgül (,):** Eş görevli kelimeleri ayırmak, sıralı cümleleri ayırmak ve uzun cümlelerde özneden sonra kullanılır.
            * **Noktalı Virgül (;):** Cümle içinde virgüllerle ayrılmış tür veya takımları ayırmak için kullanılır.
            * **İki Nokta (:):** Açıklama yapılacak cümlenin sonuna konur.
            * **Üç Nokta (...):** Tamamlanmamış cümlelerin sonuna veya alıntılardaki eksik bölümlere konur.
            """
            
        else:
            response = f"""
            **Soru Analizi:** Sorduğunuz konu ('{user_input}'), mevcut 7. Sınıf Türkçe konuları listemde (Sözcükte Anlam, Fiiller, Zarflar, vb.) bulunmamaktadır.
            Lütfen listedeki konularla ilgili bir soru sorun.
            """
            
        st.success("Robot Cevabı:")
        st.markdown(response)
    else:
        st.warning("Lütfen robotunuza bir soru yazın.")

# Alt Bilgi (Geliştirici Adı Güncellendi)
st.markdown("---")
st.caption("Geliştiren: Yusuf Efe Şahin / Son Proje")
