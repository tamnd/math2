---
tag: EYG946BY5G
kind: statement
role: theorem
name: Steinhaus theorem
msc: [28A75, 22A10]
uses: [2Z2QVWZ262, 0ZCY0Z80B6, VY0HXD3GC4]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Steinhaus_theorem
same_as:
  wikidata: Q3527166
  wikipedia: Steinhaus theorem
---

## Statement

Let $n \ge 1$ and let $A \subseteq \R^n$ be a Lebesgue measurable set with $\lambda(A) > 0$, where $\lambda$ is [[Lebesgue measure|2Z2QVWZ262]].
Then the difference set
$$A - A = \set{a - b : a, b \in A}$$
contains an open ball centred at $0$.

## Remarks

One proof uses inner regularity to find a compact set $K \subseteq A$ with $0 < \lambda(K) < \infty$.
The function $f(x) = \lambda(K \cap (K + x))$ is continuous and $f(0) = \lambda(K) > 0$, so $f(x) > 0$ for $x$ near $0$.
If $f(x) > 0$, then some $k \in K$ also lies in $K + x$, so $x = k - k'$ with $k, k' \in K$, and $x \in A - A$.
Example: if $A \subseteq \R$ is a measurable set of positive measure, then every real number $t$ with $\abs{t}$ small enough is a difference of two points of $A$.
The hypothesis $\lambda(A) > 0$ is needed: $A = \Z$ has measure zero, and $\Z - \Z = \Z$ contains no interval around $0$.
The same statement holds in every locally compact group for a measurable set of positive [[Haar measure|VY0HXD3GC4]], with $A A^{-1}$ in place of $A - A$.

## Explanations

### L1 human

Take any set of real numbers that has positive length, however scattered it is.
Then all small numbers can be written as a difference of two of its points.
So a set of positive measure, even with no interval inside it, produces a whole interval of differences.

### L2 human

The theorem is a key step in automatic continuity results: for instance, a Lebesgue measurable additive function $f \colon \R \to \R$ is continuous, hence linear.
It also shows that a measurable proper subgroup of $\R$ has measure zero, since a subgroup containing an interval around $0$ is all of $\R$.
Its analogue for Baire category is the Pettis lemma.
