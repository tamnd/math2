---
tag: 91RFB97TNV
kind: concept
name: Singular control
msc: [49K15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_control
same_as:
  wikidata: Q7524238
  wikipedia: Singular control
---

## Summary

A singular control is an optimal control, or a candidate for one, on a time interval where the maximum principle gives no information.
There the maximum condition of [[Pontryagin's maximum principle|7RPV2T29CF]] does not determine the control value.
This happens when the [[Hamiltonian|RACVWG5QTK]] is affine in the control.
The coefficient of the control, called the switching function, then vanishes on a whole interval.
On such an interval the control usually takes interior values, unlike a [[bang–bang control|GK1Z3Q1WRZ]].
Singular arcs are found by differentiating the switching function in time until the control appears.

## Explanations

### L1 human

For many problems the best control is at full power in one direction or the other, depending on the sign of a switching function.
Sometimes this switching function stays at zero for a while, and then the rule gives no answer.
The control on such a stretch is called singular, and it is usually some intermediate value.
For example, to keep a quantity at zero with a control between $-1$ and $1$, the best control after reaching zero is $0$, which is neither extreme.
