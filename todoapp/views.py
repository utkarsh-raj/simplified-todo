from django.shortcuts import render, redirect
from todoapp.models import Todo, Author
from django.contrib.auth import authenticate, login

# Create your views here.
loggedIn = {
    "status": False,
    "userId": None
}

def index(request):
    print(loggedIn)
    if loggedIn["status"] == True:
        author = Author.objects.get(id = loggedIn["userId"])
        try:
            todoList = Todo.objects.filter(author = author)
            print(todoList)

            context = {
                "todos": todoList
            }
            
            return render(request, "index.html", context)
        except:
            return redirect("new")
    else:
        return redirect("login")

def new(request):
    print(loggedIn)
    if loggedIn["status"] == True:
        if request.method == "POST":
            content = request.POST["content"]
            author = Author.objects.get(id = loggedIn["userId"])

            todo = Todo(content = content, author = author)

            todo.save()
            
            return redirect("index")
        else:
            return render(request, "new.html")
    else:
        return redirect("/")

def update(request, id):
    print(loggedIn)
    if loggedIn["status"] == True:
        print(request.method)
        if request.method == "POST":
            todo = Todo.objects.get(id = id)

            content = request.POST["content"]

            todo.content = content

            todo.save()

            return redirect("index")
        else:
            todo = Todo.objects.get(id = id)
            content = todo.content

            context = {
                "id": todo.id,
                "content": todo.content
            }

            print(context)
            return render(request, "update.html", context = context)
    else:
        return redirect("/")

def delete(request, id):
    print(loggedIn)
    if loggedIn["status"] == True:
        todo = Todo.objects.get(id = id)

        todo.delete()

        return redirect("index")
    else:
        return redirect("/")

def userLogin(request):
    print(loggedIn)
    if loggedIn["status"] == True:
        return redirect("index")
    elif request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]

        print("Request is coming here.", username, password)

        try:
            user = Author.objects.get(name = username, password = password)
            print(user.name)
            loggedIn["status"] = True
            loggedIn["userId"] = user.id
            return redirect("index")
        except:
            print("User not found.")
            return redirect("login")
    
    else:
        return render(request, "login.html")

def signup(request):
    print(loggedIn)
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        print(username, password)

        author = Author(name = username, password = password)

        author.save()

        return redirect("/todo/index")
    else:
        return render(request, "signup.html")

def logout(request):
    global loggedIn
    loggedIn = {
        "status": False,
        "userId": None
    }
    return redirect("/")

def home(request):
    if loggedIn["status"] == True:
        return redirect("index")
    else:
        return render(request, "home.html")