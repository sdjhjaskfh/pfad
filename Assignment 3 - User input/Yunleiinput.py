import streamlit as st

def main():
    # Set a custom background color
    st.markdown(
        """
        <style>
        .main {
            background-color: #91341D;
        }
        </style> 
        """,
        unsafe_allow_html=True
    )

    
    # Add a title with a larger font size
    st.markdown("<h1 style='text-align: center; color: #E96B3D;'>Welcome to the Disney Halloween!</h1>", unsafe_allow_html=True)

    # Add an image
    st.image("https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/1600/900/75/vision-dam/digital/hkdl-platform/hkdl-global-assets/custom/christmas-2024/HKDL21663-1-16x9.jpg?2024-09-11T21:27:11+00:00", use_column_width=True)
    # Add a description
    st.markdown("<p style='text-align: center;color: #F9885E'>Get ready for this magic adventure!</p>", unsafe_allow_html=True)

    # Button to start
    if st.button("Start from here!"):
        st.success("Trick or treat! Have a magical day!")
    # Display a video
        st.video("https://youtu.be/_DY3SHUvvKM")

if __name__ == "__main__":
    main()