---
tag: J64Y3JC0RE
kind: concept
name: Ultrafilter
msc: [54A20, "03E05"]
specializes: [15PF73BKY6]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter
---

## Summary

An ultrafilter on a set $X$ is a [[filter|15PF73BKY6]] on $X$ that is maximal: no strictly larger filter on $X$ exists.
Equivalently, for every subset $A$ of $X$, either $A$ or its complement belongs to it.
Every filter lies in an ultrafilter, by [[Zorn's lemma|04RXTQA5ZA]].
Ultrafilters describe [[compactness|0TVJZYB6SH]], build the Stone–Čech compactification, and give ultraproducts in logic.

## Explanations

### L1 human

An ultrafilter makes a firm decision about every subset: either the set is "big" or its complement is.
The simplest ultrafilters pick a point $a$ and call a set big when it contains $a$.
On an infinite set there are also ultrafilters that are not of this kind.
One can show that they exist, using the axiom of choice, but one cannot write one down explicitly.
