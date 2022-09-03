from django.shortcuts import render,get_object_or_404,redirect
from .models import CarType,Piece
from news.models import NewsType
from .forms import NewPieceForm,CreateCommentForm
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("<h1>hello</h1>")
    cars = CarType.objects.all()
    news1 = NewsType.objects.all()
    return render(request, 'pages/index.html',{'cars':cars,'news1':news1})
def news(request):
    return render(request,'pages/news.html')
def car_piece(request,car_id):
    car = get_object_or_404(CarType,pk=car_id)
    return render(request,'pages/pieces.html',{'car': car})
@login_required
def Add_piece(request,car_id):
    car = get_object_or_404(CarType, pk=car_id)
    if(request.method == "POST"):
        form = NewPieceForm(request.POST)
        if form.is_valid():
            piece = form.save(commit=False)
            piece.car_id = car
            #to save user who add the piece , usethe following :
            #user = request.user
            piece.save()
            return redirect('car_piece', car_id=car.pk)
    else:
        form=NewPieceForm()
    return render(request,'pages/new_piece.html',{'form': form})

def comments(request,car_id,piece_id):
    piece = get_object_or_404(Piece,car__id=car_id,pk=piece_id)
    return render(request,'pages/views.html',{'piece':piece})
@login_required
def create_comments(request,car_id,piece_id):
    piece = get_object_or_404(Piece, car__id=car_id, pk=piece_id)
    if (request.method == "POST"):
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = piece
            post.created_by = request.user
            post.save()
            return redirect('comments',car_id=car_id,piece_id=piece_id )
    else:
        form = CreateCommentForm()
    return render(request, 'pages/add_comment.html', {'piece':piece,'form': form})
