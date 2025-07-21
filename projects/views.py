from django.shortcuts import render,get_object_or_404
from projects.models import *
# Create your views here.

def projects_index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    context = {'projects':projects,'categories':categories,'statuses':statuses}
    return render(request,'project.html',context)


def one_item(request,pid):
    project1 = get_object_or_404(Project,pk=pid)
    images = project1.images.all()
    return render(request,'one-item.html',{'project1':project1,'images':images})


def categories(request,cat_name):
    categories = Category.objects.all()
    statuses = Status.objects.all()
    cat1 = get_object_or_404(Category,name__iexact=cat_name)
    project2 = Project.objects.filter(category=cat1)
    context = {'cat1':cat1,'projects':project2,'categories':categories,'statuses':statuses}
    return render(request,'project.html',context)


def statuses(request,sta_value):
    statuses = Status.objects.all()
    categories = Category.objects.all()
    sta1 = get_object_or_404(Status,value__iexact=sta_value)
    project3 = Project.objects.filter(status_value=sta1)
    context = {'statuses':statuses,'sta1':sta1,'projects':project3,'categories':categories}
    return render(request,'project.html',context)


def sort_projects(request,sort_by):
    statuses = Status.objects.all()
    categories = Category.objects.all()

    if sort_by =='title':
        project4 = Project.objects.order_by('title')
    elif sort_by =='design_year':
        project4 = Project.objects.order_by('-design_year')
    elif sort_by =='scale':
        project4 = Project.objects.order_by('-scale')

    else:
        project4 = Project.objects.order_by('title')
    context = {'categories':categories,'statuses':statuses,'projects':project4}
    return render(request,'project.html',context)



def projects_index_persian(request):
    projects_p = Project_persian.objects.all()
    categories_p = Category_persian.objects.all()
    statuses_p = Status_persian.objects.all()
    context = {'projects':projects_p,'categories':categories_p,'statuses':statuses_p}
    return render(request,'project-persian1.html',context)



def one_item_persian(request,pid):
    project1_p = get_object_or_404(Project_persian,pk=pid)
    images_p = project1_p.images.all()
    return render(request,'one-item-persian.html',{'project1':project1_p,'images':images_p})



def categories_persian(request,cat_name):
    categories_p = Category_persian.objects.all()
    statuses_p = Status_persian.objects.all()
    cat1_p = get_object_or_404(Category_persian,name__iexact=cat_name)
    project2_p = Project_persian.objects.filter(category=cat1_p)
    context = {'cat1':cat1_p,'projects':project2_p,'categories':categories_p,'statuses':statuses_p}
    return render(request,'project-persian1.html',context)



def statuses_persian(request,sta_value):
    statuses_p = Status_persian.objects.all()
    categories_p = Category_persian.objects.all()
    sta1_p = get_object_or_404(Status_persian,value__iexact=sta_value)
    project3_p = Project_persian.objects.filter(status_value=sta1_p)
    context = {'statuses':statuses_p,'sta1':sta1_p,'projects':project3_p,'categories':categories_p}
    return render(request,'project-persian1.html',context)




def sort_projects_persian(request,sort_by):
    statuses_p = Status_persian.objects.all()
    categories_p = Category_persian.objects.all()

    if sort_by =='title':
        project4_p = Project_persian.objects.order_by('title')
    elif sort_by =='design_year':
        project4_p = Project_persian.objects.order_by('-design_year')
    elif sort_by =='scale':
        project4_p = Project_persian.objects.order_by('-scale')

    else:
        project4_p = Project_persian.objects.order_by('title')
    context = {'categories':categories_p,'statuses':statuses_p,'projects':project4_p}
    return render(request,'project-persian1.html',context)


