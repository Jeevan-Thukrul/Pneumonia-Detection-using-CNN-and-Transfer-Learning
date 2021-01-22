import streamlit as st
from PIL import Image
import classify

st.set_option('deprecation.showfileUploaderEncoding', False)

# st.markdown('<style>body{background-image: url("https://www.csintelligence.asia/wp-content/uploads/2020/03/network-lines-3-1024x512.png"); background-repeat: no-repeat; background-attachment: fixed; background-size: 100% 100%;} body::before{content: ""; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: rgba(1,1,1,0.80);}</style>',unsafe_allow_html=True)
st.markdown('<style>body{color: black; text-align: center;}</style>',unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

classes = {
        0: 'Normal Chest Xray',
        1: 'Pneumonia Detected'
      }

st.title("Pneumonia Detection - Machine Learning")
st.write("")
st.write("")
st.subheader("By Jeevan Thukrul")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)



        if st.button('predict'):
                st.write("Result...")
                label = classify.predict(uploaded_file)
                label = label.item()
                res = classes.get(label)
                st.success(res)

                img1 = "Output/cnn_acc.png"
                img2 = "Output/cnn_loss.png"
                st.image(img1)
                st.image(img2)
