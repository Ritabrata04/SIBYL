# -*- coding: utf-8 -*-


category_cols = df[['certifications', 'workshops', 'Interested subjects', 'interested career area ', 'Type of company want to settle in?', 
                    'Interested Type of Books']]
for i in category_cols:
  print(i)

Certifi = list(df['certifications'].unique())
print(Certifi)
certi_code = list(df['certifications_code'].unique())
print(certi_code)

Workshops = list(df['workshops'].unique())
print(Workshops)
Workshops_code = list(df['workshops_code'].unique())
print(Workshops_code)

Certi_l = list(df['certifications'].unique())
certi_code = list(df['certifications_code'].unique())
C = dict(zip(Certi_l,certi_code))

Workshops = list(df['workshops'].unique())
print(Workshops)
Workshops_code = list(df['workshops_code'].unique())
print(Workshops_code)
W = dict(zip(Workshops,Workshops_code))

Interested_subjects = list(df['Interested subjects'].unique())
print(Interested_subjects)
Interested_subjects_code = list(df['Interested subjects_code'].unique())
ISC = dict(zip(Interested_subjects,Interested_subjects_code))

interested_career_area = list(df['interested career area '].unique())
print(interested_career_area)
interested_career_area_code = list(df['interested career area _code'].unique())
ICA = dict(zip(interested_career_area,interested_career_area_code))

Typeofcompany = list(df['Type of company want to settle in?'].unique())
print(Typeofcompany)
Typeofcompany_code = list(df['Type of company want to settle in?_code'].unique())
TOCO = dict(zip(Typeofcompany,Typeofcompany_code))

Interested_Books = list(df['Interested Type of Books'].unique())
print(Interested_subjects)
Interested_Books_code = list(df['Interested Type of Books_code'].unique())
IB = dict(zip(Interested_Books,Interested_Books_code))

Range_dict = {"poor": 0, "medium": 1, "excellent": 2}
print(Range_dict)

pip install gradio

