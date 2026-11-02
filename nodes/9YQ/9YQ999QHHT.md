---
tag: 9YQ999QHHT
kind: concept
name: Space of functions of bounded variation
msc: [26A45, "46E99"]
specializes: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_variation
---

## Summary

The space $BV([a, b])$ collects the real functions on $[a, b]$ that have [[bounded variation|A8251BHCMP]].
With a norm built from the [[total variation|8QA5DEWNYD]], it is a [[Banach space|06GZ956657]].
Its elements are exactly the differences of two monotone functions, and they serve as integrators in the Riemann–Stieltjes integral.
In several variables, $BV(\Omega)$ is the space of integrable functions whose distributional gradient is a finite measure.
It plays a role in the calculus of variations and in image processing.

## Explanations

### L1 human

A function has bounded variation when the total distance its values travel up and down is finite.
These functions form a vector space, because the variation of a sum is at most the sum of the variations.
The size of a function in this space is its starting value plus the total distance travelled.
For example, $x \mapsto x^2$ on $[-1, 1]$ goes down by $1$ and then up by $1$, so its total variation is $2$.
