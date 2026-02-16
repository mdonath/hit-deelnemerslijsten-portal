import pandas as pd


def transform(df):
    # Split rows with multiple participants
    parents = split_parents(df)
    extra = split_extra_child(df)
    df = pd.concat([df, parents, extra], ignore_index=True)

    # Sort rows
    df = df.sort_values(['Plaats', 'Kamp', 'Subgroep'])

    # Sort columns
    df = df[['Plaats',
             'Kamp',
             'Subgroep',
             'Subgroepgrootte',
             'Lidnummer',
             'Voornaam',
             'Achternaam',
             'Gender',
             'Geboortedatum',
             'Mailadres',
             'Mobiel',
             'Zwemdiploma',
             'Dieet',
             'Aandachtspunten',
             'Naam noodcontact',
             'Telefoonnummer noodcontact',
             'Relatie tot deelnemer'
    ]]

    # Clean up 'Dieet' column
    df = clean_up_mobiel(df)
    df = clean_up_dieet(df)
    df = clean_up_aandachtspunten(df)

    return df


def split_parents(df):
    parents = df.query('`Voornaam.1`.notnull() or `Achternaam.1`.notnull()', inplace=False)
    return pd.DataFrame(parents.apply(lambda row: {
        'Kamp': row['Kamp'],
        'Plaats': row['Plaats'],
        'Subgroep': row['Subgroep'],
        'Subgroepgrootte': row['Subgroepgrootte'],
        # 'Lidnummer': '---',
        'Voornaam': row['Voornaam.1'],
        'Achternaam': row['Achternaam.1'],
        'Gender': row['Gender.1'],
        'Geboortedatum': row['Geboortedatum.1'],
        'Mailadres': row['Mailadres.1'],
        'Mobiel': row['Mobiel.1'],
        # 'Zwemdiploma': '---',
        'Dieet': row['Dieet.1'],
        'Aandachtspunten': row['Aandachtspunten.1'],
        'Naam noodcontact': row['Naam noodcontact'],
        'Telefoonnummer noodcontact': row['Telefoonnummer noodcontact'],
        'Relatie tot deelnemer': row['Relatie tot deelnemer']
    }, axis=1).tolist())

def split_extra_child(df):
    extra_child = df.query('`Voornaam.2`.notnull() or `Achternaam.2`.notnull()', inplace=False)
    return pd.DataFrame(extra_child.apply(lambda row: {
        'Kamp': row['Kamp'],
        'Plaats': row['Plaats'],
        'Subgroep': row['Subgroep'],
        'Subgroepgrootte': row['Subgroepgrootte'],
        #'Lidnummer': '---',
        'Voornaam': row['Voornaam.2'],
        'Achternaam': row['Achternaam.2'],
        'Gender': row['Gender.2'],
        'Geboortedatum': row['Geboortedatum.2'],
        #'Mailadres': '---',
        'Mobiel': row['Mobiel.2'],
        'Zwemdiploma': row['Zwemdiploma.2'],
        'Dieet': row['Dieet.2'],
        'Aandachtspunten': row['Aandachtspunten.2'],
        'Naam noodcontact': row['Naam noodcontact'],
        'Telefoonnummer noodcontact': row['Telefoonnummer noodcontact'],
        'Relatie tot deelnemer': row['Relatie tot deelnemer']
    }, axis=1).tolist())


def clean_up_dieet(df):
    df.replace({'Dieet': 'none'}, None, inplace=True)
    return df

def clean_up_aandachtspunten(df):
    df = df.replace({
        'Aandachtspunten':
        {
            '-': None,
            '/': None,
            'x': None,
            'X': None,
            'nvt': None,
            'nvt.': None,
            'n.v.t': None,
            'n.v.t.': None,
            'N.v.t': None,
            'N.v.t.': None,
            'Nvt': None,
            'Nvt.': None,
            'NvT': None,
            'NVT': None,
            'N.V.T': None,
            'N.V.T.': None,
            'NVT -': None,
            'Ne': None,
            'Nee': None,
            'nee': None,
            'Nah': None,
            'nope': None,
            'nee.': None,
            'Nee.': None,
            'Neej': None,
            'Nee!': None,
            'nee -': None,
            'Nee -': None,
            'neen': None,
            'Neen': None,
            'net': None,
            'Allen nee.': None,
            'Nope': None,
            'geen': None,
            'Geen': None,
            'niet bekend': None,
            'negatief': None,
            'Negatief': None,
            'nuh uh': None,
            'geen allergie': None,
            'Geen allergie': None,
            'geen beperkingen en geen medicijnen': None,
            'geen allergie en geen medicijnen': None,
            'niet naar wij weten': None,
            'Nee dat heeft de deelnemer niet.': None,
            'nee geen bijzonderheden': None,
            'Nee geen bijzonderheden': None,
            'niet van toepassing': None,
            'Niet van toepassing': None,
            'Niet van toepassing.': None,
            'Normaal gesproken nergens last van': None,
        }}, inplace=True)
    return df

def clean_up_mobiel(df):
    df.replace({
        'Mobiel': {
            '0': None,
            '06': None,
            '000': None,
            'geen': None,
            'Geen': None,
            'geen telefoon': None,
            'nvt': None,
            'N.v.t.': None,
            '-': None,
            'x': None,
            '/': None,
            'heb ik niet': None,
            'geen mobiel': None,
            'geen mobiel toegestaan op dit kamp': None,
            'geen telefoon mee': None,
            'n.v.t. (geen telefoon mee)': None,
            'Zie ouder': None,
        }}, inplace=True)
    return df

