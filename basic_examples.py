#Making a basic Bokeh line graph

#%%
#importing bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show, output_notebook
import pandas

#%%
#prepare some data
df = pandas.read_csv("data/bachelors.csv")
x = df["Year"]
y = df["Biology"]

#%%
#prepare the output file
#output_file("Line_from_csv.html")
output_notebook()

#%%
#create a figure object
f = figure()

#%%
#create line plot
f.line(x,y)

#%%
#write the plot in the figure object
show(f)
