---
tag: 3H1YKSPH19
kind: definition
name: Standard probability space
msc: [28A05, 60A10, 28D05]
defines: QDDRDW9PXS
uses: [0NFPJVJJHX, 2Z2QVWZ262, VQQM4Y550T, 22K8CSQTYM]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_probability_space
    locator: Definition
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] whose measure is [[complete|22K8CSQTYM]].
A *model space* is built from a number $a \in [0,1]$ and a finite or countable family of numbers $p_k > 0$ with $a + \sum_k p_k = 1$.
It is the disjoint union of $[0, a]$ with points $x_k$.
Lebesgue measurable subsets of $[0,a]$ get their [[Lebesgue measure|2Z2QVWZ262]], and each point $x_k$ gets mass $p_k$.
Two complete probability spaces are *isomorphic mod $0$* if a [[null set|VQQM4Y550T]] can be removed from each so that the following holds.
There is a bijection between the remaining sets that is measurable in both directions and preserves the measure.
The space $(\Omega, \mathcal{F}, P)$ is *standard* if it is isomorphic mod $0$ to a model space.

## Remarks

Example: the unit square $[0,1]^2$ with completed Lebesgue measure is standard with $a = 1$ and no atoms.
Remove the null set of points with a dyadic rational coordinate, and interleave the binary digits of the two coordinates.
This gives a bijection mod $0$ with $[0,1]$ that sends dyadic squares to dyadic intervals of the same measure, so it preserves the measure.
Non-example: let $Z \subseteq [0,1]$ have Lebesgue inner measure $0$ and outer measure $1$, and let $\Omega = [0,1] \setminus Z$ with $P(A \cap \Omega) = \lambda(A)$ for Lebesgue measurable $A$.
This "perforated interval" is a complete probability space that is known not to be standard.
Rokhlin's Lebesgue spaces are the same spaces, defined through a countable separating family of sets and a completeness condition.
