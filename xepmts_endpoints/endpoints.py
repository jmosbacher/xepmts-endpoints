"""Main module."""
import os
import pathlib
from .utils import read_endpoint_files, resources_from_templates

SOURCE_DIR = pathlib.Path(__file__).parent
DEFAULT_TEMPLATE_DIR = SOURCE_DIR / "endpoint_templates"

def get_endpoints(template_dir=DEFAULT_TEMPLATE_DIR.absolute(), endpoint_dir=None):
    templates = read_endpoint_files(template_dir)
    endpoints = resources_from_templates(templates)
    if endpoint_dir:
        endpoints.update(read_endpoint_files(endpoint_dir))
    return endpoints
