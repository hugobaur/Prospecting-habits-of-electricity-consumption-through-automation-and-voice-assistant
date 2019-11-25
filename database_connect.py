import sqlalchemy, os
import pandas as pd
import datetime


def ler_aws():

    db_connection_str = 'mysql+pymysql://admin:98970242@aa1wojbkfs1xdfb.czzvknxexeho.us-east-1.rds.amazonaws.com/house'
    db_connection = sqlalchemy.create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM carga', con=db_connection)

    return df


def inserir_csv(valor1, valor2, valor3, valor4):
    carga = {'id': [valor1],
            'id_carga': [valor2],
            'datetime': [datetime.datetime.now()],
            'carga': [valor3],
            'id_usuario': [valor4]
        }

    df = pd.DataFrame(carga, columns=['id', 'id_carga', 'datetime', 'carga', 'id_usuario'])
    if os.path.isfile('./export_dataframe.csv'):
        df.to_csv (r'C:\Users\hugob\PycharmProjects\Prospecting-habits-of-electricity-consumption-through-automation-and-voice-assistant\export_dataframe.csv', mode ='a', index = None, header=False) #Don't forget to add '.csv' at the end of the path
    else:
        df.to_csv(
            r'C:\Users\hugob\PycharmProjects\Prospecting-habits-of-electricity-consumption-through-automation-and-voice-assistant\export_dataframe.csv',
            mode='a', index=None, header=True)

    return df


def csv_to_aws():

    db_connection_str = 'mysql+pymysql://admin:98970242@aa1wojbkfs1xdfb.czzvknxexeho.us-east-1.rds.amazonaws.com/house'
    db_connection = sqlalchemy.create_engine(db_connection_str)

    df = pd.read_csv(r'C:\Users\hugob\PycharmProjects\Prospecting-habits-of-electricity-consumption-through-automation-and-voice-assistant\export_dataframe.csv')

    with db_connection.connect() as conn, conn.begin():
        df.to_sql('carga', conn, if_exists='append', index=False)

    os.remove(r'C:\Users\hugob\PycharmProjects\Prospecting-habits-of-electricity-consumption-through-automation-and-voice-assistant\export_dataframe.csv')

    return "Enviado para AWS CLOUD e deletado banco local"


if __name__ == '__main__':
    # print(ler_aws())
    # print(inserir_csv('6','6','6','6'))
    csv_to_aws()
    # print(ler_aws())

