def print_params ( a= 125, b='строка', c= True):
    print (a,b,c)


list_= [1,2,3]

   #1.Функция с параметрами по умолчанию:
print_params ( )

print_params( 9, 8, 'grom')
print_params( a='dom', b= 12, c= False)
print_params ( b=25 )
print_params ( c=[1,2,3])

print_params (*list_)

            # 2.Распаковка параметров:

values_list = [ True, "Stroka", 8]
values_dict = {'a': True, 'b': 100, 'c': "remont"}

print_params(*values_list)
print_params(**values_dict)

 #3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