'''import gradio as gr

def inputlist(Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points, self_learning_capability, Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert, reading_and_writing_skills,
       memory_capability_score, smart_or_hard_work, Magement_or_Techinical,
       Interested_subjects, Interested_Type_of_Books,certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area ):
  
  dt = [Logical_quotient_rating, hackathons, coding_skills_rating,
       public_speaking_points, self_learning_capability,
       Extra_courses_did, certifications, workshops,
       reading_and_writing_skills, memory_capability_score,
       Interested_subjects, interested_career_area ,
       Type_of_company_want_to_settle_in,
       Taken_inputs_from_seniors_or_elders, Interested_Type_of_Books,
       worked_in_teams_ever, Introvert]
  col_list = ['Logical quotient rating', 'hackathons', 'coding skills rating',
       'public speaking points', 'self-learning capability',
       'Extra-courses did', 'certifications', 'workshops',
       'reading and writing skills', 'memory capability score',
       'Interested subjects', 'interested career area ',
       'Type of company want to settle in?',
       'Taken inputs from seniors or elders', 'Interested Type of Books',
       'worked in teams ever?', 'Introvert']
  ndff = pd.DataFrane(dt ,columns = [col_list])
  ndff.head(10)
  cols = ndff[["self-learning capability?", "Extra-courses did","Taken inputs from seniors or elders", "worked in teams ever?", "Introvert"]]
  for i in cols:  
    cleanup_nums = {i: {"Yes": 1, "No": 0}}
    ndff = ndff.replace(cleanup_nums)
    mycol = ndff[["reading and writing skills", "memory capability score"]]
  for i in mycol:
    cleanup_nums = {i: {"poor": 0, "medium": 1, "excellent": 2}}
    ndff = ndff.replace(cleanup_nums)
  
  mycol = ndff[["reading and writing skills", "memory capability score"]]
  for i in mycol:
    cleanup_nums = {i: {"poor": 0, "medium": 1, "excellent": 2}}
    ndff = ndff.replace(cleanup_nums)

  category_cols = ndff[['certifications', 'workshops', 'Interested subjects', 'interested career area ', 'Type of company want to settle in?', 
                    'Interested Type of Books']]
  for i in category_cols:
    ndff[i] = ndff[i].astype('category')
    ndff[i + "_code"] = ndff[i].cat.codes

  ndff = ndff.get_dummies(ndff, columns=["Management or Technical", "hard/smart worker"], prefix=["A", "B"])

  feed = ndff[['Logical quotient rating', 'coding skills rating', 'hackathons', 'public speaking points', 'self-learning capability?','Extra-courses did', 
           'Taken inputs from seniors or elders', 'worked in teams ever?', 'Introvert', 'reading and writing skills', 'memory capability score',  
           'B_hard worker', 'B_smart worker', 'A_Management', 'A_Technical', 'Interested subjects_code', 'Interested Type of Books_code', 'certifications_code', 
           'workshops_code', 'Type of company want to settle in?_code',  'interested career area _code']]

  feed = ndff[[Logical_quotient_rating, hackathons, coding_skills_rating,
       public_speaking_points, self_learning_capability,
       Extra_courses_did, certifications, workshops,
       reading_and_writing_skills, memory_capability_score,
       Interested_subjects, interested_career_area ,
       Type_of_company_want_to_settle_in,
       Taken_inputs_from_seniors_or_elders, Interested_Type_of_Books,
       worked_in_teams_ever, Introvert]]

  if(self_learning_capability=='Yes'):
    self_learning_capability = 1
  else:
    self_learning_capability = 0

  if(Extra_courses_did=='Yes'):
    Extra_courses_did = 1
  else:
    Extra_courses_did = 0

  if(Taken_inputs_from_seniors_or_elders=='Yes'):
    Taken_inputs_from_seniors_or_elders = 1
  else:
    Taken_inputs_from_seniors_or_elders = 0     

  if(Taken_inputs_from_seniors_or_elders=='Yes'):
    Taken_inputs_from_seniors_or_elders = 1
  else:
    Taken_inputs_from_seniors_or_elders = 0    

  if(worked_in_teams_ever=='Yes'):
    worked_in_teams_ever = 1
  else:
    worked_in_teams_ever = 0  

  if(Introvert=='Yes'):
    Introvert = 1
  else:
    Introvert = 0  
  
  feed1 = [Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points]

  input_list_col = [self_learning_capability, Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert, reading_and_writing_skills,
       memory_capability_score, smart_or_hard_work, Magement_or_Techinical,
       Interested_subjects, Interested_Type_of_Books,certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area ]
  feed=[]
  K=0
  j=0
  for i in input_list_col:
    if(i=='Yes'):
      j=1
      feed.append(j)
      continue
      print("feed 1")
    
    if(i=="No"):
      j=0
      feed.append(j)
      continue
      print("feed 2")
  
    for key in Range_dict:
      if(i==key):
        j = Range_dict[key]
        feed.append(j)
        continue
        print("feed 3")

    for key in C:
      if(i==key):
        j = C[key]
        feed.append(j)
        continue
        print("feed 4")
    
    for key in W:
      if(i==key):
        j = W[key]
        feed.append(j)
        continue
        print("feed 5")
    
    for key in ISC:
      if(i==key):
        j = ISC[key]
        feed.append(j)
        continue
        print("feed 6")

    for key in ICA:
      if(i==key):
        j = ICA[key]
        feed.append(j)
        continue
        print("feed 7")

    for key in TOCO:
      if(i==key):
        j = TOCO[key]
        feed.append(j)
        continue
        print("feed 8")

    for key in IB:
      if(i==key):
        j = IB[key]
        feed.append(j)
        continue
        print("feed 9")

    if(i=='Management'):
      j=1
      k=0
      feed.append(j)
      feed.append(K)
      continue
      print("feed 10,11")

    if(i=='Technical'):
      j=0
      k=1
      feed.append(j)
      feed.append(K)
      continue
      print("feed 12,13")

    if(i=='Smart worker'):
      j=1
      k=0
      feed.append(j)
      feed.append(K)
      continue
      print("feed 14,15")

    if(i=='Hard Worker'):
      j=0
      k=1
      feed.append(j)
      feed.append(K)
      continue
      print("feed 16,17")
  Total_feed = feed1+feed
  output = dtree.predict([Total_feed])
  return(output)
  

iface = gr.Interface(
    inputlist, 
    [
     gr.inputs.Number(default=None, label = "Logical_quotient_rating"),
     gr.inputs.Number(default=None, label = "coding_skills_rating"),
     gr.inputs.Number(default=None, label = "hackathons"),
     gr.inputs.Number(default=None, label = "public_speaking_points"),
     gr.inputs.Radio(['Yes', 'No'], label = "self_learning_capability"),
     gr.inputs.Radio(['Yes', 'No'], label = "Extra_courses_did"),
     gr.inputs.Radio(['Yes', 'No'], label = "Taken_inputs_from_seniors_or_elders"),
     gr.inputs.Radio(['Yes', 'No'], label = "worked_in_teams_ever"),
     gr.inputs.Radio(['Yes', 'No'], label = "Introvert"),
     gr.inputs.Radio(['poor','medium','excellent'], label= "reading_and_writing_skills"),
     gr.inputs.Radio(['poor','medium','excellent'], label= "memory_capability_score"),
     gr.inputs.Radio(['Smart worker', 'Hard Worker'],label= "smart_or_hard_work"),
     gr.inputs.Radio(['Management', 'Technical'],label= "Magement_or_Techinical"),
     gr.inputs.Dropdown(['programming', 'Management', 'data engineering', 'networks', 'Software Engineering', 'cloud computing', 'parallel computing', 'IOT', 'Computer Architecture', 'hacking'], label= "Interested_subjects"),
     gr.inputs.Dropdown(['Series', 'Autobiographies', 'Travel', 'Guide', 'Health', 'Journals', 'Anthology', 'Dictionaries', 'Prayer books', 'Art', 'Encyclopedias', 'Religion-Spirituality', 'Action and Adventure', 'Comics', 'Horror', 'Satire', 'Self help', 'History', 'Cookbooks', 'Math', 'Biographies', 'Drama', 'Diaries', 'Science fiction', 'Poetry', 'Romance', 'Science', 'Trilogy', 'Fantasy', 'Childrens', 'Mystery'], label= "Interested_Type_of_Books"),
     gr.inputs.Dropdown(['information security', 'shell programming', 'r programming', 'distro making', 'machine learning', 'full stack', 'hadoop', 'app development', 'python'], label= "certifications"),
     gr.inputs.Dropdown(['Testing', 'database security', 'game development', 'data science', 'system designing', 'hacking', 'cloud computing', 'web technologies'], label= "workshops"),
     gr.inputs.Dropdown(['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'], label= "Type_of_company_want_to_settle_in"),
     gr.inputs.Dropdown(['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'], label= "interested_career_area "),
     
     
     
    ],
    "text",)

if __name__ == "__main__":
    iface.launch(debug = True)'''

