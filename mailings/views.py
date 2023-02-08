from sends.models import Newsletter
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse as ht


class Index(ListView):
    model = Newsletter
    paginate_by = 3

    def get_queryset(self):
        return Newsletter.objects.filter(letter_user=self.request.user)

    def render_to_response(self, context, **response_kwargs):
        if not context['object_list']:
            return ht('_' * 100 + 'NONE')
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    def get_context_data(self, *, object_list=None, **kw):
        context = super().get_context_data(**kw)
        context['check'] = {context['page_obj'].number + (x) for x in range(-2, 3)}
        return context


class UpdateMailing(UpdateView):
    model = Newsletter
    fields = '__all__'
    success_url = reverse_lazy('mailings:index')


class DeleteMailing(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailings:index')
