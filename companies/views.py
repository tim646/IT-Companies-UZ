from django.shortcuts import render

from django.views.generic import ListView


from .models import Company
# Create your views here.

class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'company_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['company_list'] = context['company_list'].filter(name__icontains=search_input)

        context['search_input'] = search_input
        return context

# class CompanyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Company
#     fields = ('name', 'link', 'open', 'close', 'website_address', 'company_status')
#     template_name = 'company_edit.html'
#
# class CompanyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Company
#     template_name = 'company_delete.html'
#     success_url = reverse_lazy('company_list')
#
#
# class CompanyCreateView(LoginRequiredMixin, CreateView):
#     model = Company
#     template_name = 'company_new.html'
#     fields = ('name', 'location', 'open', 'close', 'website_address', 'company_status')


