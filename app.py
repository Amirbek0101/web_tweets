import streamlit as st
import pickle

st.header("Doctor")
page_description = """Bu model sizda ko'krak saratoni kasalligi bor yo'qligini tekshira oladi"""
st.markdown(page_description)

model = None
radius_mean = st.number_input("radius_mean-O'simta hujayralarining o'rtacha radiusi (hajmi).", min_value=0.0, max_value=30.0, step=1.0, value=.00)
perimeter_mean = st.number_input("perimeter_mean-O'simtaning o'rtacha perimetri (atrofi)i", min_value=0.0, max_value=200.0, step=1.0, value=0.0)
area_mean = st.number_input("area_mean-O'simtaning o'rtacha yuzasi.", min_value=0.0, max_value=2600.0, step=1.0, value=0.0)

concave_points_mean = st.number_input("concave points_mean-O'simta konturidagi o'rtacha chuqur botiqlar soni ", min_value=0.0, max_value=5.0, step=1.0, value=0.0)
radius_worst = st.number_input("perimeter_worst -O'simtaning eng katta radius qiymati.", min_value=0.0, max_value=90.0, step=1.0, value=0.0)
perimeter_worst = st.number_input("perimeter_worst-O'simtaning eng katta perimetri.", min_value=0.0, max_value=300.0, step=1.0, value=0.0)
area_worst = st.number_input("area_worst-Eng katta yuzaga ega o'simta hududi", min_value=0.0, max_value=4500.0, step=1.0, value=0.0)
concave_points_worst = st.number_input("concave_points_worst-O'simtaning eng chuqur botiqlar soni.", min_value=0.0, max_value=5.0, step=0.001, value=0.0)

with open("C:\\Suniy 2\\sentiment_model.pkl","rb") as fl:
    pr = pickle.load(fl)

if st.button("Tekshirish "):
    BreastCancer_natija = pr.predict([[radius_mean, perimeter_mean, area_mean, concave_points_mean, radius_worst, perimeter_worst, area_worst, concave_points_worst]])
    if BreastCancer_natija == 1:
        st.write("Sizda ko'krak saratoni kasalligi mavjud.Natija yomon!")
    else:
        st.write("Sizda ko'krak saratoni kasalligi yo'q.Natija yaxshi! ")
