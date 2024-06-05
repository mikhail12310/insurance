# from django.shortcuts import render, HttpResponse
# import joblib
# import sklearn

# model=joblib.load('random_forest.pkl')

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# import joblib
# import numpy as np

# def predict_insurance(request):
#     if request.method == 'POST':

#         model = joblib.load('random_forest.pkl')


#         sex= 1 if request.POST.get('sex') == 'male' else 0
#         age = float(request.POST.get('age'))
#         bmi = float(request.POST.get('bmi'))
#         children = int(request.POST.get('children'))
#         smoker = 1 if request.POST.get('smoker') == 'yes' else 0
#         if request.POST.get('region')=='southwest':
#             region=1 
#         elif request.POST.get('region')=='southeast':
#             region=2
#         elif request.POST.get('region')=='northwest':
#             region=3
#         else:
#             region=4
  
#         input_data = np.array([[age, sex, bmi, children, smoker, region]])
#         predicted_premium = model.predict(input_data)
#         return render(request, 'result.html', {'predicted_premium': predicted_premium})

#     else:
#         return render(request, 'idex.html')

def index(request):
    return render(request,'index.html')

from django.shortcuts import render
import joblib
import numpy as np

def predict_insurance(request):
    if request.method == 'POST':
        model = joblib.load('random_forest.pkl')

        sex = 1 if request.POST.get('sex') == 'male' else 0
        age = float(request.POST.get('age'))
        bmi = float(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = 1 if request.POST.get('smoker') == 'yes' else 0
        region_map = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}
        region = region_map.get(request.POST.get('region'), 0)
        input_data = np.array([[age, sex, bmi, children, smoker, region]])
        pred = model.predict(input_data)
        pred_original_scale = np.expm1(pred)
        return render(request, 'result.html', {'predicted_premium': pred_original_scale})

    else:

        return render(request, 'index.html')
