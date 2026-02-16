import os
import yaml


def read_config(config_file='hit.yaml'):
    return yaml.safe_load(open(config_file))


def current_year(hit_config):
    return hit_config['current_year']


def current_property(hit_config, property_name):
    hit = [hit for hit in hit_config['hits'] if hit['year'] == current_year(hit_config)][0]
    return hit[property_name]


def current_privacy_doc_file(hit_config):
    doc_path = current_property(hit_config, 'documents_path')
    fmt = current_property(hit_config, 'privacy_doc_file_fmt')
    year = current_year(hit_config)
    return os.path.join(doc_path, fmt.format(year))
