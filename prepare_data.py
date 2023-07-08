import csv

def prepare_data():
    with open('./data/armas.csv', 'r', encoding='utf-8', errors='replace') as armas:
        lector = csv.DictReader(armas)
        armas = [arma for arma in lector]
        tipos = list(set(arma["TIPO DE ARMA"].lower() for arma in armas))
        acc=''
        for tipo in tipos:
            filtered = list(filter(lambda arma: arma["TIPO DE ARMA"].lower() == tipo, armas))
            acc +=  f"El arma tipo {tipo.upper()} tuvo:\n"\
            
            for arma in filtered:
                cantidad = arma['CANTIDAD RETENIDA']
                mes = arma['MES']
                anio = arma['ANO']
                acc +=  f"\t-Una Cantidad retenida de {cantidad} unidades, en {mes} del {anio}\n" \

            acc += '-' * 60 + '\n\n'

        archivo_texto = open("./data/armas.txt", "w", encoding="utf-8", errors='replace')
        archivo_texto.write(acc)
