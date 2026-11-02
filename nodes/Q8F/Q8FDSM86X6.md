---
tag: Q8FDSM86X6
kind: definition
name: Mutually singular measures
msc: [28A10]
defines: EBGECZNCV5
uses: [PR11BZQQPG, N4KDT83V3S]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_measure
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]] and let $\mu$ and $\nu$ be [[measures|PR11BZQQPG]] on $\Sigma$.
The measures $\mu$ and $\nu$ are *mutually singular* if there are sets $A, B \in \Sigma$ such that:

1. $A \cap B = \emptyset$ and $A \cup B = X$.
2. $\mu(B) = 0$.
3. $\nu(A) = 0$.

This is written $\mu \perp \nu$.

## Remarks

Example: on the Borel sets of $\R$, let $\lambda$ be Lebesgue measure and let $\delta_0$ be the Dirac measure at $0$.
Take $A = \R \setminus \{0\}$ and $B = \{0\}$.
Then $\lambda(B) = 0$ and $\delta_0(A) = 0$, so $\lambda \perp \delta_0$.

Non-example: let $\mu$ be Lebesgue measure restricted to $[0, 1]$ and $\nu$ Lebesgue measure restricted to $[0, 2]$.
If $\mu(B) = 0$, then $B \cap [0, 1]$ has length $0$, so $A$ contains almost all of $[0, 1]$ and $\nu(A) \ge 1$.
So clause 3 fails for every choice, and $\mu$ and $\nu$ are not mutually singular.

The relation is symmetric.
For signed or complex measures, $\mu \perp \nu$ means that the total variations $\abs{\mu}$ and $\abs{\nu}$ are mutually singular.
A measure $\nu$ is called singular with respect to $\mu$ when $\nu \perp \mu$.
