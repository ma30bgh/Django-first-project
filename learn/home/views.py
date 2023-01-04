from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


# Create your views here.
def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})


def sey_hello(request):
    person = {'name': 'admin'}
    return render(request, 'hello.html', context=person)


# def sey_hello(reqest):
#    return render(reqest, 'hello.html', {'name': 'masumeh'})

# Both are similar(sey_hello)
# important things :
# 1- The context must be a dictionary
# 2- The context can be written directly as the third argument

#request ke hamishe sabete hala chera todo_id? chon to url injori tarifesh kardim
def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'successfully', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], create=cd['create'])
            # title avali esme fild modele dovomi form
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
       form = TodoUpdateForm(request.POST , instance=todo)
       if form.is_valid():
           form.save()
           messages.success(request,'Todo update successfully', 'success')
           return redirect('detail',todo_id)
    else:
        # chon inja mikhaym update konim pas fild ha bayad ba etelaat ghabli por shode bashan (instance)
        #agar instance ro nazari az aval mire create mikone instance yani yeseri info darim az ghabl
        #point: har ja ke forme ro seda kardi bego behesh instance ro ham bala baraye post ham payin baraye get
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', {'form': form})
