from database import engine, Base
from models import Player, Position 

# Criar as tabelas no banco de dados
print("Criando tabelas...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")