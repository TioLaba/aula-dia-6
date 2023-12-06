import calendar

# Criando um objeto de calendário
cal = calendar.TextCalendar(calendar.SUNDAY)

# Exibindo o calendário de um mês específico
calendario_do_mes = cal.formatmonth(2023, 12)
print(calendario_do_mes)
