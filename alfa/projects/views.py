from django.shortcuts import render, render_to_response
import logging
from jira.client import JIRA
from simplicity_main import settings
from alfa.projects.models import Project
from datetime import datetime
from shared.states_simplicity.models import State
from simplicity_main.settings import STATE_REGISTERED, ACTIVE
from haystack.query import SearchQuerySet
from kappa.requirements.models import Requirement

# Get an instance of a logger
logger = logging.getLogger('simplicity_main.alfa.projects.views')

def home_projects(request):
    projects = []
    projects = SearchQuerySet().models(Project).load_all()
    return render(request, 'projects_list.html', {'projects': projects})

def search_projects(request):
    projects = []
    logger.debug("searching projects: ")
    if not request.POST.get('q', '') :
        content_auto_v = "*:*"
        projects = SearchQuerySet().models(Project).load_all()
    else:
        content_auto_v = request.POST.get('q', '')
        logger.debug("searching projects by: " + content_auto_v)
        projects = SearchQuerySet().models(Project).filter(text=content_auto_v)
        
    return render_to_response('_project_result.html', {'projects': projects})

# Create your views here.
def sync(request):
    key_cert_data = None
    with open(settings.JIRA_PEM_PATH, 'r') as key_cert_file:
        key_cert_data = key_cert_file.read()
    logger.debug('key_cert_data' + key_cert_data)
    oauth_dict = {
        'access_token': settings.JIRA_ACCESS_TOKEN,
        'access_token_secret': settings.JIRA_ACCESS_TOKEN_SECRET,
        'consumer_key': settings.JIRA_CONSUMER_KEY,
        'key_cert': key_cert_data
    }
    
    jira = JIRA(options=settings.OPTIONS, oauth=oauth_dict)
    
    # Get all projects viewable by anonymous users.
    projects_jira = jira.projects()
    projects = []
    
    for project in projects_jira:
        simplicity_project = Project.objects.filter(jira_id=project.id)
        
        if not simplicity_project:
            new_project = Project()
            new_project.jira_id = project.id
            new_project.name = project.name
            
            date_created = datetime.now()
            new_project.date_created = date_created
            new_project.date_modified = date_created
            
            new_project.is_active = ACTIVE
            
            new_project.save()
            
    projects = SearchQuerySet().models(Project).load_all()
            
    return render_to_response('_project_result.html', {'projects': projects})