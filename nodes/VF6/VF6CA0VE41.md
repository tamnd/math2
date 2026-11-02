---
tag: VF6CA0VE41
kind: concept
name: Nonexpansive map
msc: [47H09, "54E40"]
specializes: [0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_map
same_as:
  wikidata: Q2713824
  wikipedia: Metric map
---

## Summary

A nonexpansive map between metric spaces is a map that never increases distances: $d(f(x), f(y)) \le d(x, y)$.
These are exactly the maps that are [[Lipschitz|0AW1E6YTJY]] with constant $1$; they are also called short maps or metric maps.
They include isometries and [[contraction mappings|0QN69YA357]].
In fixed point theory they are the borderline case where the Banach fixed point theorem no longer applies and the geometry of the space matters.

## Explanations

### L1 human

A nonexpansive map may move points around, but it never pulls two points further apart.
Rotations of the plane, reflections, and the map sending each point to the nearest point of a closed disc are all nonexpansive.
The map $x \mapsto 2x$ on the real line is not, since it doubles distances.
Unlike contractions, nonexpansive maps need not have fixed points: the shift $x \mapsto x + 1$ on the line moves every point.
