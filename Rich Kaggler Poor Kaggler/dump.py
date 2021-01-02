#Q10

data['Q10_Google'] = data['Q10_Part_10'] + data['Q10_Part_11']
data['Q10_Amazon'] = data['Q10_Part_9'] + data['Q10_Part_8']
data['Q10_Microsoft'] = data['Q10_Part_3']
data['Q10_Other'] = data['Q10_OTHER']+ data['Q10_Part_1'] + data['Q10_Part_4'] + data['Q10_Part_5'] + data['Q10_Part_6'] + data['Q10_Part_7']
data['Q10_None'] = data['Q10_Google'] + data['Q10_Amazon'] + data['Q10_Microsoft'] + data['Q10_Other']

data['Q10_GandM'] = data['Q10_Google'] * data['Q10_Microsoft']
data['Q10_GandA'] = data['Q10_Google'] * data['Q10_Amazon']
data['Q10_MandA'] = data['Q10_Microsoft'] * data['Q10_Amazon']
data['Q10_GandMandA'] = data['Q10_Microsoft'] * data['Q10_Amazon'] * data['Q10_Google']

g = dict(data['Q10_Google'].value_counts())
google_val = list(g.values())[1]
google_percent = round((google_val/len(data))*100,2)
m = dict(data['Q10_Microsoft'].value_counts())
micro_val = list(m.values())[1]
micro_percent = round((micro_val/len(data))*100,2)
a = dict(data['Q10_Amazon'].value_counts())
amazon_val = list(a.values())[1]
amazon_percent = round((amazon_val/len(data))*100)

g_ai = dict(data['Q10_Part_10'].value_counts())
g_ai_val = list(g_ai.values())[1]
g_ai_percent = round((g_ai_val/len(data))*100,2)

g_data = dict(data['Q10_Part_11'].value_counts())
g_data_val = list(g_data.values())[1]
g_data_percent = round((g_data_val/len(data))*100,2)

m_azure = dict(data['Q10_Part_3'].value_counts())
micro_azure_val = list(m_azure.values())[1]
micro_azure_percent = round((micro_azure_val/len(data))*100,2)

a_sage = dict(data['Q10_Part_8'].value_counts())
amazon_sage_val = list(a_sage.values())[1]
amazon_sage_percent = round((amazon_sage_val/len(data))*100)

a_emr = dict(data['Q10_Part_9'].value_counts())
amazon_emr_val = list(a_emr.values())[1]
amazon_emr_percent = round((amazon_emr_val/len(data))*100)



fig = make_subplots(rows=1, cols=2)
fig.add_trace(
    go.Bar(y=['Google','Microsoft','Amazon'], x=[google_percent,micro_percent,amazon_percent],
            hovertext=['27% market share', '24% market share', '19% market share'],orientation='h'),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
            x=[g_ai_percent, g_data_percent,micro_azure_percent,amazon_sage_percent,amazon_emr_percent],
            y=['Google Cloud AI Platform Notebooks','Google Cloud Datalab Notebooks','Azure Notebooks','Amazon Sagemaker Studio','Amazon EMR Notebooks'],
            orientation='h'),
    row=1, col=2
)

fig.update_layout(height=600, width=1000, title_text="Side By Side Subplots",showlegend=False)
fig.show()

data['Q10_GandM'].value_counts()
data['Q10_MandA'].value_counts()
data['Q10_Google'].value_counts()
data['Q10_Amazon'].value_counts()
data['Q10_Microsoft'].value_counts();

g = dict(data_professionals['Q26_Google'].value_counts())
google_val = list(g.values())[1]
google_percent = round((google_val/len(data_professionals))*100,2)
m = dict(data_professionals['Q26_Microsoft'].value_counts())
micro_val = list(m.values())[1]
micro_percent = round((micro_val/len(data_professionals))*100,2)
a = dict(data_professionals['Q26_Amazon'].value_counts())
amazon_val = list(a.values())[1]
amazon_percent = round((amazon_val/len(data_professionals))*100)

fig = make_subplots(rows=1, cols=2)
fig.add_trace(
    go.Bar(y=['Google','Microsoft','Amazon'], x=[google_percent,micro_percent,amazon_percent],
            hovertext=['27% market share', '24% market share', '19% market share'],orientation='h'),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
            x=[g_ai_percent, g_data_percent,micro_azure_percent,amazon_sage_percent,amazon_emr_percent],
            y=['Google Cloud AI Platform Notebooks','Google Cloud Datalab Notebooks','Azure Notebooks','Amazon Sagemaker Studio','Amazon EMR Notebooks'],
            orientation='h'),
    row=1, col=2
)

