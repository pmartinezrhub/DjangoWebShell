from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess

@csrf_exempt  # Use CSRF protection in production!
def command_executor(request):
    output = ''
    if request.method == 'POST':
        command = request.POST.get('command'.strip(), '')
        
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            output = result
        except subprocess.CalledProcessError as e:
            output = e.output
    return render(request, 'command_form.html', {'output': output})