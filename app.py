import streamlit as st
import numpy as np
import pandas as pd
import datetime

# Function to perform analysis
def perform_analysis(df):
    # Get current date and time
    current_datetime = datetime.datetime.now()
    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%m-%d-%Y %H:%M:%S")
    # gender data
    female_count = float(df[df['Attribute']=='Female']['ICount'])
    female_percentage = str(df[df['Attribute']=='Female']['Percentage']).split()[1]
    female_percentage = float(female_percentage[:len(female_percentage)-1])
    male_count = float(df[df['Attribute']=='Male']['ICount'])
    male_percentage = str(df[df['Attribute']=='Male']['Percentage']).split()[1]
    male_percentage = float(male_percentage[:len(male_percentage)-1])
    other_count = float(df[df['Attribute']=='Other']['ICount'])
    other_percentage = str(df[df['Attribute']=='Other']['Percentage']).split()[1]
    other_percentage = float(other_percentage[:len(other_percentage)-1])
    total_count = df[df['Attribute']=='Total'].loc[6,'ICount']
    no_gender_ans_count = total_count - (male_count+female_count+other_count)
    no_gender_ans_perc = np.round(no_gender_ans_count * 100/total_count)
    # diversity data
    minority_1 = "Hispanic or Latino - A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race."
    minority_2 = "Black or African American (not Hispanic or Latino) - A person having origins in any of the black racial groups of Africa."
    minority_3 = "Native Hawaiian or Other Pacific Islander (not Hispanic or Latino) - A person having origins in any of the peoples of Hawaii, Guam, Samoa, or other Pacific Islands."
    minority_4 = "American Indian or Alaska Native (not Hispanic or Latino) - A person having origins in any of the original peoples of North and South America (including Central America ), and who maintain tribal affiliation or community attachment."
    min1_count = float(df[df['Attribute']==minority_1]['ICount'])
    min1_percentage = str(df[df['Attribute']==minority_1]['Percentage']).split()[1]
    min1_percentage = float(min1_percentage[:len(min1_percentage)-1])
    min2_count = float(df[df['Attribute']==minority_2]['ICount'])
    min2_percentage = str(df[df['Attribute']==minority_2]['Percentage']).split()[1]
    min2_percentage = float(min2_percentage[:len(min2_percentage)-1])
    min3_count = float(df[df['Attribute']==minority_3]['ICount'])
    min3_percentage = str(df[df['Attribute']==minority_3]['Percentage']).split()[1]
    min3_percentage = float(min3_percentage[:len(min3_percentage)-1])
    min4_count = float(df[df['Attribute']==minority_4]['ICount'])
    min4_percentage = str(df[df['Attribute']==minority_4]['Percentage']).split()[1]
    min4_percentage = float(min4_percentage[:len(min4_percentage)-1])
    # disability data
    dis_str = 'Yes, I have a disability, or have had one in the past'
    non_dis_str = 'No, I do not have a disability and have not had one in the past'
    dis_count = float(df[df['Attribute']==dis_str]['ICount'])
    dis_percentage = str(df[df['Attribute']==dis_str]['Percentage']).split()[1]
    dis_percentage = float(dis_percentage[:len(dis_percentage)-1])
    ndis_count = float(df[df['Attribute']==non_dis_str]['ICount'])
    ndis_percentage = str(df[df['Attribute']==non_dis_str]['Percentage']).split()[1]
    ndis_percentage = float(ndis_percentage[:len(ndis_percentage)-1])
    no_dis_ans_count = total_count - (dis_count+ndis_count)
    no_dis_ans_perc = np.round(no_dis_ans_count*100/total_count)
    # veteran data
    p_str = 'I identify as one or more of the classifications of protected veteran listed above'
    np_str = 'I am not a protected veteran'
    p_count = float(df[df['Attribute']==p_str]['ICount'])
    p_percentage = str(df[df['Attribute']==p_str]['Percentage']).split()[1]
    p_percentage = float(p_percentage[:len(p_percentage)-1])
    np_count = float(df[df['Attribute']==np_str]['ICount'])
    np_percentage = str(df[df['Attribute']==np_str]['Percentage']).split()[1]
    np_percentage = float(np_percentage[:len(np_percentage)-1])
    no_p_ans_count = total_count - (p_count+np_count)
    no_p_ans_perc = np.round(no_p_ans_count*100/total_count)
    req = {'NYU EEO/Affirmative Action Voluntary Self Identification Form':['-------- GENDER DATA --------','Male', 'Female','Other','No Answer','-------- DIVERSITY DATA --------',
                   minority_1,minority_2,minority_3,minority_4,'-------- DISABILITY DATA --------',dis_str,non_dis_str,'No Answer','-------- VETERAN DATA --------',
                   p_str,np_str,'No Answer','-------- TOTAL COUNT --------','Total Count','-------- DATE AND TIME --------','Date and Time'],
       'Count':['',male_count,female_count,other_count,no_gender_ans_count,'', min1_count,min2_count,min3_count,min4_count,'',dis_count,ndis_count,no_dis_ans_count,'',p_count,np_count,no_p_ans_count,'',total_count,'',formatted_datetime],
       'Percentage(%)':['',male_percentage,female_percentage,other_percentage,no_gender_ans_perc,'',min1_percentage,min2_percentage,min3_percentage,min4_percentage,'',dis_percentage,ndis_percentage,no_dis_ans_perc,'',p_percentage,np_percentage,no_p_ans_perc,'','','','']}

    data = pd.DataFrame(req)
    return data

   
