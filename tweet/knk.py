import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# Veri setini yükle
veri_seti = pd.read_csv("tweets.csv", encoding="ISO-8859-9")
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

def tweet_tahmini():
    tweet = entry.get()  # Kullanıcının girdisi alınır
    tweet_vector = vectorizer.transform([tweet])  # Girdi vektöre dönüştürülür
    tahmin = model.predict(tweet_vector)[0]  # Model kullanılarak tahmin yapılır
    if tahmin == "Negatif":
        messagebox.showinfo("Tweet Analizi", "Girdiğiniz tweet negatif.")
    elif tahmin == "Pozitif":
        messagebox.showinfo("Tweet Analizi", "Girdiğiniz tweet pozitif.")
    else:
        messagebox.showinfo("Tweet Analizi", "Tahmin edilemedi.")

# Tkinter uygulamasını oluştur
app = tk.Tk()
app.title("Tweet Analiz Uygulaması")

# Etiket
label = tk.Label(app, text="Bir tweet girin:")
label.pack()

# Giriş kutusu
entry = tk.Entry(app, width=50)
entry.pack()

# Buton
button = tk.Button(app, text="Analiz Et", command=tweet_tahmini)
button.pack()

# Uygulamayı çalıştır
app.mainloop()
