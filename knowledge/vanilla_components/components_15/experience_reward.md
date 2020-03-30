# Vanilla Component Usage
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:experience_reward
### bee.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### blaze.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### cat.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cave_spider.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### chicken.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cow.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### creeper.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### dolphin.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### donkey.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### drowned.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### drowned.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### elder_guardian.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### enderman.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### endermite.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 3 : 0"
}
```

### evocation_illager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "10"
}
```

### fish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### fox.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ghast.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### guardian.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### horse.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### husk.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### husk.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### llama.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### magma_cube.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### mooshroom.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### mule.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ocelot.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### panda.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### parrot.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### phantom.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### pig.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### pillager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### player.json
```JSON
"minecraft:experience_reward": {
    "on_death": "Math.Min(query.player_level * 7, 100)"
}
```

### polar_bear.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### pufferfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### rabbit.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ravager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 20 : 0"
}
```

### salmon.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### sheep.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### shulker.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### silverfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### skeleton.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### skeleton_horse.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### slime.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### spider.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### squid.json
```JSON
"minecraft:experience_reward": {
    "on_death": "!query.is_baby && query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### stray.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### tropicalfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### turtle.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### vex.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### vindicator.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### witch.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### wither.json
```JSON
"minecraft:experience_reward": {
    "on_death": "50"
}
```

### wither_skeleton.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### wolf.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_horse.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie_pigman.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_pigman.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager_v2.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager_v2.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

