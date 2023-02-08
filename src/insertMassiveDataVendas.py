import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd


endereco = "local path file .csv"
vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";")
# if xlsx file use ->  variable = pd.read_excel(endereco + "ResponsavelDP.xlsx")

tbVendedor = pd.DataFrame(vendedor)

engine = sa.create_engine("sqlite:///BD/vendas.db")

conn = engine.connect()
metadata = sa.schema.MetaData(bind=engine)
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

# Client
DadosCliente = tbVendedor.to_dict(orient="records")
tabela_Cliente = sa.Table(vd.cliente.__tablename__, metadata, autoload=True)

try:
    conn.execute(tabela_Cliente.insert(), DadosCliente)
    sessao.commit()
except ValueError:
    ValueError()

print("Dados inseridos na tbDP")

sessao.close()
print("Carga de dados finalizada.")
