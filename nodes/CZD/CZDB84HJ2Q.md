---
tag: CZDB84HJ2Q
kind: concept
name: Green–Ampt infiltration model
msc: [76S05, 86A05]
sources:
  - url: https://en.wikipedia.org/wiki/Infiltration_(hydrology)
---

## Summary

The Green–Ampt model describes the infiltration of water from a ponded surface into a uniform soil as a sharp wetting front moving downward.
Above the front the soil is saturated, and below it the soil keeps its initial dryness.
W. Heber Green and G. A. Ampt proposed it in 1911.
Applying [[Darcy's law|DX8RV2XG6H]] to the saturated zone gives an ordinary differential equation for the cumulative infiltration, with a closed-form solution in implicit form.
It is a physically based model with few parameters, used in hydrology to split rainfall into infiltration and runoff.

## Explanations

### L1 human

Pour water on dry soil and keep a thin puddle on top: the water soaks in fast at first and then slower and slower.
The Green–Ampt model pictures the wet soil as a layer on top of dry soil, with a sharp front between them that moves down.
At first the wet layer is thin, the dry soil below pulls hard on the water, and infiltration is fast.
As the wet layer thickens, the pull acts over a longer distance, and the rate slows toward the conductivity of the saturated soil.
For a sandy soil the front may go down tens of centimetres in an hour.
