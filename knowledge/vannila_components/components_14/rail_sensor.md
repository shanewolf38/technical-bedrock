# Vannila Components
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:rail_sensor
### command_block_minecart.json
```JSON
minecraft:rail_sensor: {
    "check_block_types": true,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_deactivate": {
        "event": "minecraft:command_block_deactivate"
    }
}
```

### command_block_minecart.json
```JSON
minecraft:rail_sensor: {
    "check_block_types": false,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_activate": {
        "event": "minecraft:command_block_activate"
    }
}
```

### hopper_minecart.json
```JSON
minecraft:rail_sensor: {
    "on_activate": {
        "event": "minecraft:hopper_deactivate"
    }
}
```

### hopper_minecart.json
```JSON
minecraft:rail_sensor: {
    "on_deactivate": {
        "event": "minecraft:hopper_activate"
    }
}
```

### minecart.json
```JSON
minecraft:rail_sensor: {
    "eject_on_activate": true
}
```

### tnt_minecart.json
```JSON
minecraft:rail_sensor: {}
```

### tnt_minecart.json
```JSON
minecraft:rail_sensor: {}
```

### tnt_minecart.json
```JSON
minecraft:rail_sensor: {
    "on_activate": {
        "filters": {
            "all_of": [
                {
                    "test": "is_game_rule",
                    "domain": "tntexplodes",
                    "operator": "==",
                    "value": true
                }
            ]
        },
        "event": "minecraft:on_prime"
    }
}
```

