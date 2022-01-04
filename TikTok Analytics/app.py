import streamlit as st
import pandas as pd
from tiktok import get_data
from subprocess import call 
import plotly.express as px

st.set_page_config(layout='wide')
st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This dashboard allows you to analyse trending 📈 tiktoks using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>hashtag</i> you wish to analyse</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)


hashtag=st.text_input("Hashtag search",value ="")
if  st.button("get data"):
    call(['python','tiktok.py',hashtag])

    df=pd.read_csv("tiktokdata.csv")
    
    # plotly viz here 
    fig=px.histogram(df,x='desc',hover_data=['desc'],y='stats_diggCount')
    st.plotly_chart(fig,use_container_width=True)

    # split columns 
    left_col,right_col =st.columns(2)

    scatter1=px.scatter(df,x='stats_shareCount',y='stats_commentCount',hover_data=['desc'],size='stats_playCount')
    left_col.plotly_chart(scatter1,use_container_width=True)
    
    scatter2=px.scatter(df,x='authorStats_videoCount',y='authorStats_heartCount',hover_data=['author_nickname'],size='authorStats_followerCount',color='authorStats_followerCount')
    right_col.plotly_chart(scatter2,use_container_width=True)
    
    
    
    # to show in streamlit 
    df 