import csv 

data = """
... First Name,Gender,Start Date,Last Login Time,Salary,Bonus %,Senior Management,Team
... Gary,Male,1/27/2008,11:40 PM,109831,5.831,false,Sales
... Kimberly,Female,1/14/1999,7:13 AM,41426,14.543,true,Finance
... Lillian,Female,6/5/2016,6:09 AM,59414,1.256,false,Product
... Jeremy,Male,9/21/2010,5:56 AM,90370,7.369,false,Human Resources
... Shawn,Male,12/7/1986,7:45 PM,111737,6.414,false,Product
... """.lstrip()

data_iterator = iter(data.splitlines())
reader = csv.reader(data_iterator)
for row in reader:
   print(row)


['First Name', 'Gender', 'Start Date', 'Last Login Time', 'Salary', 'Bonus %', 'Senior Management', 'Team']
['Gary', 'Male', '1/27/2008', '11:40 PM', '109831', '5.831', 'false', 'Sales']
['Kimberly', 'Female', '1/14/1999', '7:13 AM', '41426', '14.543', 'true', 'Finance']
['Lillian', 'Female', '6/5/2016', '6:09 AM', '59414', '1.256', 'false', 'Product']
['Jeremy', 'Male', '9/21/2010', '5:56 AM', '90370', '7.369', 'false', 'Human Resources']
['Shawn', 'Male', '12/7/1986', '7:45 PM', '111737', '6.414', 'false', 'Product'] 

dic = {'a': 1, 'b': 2, 'c': 3}

print(dic.keys())