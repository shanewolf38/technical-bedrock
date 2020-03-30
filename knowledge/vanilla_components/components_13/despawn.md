# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:despawn
### wandering_trader.json
```JSON
"minecraft:despawn": {
    "remove_child_entities": true,
    "filters": {
        "all_of": [
            {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "self",
                        "value": "wandering_trader_despawning"
                    },
                    {
                        "test": "has_trade_supply",
                        "subject": "self",
                        "value": false
                    }
                ]
            },
            {
                "test": "distance_to_nearest_player",
                "operator": ">",
                "value": 24
            }
        ]
    }
}
```

