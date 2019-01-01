from django.shortcuts import render
from django.contrib.auth,mixin import (LoginRequiredMixin,
										PermissionRequiredMixin)
# Create your views here.

from django.core.urlresolvers import reverse
from django.views import generic
from groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, generic.CreateView):
	fields = ('name', 'description')
	model = Group

class SingleGroup(generic.DetailView):
	model = Group

class ListGroup(generic.ListView):
	model = Group