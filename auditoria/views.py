from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def directrices(request):
    context ={
        'auditoria_interna_url': 'https://docs.google.com/document/d/10NwD8irjNXTSBq7xcp5el3HNhZMjZuQ23V6y7V95PQs/edit?usp=sharing',
        'codigo_etica_url': 'https://docs.google.com/document/d/1z-8KWGw_uMN1fZc0ZHO1VNmbKRvP7TnFGwVPSYcBuxQ/edit?usp=sharing',
        'independencia_url': 'https://docs.google.com/document/d/1asff5Jf5b0nPhA6RLc36KGLWZNR6XftYAUDORjfliaA/edit?usp=sharing',
        'confidencialidad_url': 'https://docs.google.com/document/d/1Y5I3RDzh0kye5sg4VNxtmRztvd5Mx7KcuQ9CzoYqpq8/edit?usp=sharing',
    }
    return render(request, 'directrices.html', context)

@login_required
def planeacion(request):
    context ={
        # plan estrategico
        'plan_estrategico_url':'https://docs.google.com/document/d/1i0QeNtZoTZqBNZajvsc4uOdpXW_qLP1xjPXQFAD_yXI/edit?usp=sharing',
        # plan anual basado en riesgos
        'plan_auditoria_url':'https://docs.google.com/document/d/15FN8D6fC9NfsEhLQmQSqn5-VKLOBpwc4v_M8d_849Hc/edit?usp=sharing',
        # Estudio Preliminar
        'entendimiento_entidad_url':'https://docs.google.com/document/d/1LiGx5D9V-WcNMbTk50QpkKILSdr8g62swrc3W9G4bZs/edit?usp=sharing',
        'reunion_preliminar_url':'https://docs.google.com/document/d/1_ECJVMYleoTRehNV1dGoOa3wimCtOaFRp7mP6urMGKs/edit?usp=sharing',
        'entrevista_gerencia_url':'https://docs.google.com/document/d/1xa4aBMjKLzxBSuMFL9qDli6cojjLYrIeRX6a3Qqxj6w/edit?usp=sharing',
        'analisis_horizontal_url':'https://docs.google.com/spreadsheets/d/1Y98tzbnBREdgDADlLKkhxoPNorYpWzeftPIWfkPch88/edit?usp=sharing',
        'analisis_vertical_url':'https://docs.google.com/spreadsheets/d/11I0al9DYY9hcEfn8ZRMMjUr_eEbIJJoqVYdsE2WCs30/edit?usp=sharing',
        'revision_estatutos_url':'https://docs.google.com/spreadsheets/d/11vn18tIpJVxB3IFaialUPB2RDGXDa7Hm04DLvDvbJWA/edit?usp=sharing',
        'revision_actas_url':'https://docs.google.com/spreadsheets/d/1WzLN_gy0XLSOhS3wlqbt4-1oQGwh6bwqvyrxQCNMOPw/edit?usp=sharing',
        'revision_contratos_url':'https://docs.google.com/spreadsheets/d/1LEgjFShp_0vt24yc6d2OlQ7gGurgCeQQRnlW1AYUENo/edit?usp=sharing',
        'revision_manual_url':'https://docs.google.com/spreadsheets/d/1Wv9L6JVrskpLT653v_tdvmyh5B1RS4WP0ZUeh9nxV4Y/edit?usp=sharing',
        'revision_correspondencia_url':'https://docs.google.com/spreadsheets/d/1NcnCl6o_OkDbw28tThBPfEY0xrxZgpdMkLBO4WmB9uI/edit?usp=sharing',
        'revision_informes_url':'https://docs.google.com/spreadsheets/d/15VDQyU2oirrWxFvsRIMKc2Bdu8w6zb7oE_VGGWb_-Ik/edit?usp=sharing',
        'cuestionario_evaluacion_url':'https://docs.google.com/spreadsheets/d/1xF3wGsUcJvTdoeyABmjwcN8imSoeXiK_HeSKrocpXac/edit?usp=sharing',
        'evaluacion_cumplimiento_url':'https://docs.google.com/spreadsheets/d/1GQ33P5viPk1CgIn_l0O52-pwiNeww9uUWBYPflRcVe4/edit?usp=sharing',


    }
    return render(request, 'planeacion.html', context)