from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from webapp.forms import ProjectForm, SearchForm
from webapp.models import Project

User = get_user_model()


class ProjectListView(ListView):
    model = Project
    template_name = "project/projects_list.html"
    ordering = ['-started_at']
    context_object_name = "projects"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__contains=self.search_value) | Q(description__contains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class CreateProjectView(LoginRequiredMixin, CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.users.add(self.request.user)
        self.object.save()
        return response

    def get_success_url(self):
        return reverse("webapp:project_detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = self.object.tasks.filter(is_deleted=False).order_by("-created_at")
        context["users"] = self.object.users.all()
        return context


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    template_name = "project/update_project.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse("webapp:project_detail", kwargs={"pk": self.object.pk})


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy("webapp:projects")


class ManageProjectUserView(LoginRequiredMixin, TemplateView):
    template_name = 'project/manage_project_users.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        context['no_added_users'] = User.objects.exclude(id__in=self.project.users.all())
        return context

    def post(self, request, *args, **kwargs):
        cleaned_data = request.POST
        print(cleaned_data)
        if cleaned_data.get('add_user'):
            self.project.users.add(cleaned_data['add_user'])
            self.project.save()
        elif cleaned_data.get('remove_user'):
            self.project.users.remove(cleaned_data['remove_user'])
            self.project.save()
        return redirect('webapp:project_detail', pk=self.project.pk)


