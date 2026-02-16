import pandas as pd
from log import log_finished


def main():
    # Laad het Excel-bestand
    csv = pd.read_excel('output/totaal.xlsx')

    # Zoek de incomplete groepjes
    df = transform(csv)

    # Sla het bestand op
    df.to_excel('output/incompleet.xlsx', index=False)
    
    log_finished("OK")


def transform(input):
    # Beperk de kolommen tot wat nodig is voor de analyse
    output = input[['Plaats', 'Kamp', 'Subgroep', 'Subgroepgrootte']]
    # Tel het aantal deelnemers met dezelfde Plaats, Kamp en Subgroep
    output = output.groupby(['Plaats', 'Kamp', 'Subgroep', 'Subgroepgrootte'])['Subgroep'].count().reset_index(name='count')
    # Filter de rijen waar het aantal deelnemers kleiner is dan de Subgroepgrootte
    output = output[output['count'] < output['Subgroepgrootte']]

    # Merge met de originele data om de ontbrekende informatie te krijgen
    output = pd.merge(output, input, on=['Plaats', 'Kamp', 'Subgroep'], suffixes=('_df', '_csv'))
    # Selecteer alleen de relevante kolommen voor de output
    output = output[[
        'Plaats',
        'Kamp',
        'Subgroep',
        'Subgroepgrootte_csv',
        'count',
        'Voornaam',
        'Achternaam',
        'Mailadres',
        'Mobiel'
        ]]
    output.rename(columns={'Subgroepgrootte_csv': 'Subgroepgrootte'}, inplace=True)

    return output

if __name__ == "__main__":
    main()
