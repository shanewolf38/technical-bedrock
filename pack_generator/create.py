import os
import shutil
from distutils.dir_util import copy_tree
import uuid
import json

base = os.getcwd()
out = os.path.join(base, "out")
templates = os.path.join(base, "templates")
bp_manifest = os.path.join(out, "blank_BP", "manifest.json")
rp_manifest = os.path.join(out, "blank_RP", "manifest.json")
rp_id = str(uuid.uuid4())
bp_module = str(uuid.uuid4())
rp_module = str(uuid.uuid4())
bp_id = str(uuid.uuid4())

# Delete and re-create the out directory
print("Attempting to create out directory...", end="")
try:
    if os.path.exists(out) and os.path.isdir(out):
        shutil.rmtree(out)

except OSError:
    print ("Creation of the directory %s failed" % out)
    exit()
print("success!")

print("Copy in existing directories...", end="")
#Copy in the base pack information
copy_tree(templates, out)  

print("success!")

#Behavior Pack
with open(bp_manifest, 'r') as f:
    data = json.load(f)
    data['header']['uuid'] = bp_id
    data['modules'][0]['uuid'] = bp_module
    data['dependencies'][0]['uuid'] = rp_id

os.remove(bp_manifest)
with open(bp_manifest, 'w') as f:
    json.dump(data, f, indent=4)

#Resource Pack
with open(rp_manifest, 'r') as f:
    data = json.load(f)
    data['header']['uuid'] = rp_id
    data['modules'][0]['uuid'] = rp_module
    data['dependencies'][0]['uuid'] = bp_id

os.remove(rp_manifest)
with open(rp_manifest, 'w') as f:
    json.dump(data, f, indent=4)









