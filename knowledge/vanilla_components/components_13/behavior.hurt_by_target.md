# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:behavior.hurt_by_target
### blaze.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### cave_spider.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### creeper.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### dolphin.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### drowned.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### enderman.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ghast.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### husk.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### iron_golem.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "creeper"
        }
    }
}
```

### iron_golem.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "all_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "player"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "creeper"
                }
            ]
        }
    }
}
```

### llama.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "hurt_owner": true
}
```

### panda.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### pillager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### polar_bear.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ravager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### shulker.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### silverfish.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "alert_same_type": true
}
```

### skeleton.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### spider.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### stray.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### turtle.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vex.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vindicator.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### witch.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wither.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### zombie.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

