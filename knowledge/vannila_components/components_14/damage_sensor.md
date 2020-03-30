# Vannila Components
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# minecraft:damage_sensor
### bat.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### bee.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### blaze.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### cat.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### chicken.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### creeper.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            },
            "event": "minecraft:become_charged"
        },
        "deals_damage": false
    }
}
```

### ender_dragon.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### fox.json
```JSON
minecraft:damage_sensor: {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_block",
                    "subject": "block",
                    "value": "minecraft:sweet_berry_bush"
                }
            },
            "deals_damage": false
        }
    ]
}
```

### ghast.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### iron_golem.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### llama.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "all",
        "deals_damage": true,
        "on_damage": {
            "filters": {
                "test": "in_caravan",
                "value": false
            },
            "event": "minecraft:become_angry"
        }
    }
}
```

### llama.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "all",
        "deals_damage": true
    }
}
```

### magma_cube.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### mooshroom.json
```JSON
minecraft:damage_sensor: {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 0
                        }
                    ]
                },
                "event": "minecraft:become_brown"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        },
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        }
                    ]
                },
                "event": "minecraft:become_red"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        }
    ]
}
```

### ocelot.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### parrot.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### pig.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            },
            "event": "become_zombie"
        },
        "deals_damage": false
    }
}
```

### pillager.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### pillager.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### skeleton.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "other_with_families": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### skeleton_horse.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### snow_golem.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### turtle.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "cause": "lightning",
        "deals_damage": true,
        "damage_multiplier": 2000.0
    }
}
```

### villager.json
```JSON
minecraft:damage_sensor: {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### villager_v2.json
```JSON
minecraft:damage_sensor: {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### vindicator.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### vindicator.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### wandering_trader.json
```JSON
minecraft:damage_sensor: {
    "triggers": [
        {
            "cause": "entity_attack",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "projectile",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "magic",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        }
    ]
}
```

### wither.json
```JSON
minecraft:damage_sensor: {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "undead"
            }
        },
        "deals_damage": false
    }
}
```

