from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import profile,Posts,Thread,Thread_category,thread_reply,post_reply,games
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import createCustomUser,createpostform
from django.views.generic.edit import FormView
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import Group



def homepage(request):
    posts=Posts.objects.order_by('-time_created')[:3]
    return render(request,'./account/home.html',{'posts':posts})
#post creation,deletion,update,(list and detail) view----------------------------------------------------------------
class createPost(CreateView):
        model=Posts
        fields=[
        'title','body','post_img','category'
        ]
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super(createPost, self).form_valid(form)



def detailposts(request,pk):
    posts=Posts.objects.get(id=pk)
    try:
        replys=posts.post_reply_set.all
        comment=True
    except:
        comment = False
    if request.method == 'POST':
        gu = post_reply.objects.create(post=posts, author=request.user , reply = request.POST['comment'] )
        gu.save()
        return redirect('account:detail', posts.id)

    return render(request,'./account/detailview.html',{'posts':posts , 'comments':comment , 'apost':True})

class deletepost(DeleteView):
    model=Posts
    success_url = reverse_lazy('account:posts')

class updatepost(UpdateView):
    model=Posts
    fields=[
        'title','body','post_img','category'
    ]

def listview(request):
    posts=Posts.objects.order_by('-time_created')
    return render(request,'./account/list.html',{'posts':posts , 'apost':True})


#thread category creation , update , view and deletion and detail----------------------------------------------------------
def forumlist(request):
    forums=Thread_category.objects.all()
    return render(request,'./account/forums.html',{'forums':forums , 'aforum':True})

class createThreadCategory(CreateView):
        model=Thread_category
        fields=[
        'category_title','description',
        ]
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super(createThreadCategory, self).form_valid(form)
class deleteThreadCategory(DeleteView):
    model=Thread_category
    success_url = reverse_lazy('account:forums')

class updateThreadCategory(UpdateView):
    model=Thread_category
    fields=[
    'category_title','description',
    ]

def forumdetail(request,pk):
    forum=Thread_category.objects.get(id=pk)
    i=0
    try:
        threads=forum.threads_set.all
        comment=True
    except:
        comment = False
    return render(request,'./account/forumdetail.html',{'forum':forum , 'comments':comment , 'aforum':True})

# thread detail creation,deletion ,update ----------------------------------------------------------------------------------
def threaddetail(request,pk):
    thread=Thread.objects.get(id=pk)
    try:
        replys=thread.thread_reply_set.all
        comment=True
    except:
        comment = False
    if request.method == 'POST':
        reply= thread_reply.objects.create(thread=thread, reply = request.POST['comment'],author=request.user )
        reply.save()
        return redirect('account:threaddetail', thread.id)
    return render(request,'./account/threaddetail.html',{'thread':thread , 'comments':comment , 'aforum':True})

class createThread(CreateView):
    model=Thread
    fields=[
    'queston','detail','category',
    ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(createThread, self).form_valid(form)
class deleteThread(DeleteView):
    model=Thread
    success_url = reverse_lazy('account:forums')

class updateThread(UpdateView):
    model=Thread
    fields=[
    'queston','detail','category',
    ]


# game-categories creation update and delete------------------------------------------------------------------------------------
class creategame(CreateView):
        model=games
        fields=[
        'game_title','game_description','game_image',
        ]
        def form_valid(self, form):
            form.instance.author = self.request.user
            return super(creategame, self).form_valid(form)

def gamedetail(request,pk):
    game=games.objects.get(id=pk)
    posts=Posts.objects.order_by('-time_created')
    return render(request,'./account/gamedetail.html',{'game':game , 'posts' : posts, 'agame':True})

def gamelist(request):
    Games=games.objects.all()
    return render(request,'./account/games.html',{'games':Games})

class deletegame(DeleteView):
    model=games
    success_url = reverse_lazy('account:games')

class updategame(UpdateView):
    model=games
    fields=[
        'game_title','game_description','game_image',
    ]



# user creation,update,deletion-----------------------------------------------------------------------------
class SignUp(FormView):
    form_class = createCustomUser
    template_name='./account/customuser_form.html'
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = auth.authenticate(username = username , password = password)
            user.profile.Discord_name=request.POST['discordname']
            user.profile.forum_name=request.POST['forumname']
            user.save()
            my_group = Group.objects.get(name='basic')
            my_group.user_set.add(user)
            my_group.save()
            if user is not None:
                if user.is_active:
                     # my_group = Group.objects.get(name='The commoner')
                    # my_group.user_set.add(user)
                    auth.login(request,user)
                    return redirect('account:home')
        return render(request,'./account/customuser_form.html',{'form':form})
        
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'] , password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('account:home')
        return render(request,'./account/home.html',{'error':'user or password incorrect'})
    return render(request,'./account/home.html')
