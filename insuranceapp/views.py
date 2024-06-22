from django.shortcuts import render, get_object_or_404, redirect
from .models import Agent, Customer
from .forms import CustomerForm
from .models import Agent, Policy
from .forms import AgentForm, PolicyForm
from django.http import Http404

def home(request):
    return render(request, 'home.html')



def agent_dashboard(request):
    agents = Agent.objects.all()
    return render(request, 'agent_dashboard.html', {'agent': agents})




def view_agent(request, agent_id):
    try:
        agent = Agent.objects.get(id=agent_id)
    except Agent.DoesNotExist:
        raise Http404("Agent does not exist")

    return render(request, 'view_agent.html', {'agent': agent})





def add_customer(request):
   return render(request, 'add_customer.html')

def edit_customer(request):
   return render(request, 'edit_customer.html')

def delete_customer(request):
   return render(request,'delete_customer.html')

def view_customer(request):
   return render(request, 'view_customer.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def admin_dashboard(request):
    agents = Agent.objects.all()
    policies = Policy.objects.all()
    context = {
        'agents': agents,
        'policies': policies,
    }
    return render(request, 'admin_dashboard.html', context)







def add_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AgentForm()
    return render(request, 'add_agent.html', {'form': form})

def edit_agent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AgentForm(instance=agent)
    return render(request, 'edit_agent.html', {'form': form})

def delete_agent(request, agent_id):
    agent = get_object_or_404(Agent, pk=agent_id)
    if request.method == 'POST':
        agent.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_agent.html', {'agent': agent})

def add_policy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PolicyForm()
    return render(request, 'add_policy.html', {'form': form})

def edit_policy(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)
    if request.method == 'POST':
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PolicyForm(instance=policy)
    return render(request, 'edit_policy.html', {'form': form})

def delete_policy(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)
    if request.method == 'POST':
        policy.delete()
        return redirect('admin_dashboard')
    return render(request, 'delete_policy.html', {'policy': policy})