A = 'yes'
B = 'No'
col = [A,B]
for i in col:
  if(i=='yes'):
    i = 1
  print(i)

Certi_l = list(df['certifications'].unique())
certi_code = list(df['certifications_code'].unique())
C = dict(zip(Certi_l,certi_code))

Workshops = list(df['workshops'].unique())
print(Workshops)
Workshops_code = list(df['workshops_code'].unique())
print(Workshops_code)
W = dict(zip(Workshops,Workshops_code))

Interested_subjects = list(df['Interested subjects'].unique())
print(Interested_subjects)
Interested_subjects_code = list(df['Interested subjects_code'].unique())
ISC = dict(zip(Interested_subjects,Interested_subjects_code))

interested_career_area = list(df['interested career area '].unique())
print(interested_career_area)
interested_career_area_code = list(df['interested career area _code'].unique())
ICA = dict(zip(interested_career_area,interested_career_area_code))

Typeofcompany = list(df['Type of company want to settle in?'].unique())
print(Typeofcompany)
Typeofcompany_code = list(df['Type of company want to settle in?_code'].unique())
TOCO = dict(zip(Typeofcompany,Typeofcompany_code))

Interested_Books = list(df['Interested Type of Books'].unique())
print(Interested_subjects)
Interested_Books_code = list(df['Interested Type of Books_code'].unique())
IB = dict(zip(Interested_Books,Interested_Books_code))

