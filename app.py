import streamlit as st

#from sklearn.externals import joblib
import joblib

import time
from PIL import Image

gender_nv_model = open("models/naivemodel.pkl","rb")
gender_clf = joblib.load(gender_nv_model)

def predict_gender(data):
  vect = gender_cv.transform(data).toarray()
  result = gender_clf.predict(vect)
  return result

def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)

def main():
  """Gender Classifier App
    With Streamlit

  """

  st.title("Gender Classifier")
  html_temp = """
  <div style="background-color:blue;padding:10px">
  <h2 style="color:grey;text-align:center;">Streamlit App </h2>
  </div>

  """
  st.markdown(html_temp,unsafe_allow_html=True)
  load_css('icon.css')
  load_icon('people')

  name = st.text_input("Enter Name","Pleas Type Here")
  if st.button("Predict"):
    result = predict_gender([name])
    if result[0] == 0:
      prediction = 'Female'
      img = 'female.png'
    else:
      result[0] == 1
      prediction = 'Male'
      img = 'male.png'

    st.success('Name: {} was classified as {}'.format(name.title(),prediction))
    load_images(img)

