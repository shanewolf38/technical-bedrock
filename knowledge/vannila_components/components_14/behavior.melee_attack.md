# Vannila Components
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:behavior.melee_attack
### bee.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "target_dist": 1.2,
    "track_target": false,
    "attack_once": true,
    "reach_multiplier": 2.0,
    "look_distance": 30,
    "untrackable_cooldown_delay": 17,
    "speed_multiplier": 9,
    "target_tracking": {
        "refresh_period_min": 4,
        "refresh_period_max": 11,
        "backoff": [
            {
                "distance_squared_gt": 256,
                "refresh_period_delta": 50
            },
            {
                "distance_squared_gt": 1024,
                "refresh_period_delta": 100
            }
        ]
    },
    "on_attack": {
        "event": "countdown_to_perish_event",
        "target": "self"
    }
}
```

### blaze.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "max_dist": 3,
    "speed_multiplier": 1,
    "random_stop_interval": 2.0,
    "track_target": true
}
```

### cave_spider.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "random_stop_interval": 100,
    "reach_multiplier": 0.8
}
```

### cave_spider.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 1.4
}
```

### creeper.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "speed_multiplier": 1.25,
    "track_target": false,
    "reach_multiplier": 0.0
}
```

### dolphin.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 2,
    "track_target": true
}
```

### drowned.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false,
    "require_complete_path": true
}
```

### enderman.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 2,
    "speed_multiplier": 1.0,
    "track_target": false
}
```

### endermite.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": true
}
```

### fox.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 10,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

### fox.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 1,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

### husk.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### iron_golem.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 1,
    "target_dist": 1.0,
    "track_target": true
}
```

### panda.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "attack_once": true,
    "reach_multiplier": 1.0
}
```

### panda.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### pillager.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1,
    "track_target": true
}
```

### silverfish.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "speed_multiplier": 1.0,
    "track_target": true
}
```

### skeleton.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### spider.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 0.8
}
```

### stray.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### vindicator.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### wither_skeleton.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### wolf.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 5,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### zombie.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_pigman.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 3,
    "speed_multiplier": 1.5,
    "track_target": false
}
```

### zombie_villager.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_villager_v2.json
```JSON
minecraft:behavior.melee_attack: {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

