import streamlit as st
import time

image_info = {
    "logo.png": "Logo Design - Logo for Infoaid Tech.",
    "banner.png": "Banner Design - Banner for Infoaid Tech.",
    "food_menu.jpg": "Food Menu - This is a realistic image of a food menu.",
    "bookcover.png": "Book Cover Design - This is a book cover related to an evil AI story.",
}


def main():
    
    st.write(
        "<div style='text-align: center;'>"
        "<h1>Portfolio Website</h1>"
        "<h3>Welcome to my portfolio!</h3>"
        "</div>",
        unsafe_allow_html=True,
    )


    st.write("Below are some of my work examples during my internship at Infoaid Tech. Select an image from the dropdown menu to view.")

    selected_image = st.selectbox("Select Image", list(image_info.keys()), format_func=lambda x: image_info[x])

  
    image_description = image_info[selected_image]

    image_container = st.empty()
    image_container.image(selected_image, caption=image_description, use_column_width=True)


    while True:
        time.sleep(3)  

    
        selected_image_index = (list(image_info.keys()).index(selected_image) + 1) % len(image_info)
        selected_image = list(image_info.keys())[selected_image_index]
        image_description = image_info[selected_image]

     
        image_container.image(selected_image, caption=image_description, use_column_width=True)

if __name__ == "__main__":
    main()
