import streamlit as st


def main():


    audio_file = open('data2/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__ == '__main__':
    main()