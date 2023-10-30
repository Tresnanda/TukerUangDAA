import requests
import streamlit as st
from collections import Counter

def tuker2(dari, ke, nilai):
    nilai = int(nilai)
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={nilai}&from={dari}&to={ke}")
    nilai_ubah = int(response.json()['rates'][ke])
    return nilai_ubah

def tuker(dari, ke, nilai):

    #nilai = int(input("Nilai: "))

    # nilai = int(nilai)
    # print(nilai)
    # print(dari)
    # print(ke)
    # response = requests.get(
    #     f"https://api.frankfurter.app/latest?amount={nilai}&from={dari}&to={ke}")

    # nilai_ubah = int(response.json()['rates'][ke])
    # print(nilai_ubah)
    # print("")
    nilai_ubah = tuker2(dari, ke, nilai)

    pecahan = []
    i = 0
    idr_list = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    usd_list = [100, 50, 20, 10, 5, 1]
    aud_list = [100, 50, 20, 10, 5, 2, 1]
    cny_list = [100, 50, 20, 10, 5, 1]
    inr_list = [2000, 500, 200, 100, 50, 20, 10, 5, 2]
    jpy_list = [10000, 5000, 2000, 1000]
    eur_list = [500, 200, 100, 50, 20, 10, 5]
    gbp_list = [50, 20, 10, 5]
    myr_list = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    krw_list = [50000, 10000, 5000, 1000]

    if ke == 'USD':
        pecahan_list = usd_list
        #nilai_ubah = round(nilai_ubah // 10) * 5
    elif ke == 'IDR':
        pecahan_list = idr_list
        nilai_ubah = round(nilai_ubah // 10000) * 10000
    elif ke == 'AUD':
        pecahan_list = aud_list
    elif ke == 'CNY':
        pecahan_list = cny_list
    elif ke == 'INR':
        pecahan_list = inr_list
        nilai_ubah = round(nilai_ubah // 5) * 5
    elif ke == 'JPY':
        pecahan_list = jpy_list
        nilai_ubah = round(nilai_ubah // 1000) * 1000
    elif ke == 'EUR':
        pecahan_list = eur_list
        nilai_ubah = round(nilai_ubah // 5) * 5
    elif ke == 'GBP':
        pecahan_list = gbp_list
        nilai_ubah = round(nilai_ubah // 5) * 5
    elif ke == 'MYR':
        pecahan_list = myr_list
    elif ke == 'KRW':
        pecahan_list = krw_list
        nilai_ubah = round(nilai_ubah // 1000) * 1000

    print(nilai_ubah)
    while nilai_ubah != 0 and i < len(pecahan_list):
        kertas = pecahan_list[i]
        if nilai_ubah - kertas >= 0:
            pecahan.append(kertas)
            nilai_ubah = nilai_ubah - kertas
        else:
            i += 1

    return pecahan


st.title("Penukar Mata Uang")

dari = st.selectbox("Tukar Dari", ['USD', 'IDR', 'AUD', 'CNY', 'INR', 'JPY', 'EUR', 'GBP', 'MYR', 'KRW'])
ke = st.selectbox("Tukar Ke", ['USD', 'IDR', 'AUD', 'CNY', 'INR', 'JPY', 'EUR', 'GBP', 'MYR', 'KRW'])
nilai = st.number_input("Jumlah Yang Ingin Ditukar")

if st.button("Tukar"):
    nilai_ubah = tuker2(dari, ke, nilai)
    st.write(f"Nilai Tukar {nilai} {dari} ke {ke} adalah {nilai_ubah} {ke}")
    pecahan = tuker(dari, ke, nilai)
    st.write("Berhasil ditukar dengan pecahan uang kertasnya:")
    counts = Counter(pecahan)
    
    for value, count in counts.items():
        if count > 1:
            st.text(f"{str(value)} {ke} x{count}")
        else:
            st.text(str(value))