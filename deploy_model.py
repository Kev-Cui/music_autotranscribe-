###############################
# This program lets you       #
# - Create a dashboard        #
# - Evevry dashboard page is  #
# created in a separate file  #
###############################

# Python libraries
import streamlit as st
from PIL import Image

from ml import ml

def main():

    #############
    # Main page #
    #############

    options = ['Home','autoscribe','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')

    if ( choice == 'Home' ):
      st.title("Music autoscribe, you give me music, I give you notes")
      st.image('./images/photo-1501167786227-4cba60f6d58f.jpeg')
      pass

    elif ( choice == 'autoscribe' ):
      ml()

    else:
      st.stop()


main()
