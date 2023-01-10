from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from ejemplo_dos.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User  
# Create your views here.



def index(request):
    posts = Post.objects.order_by('Precio').all()
    return render(request, "ejemplo_dos/index.html", {"posts": posts})


class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post

class PostListar(LoginRequiredMixin, ListView):
    model = Post
    
class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    fields = '__all__'
    
class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    
class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo_dos_listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo_dos_listar')

class UserLogin(LoginView):
    next_page = reverse_lazy("ejemplo_dos_listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("ejemplo_dos_listar")

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("ejemplo_dos_listar")

class UserActualizar(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('ejemplo_dos_listar')

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("ejemplo_dos_mensajes_crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("ejemplo_dos_mensajes_listar")

