from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import UsualForm, SimpleForm


def show_base(request):
    return render(request, 'base.html')


def main_page(request):
    return render(request, 'main.html')


def show_equipment(request):
    return render(request, 'equipment.html')


def show_service(request):
    return render(request, 'service.html')


def show_rent(request):
    return render(request, 'rent.html')


def show_certificates(request):
    return render(request, 'certificates.html')


def success_view(request):
    return render(request, 'result_selection.html')

def show_usual(request):
    form = UsualForm()
    if request.method == 'POST':
        form = UsualForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            address = form.cleaned_data['address']
            contact_person = form.cleaned_data['contact_person']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            UPS_technology = form.cleaned_data['UPS_technology']
            input_voltage = form.cleaned_data['input_voltage']
            output_voltage = form.cleaned_data['output_voltage']
            execution = form.cleaned_data['execution']
            load_power = form.cleaned_data['load_power']
            battery_life = form.cleaned_data['battery_life']
            power_module = form.cleaned_data['power_module']
            power_module_input = form.cleaned_data['power_module_input']
            battery_type = form.cleaned_data['battery_type']
            estimated_battery_life = form.cleaned_data['estimated_battery_life']
            battery_placement = form.cleaned_data['battery_placement']
            battery_backup = form.cleaned_data['battery_backup']
            optional_equipment = form.cleaned_data['optional_equipment']
            optional_equipment_input = form.cleaned_data['optional_equipment_input']
            enviromental_monitoring = form.cleaned_data['environmental_monitoring']
            enviromental_monitoring_input = form.cleaned_data['environmental_monitoring_input']
            required_additional_equipment = form.cleaned_data['required_additional_equipment']
            required_additional_equipment_input = form.cleaned_data['required_additional_equipment_input']
            res = f'{customer_name}\n ' \
                  f'{address}\n' \
                  f'{contact_person}\n' \
                  f'{phone}\n' \
                  f' {email}\n' \
                  f' {UPS_technology}\n' \
                  f' {input_voltage}\n' \
                  f' {output_voltage}\n' \
                  f'{execution}\n' \
                  f' {load_power}\n' \
                  f' {battery_life}\n' \
                  f' {power_module}\n' \
                  f' {power_module_input}\n' \
                  f' {battery_type}\n' \
                  f'{estimated_battery_life}\n' \
                  f' {battery_placement}\n' \
                  f' {battery_backup}\n' \
                  f' {optional_equipment}\n' \
                  f'{optional_equipment_input}\n' \
                  f' {enviromental_monitoring}\n' \
                  f' {enviromental_monitoring_input}\n' \
                  f'{required_additional_equipment}\n' \
                  f' {required_additional_equipment_input}'
            try:
                send_mail('Запрос', res, 'v.murashko1999@gmail.com', ['v.murashko999@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')
        else:
            return HttpResponse('Неверный запрос.')
    context = {'form': form}
    return render(request, 'usual.html', context)


def show_simple(request):
    form = SimpleForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            equipment = form.cleaned_data['equipment']
            load = form.cleaned_data['load']
            battery_life = form.cleaned_data['battery_life']
            res = f' {name}\n {email}\n {phone}\n {equipment}\n {load}\n {battery_life}'
            try:
                send_mail('Запрос', res, 'v.murashko1999@gmail.com', ['v.murashko999@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма')
            return redirect('success')
        else:
            return HttpResponse('Неверный запрос.')
    return render(request, 'simple.html', context)


def your_select(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST['select'] == 'simple':
            return redirect(reverse_lazy(show_simple))
        elif request.POST['select'] == 'pro':
            return redirect(reverse_lazy(show_usual))
        elif request.POST['select'] == 'auto':
            return redirect('https://www.deltapowersolutions.com/ups-selector/ru.html')
    return render(request, 'selection.html')