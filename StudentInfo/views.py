from django.shortcuts import render
from django.views import View
# Create your views here.
from .forms import StudentForm
from .models import Students
from django.db.models import Q
TEMPELATE = 'StudentInfo'


def createStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()

            return render(request, TEMPELATE + '/createstudent.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, TEMPELATE + '/createstudent.html', {'form': form})


class StudentList(View):
    def get(self, request):
        search = request.GET.get('search', '')
        if search:
            students = Students.objects.filter( Q(City__icontains=search) | Q( Name__icontains=search))
        else:
            students = Students.objects.all()
        qs = Students.objects.all()
        header = list(qs.values().first().keys())
        return render(request, TEMPELATE + '/ListStudent.html', {'students': students, 'header': header})
