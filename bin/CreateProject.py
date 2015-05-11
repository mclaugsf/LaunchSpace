"""
Create a project within the local configuration database.
"""
import os
import sys

# Add relative path libraries
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.sep.join([SCRIPT_DIR, "..", "lib"])))
sys.path.append(os.path.abspath(os.path.sep.join([SCRIPT_DIR, "..", "..", "basespace-python-sdk", "src"])))

from BaseSpacePy.api.BaseSpaceAPI import BaseSpaceAPI

from ConfigurationServices import ConfigurationServices
from DataAccessCreate import DataAccessCreate

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Create a project')
    parser.add_argument('-n', '--name', type=str, required=True, dest="name", help='name of project')
    parser.add_argument('-p', '--path', type=str, required=True, dest="path", help='path where project should write')

    args = parser.parse_args()

    baseSpaceAPI = BaseSpaceAPI()
    configuration_services = ConfigurationServices()
    db_config = configuration_services.get_config("DBFile")
    data_access_create = DataAccessCreate(db_config, configuration_services)

    if not os.path.exists(args.path):
        print "must specify an output directory that already exists!"
        sys.exit(1)

    print "attempting to create/retrieve BaseSpace project"
    project = baseSpaceAPI.createProject(args.name)
    print "got Id: %s" % project.Id
    data_access_create.add_project(args.name, args.path, project.Id)
