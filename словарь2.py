a=('Разработка языка Python была начата в конце 1980-х годов[18] сотрудником голландского института CWI Гвидо ван \n' \
  ' Россумом. Для распределённой ОС Amoeba требовался расширяемый скриптовый язык, и Гвидо начал писать Python на \n' \
  ' досуге, позаимствовав некоторые наработки для языка ABC (Гвидо участвовал в разработке этого языка,\n' \
  ' ориентированного на обучение программированию). В феврале 1991 года Гвидо опубликовал исходный текст в группе \n' \
  'новостей alt.sources[19]. С самого начала Python проектировался как объектно-ориентированный язык.').split()
d={}
for b in a:
    d[b]=d.get(b,0)+1
f=max(list(d.values()))
for key,value in d.items():
    if value==f:
        m=key
print(m)
# В тексте слово Python последнее, а в словаре - нет.код выводит последний макимальный ключ в словаре.