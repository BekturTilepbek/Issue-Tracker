from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm, SearchForm
from webapp.models import Project


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


class CreateProjectView(CreateView):
    template_name = "project/create_project.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_detail", kwargs={"pk": self.object.pk})


class ProjectDetailView(DetailView):
    template_name = "project/project_detail.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = self.object.tasks.order_by("-created_at")
        return context


class UpdateProjectView(UpdateView):
    template_name = "project/update_project.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse("project_detail", kwargs={"pk": self.object.pk})


class DeleteProjectView(DeleteView):
    template_name = "project/delete_project.html"
    model = Project
    success_url = reverse_lazy("projects")

