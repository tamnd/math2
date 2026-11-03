---
tag: Z69CDPKBB5
kind: example
name: Lebesgue measure as Haar measure
msc: [43A05, 28C10, 28A75]
instance_of: [VY0HXD3GC4]
uses: [2Z2QVWZ262, KB792QTG4F]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Example

Let $n \ge 1$ and let $G = (\R^n, +)$, a locally compact abelian group with the usual topology.
Let $\lambda$ be [[Lebesgue measure|2Z2QVWZ262]] restricted to the Borel sets of $\R^n$.
Then $\lambda$ is a Haar measure of $G$.

Check of the three conditions.
It is a Radon measure: compact sets are bounded, hence have finite measure, and Lebesgue measure is outer regular and inner regular by compact sets.
It is nonzero: the unit cube $[0, 1]^n$ has measure $1$.
It is invariant: for $x \in \R^n$ and a box $B = \prod_i [a_i, b_i]$, the translate $x + B = \prod_i [a_i + x_i, b_i + x_i]$ has the same volume $\prod_i (b_i - a_i)$.
Boxes are closed under finite intersections, generate the Borel sets, and countably many of them cover $\R^n$.
So the Borel measures $A \mapsto \lambda(x + A)$ and $\lambda$, equal and finite on boxes, agree on all Borel sets: $\lambda(x + A) = \lambda(A)$ for every Borel set $A$.

By the [[existence and uniqueness of Haar measure|KB792QTG4F]], every nonzero translation-invariant Radon measure on $\R^n$ is $c\lambda$ for some $c > 0$.
So Lebesgue measure is characterized, up to a constant, by invariance under translations.

## Explanations

### L1 human

Length on the line, area in the plane and volume in space do not change when a shape is slid around without rotation.
This is exactly the invariance that defines a Haar measure for the group of translations.
Uniqueness says that, apart from the choice of a unit, there is no other reasonable way to measure sets that respects sliding.
The choice of unit is fixed by asking the unit cube to have volume $1$.
