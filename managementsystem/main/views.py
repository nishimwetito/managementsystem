from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

from . models import Member,GalleryImage,News,Sermon
from . forms import MemberForm,GalleryImageForm,NewsForm,SermonForm

import csv
from django.http import JsonResponse,HttpResponse
from datetime import datetime
import xlwt


from django.template.loader import render_to_string 
from weasyprint import HTML
import tempfile
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request,'main/base.html')


def index(request):
    return render(request,'main/index.html')


def news(request):
    return render(request,'main/news.html')


def events(request):
    return render(request,'main/events.html')



def member_list(request):
    members = Member.objects.all()
    search_query = request.GET.get('search','')
    if search_query:
        members = members.filter(
            Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
            
    


    return render(request,'main/member_list.html',{'members':members})

def member_create(request):
    if request.method=='POST':
        form = MemberForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('member_list')


    else:
        form =MemberForm()
    return render(request,'main/member_form.html',{'form':form})


def member_update(request, pk):
    member = get_object_or_404(Member,pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm(instance=member)
    return render(request, 'main/member_form.html',{'form':form})


def member_delete(request,pk):
    member = get_object_or_404(Member,pk=pk)
    if request.method=='POST':
        member.delete()
        return redirect('member_list')
    return render(request,'main/delete_form.html',{'member':member})


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request,'main/gallery.html',{'images':images})


def upload_image(request):
    if request.method=='POST':
        form = GalleryImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')

    else:
        form = GalleryImageForm()
    return render(request,'main/upload_image.html',{'form':form})



def news_list(request):
    news_posts = News.objects.all().order_by('-published_date')
    paginator = Paginator(news_posts, 6)  # Show 6 news posts per page
    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'news_list': news_list})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'main/news_detail.html', {'news': news})


def upload_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'News uploaded successfully!')
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'main/upload_news.html', {'form': form})

# Edit News
def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to news list after saving
    else:
        form = NewsForm(instance=news)
    return render(request, 'main/edit_news.html', {'form': form})

# Delete News
def delete_news(request, pk):
    new = get_object_or_404(News, pk=pk)
    if request.method=='POST':
        new.delete()
        return redirect('news')  # Redirect to news list after deletion
    return render(request,'main/delete_news.html',{'new':new})


def sermon_list(request):
    sermons = Sermon.objects.all().order_by('-published_date')
    paginator = Paginator(sermons, 6)  # 6 sermons per page
    page_number = request.GET.get('page')
    sermons_list = paginator.get_page(page_number)
    return render(request, 'main/sermons.html', {'sermons_list': sermons_list})

def add_sermon(request):
    if request.method == 'POST':
        form = SermonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sermon_list')
    else:
        form = SermonForm()
    return render(request, 'main/add_sermon.html', {'form': form})

def edit_sermon(request, sermon_id):
    sermon = get_object_or_404(Sermon, pk=sermon_id)
    if request.method == 'POST':
        form = SermonForm(request.POST, request.FILES, instance=sermon)
        if form.is_valid():
            form.save()
            return redirect('sermon_list')
    else:
        form = SermonForm(instance=sermon)
    return render(request, 'main/edit_sermon.html', {'form': form})

def delete_sermon(request, sermon_id):
    sermon = get_object_or_404(Sermon, pk=sermon_id)
    if request.method == 'POST':
        sermon.delete()
        return redirect('sermon_list')
    return render(request, 'main/delete_sermon.html', {'sermon': sermon})





def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename=Member_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
    

    writer=csv.writer(response)
    writer.writerow(['first_name',' last_name','email',' phone_nember'])
    members = Member.objects.all()
    #members = Member.objects.all().iterator() use this for large databeses
    for member in members:
        writer.writerow([
        member.first_name or '',
        member.last_name or '',
        member.email or '',
        member.phone_nember or '',
])

        

    return response

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=Member_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Member')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['first_name',' last_name','email',' phone_nember']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style = xlwt.XFStyle()

    rows = Member.objects.all().values_list('first_name','last_name','email','phone_nember')

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(response)
    return response


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=Member_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf'
    
    response['Content-Transfer-Encoding'] = 'binary'


    html_string = render_to_string (
        'main/pdf_output.html',{'members':[],'total':0}
    )

    html = HTML(string=html_string)

    result = html.write_pdf()
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name,'rb')
        response.write(output.read())

    return response








   
    

     
   



















