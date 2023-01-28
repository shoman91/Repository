import pandas as pd
import streamlit as st

#file = r'C:\Users\acer\Documents\K DOT AI\Billionaire.csv'

#reading the file
df=pd.read_csv('Billionaire.csv')

#Top Billionaire
top_bill = df[df['Rank']==1]
print(top_bill)

#find count of billionaires by country:
x= df.groupby('Country')[['Name']].count().sort_values(['Name'],ascending=False).head(10)
print(df.groupby('Country')[['Name']].count().sort_values(['Name'],ascending=False).head(10))

st.bar_chart(x)


#find the most popular sources of income
y = df.groupby('Source')[['Name']].count().sort_values(['Name'], ascending=False )
print(df.groupby('Source')[['Name']].count().sort_values(['Name'], ascending=False ))
st.area_chart(y)

#get the cumulative wealth of billionaires belong to US
def convert_values(val):
    result = val.replace('$', '').replace('B', '')
    final_result = float(result)
    return final_result

df['Updated Networth'] = df['NetWorth'].apply(convert_values)
Country_is_US = df[df['Country']=='United States']

bill_count = Country_is_US['Updated Networth'].sum()

#interactive
all_countries = df['Country'].unique()

selection = st.selectbox('Select Country', all_countries)

subset = df[df['Country'] == selection]

st.dataframe(subset)

####something new ==> containers

#display on streamlit
all_countries1 = sorted(df['Country'].unique())

col1, col2 = st.columns(2)

#column 1 
selected_country = col1.selectbox('Select Your Country', all_countries1)

#subset on selected country
subset_country = df[df['Country']==selected_country]

#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())

#display multi select option on source
selected_source = col1.multiselect('Select Source of Income', sources)

#subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

#Column 2

main_string = '{} - Billionaires'.format(selected_country)
col2.header(main_string)
col2.table(subset_country)
col2.header('Source wise info')
col2.table(subset_source)



