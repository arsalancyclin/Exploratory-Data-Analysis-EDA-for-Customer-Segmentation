# Streamlit Dashboard

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Customer Analytics', page_icon='📊')  

st.title('Customer Segmentation Dashboard')

df = pd.read_csv('customer_data.csv')
df2 = pd.read_csv('TechElectro_Customer_Data.csv')

viz = st.sidebar.selectbox('Select plot',['Pie Chart', 'Histogram', 'Scatterplot'])

if viz == 'Pie Chart':
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(df['Gender_Male'].value_counts(), labels=['Male', 'Female'], colors='bright', autopct='%1.1f%%')
    st.pyplot(fig)
    
elif viz == 'Histogram':
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df, x='AnnualIncome (USD)', kde=True, ax=ax)
    st.pyplot(fig)
    
else:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.scatterplot(data=df, x='Age', y='TotalPurchases', hue='Cluster', palette='dark', s=80, ax=ax)
    st.pyplot(fig)
    
# Display Age Distribution histogram
fig_age, ax_age = plt.subplots(figsize=(10, 5))
ax_age.hist(df['Age'], bins=20, color='green')
ax_age.set_xlabel('Age')
ax_age.set_ylabel('Count')
ax_age.set_title('Age Distribution')
st.pyplot(fig_age)

# Display Marital Status pie chart
fig_marital, ax_marital = plt.subplots(figsize=(10, 10))
ax_marital.pie(df2['MaritalStatus'].value_counts(), labels=df2['MaritalStatus'].value_counts().index, autopct='%1.1f%%')
ax_marital.set_title('Marital Status Distribution')
st.pyplot(fig_marital)

# Display Preferred Category countplot
fig_preferred, ax_preferred = plt.subplots(figsize=(10, 6))
sns.countplot(x='PreferredCategory', data=df2, ax=ax_preferred)
ax_preferred.set_title("Preferred Category Distribution")
st.pyplot(fig_preferred)

# Display Annual Income by Preferred Category boxplot
fig_box, ax_box = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df2, x='PreferredCategory', y='AnnualIncome (USD)', ax=ax_box)
ax_box.set_title('Annual Income by Preferred Category')
ax_box.set_xlabel('Preferred Category')
ax_box.set_ylabel('Annual Income (USD)')
st.pyplot(fig_box)
