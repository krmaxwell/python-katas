# RPG Engine

This exercise is from <https://github.com/Gianfrancoalongi/incremental_katas/tree/master/RPG_Inc>.

## Step 1

Welcome to RPG Inc! We sell engines for Role Playing Games, and you will join the proof of concept and prototyping unit where we try out new ideas and concepts.

We are developing a new small lightweight combat calculation engine that only uses files for input and output. For the first delivery, we would like the combat calculation engine to support the bare minimum, such as calculating each turn in the combat and outputting it as well.

For this we start out with some very basic rules.

1. Each combatant will attack when able.
2. "When able" is defined by the attack speed (minimum is 1). The combatant may attack every `N` ticks, where `N` is the attack speed.
3. Each combatant has a pre-defined health. When it reaches 0 (zero), the combatant is considered dead and the combat ends.
4. Each combatant has a weapon which does a fixed damage per attack.

The input file containing the combatants is called `combat.rpg` and the output result of the combat is called `result.rpg`.

An example `combat.rpg` file can be seen below:

```csv
'Mark the Fister', 4, 8, 'Iron Fist', 4
'John the Bagger', 1, 7, 'Small Bag', 1
```

The output `result.rpg` can be seen below:

```csv
1,'John The Bagger','Mark The Fister','Small Bag',1,7,7
2,'John The Bagger','Mark The Fister','Small Bag',1,6,7
3,'John The Bagger','Mark The Fister','Small Bag',1,5,7
4,'John The Bagger','Mark The Fister','Small Bag',1,4,7
4,'Mark The Fister','John The Bagger','Iron Fist',4,4,3
5,'John The Bagger','Mark The Fister','Small Bag',1,3,3
6,'John The Bagger','Mark The Fister','Small Bag',1,2,3
7,'John The Bagger','Mark The Fister','Small Bag',1,1,3
8,'John The Bagger','Mark The Fister','Small Bag',1,0,3
8,'Mark The Fister','John The Bagger','Iron Fist',4,0,0
9,'John The Bagger',Dead
9,'Mark The Fister',Dead
TIE
```

If 'John The Bagger' would have stayed alive, the last line would have been `John The Bagger`. If `Mark The Fister` would have stayed alive, the last line would have been `Mark The Fister`.

Time ticks where nothing happens, are written as:

`N,NOTHING`

In the result.rpg file, where N is the time tick.
