from django.shortcuts import render

from joblib import load

model = load('./../savedModels/model.joblib')


def members(request):
    # Initialize the result variable
    y_pred = None


    # Check if the request method is POST
    if request.method == 'POST':
        # Get input data from the form
        sepal_length = float(request.POST.get("sepal_length", 0))
        sepal_width = float(request.POST.get("sepal_width", 0))
        petal_length = float(request.POST.get("petal_length", 0))
        petal_width = float(request.POST.get("petal_width", 0))

         # Perform prediction using the loaded model
        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        # Interpret the prediction result
        if y_pred[0] == 0:
            y_pred = "Setosa"
        elif y_pred[0] == 1:
            y_pred = "Versicolor"
        else:
            y_pred = "Virginica"
        # Render the template with the prediction result (if available)
    return render(request, 'myfirst.html', {'result': y_pred})

       


    return render(request, 'myfirst.html', {})
