import os
import pandas as pd

from config import current_property

INPUT_DIR = 'input'

def load(hit_config):
    input_path = current_property(hit_config, 'input_path')
    input_file = [f for f in os.listdir(input_path) if f.endswith('.xlsx')][0]
    df = pd.read_excel(os.path.join(input_path, input_file))

    # Preprocess the data by dropping unnecessary columns and renaming the remaining ones
    df = preprocess(df)

    return df

def preprocess(df):
    # Drop unnecessary columns
    df = df.drop(columns=[
        'Registration ID',
        'Registration Status',
        'Payment Status',
        'Registration Phase',
        'Registration Date',
        'Event ID',
        'Subgroup ID',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht.',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht..1',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht..2',
        'Gegevens ouder',
        'Gegevens kind',
        'Selecteer een subgroepje',
        'Hoeveel deelnemers komen er in je subgroepje?'
    ])

    # Rename columns for easier access
    df.rename(columns={
        'Site Location': 'Plaats',
        'Event Name': 'Kamp',
        'Subgroup Name': 'Subgroep',
        'Subgroup Current Members': 'Subgroepgrootte',
        'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT': 'Mobiel',
        'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT.1': 'Mobiel.1',
        'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT.2': 'Mobiel.2',
        'Heb je een zwemdiploma?': 'Zwemdiploma',
        'Heb je een zwemdiploma?.1': 'Zwemdiploma.2',
        'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?': 'Aandachtspunten',
        'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?.1': 'Aandachtspunten.1',
        'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?.2': 'Aandachtspunten.2',
    }, inplace=True)
    
    return df