Range_dict = {"poor": 0, "medium": 1, "excellent": 2}
print(Range_dict)

f =[]
A = 'r programming'
clms = ['r programming',0]
for i in clms:
  for key in C:
    if(i==key):
      i = C[key]
      f.append(i)
print(f)

C = dict(zip(Certifi,certi_code))
  
print(C)

import numpy as np
array = np.array([1,2,3,4])
array.reshape(-1,1)

'''for i in clms:
  if(i==(for key in C)):
    print(i)'''

import gradio as gr
def inputlist(Name,Contact_Number,Email_address,Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points, self_learning_capability, 
       Extra_courses_did, Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert, reading_and_writing_skills,
       memory_capability_score, smart_or_hard_work, Magement_or_Techinical,
       Interested_subjects, Interested_Type_of_Books,certifications, workshops, Type_of_company_want_to_settle_in, interested_career_area ):
  #1,1,1,1,'Yes','Yes''Yes''Yes''Yes',"poor","poor","Smart worker", "Management","programming","Series","information security"."testing","BPA","testing"
  Afeed = [Logical_quotient_rating, coding_skills_rating, hackathons, public_speaking_points]

  input_list_col = [self_learning_capability,Extra_courses_did,Taken_inputs_from_seniors_or_elders,worked_in_teams_ever,Introvert,reading_and_writing_skills,memory_capability_score,smart_or_hard_work,Magement_or_Techinical,Interested_subjects,Interested_Type_of_Books,certifications,workshops,Type_of_company_want_to_settle_in,interested_career_area]
  feed = []
  K=0
  j=0
  for i in input_list_col:
    if(i=='Yes'):
      j=2
      feed.append(j)
       
      print("feed 1",i)
    
    elif(i=="No"):
      j=3
      feed.append(j)
       
      print("feed 2",j)
    
    elif(i=='Management'):
      j=1
      k=0
      feed.append(j)
      feed.append(K)
       
      print("feed 10,11",i,j,k)

    elif(i=='Technical'):
      j=0
      k=1
      feed.append(j)
      feed.append(K)
       
      print("feed 12,13",i,j,k)

    elif(i=='Smart worker'):
      j=1
      k=0
      feed.append(j)
      feed.append(K)
       
      print("feed 14,15",i,j,k)

    elif(i=='Hard Worker'):
      j=0
      k=1
      feed.append(j)
      feed.append(K)
      print("feed 16,17",i,j,k)
    
    else:
      for key in Range_dict:
        if(i==key):
          j = Range_dict[key]
          feed.append(j)
         
          print("feed 3",i,j)

      for key in C:
        if(i==key):
          j = C[key]
          feed.append(j)
          
          print("feed 4",i,j)
      
      for key in W:
        if(i==key):
          j = W[key]
          feed.append(j)
          
          print("feed 5",i,j)
      
      for key in ISC:
        if(i==key):
          j = ISC[key]
          feed.append(j)
          
          print("feed 6",i,j)

      for key in ICA:
        if(i==key):
          j = ICA[key]
          feed.append(j)
          
          print("feed 7",i,j)

      for key in TOCO:
        if(i==key):
          j = TOCO[key]
          feed.append(j)
          
          print("feed 8",i,j)

      for key in IB:
        if(i==key):
          j = IB[key]
          feed.append(j)
          
          print("feed 9",i,j)

   
       
  t = Afeed+feed    
  output = dtree.predict([t])

 

  
  return(output)
  
  

