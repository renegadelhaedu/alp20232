pop_pocoJM = 8000
pop_JOCA = 20000
anos = 0

while(pop_pocoJM < pop_JOCA):
    anos = anos + 1

    pop_pocoJM = pop_pocoJM * 1.03 #aumentando 3%
    pop_JOCA = pop_JOCA * 1.015 #aumentando 1,5%

pop_JOCA = int(pop_JOCA)
pop_pocoJM = int(pop_pocoJM)

print(f'em {anos} anos a cidade de poço jose de moura deixará de ser menor que joca claudino')
print(f'administrada pelo prefeito matheus rian, chegou a ter {pop_pocoJM} habitantes')
print(f'administrada pelo prefeito felipe, chegou a ter {pop_JOCA} habitantes')

