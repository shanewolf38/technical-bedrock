# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:breedable
### cat.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "allow_sitting": true,
    "breeds_with": {
        "mate_type": "minecraft:cat",
        "baby_type": "minecraft:cat",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### chicken.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:chicken",
        "baby_type": "minecraft:chicken",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ]
}
```

### cow.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:cow",
        "baby_type": "minecraft:cow",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### donkey.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:donkey",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### fox.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "sweet_berries",
    "breeds_with": {
        "mate_type": "minecraft:fox",
        "baby_type": "minecraft:fox",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### horse.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:horse",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### llama.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "love_filters": {
        "test": "is_mark_variant",
        "subject": "self",
        "operator": "!=",
        "value": 1
    },
    "breeds_with": {
        "mate_type": "minecraft:llama",
        "baby_type": "minecraft:llama",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "hay_block"
    ]
}
```

### mooshroom.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:mooshroom",
        "baby_type": "minecraft:mooshroom",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "deny_parents_variant": {
        "chance": 0.00098,
        "min_variant": 0,
        "max_variant": 1
    }
}
```

### ocelot.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:ocelot",
        "baby_type": "minecraft:ocelot",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### panda.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "blend_attributes": false,
    "environment_requirements": {
        "blocks": "bamboo",
        "count": 8,
        "radius": 5
    },
    "breed_items": "bamboo",
    "breeds_with": {
        "mate_type": "minecraft:panda",
        "baby_type": "minecraft:panda",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "mutation_factor": {
        "variant": 1.0
    }
}
```

### pig.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:pig",
        "baby_type": "minecraft:pig",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "carrot",
        "beetroot",
        "potato"
    ]
}
```

### rabbit.json
```JSON
"minecraft:breedable": {
    "breed_items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ],
    "breeds_with": {
        "mate_type": "minecraft:rabbit",
        "baby_type": "minecraft:rabbit"
    },
    "require_tame": false,
    "mutation_factor": {
        "variant": 0.2
    }
}
```

### sheep.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:sheep",
        "baby_type": "minecraft:sheep"
    },
    "breed_items": "wheat"
}
```

### turtle.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "causes_pregnancy": true,
    "breeds_with": {
        "mate_type": "minecraft:turtle",
        "baby_type": "minecraft:turtle",
        "breed_event": {
            "event": "minecraft:become_pregnant",
            "target": "self"
        }
    },
    "breed_items": [
        "seagrass"
    ]
}
```

### wolf.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "breeds_with": {
        "mate_type": "minecraft:wolf",
        "baby_type": "minecraft:wolf",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "muttonRaw",
        "muttonCooked",
        "porkchop",
        "cooked_porkchop",
        "rabbit",
        "cooked_rabbit",
        "rotten_flesh"
    ]
}
```

