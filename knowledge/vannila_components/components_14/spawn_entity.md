# Vannila Components
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:spawn_entity
### chicken.json
```JSON
minecraft:spawn_entity: {
    "min_wait_time": 300,
    "max_wait_time": 600,
    "spawn_sound": "plop",
    "spawn_item": "egg",
    "filters": {
        "test": "rider_count",
        "subject": "self",
        "operator": "==",
        "value": 0
    }
}
```

### wandering_trader.json
```JSON
minecraft:spawn_entity: [
    {
        "min_wait_time": 0,
        "max_wait_time": 0,
        "spawn_entity": "llama",
        "spawn_event": "minecraft:from_wandering_trader",
        "single_use": true,
        "num_to_spawn": 2,
        "should_leash": true
    }
]
```

