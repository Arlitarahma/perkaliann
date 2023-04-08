# library

import streamlit as st

# Write
st.title('Perkalian')
st.write('Ini adalah aplikasi untuk mengalikan bilangan bulat')

# Input bilangan pertama
number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

# Input bilangan kedua
number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

# Hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silahkan pencet tombol hitung!')

st.snow()