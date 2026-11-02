---
tag: R3SHZX0NZR
kind: concept
name: Semilocally simply connected space
msc: [57M10, 55Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-locally_simply_connected
same_as:
  wikidata: Q7449310
  wikipedia: Semi-locally simply connected
---

## Summary

A space is semilocally simply connected if every point has a neighbourhood whose loops can all be shrunk to a point inside the whole space.
The loops need not shrink inside the neighbourhood itself, which is why the condition is only "semi" local.
It is exactly the condition, together with local path-connectedness, under which a connected space has a [[universal cover|Y1YPE6PM52]].

## Explanations

### L1 human

The condition forbids arbitrarily small loops that cannot be undone.
Manifolds satisfy it, because every point has a neighbourhood that looks like a ball, and CW complexes satisfy it too.
The [[Hawaiian earring|73EBKQPP8Q]], a union of circles of radius $1/n$ that all touch at one point, fails it.
Every neighbourhood of the touching point contains a whole small circle, and that circle cannot be shrunk to a point in the earring.
