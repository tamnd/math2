---
tag: KXS5DQDFYD
kind: concept
name: Dedekind zeta function
msc: [11R42]
specializes: [8MWTEF6462]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_zeta_function
same_as:
  wikidata: Q1182160
  wikipedia: Dedekind zeta function
---

## Summary

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]].
Its Dedekind zeta function $\zeta_K(s)$ is the sum of $N(\mathfrak{a})^{-s}$ over the nonzero ideals $\mathfrak{a}$ of the ring of integers.
For $K = \Q$ it is the [[Riemann zeta function|1XWBY4N0VT]].
It has an Euler product over the prime ideals and a functional equation.
It extends to a meromorphic function on the whole complex plane with a single simple pole at $s = 1$.
Its residue at $s = 1$ is given by the [[class number formula|55XX5A7XZV]].
This formula ties together the class number, the [[regulator|RWK0HNF1NA]] and the [[discriminant|E0VZTNPJXA]].

## Explanations

### L1 human

The Riemann zeta function adds up $1/n^s$ over the positive integers.
The Dedekind zeta function does the same for a number field, with ideals in place of integers and their norms in place of $n$.
For the Gaussian integers, the ideals of norm $5$ are $(2 + i)$ and $(2 - i)$, so the term $5^{-s}$ appears twice.
The analytic behaviour of this function encodes how the prime ideals of the field are distributed.
