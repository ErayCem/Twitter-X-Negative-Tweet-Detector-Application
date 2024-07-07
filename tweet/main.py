import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

def tweet_tahmini():
    tweet = tweet_entry.get()  # Kullanıcının girdisi alınır
    isim = isim_entry.get()  # Kullanıcının adını al
    tweet_vector = vectorizer.transform([tweet])  # Girdi vektöre dönüştürülür
    isim_vector = vectorizer.transform([isim])  # İsim vektöre dönüştürülür
    tahmin_tweet = model.predict(tweet_vector)[0]  # Tweet için model kullanılarak tahmin yapılır
    tahmin_isim = model.predict(isim_vector)[0]  # İsim için model kullanılarak tahmin yapılır
    if tahmin_tweet == "Negatif":
        tweet_message = "negatif."
    elif tahmin_tweet == "Pozitif":
        tweet_message = "pozitif."
    else:
        tweet_message = "tahmin edilemedi."
    if tahmin_isim == "Negatif":
        isim_message = "negatif bir çağrışım içeriyor."
    elif tahmin_isim == "Pozitif":
        isim_message = "pozitif bir çağrışım içeriyor."
    else:
        isim_message = "tahmin edilemedi."
    messagebox.showinfo("Tweet ve İsim Analizi", f"Girdiğiniz tweet {tweet_message}\nGirdiğiniz isim {isim_message}")

# Veri setini yükle
veri_seti = pd.read_csv("C:\\Users\\90552\\Desktop\\tweets.csv", encoding="ISO-8859-9")
veri_seti.dropna(inplace=True)

# Bağımsız değişken (X) ve bağımlı değişken (y) olarak ayır
X = veri_seti["Paylaşım"]
y = veri_seti["Tip"]

# Metin verilerini vektörlere dönüştürmek için bir vektörleştirici oluştur
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Naive Bayes modelini oluştur
model = MultinomialNB()
model.fit(X, y)

# Tkinter uygulamasını oluştur
app = tk.Tk()
app.title("Tweet ve İsim Analiz Uygulaması")

# Fotoğraf
photo = PhotoImage(file="C:\\Users\\90552\\Desktop\\200w.gif")  # Resim dosyasının yolunu belirtin
photo_label = tk.Label(app, image=photo, bg="#f0f0f0")
photo_label.pack(pady=10)
app.configure(bg="#f0f0f0")  # Arka plan rengini ayarla

# Frame
frame = tk.Frame(app, bg="#ffffff", bd=2, relief="groove")
frame.pack(padx=20, pady=20)



# Tweet etiketi
tweet_label = tk.Label(frame, text="Tweet:", font=("Arial", 12), bg="#ffffff")
tweet_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Tweet giriş kutusu
tweet_entry = tk.Entry(frame, width=50, font=("Arial", 12))
tweet_entry.grid(row=0, column=1, padx=10, pady=10)

# İsim etiketi
isim_label = tk.Label(frame, text="İsim:", font=("Arial", 12), bg="#ffffff")
isim_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# İsim giriş kutusu
isim_entry = tk.Entry(frame, width=50, font=("Arial", 12))
isim_entry.grid(row=1, column=1, padx=10, pady=10)

# Analiz Et butonu
button = tk.Button(frame, text="Analiz Et", command=tweet_tahmini, font=("Arial", 12), bg="#007bff", fg="#ffffff")
button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Uygulamayı çalıştır
app.mainloop()
