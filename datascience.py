import pandas as pd

data = {
        'Alunos': ['Ederson','Jorge'],
        'Idade': [20,50],
        'Notas': [8,9]
        }

df = pd.DataFrame(data, columns=['Alunos', 'Idade', 'Notas'])