# Streamlit app
def main():
    st.title("Diversity Statistics")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV/Excel file", type=["csv"])

    dep_name = st.text_input("Enter Department Name:")

    job_id = st.text_input("Enter Interfolio Job ID:")

    if uploaded_file is not None:
        # Read CSV file
        df = pd.read_csv(uploaded_file,names=['Attribute','ICount','Percentage'])

        # Display uploaded data
        st.write("Uploaded Data:")
        st.write(df)

        # Perform analysis
        analysis_result = perform_analysis(df)

        # Display analysis result
        st.write("Analysis Result:")
        st.write(analysis_result)

        # Download button for analysis result
        st.download_button(
            label="Download Analysis Result",
            data=analysis_result.to_csv(index=False).encode(),
            file_name= str(dep_name) + "_ID-" + str(job_id) + "_demography_analysis_result.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()

# import streamlit as st
# import numpy as np
# import pandas as pd

# # Function to perform analysis
# def perform_analysis(df):
#     # gender data
#     female_count = float(df[df['Attribute']=='Female']['ICount'])
#     female_percentage = str(df[df['Attribute']=='Female']['Percentage']).split()[1]
#     female_percentage = float(female_percentage[:len(female_percentage)-1])
#     male_count = float(df[df['Attribute']=='Male']['ICount'])
#     male_percentage = str(df[df['Attribute']=='Male']['Percentage']).split()[1]
#     male_percentage = float(male_percentage[:len(male_percentage)-1])
#     other_count = float(df[df['Attribute']=='Other']['ICount'])
#     other_percentage = str(df[df['Attribute']=='Other']['Percentage']).split()[1]
#     other_percentage = float(other_percentage[:len(other_percentage)-1])
#     total_count = df[df['Attribute']=='Total'].loc[6,'ICount']
#     no_gender_ans_count = total_count - (male_count+female_count+other_count)
#     no_gender_ans_perc = np.round(no_gender_ans_count * 100/total_count)
#     # diversity data
#     minority_1 = "Hispanic or Latino - A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin regardless of race."
#     minority_2 = "Black or African American (not Hispanic or Latino) - A person having origins in any of the black racial groups of Africa."
#     minority_3 = "Native Hawaiian or Other Pacific Islander (not Hispanic or Latino) - A person having origins in any of the peoples of Hawaii, Guam, Samoa, or other Pacific Islands."
#     minority_4 = "American Indian or Alaska Native (not Hispanic or Latino) - A person having origins in any of the original peoples of North and South America (including Central America ), and who maintain tribal affiliation or community attachment."
#     min1_count = float(df[df['Attribute']==minority_1]['ICount'])
#     min1_percentage = str(df[df['Attribute']==minority_1]['Percentage']).split()[1]
#     min1_percentage = float(min1_percentage[:len(min1_percentage)-1])
#     min2_count = float(df[df['Attribute']==minority_2]['ICount'])
#     min2_percentage = str(df[df['Attribute']==minority_2]['Percentage']).split()[1]
#     min2_percentage = float(min2_percentage[:len(min2_percentage)-1])
#     min3_count = float(df[df['Attribute']==minority_3]['ICount'])
#     min3_percentage = str(df[df['Attribute']==minority_3]['Percentage']).split()[1]
#     min3_percentage = float(min3_percentage[:len(min3_percentage)-1])
#     min4_count = float(df[df['Attribute']==minority_4]['ICount'])
#     min4_percentage = str(df[df['Attribute']==minority_4]['Percentage']).split()[1]
#     min4_percentage = float(min4_percentage[:len(min4_percentage)-1])
#     # disability data
#     dis_str = 'Yes, I have a disability, or have had one in the past'
#     non_dis_str = 'No, I do not have a disability and have not had one in the past'
#     dis_count = float(df[df['Attribute']==dis_str]['ICount'])
#     dis_percentage = str(df[df['Attribute']==dis_str]['Percentage']).split()[1]
#     dis_percentage = float(dis_percentage[:len(dis_percentage)-1])
#     ndis_count = float(df[df['Attribute']==non_dis_str]['ICount'])
#     ndis_percentage = str(df[df['Attribute']==non_dis_str]['Percentage']).split()[1]
#     ndis_percentage = float(ndis_percentage[:len(ndis_percentage)-1])
#     no_dis_ans_count = total_count - (dis_count+ndis_count)
#     no_dis_ans_perc = np.round(no_dis_ans_count*100/total_count)
#     # veteran data
#     p_str = 'I identify as one or more of the classifications of protected veteran listed above'
#     np_str = 'I am not a protected veteran'
#     p_count = float(df[df['Attribute']==p_str]['ICount'])
#     p_percentage = str(df[df['Attribute']==p_str]['Percentage']).split()[1]
#     p_percentage = float(p_percentage[:len(p_percentage)-1])
#     np_count = float(df[df['Attribute']==np_str]['ICount'])
#     np_percentage = str(df[df['Attribute']==np_str]['Percentage']).split()[1]
#     np_percentage = float(np_percentage[:len(np_percentage)-1])
#     no_p_ans_count = total_count - (p_count+np_count)
#     no_p_ans_perc = np.round(no_p_ans_count*100/total_count)
#     req = {'NYU EEO/Affirmative Action Voluntary Self Identification Form':['-------- GENDER DATA --------','Male', 'Female','Other','No Answer','-------- DIVERSITY DATA --------',
#                    minority_1,minority_2,minority_3,minority_4,'-------- DISABILITY DATA --------',dis_str,non_dis_str,'No Answer','-------- VETERAN DATA --------',
#                    p_str,np_str,'No Answer','-------- TOTAL COUNT --------','Total Count'],
#        'Count':['',male_count,female_count,other_count,no_gender_ans_count,'', min1_count,min2_count,min3_count,min4_count,'',dis_count,ndis_count,no_dis_ans_count,'',p_count,np_count,no_p_ans_count,'',total_count],
#        'Percentage(%)':['',male_percentage,female_percentage,other_percentage,no_gender_ans_perc,'',min1_percentage,min2_percentage,min3_percentage,min4_percentage,'',dis_percentage,ndis_percentage,no_dis_ans_perc,'',p_percentage,np_percentage,no_p_ans_perc,'','']}

#     data = pd.DataFrame(req)
#     return data

   
# # Streamlit app
# def main():
#     st.title("Diversity Statistics")

#     # Upload CSV file
#     uploaded_file = st.file_uploader("Upload a CSV/Excel file", type=["csv"])

#     dep_name = st.text_input("Enter Department Name:")

#     job_id = st.text_input("Enter Interfolio Job ID:")

#     if uploaded_file is not None:
#         # Read CSV file
#         df = pd.read_csv(uploaded_file,names=['Attribute','ICount','Percentage'])

#         # Display uploaded data
#         st.write("Uploaded Data:")
#         st.write(df)

#         # Perform analysis
#         analysis_result = perform_analysis(df)

#         # Display analysis result
#         st.write("Analysis Result:")
#         st.write(analysis_result)

#         # Download button for analysis result
#         st.download_button(
#             label="Download Analysis Result",
#             data=analysis_result.to_csv(index=False).encode(),
#             file_name= str(dep_name) + "_ID-" + str(job_id) + "_demography_analysis_result.csv",
#             mime="text/csv"
#         )

# if __name__ == "__main__":
#     main()
