import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import jieba
import codecs
import pandas as pd
import re

from similar_song_predict import all_predict
from tfidf_predict import categorize
# from recommend import categorize
from recommend import similar_predict
# from recommend import all_predict


st.write("# Song Classifier and Recommender")
mode = st.selectbox("Mode", ["Select Mode", "Classify","Recommend with category", "Recommend"])
# mode = st.selectbox("Mode", ["Classify","Recommend with category"])
# lyrics = st.text_input("Lyrics")



if(mode == "Classify"):
    lyrics = st.text_input("Lyrics")
    if(lyrics != ''):
        category = categorize(lyrics)
        text_type = st.text_area("Type", value=category)
    

elif(mode == "Recommend"):
    lyrics = st.text_input("Lyrics")
    # lyric_seg, category = categorize(lyrics)
    # text_type = st.text_area("Type", value=category)
    # song_names, song_lyrics, acc = all_predict(lyric_seg)
    if(lyrics != ''):
        song_names, song_lyrics, acc = all_predict(lyrics) 
        text_song_name0 = st.text_area("Song 1", value=song_names[0], height=12)
        text_song_0 = st.text_area("Lyrics", value=song_lyrics[0])
        text_song_name1 = st.text_area("Song 2", value=song_names[1], height=12)
        text_song_1 = st.text_area("Lyrics", value=song_lyrics[1])
        text_song_name2 = st.text_area("Song 3", value=song_names[2], height=12)
        text_song_2 = st.text_area("Lyrics", value=song_lyrics[2])
        text_song_name3 = st.text_area("Song 4", value=song_names[3], height=12)
        text_song_3 = st.text_area("Lyrics", value=song_lyrics[3])
        text_song_name4 = st.text_area("Song 5", value=song_names[4], height=12)
        text_song_4 = st.text_area("Lyrics", value=song_lyrics[4])
elif(mode == "Recommend with category"):
    lyrics = st.text_input("Lyrics")
    # lyric_seg, category = categorize(lyrics)
    # text_type = st.text_area("Type", value=category)
    if(lyrics != ''):
        category, song_names, song_lyrics, acc = similar_predict(lyrics) 
        text_type = st.text_area("Type", value=category)
        text_song_name0 = st.text_area("Song 1", value=song_names[0], height=12)
        text_song_0 = st.text_area("Lyrics", value=song_lyrics[0])
        text_song_name1 = st.text_area("Song 2", value=song_names[1], height=12)
        text_song_1 = st.text_area("Lyrics", value=song_lyrics[1])
        text_song_name2 = st.text_area("Song 3", value=song_names[2], height=12)
        text_song_2 = st.text_area("Lyrics", value=song_lyrics[2])
        text_song_name3 = st.text_area("Song 4", value=song_names[3], height=12)
        text_song_3 = st.text_area("Lyrics", value=song_lyrics[3])
        text_song_name4 = st.text_area("Song 5", value=song_names[4], height=12)
        text_song_4 = st.text_area("Lyrics", value=song_lyrics[4])

    # text_song2 = st.text_area("Song 2", value=song_names[1] + "\n" + song_lyrics[1])
    # text_song3 = st.text_area("Song 3", value=song_names[2] + "\n" + song_lyrics[2])
    # text_song4 = st.text_area("Song 4", value=song_names[3] + "\n" + song_lyrics[3])
    # text_song5 = st.text_area("Song 5", value=song_names[4] + "\n" + song_lyrics[4])
    