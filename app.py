import sim 

# Print the values in dataframe values_df in a line grapgh 
print(sim.values_df)

# rest_index(): resets the dataframe every time the inputs change and prints out a new line chart 
sim.values_df.reset_index().plot.scatter(x = "index", y ='y')
sim.plt.show()