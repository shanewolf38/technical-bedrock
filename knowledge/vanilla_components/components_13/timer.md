# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:timer
### dolphin.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 20,
    "time_down_event": {
        "event": "minecraft:dried_out"
    }
}
```

### guardian.json
```JSON
"minecraft:timer": {
    "time": [
        1,
        3
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:target_far_enough",
        "target": "self"
    }
}
```

### husk.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_zombie"
    }
}
```

### player.json
```JSON
"minecraft:timer": {
    "time": [
        0.0,
        0.0
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:clear_add_bad_omen",
        "target": "self"
    }
}
```

### pufferfish.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 0.05,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_full_puff"
    }
}
```

```JSON
"minecraft:timer": {
    "looping": false,
    "time": 1,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_normal_puff"
    }
}
```

```JSON
"minecraft:timer": {
    "looping": false,
    "time": 10,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_deflate"
    }
}
```

### ravager.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 2,
    "time_down_event": {
        "event": "minecraft:start_roar"
    }
}
```

### wandering_trader.json
```JSON
"minecraft:timer": {
    "looping": false,
    "random_time_choices": [
        {
            "weight": 50,
            "value": 2400
        },
        {
            "weight": 50,
            "value": 3600
        }
    ],
    "time_down_event": {
        "event": "minecraft:start_despawn",
        "target": "self"
    }
}
```

### zombie.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_drowned"
    }
}
```

