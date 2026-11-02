---
tag: WAGJVK2NWE
kind: statement
role: theorem
name: Jordan decomposition of a signed measure
msc: [28A10]
uses: [VG2P7R91Z7, PR11BZQQPG, EBGECZNCV5, 2PKHANZ8JS]
about: [VG2P7R91Z7]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_decomposition_theorem
---

## Statement

Let $(X, \Sigma)$ be a measurable space and let $\nu$ be a [[signed measure|VG2P7R91Z7]] on it.
Then there are unique [[measures|PR11BZQQPG]] $\nu^+$ and $\nu^-$ on $(X, \Sigma)$ such that $\nu^+$ and $\nu^-$ are [[mutually singular|EBGECZNCV5]] and
$$\nu = \nu^+ - \nu^-.$$
At least one of $\nu^+$ and $\nu^-$ is finite.

## Remarks

Existence comes from a [[Hahn decomposition|2PKHANZ8JS]] $X = P \cup N$: put $\nu^+(E) = \nu(E \cap P)$ and $\nu^-(E) = -\nu(E \cap N)$.
These are measures, they are concentrated on the disjoint sets $P$ and $N$, and their difference is $\nu$.
Since $\nu$ takes at most one infinite value, one of them is finite.
Uniqueness: any such pair gives a Hahn decomposition, and two Hahn decompositions differ by a $\nu$-null set.

Example: for $\nu(E) = \int_E f \, d\mu$ with $f \in L^1(\mu)$ real, $\nu^+(E) = \int_E f^+ \, d\mu$ and $\nu^-(E) = \int_E f^- \, d\mu$, where $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$.

Mutual singularity is what makes the decomposition unique.
Without it, $\nu = (\nu^+ + \mu) - (\nu^- + \mu)$ for any finite measure $\mu$.

## Explanations

### L1 human

Every signed measure is the difference between a positive part and a negative part.
The two parts live on separate regions of the space, so they do not cancel each other anywhere.
It is the measure version of writing a number as its positive part minus its negative part.

### L2 human

The Jordan decomposition reduces signed measures to ordinary measures: one integrates against $\nu$ by integrating against $\nu^+$ and $\nu^-$.
The sum $\nu^+ + \nu^-$ is the [[total variation|EPBND51CR5]] $\abs{\nu}$, the natural size of $\nu$.
The name comes from the [[Jordan decomposition of a function of bounded variation|KDT3E0VE0K]] as a difference of increasing functions.
For the measure $dF$ of such a function $F$ the two decompositions correspond.
