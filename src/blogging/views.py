from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm, AddPost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogging/index.html'
    paginate_by = 5 # pagination 3 post per page

class PostDetail(generic.DetailView):
    model =Post
    template_name = 'blogging/postDetail.html'

# add post
# @login_required(login_url="/accounts/login/")
class AddPost(generic.CreateView):
    model = Post
    form_class = AddPost
    template_name = 'blogging/addPost.html'
    # fields = __all__
    # fields = ('title','content')

# Update post
# @login_required(login_url="/accounts/login/")
class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'blogging/updatePost.html'
    fields = ('title','content','status')

# delete post
# @login_required(login_url="/accounts/login/")
class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'blogging/deletePost.html'
    success_url = reverse_lazy('home')

def post_detail(request,slug):
    template_name = 'blogging/postDetail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Created a Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assigning the current post to the comment
            new_comment.post = post
            # Saving comment to DB
            new_comment.save()
        
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post':post,
                                           'comments':comments,
                                           'new_comment':new_comment,
                                           'comment_form':comment_form})


# signup View
# def registerUser(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request,'Registration Successful.')
#             return redirect('home')
#         messages.error(request,'Unsuccessful registration. Invalid! information.')
#     form = NewUserForm()
#     return render(request, 'blogging/registration/signup.html', context={'register_form':form})

# login view
# def loginUser(request):
#     if request.method =='POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
#                 messages.info(request, f'You are logged in as  {username}')
#                 return redirect('home')
#             else:
#                 messages.error(request,'Invalid username or password.')
#         else:
#             messages.error(request, "Enter username or password")
#     form = AuthenticationForm()
#     return render(request=request, template_name='blogging/registration/login.html',context={'login_form':form})
            