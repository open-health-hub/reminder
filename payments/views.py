import stripe

from django.conf import settings
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages

from .models import Subscription

from .forms import StripeForm


class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_CONFIG["PUBLIC_KEY"]
        context['email'] = self.request.user.email
        return context


class SuccessView(TemplateView):
    template_name = 'payments/thank_you.html'

    def get(self, request):
        return HttpResponseRedirect(reverse("reminder_new"))


class SubscribeView(StripeMixin, FormView):
    template_name = 'please_subscribe.html'
    form_class = StripeForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_CONFIG["SECRET_KEY"]

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripeToken']
        }
        customer = stripe.Customer.create(**customer_data)

        subscription = customer.subscriptions.create(plan=settings.STRIPE_CONFIG["PLAN_ID"])

        s = Subscription(stripe_subscription_id=subscription.id,owner_id=self.request.user.id)
        s.save()

        messages.success(self.request, 'Your subscription has been setup succesfully')
        return super(SubscribeView, self).form_valid(form)
