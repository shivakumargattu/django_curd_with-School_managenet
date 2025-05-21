from django.shortcuts import render,redirect
from .models import Teacher

def teacher_list(req):
    teacher=Teacher.objects.all()
    return render(req,"index.html", {"allteachers":teacher})

def add_teacher(req):
    if(req.method=="POST"):
        name = req.POST.get('name')
        subject = req.POST.get('subject')
        email = req.POST.get('email')
        contact= req.POST.get('contact')
        
        teacher=Teacher(
            name=name,
            subject=subject,
            email=email,
            contact=contact
        )
        
        teacher.save()
        return redirect("all-teachers")
    return render(req, "index.html")


def update_teacher(req,id):
    teacher = Teacher.objects.get(id=id)  # Get the existing teacher

    if(req.method=="POST"):
        name = req.POST.get('name')
        subject = req.POST.get('subject')
        email = req.POST.get('email')
        contact= req.POST.get('contact')
        
        teacher=Teacher(
            id=id,
            name=name,
            subject=subject,
            email=email,
            contact=contact
        )
        
        teacher.save()
        return redirect("all-teachers")
    return render(req, "index.html", {"teacher":teacher})

def delete_teacher(request, id):
    
    teacher=Teacher.objects.filter(id=id)
    teacher.delete()
        
    return redirect("all-teachers")  