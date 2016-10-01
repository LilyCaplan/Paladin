from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db import models
from .models import Opportunity_Request
from .models import Stats
from .models import Attorney_List
from .models import Nonprofit_Partner

def home(request):
    count_name = 0
    total_hours = 0
    total_projects= 0
    for object_d in Stats.objects.all():
        total_hours+=object_d.Hours
        total_projects+=object_d.Completed_Projects
        count_name +=1
    Average = (total_hours/count_name)

    All_items=[]
    for count,R in enumerate(Attorney_List.objects.all()):
        if count %2 ==0:
            listItem = "<li class = 'even'>"+ "<p class= 'employees'>" + R.Attorneys + "</p>"
            if "Available" in  R.Status:
                listItem +=  "<div class = 'Case_Status'>"+ R.Status +"</div>"+ "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"
            elif "Engaged" in  R.Status:
                listItem+="<div class = 'Case_Status_Engaged'>"+ R.Status+"</div>" + "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"
            elif "Interested" in R.Status:
                listItem+="<div class= 'Case_Status_Interested'>"+R.Status+"</div>" + "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"
            All_items.append(listItem)
        else :
            listItem = "<li class = 'odd'>"+ "<p class= 'employees'>" + R.Attorneys + "</p>"
            if "Available" in  R.Status:
                listItem +=  "<div class = 'Case_Status'>"+ R.Status +"</div>" + "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"
            elif "Engaged" in  R.Status:
                listItem+="<div class = 'Case_Status_Engaged'>"+ R.Status+"</div>"+ "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"
            elif "Interested" in R.Status:
                listItem+="<div class= 'Case_Status_Interested'>"+R.Status+"</div>"+ "<p class='Attorney_List_Cases'>" + R.Cases + "</p></li>"

            All_items.append(listItem)






    for object_i in Opportunity_Request.objects.all():
        Attorneys_Who_Request=object_i.Attorneys_Who_Request
        Requested_Cases=object_i.Requested_Cases

    for j in Nonprofit_Partner.objects.all():
        Nonprofit=j.Nonprofit

        template= loader.get_template('stats/Dash.html')
        context= {

        'count_name' :count_name,
        'total_hours':total_hours,
        'total_projects': total_projects,
        'Average': Average,
        'Opportunity_Requests': Opportunity_Request.objects.all(),
        'Attorneys_Who_Request': Attorneys_Who_Request,
        'Requested_Cases': Requested_Cases,
        'Attorney_List': Attorney_List.objects.all(),
        'Nonprofit_List': Nonprofit_Partner.objects.all(),
        'Nonprofit': Nonprofit,
        'Attorneys_Items':All_items
                 }
    return HttpResponse(template.render(context, request))

