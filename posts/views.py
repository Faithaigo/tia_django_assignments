from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "posts":[
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            }
        ]
    }
    return render(request,'posts/index.html', context)

def posts(request):
    context = {
        "posts":[
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            },
            {
                "id":1,
                "title":"First post",
                "content":"Sample content",
                "author":"John Doe"
            }
        ]
    }
    return render(request,'posts/posts.html', context)

def new_post(request):
    return render(request,'posts/new_post.html')