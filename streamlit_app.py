import streamlit as st

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_show)

# New Section to display fruityvice api response
st.header("Fruityvice Fruit Advice!")

import requests as rq
fruityvice_response = rq.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
st.dataframe(fruityvice_normalized)
