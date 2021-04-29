from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import UpdateView

from .forms import ProfileFormset, UserForm
from .models import Product, Tag


def index(request):
    turn_on_block = True
    user = request.user
    return render(request, 'main/index.html', {'turn_on': turn_on_block, 'user': user})


class ProductListView(generic.ListView):
    model = Product
    template_name = 'main/goods.html'
    paginate_by = 3
    context_object_name = 'goods'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.GET.get("tag"):
            return qs.filter(tags__title=self.request.GET.get("tag"))
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["tag"] = self.request.GET.get("tag")
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/detail_goods.html'


class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'main/profile.html'
    success_url = '/accounts/profile/'
    form_class = UserForm
    redirect_field_name = 'redirect_to'

    def get_object(self, request):
        return request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ProfileFormset(instance=self.get_object(kwargs['request']))
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(request)
        return self.render_to_response(self.get_context_data(request=request))

    def form_valid_formset(self, form, formset):
        if formset.is_valid():
            formset.save(commit=False)
            formset.save()
        else:
            return HttpResponseRedirect(self.get_success_url())
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(request)
        form = self.get_form()
        formset = ProfileFormset(self.request.POST, self.request.FILES, instance=self.object)
        if form.is_valid():
            return self.form_valid_formset(form, formset)
        else:
            return self.form_invalid(form)


class ProductCreate(generic.edit.CreateView):
    model = Product
    fields = [field.name for field in Product._meta.get_fields()]
    template_name = 'main/create_product.html'
    success_url = 'add'


class ProductUpdate(UpdateView):
    model = Product
    fields = [field.name for field in Product._meta.get_fields()]
    template_name_suffix = '_update'
    success_url = '/goods'
