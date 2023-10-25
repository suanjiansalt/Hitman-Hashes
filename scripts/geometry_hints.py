import os
import json
import re

dir_path = 'E:\\game-file-extensions\\TEMP\\'  # Using the TEMP folder generated by QNE's GFE script (blueprint hashes below will need to be changed to paths if you use files extracted by the RPKG Tool)

matched_entities = {}

# Removes numbers from the end of the entity name
pattern = re.compile(r'(_\d+|\d+)$')

for filename in os.listdir(dir_path):
    if filename.endswith('.entity.json'):
        full_path = os.path.join(dir_path, filename)
        
        with open(full_path, 'r') as file:
            data = json.load(file)
            
            for entity in data['entities'].values():
                blueprint = entity.get('blueprint', '')
                if blueprint.endswith('008130A85A690BE8') or blueprint.endswith('00C7E348A80A6E6E') or blueprint.endswith('002E141E1B1C6EFE'):
                    name = pattern.sub('', entity.get('name', ''))
                    factory = entity.get('factory', '')
                    matched_entities[factory] = f"{factory}.TEMP,{name}"

for entity in matched_entities.values():
    print(entity)