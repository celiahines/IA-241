
# coding: utf-8

# In[19]:


from urllib import request

import json

from pprint import pprint

import xlwt

import xlrd


# In[13]:


census_api_key = '949dbcdffc7ac237a28e19b3dc8c7bc712357a53' #get your key from https://api.census.gov/data/key_signup.html


# In[14]:


url_str = 'https://api.census.gov/data/2017/acs/acs5?get=B01001_002E,B01001_001E,NAME&for=county:*&in=state:51&key='+census_api_key # create the url of your census data


# In[15]:


print (url_str)


# In[16]:


response = request.urlopen(url_str) # read the response into computer
html_str = response.read().decode("utf-8") # convert the response into string


# In[17]:


print(html_str)


# # Q3

# In[10]:


book = xlwt.Workbook()
sheet=book.add_sheet('va_pop')
i=0
if html_str:
    json_data = json.loads (html_str) 
    for record in json_data:
        total_pop,male_pop,  name, state, count_num= record
        sheet.write(i,0,total_pop)
        sheet.write(i,1,male_pop)
        i +=1
book.save ('census.xls')


# # Q4

# In[23]:


book = xlrd.open_workbook('census.xls')
my_sheet = book.sheet_by_name('va_pop')
print (my_sheet.nrows) #nrows calls the number of rows within the sheet 
for i in range(10):
    row=my_sheet.row_values(i)
    tot,male=row
    print (tot,male)


# # Q5

# In[43]:


from xlutils.copy import copy


# In[46]:


read_book = xlrd.open_workbook('census.xls')
writing_book= copy(read_book) #this creates a copy
write_sheet=writing_book.get_sheet(0) #using get function to access a section from a sheet
my_sheet=read_book.sheet_by_name('va_pop')


for i in range (my_sheet.nrows):
    row=my_sheet.row_values(i)
    male,tot,ratio=row
    if i == 0:
        write_sheet.write(i,2,'ratio')
    else:
        write_sheet.write(i,2,int(male)/int(tot))
        
writing_book.save('census.xls')


# # Q6

# In[47]:


book = xlrd.open_workbook('census.xls')
my_sheet = book.sheet_by_name('va_pop')
for i in range(10):
    row=my_sheet.row_values(i)
    tot,male,ratio=row
    print (tot,male)

