from django.shortcuts import render,get_object_or_404,redirect
from .models import NewsType,NewsTopic,posts
from .forms import NewNewsForm,CommentForm
from django.views.generic import UpdateView,ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime as dt
# Create your views here.
def News(request,news_id):
    news = get_object_or_404(NewsType, pk=news_id)
    #عمل عمود وهمي في الجدول عن طريق annotate
    #coulmn name= comments
    #queryset = news.topics.order_by('-created_dt').annotate(comments=Count('posts'))
    #queryset = NewsTopic.objects.filter(type__type = news).order_by('-description')
    queryset = NewsTopic.objects.filter(type__type = news)
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
    return render(request,'news/news.html',{'n':news,'topics':topics})
#او بطريقة GCBV
#class NewsListView(ListView):
 #   model= NewsType
  #  context_object_name = 'n'
   # page_kwarg = 'news_id'
    #template_name='news/news.html'
@login_required
def NewNews(request,news_id):
    news = get_object_or_404(NewsType, pk=news_id)
    if (request.method == "POST"):
        form = NewNewsForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            # to save the user who create the news :
            #created_by= request.user
            topic.type= news
            topic.save()

            return redirect('news_page', news_id=news.pk)
    else:
        form = NewNewsForm()
    return render(request, 'news/new_news.html', {'form': form})

def topic_posts(request,news_id,topic_id):
    topic = get_object_or_404(NewsTopic,type__id=news_id,pk=topic_id)
    return render(request,'news/topic_posts.html',{'topic':topic})
def comment(request,news_id,topic_id):
    topic = get_object_or_404(NewsTopic,type__id=news_id,pk=topic_id)
    if (request.method == "POST"):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # to save the user who create the news :
            post.created_by= request.user
            post.topic = topic
            post.save()
            return redirect('topic_posts', news_id=topic.type.pk,topic_id=topic.pk)
    else:
        form = CommentForm()
    return render(request,'news/comment.html',{'topic':topic,'form':form})
#طريقة اخرى لكتابة view
#تسمى هذه الطريقة ب GCBV
#وهي تعتمد على كلاس جاهز وتعطيه بعض المعلومات وفنكشن
class PostUpdateView(UpdateView):
    model = posts
    fields = ('message',)
    template_name = 'news/edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    def form_valid(self, form):
        post=form.save(commit=False)
        post.updated_date = timezone.now()
        post.save()
        return redirect('topic_posts',news_id=post.topic.type.pk,topic_id=post.topic.pk)
