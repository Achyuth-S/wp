from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    form = StudentForm()
    student_details = ""
    percentage = None

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Extract data from the form
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']

            # Calculate total percentage
            total_marks = english_marks + physics_marks + chemistry_marks
            percentage = total_marks / 3

            # Prepare student details to display in the textarea
            student_details = f"""
Name: {name}
Date of Birth: {dob}
Address: {address}
Contact Number: {contact_number}
Email ID: {email}
Marks - English: {english_marks}, Physics: {physics_marks}, Chemistry: {chemistry_marks}
"""

    return render(request, 'student_form.html', {
        'form': form,
        'student_details': student_details,
        'percentage': percentage,
    })
