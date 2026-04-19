import pandas as pd
import numpy as np
import plotly.express as px

file = "Code Fest.xlsx"
data = pd.read_excel(file)

filterData2019 = data[(data['2019 Accomidation'] != 0) & (data['2019 Expenditure'] != 0)]
filterData2020 = data[(data['2020 Accomidation'] != 0) & (data['2020 Expenditure'] != 0)]
filterData2021 = data[(data['2021 Accomidation'] != 0) & (data['2021 Expenditure'] != 0)]
filterData2022 = data[(data['2022 Accomidation'] != 0) & (data['2022 Expenditure'] != 0)]

x = np.concatenate((filterData2019['2019 Accomidation'], 
    filterData2020['2020 Accomidation'], 
    filterData2021['2021 Accomidation'], 
    filterData2022['2022 Accomidation']))

y = np.concatenate((filterData2019['2019 Expenditure'], 
    filterData2020['2020 Expenditure'], 
    filterData2021['2021 Expenditure'], 
    filterData2022['2022 Expenditure']))

countries = np.concatenate((filterData2019['Country'], 
    filterData2020['Country'], 
    filterData2021['Country'], 
    filterData2022['Country']))

years = np.concatenate((['2019'] * len(filterData2019), 
    ['2020'] * len(filterData2020), 
    ['2021'] * len(filterData2021), 
    ['2022'] * len(filterData2022)))

countryYear = countries + ' ' + years

plot_data = pd.DataFrame({
    'Accommodation': x,
    'Expenditure': y,
    'Country': countries,
    'Label': countryYear
})

fig = px.scatter(
    plot_data, 
    x = 'Accommodation', 
    y = 'Expenditure', 
    color = 'Country', 
    hover_name = 'Label',
    title = 'Scatter Plot of Accommodation vs Expenditure (2019-2022)',
    labels = {'Accommodation': 'Accommodation (Thousands)', 'Expenditure': 'Expenditure (Millions)'}
)

fig.show()
#fig.write_html("CodeFest.html")