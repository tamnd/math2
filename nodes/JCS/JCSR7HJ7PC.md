---
tag: JCSR7HJ7PC
kind: concept
name: Haar measure on a Lie group
msc: ["22E30", 28C10]
specializes: [VY0HXD3GC4]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Summary

On a [[Lie group|7JBRGCVJRB]], the [[Haar measure|VY0HXD3GC4]] can be written down explicitly as the measure defined by a nonzero left-invariant differential form of top degree.
This gives a smooth density in every chart, so integrals over the group can be computed with ordinary calculus.
The left and right Haar measures agree exactly when $\abs{\det \operatorname{Ad}(g)} = 1$ for all $g$, which holds for compact, abelian and semisimple groups.
It is the basic tool for averaging over a group, as in the proof that representations of compact groups are unitarisable.

## Explanations

### L1 human

A Haar measure is a way to measure the size of sets of group elements that does not change when the set is moved by the group.
On a Lie group one gets it by fixing a small volume element at the identity and carrying it to every other point by left multiplication.
On the circle group this gives the arc length $d\theta$.
On the positive real numbers under multiplication it gives $dx/x$, which is unchanged by the substitution $x \mapsto cx$.
