# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:on_target_acquired
### bee.json
```JSON
"minecraft:on_target_acquired": {
    "event": "attacked",
    "target": "self"
}
```

### cave_spider.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### dolphin.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### dolphin.json
```JSON
"minecraft:on_target_acquired": {}
```

### drowned.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:has_target",
    "target": "self"
}
```

### enderman.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### llama.json
```JSON
"minecraft:on_target_acquired": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:mad_at_wolf",
    "target": "self"
}
```

### magma_cube.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_target_acquired": {}
```

### polar_bear.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

### polar_bear.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### silverfish.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### slime.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### spider.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### spider.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### vindicator.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggro",
    "target": "self"
}
```

### wolf.json
```JSON
"minecraft:on_target_acquired": {}
```

### wolf.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### zombie_pigman.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

