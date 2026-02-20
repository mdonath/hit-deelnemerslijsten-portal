import pyminizip
import os
import shutil
from pathvalidate import sanitize_filename
from config import current_privacy_doc_file, current_property
from log import log_ok
from passwords import create_password_kamp, create_password_plaats, write_password_file, write_plaats_password_file


COMPRESSION_LEVEL = 1


def write(df, hit_config):
    output_path = current_property(hit_config, 'output_path')

    # Totaalbestand met alles
    df.to_excel(os.path.join(output_path, 'totaal.xlsx'), index=False)
    log_ok("Totaal bestand is klaar")

    plaats_passwords = {}

    # Maak bestand per plaats
    for plaats, plaats_deelnemers in df.groupby('Plaats'):
        plaats = sanitize_filename(plaats)
        plaats_path = os.path.join(output_path, plaats)
        shutil.rmtree(plaats_path, ignore_errors=True)
        output_path_plaats = create_path_if_not_exists(plaats_path)
        write_files(output_path_plaats, plaats, plaats_deelnemers)

        passwords = {}

        password = create_password_plaats(plaats, hit_config)
        passwords['C-team'] = password
        plaats_passwords[plaats] = password

        zip_excels(output_path_plaats, output_path_plaats, f'C-team HIT {plaats}', password, hit_config)

        # Maak bestand per kamp
        per_kamp = plaats_deelnemers.groupby('Kamp')
        for kamp, kamp_deelnemers in per_kamp:
            kamp = sanitize_filename(kamp)
            output_path_kamp = create_path_if_not_exists(os.path.join(output_path, plaats, kamp))
            write_files(output_path_kamp, kamp, kamp_deelnemers)

            password = create_password_kamp(kamp, hit_config)
            passwords[kamp] = password
            zip_excels(output_path_plaats, output_path_kamp, kamp, password, hit_config)

        write_password_file(output_path_plaats, passwords, hit_config)

        zip_zips(output_path, os.path.join(output_path, plaats), plaats, hit_config)

        write_plaats_password_file(output_path, plaats_passwords, hit_config)
        log_ok(f"{plaats} is klaar met {len(per_kamp)} kampen")


def write_files(output_path, naam, df):
    write_alles_file(output_path, naam, df)
    write_medisch_file(output_path, naam, df)
    write_foerage_file(output_path, naam, df)

def write_alles_file(output_path, naam, df):
    df.to_excel(os.path.join(output_path, f"{naam}-alles.xlsx"), index=False)
    write_filtered_file(
        output_path,
        naam,
        df,
        None,
        df.columns.values.tolist(),
        'alles.xlsx'
    )


def write_medisch_file(output_path, naam, df):
    write_filtered_file(
        output_path,
        naam,
        df,
        '`Aandachtspunten`.notnull()',
        [
            'Kamp',
            'Subgroep',
            'Voornaam',
            'Achternaam',
            'Geboortedatum',
            'Dieet',
            'Aandachtspunten',
            'Naam noodcontact',
            'Telefoonnummer noodcontact',
            'Relatie tot deelnemer'
        ],
        'medisch.xlsx'
    )


def write_foerage_file(output_path, naam, df):
    write_filtered_file(
        output_path,
        naam,
        df,
        '`Aandachtspunten`.notnull() or `Dieet`.notnull()',
        [
            'Kamp',
            'Subgroep',
            'Voornaam',
            'Achternaam',
            'Dieet',
            'Aandachtspunten',
        ],
        'foerage.xlsx'
    )


def write_filtered_file(output_path, naam, df, filter, columns, suffix):
    filtered = df.query(filter) if filter else df
    filtered = filtered[columns]
    filtered.to_excel(os.path.join(output_path, f'{naam}-{suffix}'), index=False)


def zip_excels(output_path, files_path, naam, password, hit_config):
    te_zippen = [
        current_privacy_doc_file(hit_config),
    ]
    for file in os.listdir(files_path):
        if file.endswith('.xlsx'):
            te_zippen.append(os.path.join(files_path, file))

    pyminizip.compress_multiple(
        te_zippen,
        [],
        os.path.join(output_path, f"{naam}.zip"),
        password,
        COMPRESSION_LEVEL
    )


def zip_zips(output_path, files_path, plaats, hit_config):
    te_zippen = [
        current_privacy_doc_file(hit_config),
        os.path.join(files_path, current_property(hit_config, 'passwords_file')),
    ]
    for file in os.listdir(files_path):
        if file.endswith('.zip'):
            te_zippen.append(os.path.join(files_path, file))

    password = create_password_plaats(plaats, hit_config)

    pyminizip.compress_multiple(
        te_zippen,
        [],
        os.path.join(output_path, f"{plaats}.zip"),
        password,
        COMPRESSION_LEVEL
    )


def create_path_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path
