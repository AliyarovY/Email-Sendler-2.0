from sends.models import Newsletter
from authh.models import User
from django.views.generic import ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class Users(LoginRequiredMixin, ListView):
    model = User
    template_name = 'mailings/users.html'

    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Manager').exists():
            raise Http404()

        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


class Index(LoginRequiredMixin, ListView):
    model = Newsletter
    paginate_by = 3

    def get_queryset(self):
        if self.request.user.groups.filter(name='Manager').exists():
            return Newsletter.objects.all()
        return Newsletter.objects.filter(letter_user=self.request.user)

    def render_to_response(self, context, **response_kwargs):
        if not context['object_list']:
            return HttpResponse('_' * 100 + 'NONE')
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

    def get_context_data(self, *, object_list=None, **kw):
        global page_all_
        context = super().get_context_data(**kw)
        context['request'] = self.request
        context['check'] = {context['page_obj'].number + (x) for x in range(-2, 3)}
        page = context['page_obj'].number
        page_all_ = context['paginator'].num_pages
        with open('previous_page', 'w') as file:
            file.write(f'/mailings/?page={page}')
        return context


class UpdateMailing(UpdateView):
    model = Newsletter
    fields = ('letter_time', 'letter_periood', 'letter_status', 'letter_mails',)

    def get_success_url(self):
        with open('previous_page', 'r') as file:
            url = file.read()
        return url


class DeleteMailing(DeleteView):
    model = Newsletter

    def get_success_url(self):
        with open('previous_page', 'r') as file:
            url = file.read()
        return url


def page_not_found(request, exception):
    return redirect('mailings:index')
