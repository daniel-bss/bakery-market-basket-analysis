import streamlit as st
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import association_rules, apriori

st.set_page_config(page_title="MarketBasket Web App", page_icon="🍞", layout="wide", initial_sidebar_state="expanded", menu_items=None)

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)

with open("style.css") as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown(
"""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a href="/" target="_blank" id="main-btn">MarketBasket WebApp</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav"">
      <li class="nav-item">
        <a id="notebook" class="nav-link active" href="https://www.kaggle.com/code/danielsimamora/market-basket-analysis" target="_blank">📄Notebook</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html = True)

st.markdown("""<p id="title-1z2x">Bakery Shop Item Recommender</p>""", unsafe_allow_html=True)
st.markdown("""<p id="caption-1z2x">A Web App that helps recommend items to customer!</p>""", unsafe_allow_html=True)

# Processing the CSV as Pandas DataFrame
data_depl = pd.read_csv("https://raw.githubusercontent.com/daniel-bss/MarketBasketAnalysis/main/bread_basket.csv")
data_depl['date_time'] = pd.to_datetime(data_depl['date_time'], format = "%d-%m-%Y %H:%M")

data_depl["month"] = data_depl['date_time'].dt.month
data_depl["day"] = data_depl['date_time'].dt.weekday

data_depl["month"].replace([i for i in range(1, 12 + 1)], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], inplace = True)
data_depl["day"].replace([i for i in range(6 + 1)], ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], inplace = True)

# Filter the data based on User Inputs
def get_data(period_day = '', weekday_weekend = '', month = '', day = ''):
    data = data_depl.copy()
    filtered = data.loc[
        (data["period_day"].str.contains(period_day)) & 
        (data["weekday_weekend"].str.contains(weekday_weekend)) & 
        (data["month"].str.contains(month.title())) &
        (data["day"].str.contains(day.title()))
    ]
    return filtered if filtered.shape[0] else "No result!"

st.sidebar.header('User Input')
st.sidebar.text("Use these widgets to input values")

def user_input_features():
    item = st.sidebar.selectbox("Item", ['Bread', 'Scandinavian', 'Hot chocolate', 'Jam', 'Cookies', 'Muffin', 'Coffee', 'Pastry', 'Medialuna', 'Tea', 'Tartine', 'Basket', 'Mineral water', 'Farm House', 'Fudge', 'Juice', "Ella's Kitchen Pouches", 'Victorian Sponge', 'Frittata', 'Hearty & Seasonal', 'Soup', 'Pick and Mix Bowls', 'Smoothies', 'Cake', 'Mighty Protein', 'Chicken sand', 'Coke', 'My-5 Fruit Shoot', 'Focaccia', 'Sandwich', 'Alfajores', 'Eggs', 'Brownie', 'Dulce de Leche', 'Honey', 'The BART', 'Granola', 'Fairy Doors', 'Empanadas', 'Keeping It Local', 'Art Tray', 'Bowl Nic Pitt', 'Bread Pudding', 'Adjustment', 'Truffles', 'Chimichurri Oil', 'Bacon', 'Spread', 'Kids biscuit', 'Siblings', 'Caramel bites', 'Jammie Dodgers', 'Tiffin', 'Olum & polenta', 'Polenta', 'The Nomad', 'Hack the stack', 'Bakewell', 'Lemon and coconut', 'Toast', 'Scone', 'Crepes', 'Vegan mincepie', 'Bare Popcorn', 'Muesli', 'Crisps', 'Pintxos', 'Gingerbread syrup', 'Panatone', 'Brioche and salami', 'Afternoon with the baker', 'Salad', 'Chicken Stew', 'Spanish Brunch', 'Raspberry shortbread sandwich', 'Extra Salami or Feta', 'Duck egg', 'Baguette', "Valentine's card", 'Tshirt', 'Vegan Feast', 'Postcard', 'Nomad bag', 'Chocolates', 'Coffee granules ', 'Drinking chocolate spoons ', 'Christmas common', 'Argentina Night', 'Half slice Monster ', 'Gift voucher', 'Cherry me Dried fruit', 'Mortimer', 'Raw bars', 'Tacos/Fajita'])
    period_day = st.sidebar.selectbox('Period Day', ['Morning', 'Afternoon', 'Evening', 'Night'])
    weekday_weekend = st.sidebar.selectbox('Weekday / Weekend', ['Weekend', 'Weekday'])
    month = st.sidebar.select_slider("Month", ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    day = st.sidebar.select_slider('Day', ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    return period_day, weekday_weekend, month, day, item

period_day, weekday_weekend, month, day, item = user_input_features()

data = get_data(period_day.lower(), weekday_weekend.lower(), month, day)

st.text("")
st.text("")
try:
  st.text("User Input Dataframe:")
  st.dataframe(data)
except:
  st.markdown("""<h4 style="text-align: center;">No transaction was done on that values😕</h4>""", unsafe_allow_html=True)
  st.markdown("""
    <div id="roti-manis">
      <p>Here are some input values to give a try!</p>
      <ul style="margin: 0 auto">
        <li>Period Day: &nbsp;<i>Morning</i></li>
        <li>Weekday/Weekend: &nbsp;<i>Weekend</i></li>
        <li>Month: &nbsp;<i>Jan</i></li>
        <li>Day: &nbsp;<i>Sun</i></li>
      </ul>
    </div>
  """, unsafe_allow_html=True)


# ==========================================================================================================================================================================

def encode(x):
    if x <= 0:
        return 0
    elif x >= 1:
        return 1

if type(data) != type("No result!"):
  item_count = data.groupby(["Transaction", "Item"])["Item"].count().reset_index(name = "Count")
  item_count_pivot = item_count.pivot_table(index='Transaction', columns='Item', values='Count', aggfunc='sum').fillna(0)
  item_count_pivot = item_count_pivot.applymap(encode)

  support = 0.01 # atau 1%
  frequent_items = apriori(item_count_pivot, min_support = support, use_colnames = True)

  metric = "lift"
  min_threshold = 1

  rules = association_rules(frequent_items, metric = metric, min_threshold = min_threshold)[["antecedents", "consequents", "support", "confidence", "lift"]]
  rules.sort_values('confidence', ascending = False, inplace = True)

def parse_list(x):
    x = list(x)
    if len(x) == 1:
        return x[0]
    elif len(x) > 1:
        return ", ".join(x)
    
def return_item_df(item_antecedents):
    data = rules[["antecedents", "consequents"]].copy()
    
    data["antecedents"] = data["antecedents"].apply(parse_list)
    data["consequents"] = data["consequents"].apply(parse_list)
    
    return list(data.loc[data["antecedents"] == item_antecedents].iloc[0,:])


# ==========================================================================================================================================================================

st.text("")
st.text("")

if type(data) != type("No result!"):
  st.markdown("""<p id="recommendation-1z2x">Recommendation:</p>""", unsafe_allow_html=True)
  st.markdown(f"Customer who buys **{item}**, also buys **{return_item_df(item)[1]}**!")
