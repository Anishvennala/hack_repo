#Intro & starting info
print('Welcome to the (unofficial) Ontario Covid-19 Screening-Analysis Machine.')
lastDate = input('What is the date at the time of taking this diagnostic?   \n(DD/MM/YYYY)  \n')

#Screening questions
q1 = input('Do you currently have any of the following symptoms (unrelated to prior causes or conditions):    \n-Fever of 37.8°C or more    \n-Coughing or \"Barking\" cough    \n-Shortness of breath/difficulty breathing    \n-Decreased or lost sense of smell and/or taste    \nAnswer "y" for Yes and "n" for No.    \n')
while q1 != 'y' and q1 != 'n' :
    q1 = input('Sorry, you mistyped. Answer "y" for Yes and "n" for No.    \n')
if q1 == 'y' :
  q1 = True
elif q1 == 'n' :
  q1 = False

q2 = int(input('How many of the following symptoms do you currently have (unrelated to prior causes or conditions):    \n-Sore throat, pain when swallowing    \n-Runny or congested nose    \n-Unusual or long lasting headache    \n-Nausea and/or vomiting and/or diarrhea    \n-Fatigue, lack of energy    \nAnswer with numbers 0-6    \n'))
#q2 has more than just two possibilities (T/F), so it has been split into two variables
while q2 > 6 or q2 < 0 :
  #q2 is whether or not you have any symptoms at all, q2i is only one, q2ii it 2+
  q2 = int(input('Sorry, you mistyped. Answer with numbers 0-6    \n'))
if q2 == 0 :
  q2i = False
  q2ii = False
  q2 = False
elif q2 == 1 :
  q2i = True
  q2ii = False
  q2 = True
elif q2 > 1 :
  q2i = False
  q2ii = True
  q2 = True

q3 = input('Have you travelled outside of the country in the last 14 days?    \nAnswer "y" for Yes and "n" for No.    \n')
while q3 != 'y' and q3 != 'n' :
    q3 = input('Sorry, you mistyped. Answer "y" for Yes and "n" for No.    \n')
if q3 == 'y' :
  q3 = True
elif q3 == 'n' :
  q3 = False

q4 = input('Have you been identified as a close contact to someone who currently has Covid-19 by a public health unit?    \nAnswer with "y" for Yes and "n" for No.    \n')
while q4 != 'y' and q4 != 'n' :
    q4 = input('Sorry, you mistyped. Answer "y" for Yes and "n" for No.    \n')
if q4 == 'y' :
  q4 = True
elif q4 == 'n' :
  q4 = False

q5 = input('Have you been told to isolate by a doctor, health care provider, or public health unit?    \nAnswer with "y" for Yes and "n" for No.    \n')
while q5 != 'y' and q5 != 'n' :
    q5 = input('Sorry, you mistyped. Answer "y" for Yes and "n" for No.    \n')
if q5 == 'y' :
  q5 = True
elif q5 == 'n' :
  q5 = False

q6 = input('Have you recieved a COVID Alert exposure notification on your cell phone in the last 14 days?    \nAnswer with "y" for Yes and "n" for No.    \n')
while q6 != 'y' and q6 != 'n' :
    q6 = input('Sorry, you mistyped. Answer "y" for Yes and "n" for No.    \n')
if q6 == 'y' :
  q6 = True
elif q6 == 'n' :
  q6 = False

#Results of answers
if q1 or q2 or q3 or q4 or q5 or q6 :
  riskRes = ', YOU ARE AT RISK OF HAVING CONTRACTED COVID-19.    \nContact your school or workplace about your result.'
  
else :
  riskRes = ', You are NOT at risk.'

print('As of ' + lastDate + riskRes)

#Whether the user should isolate
if q1 or q2ii:
  isoRes = 'Stay home unless being tested or in an emergency.'

elif q3 or q4 or q5 or q6 :
  isoRes = 'Stay home for 14 days unless being tested or in an emergency.'

elif q2i :
  isoRes = 'Stay home for 24 hours. If your condition improves, no further action is required and there is no need to get tested.'

print(isoRes)

#Whether to call a doctor or health care provider
if q1 or q2ii or q3 or q4 or q5 or q6 :
  docRes = 'Speak to your doctor or healthcare provider about your result.'

print(docRes)

print('Thank you for using the (unofficial) Ontario Covid-19 Screening-Analysis Machine.    \nRemember that it is important to do self-checkups regularly.')