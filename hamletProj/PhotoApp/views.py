from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from PhotoApp.models import Photo
from datetime import datetime
from .filters import PhotoFilter,MyPhotoFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from PhotoApp.tables import PhotoTable
from django.http import HttpResponseRedirect
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

@login_required
def index(request):
    return HttpResponseRedirect('/photo/search')    

@method_decorator(login_required,name='dispatch')
class FilteredPhotoListView(SingleTableMixin, FilterView):
    table_class = PhotoTable
    model = Photo
    template_name = "PhotoApp/photo_search.html"
    filterset_class = PhotoFilter
    fields = ('title','image','captions','publishedDate','user')
    def get_queryset(self):
        queryset = Photo.objects.all().filter(saveAsDraft = False)
        return queryset
    
@method_decorator(login_required,name='dispatch')
class PhotoMyDraftsView(SingleTableMixin, ListView):
    table_class = PhotoTable
    model = Photo
    template_name = "PhotoApp/photo_list.html"
    fields = ('title','image','captions','publishedDate','user')
    def get_queryset(self):
        queryset = Photo.objects.all().filter(saveAsDraft = True).filter(user_id=self.request.user)
        return queryset

@method_decorator(login_required,name='dispatch')
class PhotoMyListView(SingleTableMixin, FilterView):
    table_class = PhotoTable
    model = Photo
    template_name = "PhotoApp/photo_search.html"
    filterset_class = MyPhotoFilter
    fields = ('title','image','captions','publishedDate','user')
    def get_queryset(self):
        queryset = Photo.objects.all().filter(saveAsDraft = False).filter(user_id=self.request.user)
        return queryset

@method_decorator(login_required,name='dispatch')
class PhotoCreate(CreateView):
    model = Photo
    fields = ('title','image','captions','saveAsDraft')
    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.image = form.cleaned_data['image']
        obj.user = self.request.user
        if obj.saveAsDraft == False:
            obj.publishedDate = datetime.now()
        return super().form_valid(form)
@method_decorator(login_required,name='dispatch')
class PhotoUpdate(UpdateView):
    model = Photo
    fields = ('title','image','captions','saveAsDraft')
    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.saveAsDraft == False:
            obj.publishedDate = datetime.now()
        return super().form_valid(form)
@method_decorator(login_required,name='dispatch')
class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo_mylist')
