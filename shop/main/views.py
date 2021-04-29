from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import ProfileForm, ProfileFormSet
from .models import Product


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


def user_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        formset = ProfileFormSet(request.POST, request.FILES, instance=user)
        if form.is_valid() and formset.is_valid():
            user.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileForm(instance=user)
        formset = ProfileFormSet(instance=user)

    return render(request, 'main/profile.html', {'form': form, 'formset': formset})

