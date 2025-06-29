from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm


# Create your views here.
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')

            if Student.objects.filter(name=name, email=email).exists():
                form.add_error(None, 'Student with this name and email already exists')
            else:
                form.save()
                form = StudentForm()  # Clear the form after successful save
    else:
        form = StudentForm()

    stud = Student.objects.all()
    return render(request, 'add.html', {'formss': form, 'stud': stud})

def delete(request,id):
    stud=get_object_or_404(Student,pk=id)
    stud.delete()
    return redirect('add')

def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('add') 
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form})

