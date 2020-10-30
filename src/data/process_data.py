import argparse
import pandas as pd


def process(year: str):
    """Import data and make initial process.

    Args:
        year (str): Year to process.
    """
    columns = ['NU_IDADE', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',
            'IN_BAIXA_VISAO', 'IN_CEGUEIRA', 'IN_SURDEZ', 'IN_DEFICIENCIA_AUDITIVA',
            'IN_SURDO_CEGUEIRA', 'IN_DEFICIENCIA_FISICA', 'IN_DEFICIENCIA_MENTAL',
            'IN_DEFICIT_ATENCAO', 'IN_DISLEXIA', 'IN_DISCALCULIA', 'IN_AUTISMO',
            'IN_VISAO_MONOCULAR', 'IN_OUTRA_DEF',
            'Q001', 'Q002', 'Q003', 'Q004', 'Q005', 'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q011',
            'Q012', 'Q013', 'Q014', 'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022',
            'Q023', 'Q024', 'Q025', 'Q026', 'Q027', 'NU_NOTA_REDACAO']

    raw_file = '../../data/raw/MICRODADOS_ENEM_%s.csv' % year

    df = pd.read_csv(raw_file,
                    encoding='latin-1',
                    delimiter=';',
                    usecols=columns,
                    nrows=1000000)

    # Removing rows without essay score - NU_NOTA_REDACAO.
    na_output = df['NU_NOTA_REDACAO'].isna()
    df = df.loc[na_output, :]

    # Save processed_data.csv
    processed_file = '../../data/processed/MICRODADOS_ENEM_%s.csv' % year
    df.to_csv(processed_file, encoding='latin-1')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process huge CSV data.')
    parser.add_argument('year',
                        metavar='year',
                        type=str,
                        help='Year of data.')
    args = parser.parse_args()

    process(year=args.year)
