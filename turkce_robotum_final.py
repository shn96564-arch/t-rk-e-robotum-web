import streamlit as st

# Uygulamanın Başlığı ve Açıklaması
st.title("🤖 Türkçe Robotum - Final Projesi")
st.write("Bu Streamlit uygulaması, bir yapay zeka robotunun arayüzüdür.")

# Kullanıcıdan Girdi Alma
user_input = st.text_area("Lütfen robotunuza bir soru sorun:", height=150)

# Cevap Üretme Butonu
if st.button("Cevap Üret"):
    if user_input:
        # Gerçek uygulamada buraya AI modelinizin kodu gelecek.
        # Basit bir örnek cevap döndürüyoruz:
        
        if "hava" in user_input.lower():
            response = "Hava durumu bilgisi için internete bakmanız gerekebilir."
        elif "adın" in user_input.lower():
            response = "Ben bir yapay zeka robotuyum ve adım yok."
        elif "ders" in user_input.lower() or "proje" in user_input.lower():
            response = "Projeniz için size başarılar dilerim! Hangi konuda yardıma ihtiyacınız var?"
        else:
            response = f"Sorunuz: '{user_input}' üzerine düşünüyorum ve size kısa süre içinde en iyi cevabı sunacağım."
            
        st.success("Robot Cevabı:")
        st.markdown(response)
    else:
        st.warning("Lütfen robotunuza bir soru yazın.")

# Alt Bilgi
st.markdown("---")
st.caption("Geliştiren: Vahap / Son Proje")
