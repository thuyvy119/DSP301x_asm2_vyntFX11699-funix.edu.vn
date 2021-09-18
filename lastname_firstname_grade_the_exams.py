#!/usr/bin/env python
# coding: utf-8

### Assignment 2

# ### Task 1

# In[ ]:

import numpy as np
import pandas as pd

file_open= False
while file_open==False:
    filename = input("Enter a filename: ")
    file= filename + '.txt'
    try:
        f= open(str(file),'r')     #open file with file name entering by user
        file_open= True
        print("Successfully opened ", file)
    except:
        print(file, " does not exist. Please try again")

# ### Task 2

# In[ ]:


print("------------------ANALYZING------------------")
lcount=0
valid_count=0
valid_line_list= []
for line in f:
    lcount+= 1
    stripped_line= line.strip()          #remove the space before or after each line
    num_elm_in_line = len(stripped_line.split(','))         #the number of elements in each line
    line_list= stripped_line.split(',')                     #covert all line elements into list
    first_element_split= [char for char in line_list[0]]                #
    
    num_char_ID=0
    ###---------Check the first condition of every valid line having 26 elements splitted by a comma---------###
    if num_elm_in_line == 26: 
        ###---------Then check ID element whether starting by N character and consisting of 9 chars---------### 
        if first_element_split[0]=='N' and  len(first_element_split)==9:
            ###---------Check if the last 8 chars of ID are digits, if it's correct then count the valid line ---------###
            for b in range(1,9):
                if first_element_split[b].isdigit()== True:
                    first_element_split[b]= int(first_element_split[b])
                    num_char_ID+= 1
            if num_char_ID== 8:     # if the last 8 chars are digits then count valid line
                valid_count+= 1
                valid_line_list.append(line_list)
            else:                   # else the valid count still remained
                valid_count= valid_count
                print('Invalid line of data: N# is invalid\n', line)
        else:
            print('Invalid line of data: N# is invalid\n',  line)
    else:
        print('Invalid line of data: does not contain exactly 26 elements\n',  line)
        
###--------- If all lines in text file are valid, then notify NO ERROR ---------###    
if lcount== valid_count:
    print("NO ERROR FOUND")
print("------------------REPORT------------------")
print("Total number of lines in file is: ", lcount)
print('Total valid lines of data is: ', valid_count)
print('Total invalid lines of data is: ', lcount- valid_count)
#print('Valid lines list: ', valid_line_list)


# ### Task 3

# In[ ]:


answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"


# In[ ]:


answer_key_list= answer_key.split(',')        #split answer key


# In[ ]:


ans_list=[]
stu_ID= []
###--------- Separate answer and student ID from each valid line then comprise in lists---------###

for a in valid_line_list:
    ans_line= []
    stu_ID.append(a[0])   # list of students' ID
    for b in range(1,len(a)):
        ans_line.append(a[b])
    ans_list.append(ans_line)   #list of students' answers
    
###--------- Calculate grade for each valid line based on the answer key and list of answers ---------###
grade_list=[]
for i in range(len(ans_list)):
    grade_count= 0
    for j in range(len(answer_key_list)):           #Check students' answers with the answer key
        if ans_list[i][j]== answer_key_list[j]:     #student will gain +4 points for each correct answer
            grade_count+= 4
        elif ans_list[i][j]== '':                   #no point for each missed answer
            grade_count = grade_count
        else:                                       #and will be minused 1 point for each wrong answer
            grade_count = grade_count- 1
    grade_list.append(grade_count)

###--------- Combine and convert 2 lists students ID and grade into pandas dataframe ---------###
df= pd.DataFrame(list(zip(stu_ID,grade_list)), columns= ['Student ID', 'Grade'])

###--------- Get mean, min, max, range of scores, and median from grade list--------- ###
max_score= df['Grade'].max()
min_score= df['Grade'].min()
range_score= max_score- min_score
print('Mean (average) score: ', df['Grade'].mean())
print('Highest score: ', max_score)
print('Lowest score: ', min_score)
print('Range of scores: ', range_score)
print('Median score: ', df['Grade'].median())


# ### Task 4

# In[ ]:


###--------- Write pandas dataframe into text file --------- ###
class_grade= filename+ '_grades.txt'
df.to_csv(class_grade, header=None, index=None, sep=',', mode='w')


# In[ ]:




