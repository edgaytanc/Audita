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
        # Area de caja y bancos
        'cuestionario_evaluacion_url':'https://docs.google.com/document/d/1bXqPyZwVhNOha6juIvs8QFwtDsPSIo95LEUZP-FRXRo/edit?usp=sharing',
        'evaluacion_cuentas_url':'https://docs.google.com/spreadsheets/d/1Nz685Lhgmg0asGZyXTZOvk2x08DV6tb8zmIbpVp59Zo/edit?usp=sharing',
        'entendimiento_control_interno_url':'https://docs.google.com/document/d/1jHQFiq0qU47M1X8iVG5XzSVg87HpiQoe_Z3sLa5hX5E/edit?usp=sharing',
        'documentar_proceso_url':'https://docs.google.com/document/d/1ek-lfzVL4IITOt5BvROy2HwFJnya5ozqRldQVH2MP5Q/edit?usp=sharing',
        'evaluacion_riesgos_url':'https://docs.google.com/document/d/1JBTyVSPhiC8axECqvE0SC3e25RC_Fq-76GlXscsPZLs/edit?usp=sharing',
        'evaluar_eficacia_url':'https://docs.google.com/document/d/13_2ecipcsJntiRzwo9bQwGHdaBLDcVgOETCLNNdvE9k/edit?usp=sharing',
        # Area de cuantas por cobrar
        'cuestionario_evaluacion_cobrar_url':'https://docs.google.com/document/d/1fWFQuQKzZUrTCq9q3xjc2CXaw50pZACex_DMQTIY52w/edit?usp=sharing',
        'evaluacion_cuentas_cobrar_url':'https://docs.google.com/spreadsheets/d/1b1YM1d9zszcX-t7GnyrRuxyslMERWg819Tk11F-p14Q/edit?usp=sharing',
        'entendimiento_control_interno_cobrar_url':'https://docs.google.com/document/d/15eN2tMLx3YHTUsvdIUefnGScRB9ticGowIlY0HYixFg/edit?usp=sharing',
        'documentar_proceso_cobrar_url':'https://docs.google.com/document/d/1Me3l0GU3slqdBHmT8JLy2ydd61tr3LuI9R9KxFLNwkw/edit?usp=sharing',
        'evaluacion_riesgos_cobrar_url':'https://docs.google.com/document/d/1v676XaKsimVax1TtBg6QYvYmKNhwGk-M_0k2E17ov7M/edit?usp=sharing',
        'evaluar_eficacia_cobrar_url':'https://docs.google.com/document/d/1kadKUQ_H-WhyUY5hHIPbWIBWgEgJV4QQXhNjqm36JbQ/edit?usp=sharing',
        # Area de inversion
        'cuestionario_evaluacion_inversion_url':'https://docs.google.com/document/d/14CJQyQLSaGtmGs-kiTEqEA2hyGNcbCBD8fDs1d-4ek0/edit?usp=sharing',
        'evaluacion_cuentas_inversion_url':'https://docs.google.com/spreadsheets/d/1cgeV9rqFU3eW7XqBXuTa8UVucdBaA35UzXwk4Ox6wDc/edit?usp=sharing',
        'entendimiento_control_interno_inversion_url':'https://docs.google.com/document/d/10-7yl8Y-rYIIQp4-V165Ehw8YcGEQ3MN1d7I-Iar3Co/edit?usp=sharing',
        'documentar_proceso_inversion_url':'https://docs.google.com/document/d/1fc3x9_RCafbV-VJqoWHk-6vruUHNhI5Nt-6wqwpScPI/edit?usp=sharing',
        'evaluacion_riesgos_inversion_url':'https://docs.google.com/document/d/1O1nxarm4i9VsMj1n0CMRPwWiY6AXC3Dtx8ZxcsNv3IU/edit?usp=sharing',
        'evaluar_eficacia_inversion_url':'https://docs.google.com/document/d/1keDaHEIWxETlTMqseX4zuj6RiERAoaaGekImdWyGv0k/edit?usp=sharing',
        # Area de Construcciones en Proceso
        'cuestionario_evaluacion_construccion_url':'https://docs.google.com/document/d/1dXmKBCVEYDQVuydOjWOszdC7QdhpM43_BTIBl-4jGVI/edit?usp=sharing',
        'evaluacion_cuentas_construccion_url':'https://docs.google.com/spreadsheets/d/10o1U_JwkwT1bwusB1sKwtJyWY3ldq_jQ2835NID2kdg/edit?usp=sharing',
        'entendimiento_control_interno_construccion_url':'https://docs.google.com/document/d/1S2xn7COr6rWAlCUba-pgKIwN4tfgxJb7P6O0zhkp_C8/edit?usp=sharing',
        'documentar_proceso_construccion_url':'https://docs.google.com/document/d/16N_V7W1zx1ZS0wS0m81JBOISWmBFiFvBEFLSZp5QK18/edit?usp=sharing',
        'evaluacion_riesgos_construccion_url':'https://docs.google.com/document/d/1Dq9D0Ts4w-8jWpUP-L0TturjqTwiZnXioj27fUMAlII/edit?usp=sharing',
        'evaluar_eficacia_construccion_url':'https://docs.google.com/document/d/1GoMAXB5ytvoRru_8cfAvKyQFZi1QNx4YuU8eWgLPEz4/edit?usp=sharing',
        # Area de Propiedad, Planta y Equipo
        'cuestionario_evaluacion_propiedad_url':'https://docs.google.com/document/d/1edohbhjbhVuqflafZsYZx0KH_jD0jeGirer6_0DaHoE/edit?usp=sharing',
        'evaluacion_cuentas_propiedad_url':'https://docs.google.com/spreadsheets/d/1iS4nDRmvlSUzswSJ20fA4DU5GM2PsrS0d5xEBdjtCE0/edit?usp=sharing',
        'entendimiento_control_interno_propriedad_url':'https://docs.google.com/document/d/1juCVpz2H0qPpaNq0St_ZbcfI3t9cOvDIlOBRDgRzmrs/edit?usp=sharing',
        'documentar_proceso_propiedad_url':'https://docs.google.com/document/d/1iZFKUZo-0P04bU5_18rUK9g0CVDlZWhj6G43VDlzbhI/edit?usp=sharing',
        'evaluacion_riesgos_propiedad_url':'https://docs.google.com/document/d/1BeJ-WSQXMQRvk4HlLq_F9TG3ToqpFa9ZUOBBioaSALY/edit?usp=sharing',
        'evaluar_eficacia_propiedad_url':'https://docs.google.com/document/d/1Ufn2O_TSedmmBG7ApZ30ocIFBi4PyhRc-wypD2NB06o/edit?usp=sharing',
        # Área de Activo Intangible
        'cuestionario_evaluacion_diferido_url':'https://docs.google.com/document/d/1G7lILFDiOz4oXG9zgUBCfgy5k1vYwzw3jbkpS6WGlmo/edit?usp=sharing',
        'evaluacion_cuentas_diferido_url':'https://docs.google.com/spreadsheets/d/1UXNJRKInMqWXuLt-OPmy2nKRLz8CZruU-aosecMCvNo/edit?usp=sharing',
        'entendimiento_control_interno_diferido_url':'https://docs.google.com/document/d/1ODCxbWhvDob98E8NnQT2vO9Ld_MvAO62Gy6BNAyeb2w/edit?usp=sharing',
        'documentar_proceso_diferido_url':'https://docs.google.com/document/d/1pL6VeKnjxE3Q9rqjCBwqph3MWCP6ms1gWHEn25CBUck/edit?usp=sharing',
        'evaluacion_riesgos_diferido_url':'https://docs.google.com/document/d/1NTq-6I_Bw_I0pxrpbbpV8wpZXLn5XdxTTZ93jz7QE3E/edit?usp=sharing',
        'evaluar_eficacia_diferido_url':'https://docs.google.com/document/d/1vdjf_dFpAx5WtyFqDLUxv3AgM9PUyFaWpxrY9n-EFKo/edit?usp=sharing',
        # Área de cuentas por pagar
        'cuestionario_evaluacion_pagar_url':'https://docs.google.com/document/d/1UZOpZU-n6ZDBaHV-kiRmXIaMZJj40PiUAIJSFtWMxn4/edit?usp=sharing',
        'evaluacion_cuentas_pagar_url':'https://docs.google.com/spreadsheets/d/1ZRwywGgkavHySuK-Lc_g5dWVpom9u6WOBDmeoxV7zr0/edit?usp=sharing',
        'entendimiento_control_interno_pagar_url':'https://docs.google.com/document/d/1KWlnESn637HQ9FSjPge8DtAFVG99zcx0a8rqtKUSPDc/edit?usp=sharing',
        'documentar_proceso_pagar_url':'https://docs.google.com/document/d/1fXCywDihFmPJOjlYmMhrIfSu3WIGsjvAwJaFUQMx368/edit?usp=sharing',
        'evaluacion_riesgos_pagar_url':'https://docs.google.com/document/d/1m56IBbrIMSKP0Pd3HhNfr3wImjg4D_boEVX3L6kVs4Q/edit?usp=sharing',
        'evaluar_eficacia_pagar_url':'https://docs.google.com/document/d/109AWYHbRDCreYw6Nx6w5fasyvNT5KP1OjiD-9WpWX3s/edit?usp=sharing',
        # Área de prestamos por pagar
        'cuestionario_evaluacion_prestamos_url':'https://docs.google.com/document/d/1h5P2mU-xYl6u1hTpFHKjEdRj9qiZ__T-c7qpKkOwWeM/edit?usp=sharing',
        'evaluacion_cuentas_prestamos_url':'https://docs.google.com/spreadsheets/d/17rfP_YBNHJFRDdES2FHqqq9AWAaubXyOx4_56N0H5lI/edit?usp=sharing',
        'entendimiento_control_interno_prestamos_url':'https://docs.google.com/document/d/1EJfhl75DpX4hU0h7NsZYBpVG1wavjfN2XsHOrDwvK8Q/edit?usp=sharing',
        'documentar_proceso_prestamos_url':'https://docs.google.com/document/d/1tBXbx_vp0UUBs0qwD7f8bzelUdlIMP-hxKr-SgfETws/edit?usp=sharing',
        'evaluacion_riesgos_prestamos_url':'https://docs.google.com/document/d/1aVHWU3DBavQpTX8JHPvP6XI7it6GVxw91qe7D-StSNk/edit?usp=sharing',
        'evaluar_eficacia_prestamos_url':'https://docs.google.com/document/d/18-JzuchnAtxxj-Ixpwl-7dSxFL6T7TEfADzAFujff5I/edit?usp=sharing',
        # Área de Patrimonio
        'cuestionario_evaluacion_patrimonio_url':'https://docs.google.com/document/d/1ifPeYjCfn_gHsYw8NCCam8-MOYKC5WrHRHgV5ycEswU/edit?usp=sharing',
        'evaluacion_cuentas_patrimonio_url':'https://docs.google.com/spreadsheets/d/1sNKnnS1wS1Y5t5fBxZOR-Usa-ng4X4oLg7Fj3urR2_k/edit?usp=sharing',
        'entendimiento_control_interno_patrimonio_url':'https://docs.google.com/document/d/1qAz4_RQrpy7jf_C7PZWHDAw1tl9Jll93yrCQuUp_iSc/edit?usp=sharing',
        'documentar_proceso_patrimonio_url':'https://docs.google.com/document/d/1v4f1n51j0lPPVzudtqkmHAiz7AgQoOvWkTBK643tRUo/edit?usp=sharing',
        'evaluacion_riesgos_patrimonio_url':'https://docs.google.com/document/d/1R1t01pz01bHKIofoQYUuYQd6G63vsC-wMkG2snPZgN8/edit?usp=sharing',
        'evaluar_eficacia_patrimonio_url':'https://docs.google.com/document/d/12VrWW6VYLnHHvujYm5SfD7Nvak8lYYEtK-BxZU1E4Jk/edit?usp=sharing',
        # Área de Nominas
        'cuestionario_evaluacion_nomina_url':'https://docs.google.com/document/d/1It6jLdlKV_sYZ-Ptd1KD4a_yoIFhqKiHdTPsSfwU8NM/edit?usp=sharing',
        'evaluacion_cuentas_nomina_url':'https://docs.google.com/spreadsheets/d/1iA3J0Rfe-MAP_dc_4Xpc5lg4kaFQpjOmUrMiAP3VYv4/edit?usp=sharing',
        'entendimiento_control_interno_nomina_url':'https://docs.google.com/document/d/1KXEey66SyfcnTCVEcjaUhQAk5frJtADndT5vkyg_DMw/edit?usp=sharing',
        'documentar_proceso_nomina_url':'https://docs.google.com/document/d/1EtSEThIFCjNnhClF_VBKFRLOhFf2ZQnudogR0ZOoP_s/edit?usp=sharing',
        'evaluacion_riesgos_nomina_url':'https://docs.google.com/document/d/1Ai7UXKVaNQTIMgCSUuAcCA5zwjGWNwB0A7unNYyYkys/edit?usp=sharing',
        'evaluar_eficacia_nomina_url':'https://docs.google.com/document/d/1mMa7DFbrjwoII-oXIlk0r5lsOQCk03MXKsqTcF_he_g/edit?usp=sharing',
        # Área de Impuestos
        'cuestionario_evaluacion_impuesto_url':'https://docs.google.com/document/d/1bbsi972GWL1c19eDW9UBTcpvBPh88sXKgdmiDsyQBDk/edit?usp=sharing',
        'evaluacion_cuentas_impuesto_url':'https://docs.google.com/spreadsheets/d/1tze1cKf6TOwGPks3Iwshn_OJiJhb2dqRznIDdXEvmpI/edit?usp=sharing',
        'entendimiento_control_interno_impuesto_url':'https://docs.google.com/document/d/1YicULLUK2MdmvF8X1xVhvdYPsZPjlO-IDXfDp0haJWw/edit?usp=sharing',
        'documentar_proceso_impuesto_url':'https://docs.google.com/document/d/1ITCA4fpy0mNiblx3cf_ZcInCEiZbnOJoeVv8wJDs7Y8/edit?usp=sharing',
        'evaluacion_riesgos_impuesto_url':'https://docs.google.com/document/d/1F3e1KMcpZCuvvhcmJJ33EAmLMDLZ3s58S4HFhOXUrwg/edit?usp=sharing',
        'evaluar_eficacia_impuesto_url':'https://docs.google.com/document/d/1QO2jd2aCF6yKcc7vwJQn0VxpwU5o1CJtqT08d-FzLqQ/edit?usp=sharing',
        # varios
        'horas_hombre_url':'https://docs.google.com/spreadsheets/d/1xT2zfg73JlgbYFrVtBt4ZywS79ffnGxlPzLYhyMYF5k/edit?usp=sharing',
        'cronograma_actividades_url':'https://docs.google.com/document/d/18vNAAVmF0EeX8SeAtY38C9VTNoujsCMmoakxwuuw7cc/edit?usp=sharing',
        'seguimiento_plan_url':'https://docs.google.com/spreadsheets/d/1YRu6d2hNUzhCKPOcERd3dhaKF38TAJjO3ibbdisSjww/edit?usp=sharing',


    }
    return render(request, 'planeacion.html', context)


