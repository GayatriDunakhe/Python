from django.shortcuts import render

def check_age(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        if age >= 18:
            message = "You are eligible to vote!"
        else:
            message = "You are not eligible to vote."
        return render(request, 'result.html', {'message': message})
    return render(request, 'check_age.html')