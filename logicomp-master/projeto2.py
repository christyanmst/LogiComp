#pip install pandas

import pandas as pd
from pathlib import Path

arquivo= pd.read_csv(Path(__file__).parent /'arquivos_pacientes/column_bin_5a_3p.csv' ,sep=',')
arquivo.index += 1
print(arquivo)
