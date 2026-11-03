---
tag: JQT1GBRYTY
kind: concept
name: Plane strain
msc: [74B05, 74A05]
sources:
  - url: https://en.wikipedia.org/wiki/Infinitesimal_strain_theory
---

## Summary

In plane strain every point moves parallel to a fixed plane, and the motion does not change along the normal direction.
Then the components of the [[strain tensor|8QS6QMJF5Z]] that involve the normal direction vanish.
It models long bodies of constant cross-section loaded uniformly along their length, such as dams and tunnels.
Like [[plane stress|AS7WQTM99W]], it reduces their analysis to two dimensions.

## Explanations

### L1 human

Picture a very long dam holding back water.
Far from its ends, every slice across the dam looks the same and deforms the same way.
The material cannot stretch along the length of the dam, because the neighbouring slices hold it in place.
So all the deformation happens within the cross-section, and one only has to study a single slice.
Unlike plane stress, here the stress along the length is not zero: it is what keeps the slices from stretching.
