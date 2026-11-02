---
tag: ZCG4DJ7GH3
kind: concept
name: Amenable group action
msc: [43A07, 37A15]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Summary

An action of a group on a set is amenable when the bounded functions on the set carry a [[mean|ZYNY2VFECQ]] that the group leaves invariant.
This is one common meaning; in ergodic theory the phrase also often means simply an action of an amenable group.
This extends amenability from [[groups|CEAT9BESKK]] to group actions: a group is amenable exactly when its action on itself by left translation is amenable.
Every action of an amenable group is amenable, but a non-amenable group can also act amenably, for example with a finite orbit.
Means and Følner sets are the tools that let ergodic theorems pass from $\Z$ to more general groups.

## Explanations

### L1 human

A mean is a way to take an average of every bounded function on a set, even an infinite one.
It must be linear, give $1$ to the constant function $1$, and give a nonnegative answer for nonnegative functions.
The action is amenable if some mean does not change when the group moves the points of the set.
If the group has a finite orbit, averaging over that orbit gives such a mean.
The free group on two generators acting on itself has no such mean, which is the root of paradoxical decompositions.