fig.update_layout(height=600, width=1000, title_text="Side By Side Subplots",showlegend=False)
fig.show()
a_ec2 = dict(data_professionals['Q27_A_Part_1'].value_counts())
a_ec2_val = list(a_ec2.values())[1]
a_ec2_percent = round((a_ec2_val/len(data_professionals))*100,2)

a_lambda = dict(data_professionals['Q27_A_Part_2'].value_counts())
a_lambda_val = list(a_lambda.values())[1]
a_lambda_percent = round((a_lambda_val/len(data_professionals))*100,2)

a_elastic = dict(data_professionals['Q27_A_Part_3'].value_counts())
a_elastic_val = list(a_elastic.values())[1]
a_elastic_percent = round((a_elastic_val/len(data_professionals))*100,2)

m_service = dict(data_professionals['Q27_A_Part_4'].value_counts())
m_service_val = list(m_service.values())[1]
m_service_percent = round((m_service_val/len(data_professionals))*100,2)

m_container = dict(data_professionals['Q27_A_Part_5'].value_counts())
m_container_val = list(m_container.values())[1]
m_container_percent = round((m_container_val/len(data_professionals))*100,2)

m_functions = dict(data_professionals['Q27_A_Part_6'].value_counts())
m_functions_val = list(m_functions.values())[1]
m_functions_percent = round((m_functions_val/len(data_professionals))*100,2)

g_compute = dict(data_professionals['Q27_A_Part_7'].value_counts())
g_compute_val = list(g_compute.values())[1]
g_compute_percent = round((g_compute_val/len(data_professionals))*100)

g_functions = dict(data_professionals['Q27_A_Part_8'].value_counts())
g_functions_val = list(g_functions.values())[1]
g_functions_percent = round((g_functions_val/len(data_professionals))*100)

g_run = dict(data_professionals['Q27_A_Part_9'].value_counts())
g_run_val = list(g_run.values())[1]
g_run_percent = round((g_run_val/len(data_professionals))*100)

g_app = dict(data_professionals['Q27_A_Part_10'].value_counts())
g_app_val = list(g_app.values())[1]
g_app_percent = round((g_app_val/len(data_professionals))*100)
x = [a_ec2_percent,a_lambda_percent,a_elastic_percent,m_service_percent,m_container_percent,m_functions_percent,g_compute_percent,g_functions_percent,g_run_percent,g_app_percent]
y = []
data['Q27_Google'] = data['Q27_A_Part_7'] + data['Q27_A_Part_8'] + data['Q27_A_Part_9']  + data['Q27_A_Part_10']
data['Q27_Amazon'] = data['Q27_A_Part_1'] + data['Q27_A_Part_2'] + data['Q27_A_Part_3']
data['Q27_Microsoft'] = data['Q27_A_Part_5'] + data['Q27_A_Part_4'] + data['Q27_A_Part_6']
data['Q27_Other'] = data['Q27_A_OTHER']   

data['Q28_Google'] = data['Q28_A_Part_6'] + data['Q28_A_Part_7'] + data['Q28_A_Part_8'] + data['Q28_A_Part_7'] 
data['Q28_Amazon'] = data['Q28_A_Part_1'] + data['Q28_A_Part_2'] + data['Q28_A_Part_3']
data['Q28_Microsoft'] = data['Q28_A_Part_5'] + data['Q28_A_Part_4']
data['Q28_Other'] = data['Q28_A_OTHER']   
data['Q29_Google'] = data['Q29_A_Part_14'] + data['Q29_A_Part_15'] + data['Q29_A_Part_16'] 
data['Q29_Amazon'] = data['Q29_A_Part_11'] + data['Q29_A_Part_12'] + data['Q29_A_Part_13']
data['Q29_Microsoft'] = data['Q29_A_Part_8'] + data['Q29_A_Part_9'] + data['Q29_A_Part_9']
data['Q29_Other'] = data['Q29_A_Part_1'] + data['Q29_A_Part_2'] + data['Q29_A_Part_3'] + data['Q29_A_Part_4'] + data['Q29_A_Part_5'] + data['Q29_A_Part_6'] + data['Q29_A_Part_7']+ data['Q29_A_OTHER']   
data['Q31_Google'] = data['Q31_A_Part_3'] 
data['Q31_Amazon'] = data['Q31_A_Part_1'] 
data['Q31_Microsoft'] = data['Q31_A_Part_2']
data['Q31_Other'] = data['Q31_A_Part_4'] + data['Q31_A_Part_5'] + data['Q31_A_Part_6'] + data['Q31_A_Part_7'] + data['Q31_A_Part_8'] + data['Q31_A_Part_9'] + data['Q31_A_Part_10']+data['Q31_A_Part_11']+ data['Q31_A_Part_12']+data['Q31_A_Part_13']+ data['Q31_A_OTHER']   

cols = list(data.columns)
for col in cols:
    
      if 'Q25' in col:
            print(col)
