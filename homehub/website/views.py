
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.management import call_command

def landing(request):
    return render(request, "index.html", {})

@require_http_methods(["GET", "POST"])
@login_required
def reboot_app(request):
    if request.method == "GET":
        return render(request, "reboot.html", {})
    elif request.method == "POST":
        call_command("reboot_system")
        return render(request, "reboot.html", {"rebooting":True})
    else:
        raise NotImplementedError
