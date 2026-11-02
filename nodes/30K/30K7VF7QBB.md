---
tag: 30K7VF7QBB
kind: concept
name: Toda bracket
msc: [55Q35, 55Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Toda_bracket
same_as:
  wikidata: Q7812118
  wikipedia: Toda bracket
---

## Summary

The Toda bracket is a secondary composition operation on homotopy classes of maps.
It takes three maps $f$, $g$, $h$ such that $g \circ f$ and $h \circ g$ are null-homotopic.
It produces a set of maps out of the suspension of the source of $f$.
Toda introduced it to compute the [[homotopy groups of spheres|YD6VAXXSBM]].
It remains a basic tool for finding relations in the [[stable homotopy groups of spheres|HGZAYPQBXW]].

## Explanations

### L1 human

If $g \circ f$ is homotopic to a constant map, there is a homotopy that witnesses this.
If also $h \circ g$ is null, there is a second witnessing homotopy.
Comparing the two witnesses for the triple composite $h \circ g \circ f$ gives a loop of maps, and this loop is a map out of a suspension.
The Toda bracket is the set of all maps that arise from such choices.
For example, in the stable homotopy groups of spheres the bracket $\langle 2, \eta, 2 \rangle$ is the single element $\eta^2$, where $\eta$ is the stable Hopf map.
