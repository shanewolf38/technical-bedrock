# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:transformation
### husk.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### mooshroom.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:cow"
}
```

### pig.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:pig_zombie",
    "delay": 0.5
}
```

### stray.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:skeleton",
    "delay": 0.5
}
```

### villager.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "keep_level": true
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager"
}
```

### villager_v2.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": true
}
```

### zombie.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### zombie_villager.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": false
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:villager",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

### zombie_villager_v2.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "keep_level": true,
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

