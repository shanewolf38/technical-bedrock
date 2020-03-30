# Vannila Components
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:on_target_escape
### creeper.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:stop_exploding",
    "target": "self"
}
```

### creeper.json
```JSON
minecraft:on_target_escape: {}
```

### creeper.json
```JSON
minecraft:on_target_escape: {}
```

### dolphin.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### drowned.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:lost_target",
    "target": "self"
}
```

### llama.json
```JSON
minecraft:on_target_escape: {
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
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### magma_cube.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### panda.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### pillager.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:calm",
    "target": "self"
}
```

### pillager.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:calm",
    "target": "self"
}
```

### slime.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### vindicator.json
```JSON
minecraft:on_target_escape: {
    "event": "minecraft:stop_aggro",
    "target": "self"
}
```