iface = gr.Interface(
    inputlist, 
    [
     gr.inputs.Textbox(default=None, label = "Name"),
     gr.inputs.Textbox(default=None, label = "Email_addres"),
     gr.inputs.Number(default=None, label = "Contact_Number"),
     gr.inputs.Radio(['1','2','3','4','5','6','7','8','9','10'], label = "Logical_quotient_rating"),
     gr.inputs.Radio(['1','2','3','4','5','6','7','8','9','10'], label = "coding_skills_rating"),
     gr.inputs.Radio(['1','2','3','4','5','6','7','8','9','10'], label = "hackathons"),
     gr.inputs.Radio(['1','2','3','4','5','6','7','8','9','10'], label = "public_speaking_points"),
     gr.inputs.Radio(['Yes', 'No'], label = "self_learning_capability"),
     gr.inputs.Radio(['Yes', 'No'], label = "Extra_courses_did"),
     gr.inputs.Radio(['Yes', 'No'], label = "Taken_inputs_from_seniors_or_elders"),
     gr.inputs.Radio(['Yes', 'No'], label = "worked_in_teams_ever"),
     gr.inputs.Radio(['Yes', 'No'], label = "Introvert"),
     gr.inputs.Radio(['poor','medium','excellent'], label= "reading_and_writing_skills"),
     gr.inputs.Radio(['poor','medium','excellent'], label= "memory_capability_score"),
     gr.inputs.Radio(['Smart worker', 'Hard Worker'],label= "smart_or_hard_work"),
     gr.inputs.Radio(['Management', 'Technical'],label= "Magement_or_Techinical"),
     gr.inputs.Dropdown(['programming', 'Management', 'data engineering', 'networks', 'Software Engineering', 'cloud computing', 'parallel computing', 'IOT', 'Computer Architecture', 'hacking'], label= "Interested_subjects"),
     gr.inputs.Dropdown(['Series', 'Autobiographies', 'Travel', 'Guide', 'Health', 'Journals', 'Anthology', 'Dictionaries', 'Prayer books', 'Art', 'Encyclopedias', 'Religion-Spirituality', 'Action and Adventure', 'Comics', 'Horror', 'Satire', 'Self help', 'History', 'Cookbooks', 'Math', 'Biographies', 'Drama', 'Diaries', 'Science fiction', 'Poetry', 'Romance', 'Science', 'Trilogy', 'Fantasy', 'Childrens', 'Mystery'], label= "Interested_Type_of_Books"),
     gr.inputs.Dropdown(['information security', 'shell programming', 'r programming', 'distro making', 'machine learning', 'full stack', 'hadoop', 'app development', 'python'], label= "certifications"),
     gr.inputs.Dropdown(['Testing', 'database security', 'game development', 'data science', 'system designing', 'hacking', 'cloud computing', 'web technologies'], label= "workshops"),
     gr.inputs.Dropdown(['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'], label= "Type_of_company_want_to_settle_in"),
     gr.inputs.Dropdown(['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'], label= "interested_career_area "),

     
    ],
    "text",title="Career Prediction ",
    description="                         This application takes input from user about various feilds and predicts the more likely carrer area for the user :)",)

if __name__ == "__main__":
    iface.launch(debug = True)

o = inputlist(1,1,1,1,'Yes','Yes','Yes','Yes','Yes','poor','poor','Smart worker','Management','programming','Series','information security','Testing','BPA','testing')
print (o)

print(o)

1,1,1,1,'Yes','Yes','Yes','Yes','Yes','poor','poor','Smart worker','Management','programming','Series','information security','testing','BPA','testing'

