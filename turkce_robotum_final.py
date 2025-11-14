import streamlit as st

# Uygulamanın Başlığı ve Açıklaması
st.title("🤖 Türkçe Robotum - Final Projesi")
st.write("Bu Streamlit uygulaması, bir yapay zeka robotunun arayüzüdür.")

# Kullanıcıdan Girdi Alma
user_input = st.text_area("Lütfen robotunuza bir soru sorun:", height=150)

# Cevap Üretme Butonu
if st.button("Cevap Üret"):
    if user_input:
        
        # --- UZUN KONU ANLATIMLARI İÇİN YENİ CEVAPLAR ---
        if "hava" in user_input.lower():
            response = """
            **Hava Durumu Bilgisi:** Hava durumu, belirli bir alanda ve belirli bir zamanda atmosferin mevcut durumunu ifade eder. 
            Bu durum sıcaklık, nem, rüzgar hızı ve yönü, bulutluluk ve yağış gibi faktörlerle belirlenir. Meteoroloji bilimi, 
            bu faktörleri inceleyerek tahminler yapar. Günümüzde hava durumu tahmini, genellikle uydu görüntüleri, radar sistemleri 
            ve yüksek performanslı bilgisayar modelleri kullanılarak gerçekleştirilir. Bu tahminler, günlük planlarımızdan, tarım 
            ve havacılık gibi büyük sektörlerin kararlarına kadar geniş bir yelpazeyi etkiler.
            """
        elif "adın" in user_input.lower():
            response = """
            Benim adım yok. Ben Google tarafından eğitilmiş büyük bir dil modeliyim.
            Bu robot uygulaması ise tamamen **Yusuf Efe Şahin** tarafından geliştirilmiş bir arayüzdür.
            """
        elif "ders" in user_input.lower() or "proje" in user_input.lower():
            response = """
            **Proje Geliştirme Süreçleri:** Bir yazılım projesinin başarılı olması için genellikle şu adımlar izlenir:
            1.  **Planlama ve Kapsam Belirleme:** Projenin ne yapacağı, hedef kitlesi ve teslim tarihi belirlenir.
            2.  **Tasarım:** Veritabanı yapısı, kullanıcı arayüzü (UI/UX) ve sistem mimarisi tasarlanır.
            3.  **Kodlama:** Seçilen programlama dilleri (sizin durumunuzda Python/Streamlit) kullanılarak yazılım geliştirilir.
            4.  **Test Etme:** Yazılımın hataları (bug) ayıklanır ve tüm işlevlerin beklendiği gibi çalıştığından emin olunur.
            5.  **Dağıtım (Deployment):** Uygulama, son kullanıcıların erişebileceği bir ortama (Streamlit Cloud gibi) yerleştirilir.
            
            Projeniz için başarılar dilerim!
            """
        else:
            response = f"""
            **Soru Analizi:** Sorduğunuz soru ('{user_input}'), yapay zeka algoritmamız tarafından derinlemesine incelenmektedir.
            Bu tür karmaşık konular, genellikle birden fazla veri setinin ve dil modelinin karşılaştırılmasını gerektirir. 
            Analiz tamamlandığında, size en doğru ve kapsamlı cevabı sunmak için çalışıyorum.
            """
            
        st.success("Robot Cevabı:")
        st.markdown(response)
    else:
        st.warning("Lütfen robotunuza bir soru yazın.")

# Alt Bilgi (Geliştirici Adı Güncellendi)
st.markdown("---")
st.caption("Geliştiren: Yusuf Efe Şahin / Son Proje")
