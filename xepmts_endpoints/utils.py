import os
from copy import deepcopy

from .config import EXPERIMENTS, INCLUDE_AS_IS

def deep_find_files(path, extensions):
    paths = []
    if not os.path.isdir(path):
        raise ValueError("{} is not a valid directory".format(path))
    for root, dirs, files in os.walk(path):
        for fname in files:
            if fname.split(".")[-1] in extensions:
                paths.append(os.path.join(root, fname))
    return paths

def find_yaml_files(path):
    return deep_find_files(path, ["yaml", "yml"])

def find_json_files(path):
    return deep_find_files(path, ["json"])

def read_endpoint_files(root):
    import yaml
    import json
    import os
    domain = {}
    for path in find_yaml_files(root): 
        with open(path, "r") as f:
            domain.update(yaml.safe_load(f))

    for path in find_json_files(root): 
        with open(path, "r") as f:
            domain.update(json.safe_load(f))
    return domain

def read_endpoint_dirs(roots):
    domain = {}
    for root in roots:
        domain.update(read_endpoint_files(root))


def resources_from_templates(templates, experiments=EXPERIMENTS,
                             include_as_is=INCLUDE_AS_IS,
                            ):
    resources = {}
    for experiment_name, experiment in experiments.items():
        for detector in experiment["detectors"]:
            for name, resource in templates.items():
                if name in include_as_is:
                    resources[name] = resource
                    continue
                new_resource = deepcopy(resource)
                new_resource["item_title"] = "_".join([detector, new_resource["item_title"], experiment["name_suffix"]]).strip("_").title().replace("_", " ")
                new_resource["resource_title"] = "_".join([detector, new_resource["resource_title"], experiment["name_suffix"]]).strip("_").title().replace("_", " ")
                
                new_resource["url"] = '/'.join([experiment["url_prefix"], detector, new_resource.get("url", name)]).strip("/")
                new_resource["datasource"]["source"] = f'{detector}_{new_resource["datasource"]["source"]}'
                if experiment["name_suffix"]:
                    new_resource["datasource"]["source"] += f'_{experiment["name_suffix"]}'
                if "experiment" in new_resource["schema"]:
                    new_resource["schema"]["experiment"]["default"] = experiment_name
                if "detector" in new_resource["schema"]:    
                    new_resource["schema"]["detector"]["default"] = detector
                
                new_resource["mongo_prefix"] = experiment["mongo_prefix"]
                new_name = "_".join([experiment_name, detector, name])
    
                resources[new_name] = new_resource
                # resources[detector.capitalize() + name + experiment["name_suffix"]] = new_resource
    return resources

