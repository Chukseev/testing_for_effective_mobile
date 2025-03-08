from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyForm

def main(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()

    return render(request, 'mainapp/index.html', {'form': form})

def success(request):
    if request.method == "POST":
        return render(request, 'mainapp/success.html')
    else:
        return redirect('mainapp:main')