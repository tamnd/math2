---
tag: MCDP25YMSE
kind: definition
name: Linear continuum
msc: [54F05, 06A05]
defines: MM0QPT0GT0
uses: [0FRXBVVR03, 0R3H5PANRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_continuum
---

## Definition

Let $L$ be a set with more than one element and let $<$ be a [[total order|0FRXBVVR03]] on $L$.
The ordered set $(L, <)$ is a *linear continuum* if:

1. Every nonempty subset of $L$ that is bounded above has a least upper bound, a [[supremum|0R3H5PANRQ]], in $L$.
2. For all $x, y \in L$ with $x < y$, there is $z \in L$ with $x < z < y$.

## Remarks

The real line $\R$ is a linear continuum: clause 1 is the completeness of $\R$, and for clause 2 one takes $z = (x + y)/2$.
The integers $\Z$ satisfy clause 1, but they fail clause 2, since there is no integer strictly between $1$ and $2$.
The rationals $\Q$ satisfy clause 2 but fail clause 1: the set $\set{q \in \Q : q^2 < 2}$ is bounded above but has no least upper bound in $\Q$.
The square $[0, 1] \times [0, 1]$ with the dictionary order is a linear continuum that is not order isomorphic to an interval of $\R$.
A linear continuum and each of its intervals are [[connected|0V032VWTHD]] in the order topology.

## Explanations

### L1 human

A linear continuum is an ordered set with no gaps and no jumps.
"No gaps" means that bounded sets have a least upper bound, and "no jumps" means that between two elements there is always a third one.
