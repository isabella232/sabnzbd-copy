#! /usr/bin/python3
import sys
import os
import re
import shutil
import json

class SabnzbdCopy:

  def run(self, directory, category):
    print("Running post-process script for ", directory)

    #read configuration
    home = os.path.expanduser("~")
    config_path = os.path.join(home, ".sabnzbd-copy")
    read_config = self.read_configuration(config_path)
    if not read_config:
      return 1

    if category not in self.categories:
      print("Category " + category + " is not configured")
      return 1 

    largest_file = self.get_largest_file(directory)
    if largest_file is None:
      print("Could not find largest file")
      return 1
    new_dir = self.get_directory_to_move_to(largest_file, category)
    self.move_file(largest_file,new_dir)
    print("Done processing ", directory)
    return 0

  def move_file(self, file_path,new_dir):
    target_dir = os.path.join(self.base_path,new_dir)
    print("Moving " + file_path + " to " + target_dir)
    shutil.move(file_path,target_dir)  
    file_name = os.path.basename(file_path)
    new_file_path = os.path.join(target_dir,file_name)
    print("Setting permissions for file ", new_file_path)
    os.chmod(new_file_path,0o664)  
    print("Updating timestamp of file ", new_file_path)
    os.utime(new_file_path,None)

  def get_largest_file(self, directory):
    largest_file = self.get_largest_file_rec(directory,None)
    if largest_file is None:
      return None
    else:
      return largest_file[0]

  def get_largest_file_rec(self, directory, largest_file):
    for file_path in os.listdir(directory):
      file_path = os.path.join(directory,file_path)
      if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        if largest_file is None or file_size > largest_file[1]:
          largest_file = (file_path, file_size)
      elif os.path.isdir(file_path):
        largest_file = self.get_largest_file_rec(file_path, largest_file)
    return largest_file

  def get_directory_to_move_to(self, file_path, category):
    config = self.categories[category]
    if "patterns" in config:
      file_name = os.path.basename(file_path)
      for folder, folder_patterns in config["patterns"].items():
        for folder_pattern in folder_patterns:
          regex = re.compile(folder_pattern, re.IGNORECASE)
          if(regex.match(file_name)):
            return config["subFolder"] + "/"  + folder 
    print("Could not determine new directory for file " + file_path)
    if "miscFolder" in config:
      return config["subFolder"] + "/" + config["miscFolder"]
    else:
      return config["subFolder"] 

  def read_configuration(self, config_path):
    try:
      json_data_file =  open(config_path)
      config_data = json.load(json_data_file)
      self.categories = config_data["categories"]
      self.base_path = config_data["basePath"]
      return True
    except ValueError as e:
      print("Config file " + config_path + " has invalid format: " + str(e))
    except FileNotFoundError:
      print("Could not find config file at " + config_path)
    finally:
      json_data_file.close()
    return False



