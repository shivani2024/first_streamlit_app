import streamlit
streamlit.title('My First ever Python App')
streamlit.header('Breakfast Menu')
streamlit.header('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('kale,spinach and Rocket smoothie')
streamlit.text('Hard Boiled Free Range Egg')
streamlit.text('Avacode toast')
streamlit.header('Create your own Fruit smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index).['Avacado','Strawberries'])
streamlit.dataframe(my_fruit_list)

