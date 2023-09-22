from django.shortcuts import render
import pandas as pd
import pickle
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        input_data = pd.DataFrame({'Subscription_Length_Months':[0],
       'Monthly_Bill':[0], 'Total_Usage_GB':[0], 'Total_bill':[0], 'Cost_per_GB':[0],
       'scaled_subscription_length':[0], 'Female':[0], 'Male':[0], 'Chicago':[0], 'Houston':[0],
       'Los Angeles':[0], 'Miami':[0], 'New York':[0], '0-18':[0], '19-30':[0], '31-45':[0], '46-60':[0],
       '61+':[0]})
        
        input_dict = dict(request.POST)

        print(input_dict)

        age = request.POST['age']
        gender = request.POST['gender']
        location = request.POST['Location']
        sub_length = request.POST['Subscription_Length_Months']
        usage = request.POST['Total_Usage_GB']
        monthly_bill = request.POST.get('Monthly_Bill')
        print(monthly_bill)
        total_bill = int(monthly_bill) * int(sub_length)
        cost_per_gb = int(monthly_bill) / int(usage)

        if int(age)<=18:
            input_data.loc[0, '0-18'] = 1 
        elif int(age) in range(18,31):
            input_data.loc[0, '19-30'] = 1 
        elif int(age) in range(31,46):
            input_data.loc[0,'31-45'] = 1
        elif int(age) in range(46,60):
            input_data.loc[0,'46-60'] = 1
        elif int(age)>=61:
            input_data.loc[0,'61+'] = 1
        else:
            print('wtf bro')

        if location=='Los Angeles':
            input_data.loc[0,'Los Angeles'] = 1
        elif location=='New York':
            input_data.loc[0,'New York'] = 1
        elif location=='Miami':
            input_data.loc[0,'Miami'] = 1
        elif location=='Chicago':
            input_data.loc[0,'Chicago'] = 1
        elif location=='Houston':
            input_data.loc[0,'Houston'] = 1
        else:
            pass

        if gender=='male':
            input_data.loc[0,'Male'] = 1
        else:
            input_data.loc[0,'Female'] = 1

        input_data.loc[0,'Subscription_Length_Months'] = sub_length
        input_data.loc[0,'Total_Usage_GB'] = usage
        input_data.loc[0,'Total_bill'] = total_bill
        input_data.loc[0,'Cost_per_GB'] = cost_per_gb
        input_data.loc[0,'Monthly_Bill'] = monthly_bill




        print(input_data.head())
        print(input_data.isna())

        with open('decision_tree.pth','rb') as file:
            dt_model = pickle.load(file)
        
        output = dt_model.predict(input_data)

        if output[0]==0:
            result = 'Churn'
        else:
            result = 'No Churn'
        
        response_data = {
            'result': result
        }
        
        return JsonResponse(response_data)


    return render(request, 'index.html')