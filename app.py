import streamlit as st

st.title("Baumberechnungstool")



zahl1 = float(st.number_input("Kleinerer Radius:"))
zahl2 = float(st.number_input("Größerer Radius:"))
laenge = float(st.number_input("Länge des Baumes:"))

if st.button("Berechnen"):
    wert1 = zahl1 + zahl2 / 2
    wert2 = wert1 * 3.14
    wert3 = wert2 * laenge
    wert4 = wert3 / 1000000
    
    st.write("Ergebnis:", wert4,"m³")