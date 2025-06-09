For the first eight questions, use cars-sample35.txt. The seven distinct values represent attributes of a single type of automobile. Specifically we have the following:  
\- Price  
\- Maintenance cost  
\- Number of doors  
\- Number of passengers  
\- Luggage capacity  
\- Safety rating  
\- Classification of vehicle

1.  Upload the data to github. Upload the data to python using Pandas and give it headers.
2.  Extract these seven attributes from each line of the file and create seven distinct Python list objects comprised solely of the values you extracted for a given attribute. In other words, you should have lists of prices, maintenance costs, number of doors, etc.
3.  Find the list index values of each automobile having a “price” rating of "med". Create a new list object with your result. HINT: you can accomplish this task by searching the list of price values you created earlier. Be sure to print your results.
4.  Find the "number of passengers" value for each auto having a "price" value of "med". Create a new list to store your findings and be sure to print your results.
5.  Find the index value for each automobile having a “price” value of "high" and a “maintenance” value that is not "low". Create a new list to store your findings and be sure to print your results.
6.  Find the list index values of each automobile having a price rating of "med using a list comprehension instead of a basic for or while loop. The list comprehension should create a new list containing your result. Be sure to print your results to the screen.
7.  Find the "number of passengers" value for each auto having a "price" value of "med" using a list comprehension instead of a basic for or while loop. The list comprehension should create a new list containing your findings. Be sure to print your results to the screen.
8.  Find the index value for each automobile having a price value of "high" and a maintenance value that is not "low" using a list comprehension. The list comprehension should create a new list containing your findings. Be sure to print your results to the screen.

Nested List Comprehension (no file needed):

1.  Consider the following list of lists: nlist = \[ \[1, 2, 3\], \[‘A’, ‘B’, ‘C’\], \[4, 5\], \[‘D’, ‘E’\] \]. Extract each individual element of the component lists contained within nlist and add them to a new list.  Do NOT use a nested for loop, use a list comprehension.
