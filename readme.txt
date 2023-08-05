Revision
# Flight Data 
	 1) Import Data
	 2) Use basic Features like info, describe
	 3) Convert Date-Time format --- > Int 
	 4) Convert (Possible int data) --- > Int 
	 			(Duration in hh:mm) ---> Int (in Min)
	 			# Use Regular expressions to avoid any error 

	 5) Convert the Stops data ----> Int using Lable Encoding (map function)
	 6) Convert the Categorical ---> Inr using OneHot Encoding / 
	    When there are less number of features, use Onehot encoding othwewise target guided ordinal encoding

# App Store
	1) Import Data
	2) Use Basic Stuff like Info, Describe, Shape
	3) Check for missing values 
	4) Try to convert Reviews into Numeric data 
	   You will encounter an error 3.0 M which cant be type casted to int directly 
	5) Convert the Size into Kb
	   Mega Byte ----- > Kilo Byte 
	   While Converting be carefull, There are few apps "Varries with devices"
	6) Now Convert 'Prices' and 'Installs' into float,
		Just make a function and replace char with ''
	7) Extract date-time from "Last Updated"
		Use pd.to_datetime
	8) Duplicated Observation 
		Remove the Duplicated, keep the first entry, serarch via "App"