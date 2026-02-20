import os
import pandas as pd

from config import current_property


def load(hit_config):
    """
    Laadt het Excel-bestand met de inschrijvingen en bewerkt deze zodat deze makkelijker te gebruiken is.
    
    :param hit_config: Description
    """
    input_path = current_property(hit_config, 'input_path')
    input_file = [f for f in os.listdir(input_path) if f.endswith('.xlsx')][0]
    df = pd.read_excel(os.path.join(input_path, input_file))

    preprocess(df)

    return df


def preprocess(df):
    """
    Bewerkt de data zodat deze minder data bevat die niet relevant is voor de analyse, en zodat de kolomnamen makkelijker te gebruiken zijn.
    
    :param df: DataFrame met de ruwe data van de inschrijvingen.
    :return: DataFrame met de bewerkte data.
    """
    drop_columns(df)
    rename_columns(df)


def drop_columns(df):
    """
    Verwijdert onnodige kolommen.
    
    :param df: DataFrame met de ruwe data van de inschrijvingen.
    :return: DataFrame zonder onnodige kolommen.
    """

    # Verwijder newlines in de namen van de kolommen
    df.columns = [col.replace('\n', '') for col in df.columns]
    

    # Verwijder onnodige kolommen
    df.drop(columns=[
        'Registration ID',
        'Registration Status',
        'Payment Status',
        'Registration Phase',
        'Registration Date',
        'Last Updated',
        'User Email',
        'User Display Name',
        'WooCommerce Order ID',
        # 'Event Name',
        'Event ID',
        'Event Status',
        'Participation Cost',
        'Parent-Child Event',
        'Minimum Age',
        'Maximum Age',
        'Max Participants',
        'Site Name',
        # 'Site Location',
        'Project Name',
        'Project Year',
        # 'Subgroup Name',
        'Subgroup ID',
        'Subgroup Max Members',
        # 'Subgroup Current Members',
        'HIT Plaats',
        'HIT Kamp',
        'Ouder-kind kamp',
        'Alleen ouder lid ok?',
        'Minimum geboortedatum',
        'Maximum geboortedatum',
        'Minimum geboortedatum ouder',
        'Maximum geboortedatum ouder',
        'Min deelnemers',
        'Max deelnemers',
        'Subgroep min aantal',
        'Subgroep max aantal',
        'Subgroep min grootte',
        'Subgroep max grootte',
        'Subgroep deelbaar door',
        'Als wie schrijf je in?',
        # 'Lidnummer',
        # 'Voornaam',
        # 'Achternaam',
        # 'Gender',
        # 'Geboortedatum',
        # 'Mailadres',
        # 'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT',
        # 'Heb je een zwemdiploma?',
        # 'Dieet',
        # 'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht.',
        # 'Naam noodcontact',
        # 'Telefoonnummer noodcontact',
        # 'Relatie tot deelnemer',
        # 'Voornaam.1',
        # 'Achternaam.1',
        # 'Gender.1',
        # 'Geboortedatum.1',
        # 'Mailadres.1',
        # 'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT.1',
        # 'Dieet.1',
        # 'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?.1',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht..1',
        # 'Voornaam.2',
        # 'Achternaam.2',
        # 'Gender.2',
        # 'Geboortedatum.2',
        # 'Telefoonnummer van de mobiele telefoon die je mee neemt naar de HIT.2',
        # 'Heb je een zwemdiploma?.1',
        # 'Dieet.2',
        # 'Heeft de deelnemer een allergie, lichamelijke of geestelijke beperkingen of gebruikt hij/zij medicijnen?.2',
        'De ouder/verzorger of deelnemer (18 jaar of ouder) gaat er mee akkoord dat medisch handelen is toegestaan, als een arts dit noodzakelijk acht..2',
        'Selecteer een subgroepje',
        'Hoeveel deelnemers komen er in je subgroepje?'
    ], inplace=True)


def rename_columns(df):
    """
    Hernoemt kolommen zodat ze makkelijker te gebruiken zijn.
    
    :param df: DataFrame met de ruwe data van de inschrijvingen.
    :return: DataFrame met de hernoemde kolommen.
    """
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

