from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def student_info(request):
    # Get all rows or objects from Student table
    stu_rows = Student.objects.all()
    print('All rows or objects: ', stu_rows)
    return render(request, 'enroll/stu_details.html', {'stu_qs': stu_rows})
    
    '''
    # Get a single row from Student table
    stu_single_row = Student.objects.get(pk=1)
    return render(request, 'enroll/stu_details.html', 
                  {'stu_qs': stu_single_row})
    '''