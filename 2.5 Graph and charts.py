import openpyxl
from openpyxl.chart import PieChart, Reference, Series, PieChart3D
# needs to import different things for different chart, for pie chart-import above module from openpyxl.chart

wb = openpyxl.Workbook()
ws = wb.active

data = [
    ['Flavor', 'Sold'],
    ['Vanilla', '1500'],
    ['Chocolate', '1700'],
    ['Strawberry', '600'],
    ['Pumpkin Spice', '950'],
]

for rows in data:
    ws.append(rows)
# loop over data and append it to worksheet

chart = PieChart()
# create a chart variable then inform excel how to use the data and map it to the chart

labels = Reference(ws, min_col=1, min_row=2, max_row=5)
data = Reference(ws, min_col=2, min_row=2, max_row=5)
# create two variables to store the two sections of data (label and numerical); both use Reference to look for location for the data 
# when using Reference, no need to specify a max column as it is same as min col

chart.add_data(data, titles_from_data=True)
# use function add_data to import the data into chart data

chart.set_categories(labels)
# add chart label

chart.title = 'Ice Cream by Flavor'
# add chart title

ws.add_chart(chart, 'C1')
# load chart into excel, set the top left corner of the chart in C1

wb.save('Pie.xlsx')
