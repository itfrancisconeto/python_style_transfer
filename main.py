import streamlit as st
from PIL import Image

import style

'''
Reference:
https://www.youtube.com/watch?v=M3lZNbFJ6I0
'''

st.title("Pytorch Style Transfer")

img = st.sidebar.selectbox(
    'Select Image',
    ('arena_romana.jpg', 'piramide_maia.jpg', 'torre_eiffel.jpg')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "_" + img

st.write("### Source Image:")
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button("Stylize")
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)
    st.write("### Output Image:")
    image = Image.open(output_image)
    st.image(image, width=400)