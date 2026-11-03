---
tag: ADN3TKD39T
kind: concept
name: Objective stress rate
msc: [74A20, 74A10]
sources:
  - url: https://en.wikipedia.org/wiki/Objective_stress_rate
same_as:
  wikidata: Q17105043
  wikipedia: Objective stress rate
---

## Summary

An objective stress rate is a time derivative of the [[Cauchy stress tensor|KG2XWEMJ30]] that does not depend on the rotation of the observer.
The plain material time derivative of stress fails this test.
Indeed, a rigid rotation of a stressed body changes the stress components even when nothing is deformed.
Objective rates, such as the Jaumann rate and the Truesdell rate, are used in rate-type [[constitutive equations|Q4C55V47A8]] for large deformations.
They make such laws respect the [[principle of material frame-indifference|EZQ0E262QV]].

## Explanations

### L1 human

Take a stretched rubber band and turn it in your hand without stretching it more.
The stress inside has not changed in any physical sense, but its components in a fixed set of axes do change.
So the ordinary time derivative of the stress components is not zero, and a law that relates it to the rate of stretching would give nonsense.
An objective stress rate corrects the derivative by subtracting the part that comes from spinning.
For a rigid spin of a pre-stressed body, the Jaumann rate is zero, as it should be.