@login_required
def ejecucion(request):
    context = {
        # Area Caja y bancos
        'auditoria_caja_bancos_url':'https://docs.google.com/document/d/1dIdzMq2CGUOd8PY2yRZqGYoCZpv_hJcdnP9blH4aGVg/edit?usp=sharing',
        'sumaria_caja_bancos_url':'https://docs.google.com/spreadsheets/d/16c0bjYSQLCLiRfvElUGzNff6tYoxawH7baIYTulBU2Y/edit?usp=sharing',
        'Arqueo_caja_url':'https://docs.google.com/spreadsheets/d/11g1163Ol8M4PqwIZPyigst9b-PqjFIgDnr7rZvBVjWg/edit?usp=sharing',
        'corte_cheques_url':'https://docs.google.com/spreadsheets/d/1RuGqtX-7S-uDFRxlI-lSpy7A_W20JkMfrhwRNGVeYZ4/edit?usp=sharing',
        'integracion_caja_chica_url':'https://docs.google.com/document/d/1OjOueYjpqKUWUBBjRpzSBJhUDzWP5LtUUyLibDMXpf4/edit?usp=sharing',
        'arqueo_caja_chica_url':'https://docs.google.com/document/d/12K6yqFeyJjem_P8VzY9wTrAqUIZUo-8h3BPietCahbE/edit?usp=sharing',
        'analitica_caja_chica_url':'https://docs.google.com/document/d/17F8UxQvzbDv9ZnJHxYxx97zWEO40zI5OviUtKwG7h7A/edit?usp=sharing',
        'conciliacion_bancaria_url':'https://docs.google.com/document/d/15M2hIZ08pGcleE9UU3ktcaopi0jzdw5_6IbWBmi2wSY/edit?usp=sharing',
        'conciliacion_bancaria_uno_url':'https://docs.google.com/document/d/1elZri73q_j1463AsfZ_qFtmCfN4r_vfmgBb9uK6Ro6A/edit?usp=sharing',
        'conciliacion_bancaria_dos_url':'https://docs.google.com/document/d/1WpLdRwpINfOb_rpd8WIWrWjwYtLD7iUZkhv6rMunVA4/edit?usp=sharing',
        'confirmacion_bancaria_url':'https://docs.google.com/document/d/1S1wYjaBZtPD_fMq0vO2LVI894ksAAcDC4WnRrSGunKM/edit?usp=sharing',
        'estado_cuenta_url':'https://docs.google.com/document/d/17MPfJRgYFXY_lhSjOrv-OgqdS9JsYP6Lr9J23Jp7Nzw/edit?usp=sharing',
        'confirmacion_bancaria_url':'https://docs.google.com/spreadsheets/d/18XL9WFc8rDn_yJN1PCb4msy4VVuXkp8oQrncztWD9Dc/edit?usp=sharing',
        'integracion_ingresos_url':'https://docs.google.com/spreadsheets/d/1gxla_8N999y3OF2J9fyvqYpCMxmJDWAKspRKhWZJqmI/edit?usp=sharing',
        'integracion_egresos_url':'https://docs.google.com/spreadsheets/d/1GU-bL0Kfu8Pd99_MfrttvaGXBx9ZCV3qtkDXpDBXIZc/edit?usp=sharing',
        'ingresos_caja_banco_url':'https://docs.google.com/spreadsheets/d/14UxQJD7CrZ0nYXh41qD9FdlGlddsnWJPy9Woh00TzAc/edit?usp=sharing',
        'egresos_caja_banco_url':'https://docs.google.com/spreadsheets/d/12E0x4FHsS2Ap_eoa875HeFboI_1-Y7N3pkEHNaaKBNk/edit?usp=sharing',
        'partida_ajuste_url':'https://docs.google.com/document/d/1iVTNTwHPF2lwc2raikeMJmhbcWjWg6osO_acMak4lIM/edit?usp=sharing',
        'partida_reclasificacion_url':'https://docs.google.com/document/d/1NaoQcoFsYJ6P1dmKAYgvU4roEDFBS4pcdj--j7C49mM/edit?usp=sharing',
        'cedula_marca_url':'https://docs.google.com/document/d/1FZ3enHMTooH9QzSu9_bdyVVcfLhkcrQnjuV2QuiqaAk/edit?usp=sharing',
        # Area Cuentas por cobrar
        'auditoria_cuentas_cobrar_url':'https://docs.google.com/document/d/1prsgnJ1cqSi2LvfK8oilgfqStqSCb9R3_IMahaRKXHs/edit?usp=sharing',
        'sumaria_cuentas_cobrar_url':'https://docs.google.com/spreadsheets/d/11UzADx261fFhJAPE5JqTbZGrrCcl_Br5HcOW9wKkyzY/edit?usp=sharing',
        'integracion_clientes_url':'https://docs.google.com/document/d/1vaC3lvyMrscqR_Zs4tC-X8K9OkcbMi1hgjuQLXi4O9Y/edit?usp=sharing',
        'integracion_deudores_url':'https://docs.google.com/document/d/1F9gFhjCn0TX96qLsJJSTPaZ9xPDjx1uYf3knhcAXs00/edit?usp=sharing',
        'circularizacion_clientes_url':'https://docs.google.com/document/d/15Itoqh4CQvJ_143PEEB0wa5WOspfLGPmGhjouBAWKeM/edit?usp=sharing',
        'circularizacion_clientes_uno_url':'https://docs.google.com/document/d/1rcrUB8Kdv__eB26VSskrHRIPfEU-RNGz-Bkn0YlbtmE/edit?usp=sharing',
        'circularizacion_clientes_dos_url':'https://docs.google.com/document/d/1eTbnSn-nSkbaJ41WgUGRewxe_xsQEhAxtVN0oIJGym0/edit?usp=sharing',
        'circularizacion_clientes_tres_url':'https://docs.google.com/document/d/1fnmLshZwb6Mv-qz5tYAojMMnZN8Hr5RqtNlYAAi9NmM/edit?usp=sharing',
        'circularizacion_clientes_cuatro_url':'https://docs.google.com/document/d/1GvWHIhMYqS9do5SxscalFyAcX9Sh3eBIwyaL5rcv4Lk/edit?usp=sharing',
        'circularizacion_clientes_cinco_url':'https://docs.google.com/document/d/1Ti1OM3eSFv3qHD_nmIWPilYhYrZsR_grHv80xd_sQuU/edit?usp=sharing',
        'circularizacion_url':'https://docs.google.com/document/d/1OuJHZBZRGZIRkV4dcPKuqbDI1pkKzYAT2jtF08wxsTA/edit?usp=sharing',
        'estadistica_circularizacion_url':'https://docs.google.com/document/d/1k5UDGGHtsBLl7cB9d5hjN9_sepWxX_0AzL6pZvftXws/edit?usp=sharing',
        'analisis_antiguedad_url':'https://docs.google.com/spreadsheets/d/1rhoupY4bsI_VZn2r6lnJkJzbRUuLEH8ES0GwYKd3JVs/edit?usp=sharing',
        'prueba_cobros_url':'https://docs.google.com/spreadsheets/d/1hOBIqieEhRyw9_1hadQ0W0NaJ3AZmSz3RtODhM5J3Ks/edit?usp=sharing',
        'corte_formas_url':'https://docs.google.com/document/d/1wZEkVwh1Ev92bjbKkg4aFGIsq1FGWzOJQa7geQyydNc/edit?usp=sharing',
        'cuentas_incobrables_url':'https://docs.google.com/document/d/1NlayQCa06EWyNOzaFdwAha8C2hOMb5x-DzOakrXSV4w/edit?usp=sharing',
        'partida_ajustes_url':'https://docs.google.com/document/d/1wsDusd_ZKpGlZRJ6tMPucax8VUWDLePouuWu1H-BafE/edit?usp=sharing',
        'partida_reclasificacion_url':'https://docs.google.com/document/d/1uZZKVzIAx_4EzwCzEQTv9IdUhuUr4MFwz8nDdBoGE0s/edit?usp=sharing',
        'cedula_reclasificacion_url':'https://docs.google.com/document/d/1v3mPdUsyM7fY2pfrJ_E6kSOkjoHb8OuODhJtOKRBBg4/edit?usp=sharing',
        
    }
    return render(request, 'ejecucion.html', context)