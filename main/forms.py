from django import forms
from django.forms import SelectMultiple, MultiWidget, TextInput

from main.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class ContactForm(forms.Form):
    name_surname = forms.CharField(max_length=150, label='ФИО')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=150, label='Телефон')
    equipment = forms.CharField(max_length=200, label='Какое оборудование Вам нужно?')
    load = forms.CharField(max_length=200, label='Мощность и тип нагрузки?')
    time_working = forms.CharField(max_length=150, label='Время автономной работы?')


ups_technology_choice = (
    ('online', 'online'),
    ('line-interactive', 'line-interactive'),
)
input_output_voltage = (
    ('220', '220'),
    ('380', '380'),
)
execution = (
    ('Rack', 'Rack'),
    ('Tower', 'Tower'),
    ('Rack/Tower', 'Rack/Tower'),
)
power_module = (
    ('не требуется', 'не требуется'),
    ('N+1', 'N+1'),
    ('2N', '2N'),
)
battery_type = (
    ('Li-on', 'Li-on'),
    ('AGM', 'AGM'),
    ('Свинцово-кислотные', 'Свинцово-кислотные'),
)
estimated_battery_life = (
    ('5', '5'),
    ('10', '10'),
    ('более 10 лет', 'более 10 лет'),
)
battery_placement = (
    ('баттарейный модуль', 'баттарейный модуль'),
    ('баттарейный кабинет', 'баттарейный кабинет'),
    ('стеллаж', 'стеллаж'),
    ('отдельно стоящие АКБ', 'отдельно стоящие АКБ'),
)
battery_backup = (
    ('не требуется', 'не требуется'),
    ('2 ветви', '2 ветви'),
    ('3 ветви и более', '3 ветви и более'),
)
optional_equipment = (
    ('SNMP-карта', 'SNMP-карта'),
    ('Modbus-карта', 'Modbus-карта'),
    ('датчик температуры батарейного кабинета', 'датчик температуры батарейного кабинета'),
    ('карта 3-х релейных выходных сигналов', 'карта 3-х релейных выходных сигналов'),
    ('карта 6-х релейных выходных сигналов', 'карта 6-х релейных выходных сигналов'),

)
environmental_monitoring = (
    ('температура', 'температура'),
    ('влажность', 'влажность'),
    ('входные сигналы', 'входные сигналы'),
    ('управление внешними устройствами', 'управление внешними устройствами'),
    ('датчик протечки жидкости', 'датчик протечки жидкости'),
    ('мониторинг АКБ', 'мониторинг АКБ'),
)
required_additional_equipment = (
    ('телекоммуникационный шкаф', 'телекоммуникационный шкаф'),
    ('телекоммуникационная стойка', 'телекоммуникационная стойка'),
    ('панель распределения питания PDU (количество и номиналы выходов с мониторингом/с управлением/с АВР)',
     'панель распределения питания PDU (количество и номиналы выходов с мониторингом/с управлением/с АВР)'),
    ('ручной механический байпас', 'ручной механический байпас'),
    ('устройство дистанционного управления и мониторинга с ПО',
     'устройство дистанционного управления и мониторинга с ПО'),
    ('степень защиты от пыли и влаги', 'степень защиты от пыли и влаги'),
)


class UsualForm(forms.Form):
    customer_name = forms.CharField(max_length=
                                    150, label='Название учреждения(Заказчика)')
    address = forms.CharField(max_length=200, label='Адрес')
    contact_person = forms.CharField(max_length=200, label='Контактное лицо (фамилия, должность)')
    phone = forms.CharField(max_length=30, label='Телефон')  # регулярку сделать или чтобы начинался с +375
    email = forms.EmailField(label='Email')
    UPS_technology = forms.MultipleChoiceField(label='Технология ИБП', choices=ups_technology_choice,
                                               widget=forms.CheckboxSelectMultiple, required=False)
    input_voltage = forms.MultipleChoiceField(label='Входное напряжение', choices=input_output_voltage,
                                              widget=forms.CheckboxSelectMultiple, required=False)
    output_voltage = forms.MultipleChoiceField(label='Выходное напряжение', choices=input_output_voltage,
                                               widget=forms.CheckboxSelectMultiple, required=False)
    execution = forms.ChoiceField(label='Исполнение', choices=execution, widget=forms.RadioSelect, required=False)
    load_power = forms.CharField(label='Расчетная мощность нагрузки (кВА / кВт)', max_length=200, required=False)
    battery_life = forms.CharField(label='Расчетное время автономной работы (мин.):', required=False)
    power_module = forms.ChoiceField(label='Резервирование силовых модулей: ', choices=power_module,
                                     widget=forms.RadioSelect, required=False)
    power_module_input = forms.CharField(max_length=100, label='другое',required=False)
    battery_type = forms.ChoiceField(label='Тип АКБ', choices=battery_type, widget=forms.RadioSelect, required=False)
    estimated_battery_life = forms.ChoiceField(label='Расчетный срок службы АКБ (лет)', choices=estimated_battery_life,
                                               widget=forms.RadioSelect, required=False)
    battery_placement = forms.MultipleChoiceField(label='Размещение АКБ', choices=battery_placement,
                                                  widget=forms.CheckboxSelectMultiple, required=False)
    battery_backup = forms.ChoiceField(label='Резервирование АКБ', choices=battery_backup, widget=forms.RadioSelect, required=False)
    optional_equipment = forms.MultipleChoiceField(label='Дополнительное оборудование', choices=optional_equipment,
                                                   widget=forms.CheckboxSelectMultiple, required=False)
    optional_equipment_input = forms.CharField(max_length=100, label='другое', required=False)
    environmental_monitoring = forms.MultipleChoiceField(
        label='Мониторинг окружающей среды: (температура, влажность, входные сигналы, управление)',
        choices=environmental_monitoring, widget=forms.CheckboxSelectMultiple, required=False)
    environmental_monitoring_input = forms.CharField(max_length=100, label='другое', required=False)
    required_additional_equipment = forms.MultipleChoiceField(label='Требуемое дополнительное оборудование',
                                                              widget=forms.CheckboxSelectMultiple,
                                                              choices=required_additional_equipment, required=False)
    required_additional_equipment_input = forms.CharField(max_length=100, label='другое', required=False)


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=150, label='Имя')
    email = forms.EmailField(max_length=150, label='Email')
    phone = forms.CharField(max_length=30, label='Телефон')
    equipment = forms.CharField(max_length=300, label='Какое оборудование Вам нужно?', required=False)
    load = forms.CharField(max_length=100, label='Мощность и тип нагрузки?', required=False)
    battery_life = forms.CharField(max_length=100, label='Время автономной работы?', required=False)
