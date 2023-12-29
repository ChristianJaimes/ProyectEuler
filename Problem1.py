def multiplos(numero):
    return numero % 5 == 0 or numero % 3 == 0

def suma_naturales_hasta(end_number):
    sum = 0
    for i in range(1,int(end_number)):
        if multiplos(i):
            sum += i      
    return sum

if __name__ == '__main__':  
    suma =suma_naturales_hasta(1000)
    print(f'El resultado es: {suma}')