---
tag: 74VMD07DRX
kind: statement
role: theorem
name: Lebesgue decomposition theorem
msc: [28A10, 28A15]
uses: [WEBBT18D4X, P0P21KDV6E, EBGECZNCV5]
about: [P0P21KDV6E, EBGECZNCV5]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue's_decomposition_theorem
same_as:
  wikidata: Q191693
  wikipedia: Lebesgue's decomposition theorem
---

## Statement

Let $(X, \Sigma)$ be a measurable space and let $\mu$ and $\nu$ be [[σ-finite measures|WEBBT18D4X]] on $\Sigma$.
Then there are measures $\nu_a$ and $\nu_s$ on $\Sigma$ such that:

1. $\nu = \nu_a + \nu_s$.
2. $\nu_a$ is [[absolutely continuous|P0P21KDV6E]] with respect to $\mu$.
3. $\nu_s$ and $\mu$ are [[mutually singular|EBGECZNCV5]].

The measures $\nu_a$ and $\nu_s$ are unique.

## Remarks

One proof applies the Radon–Nikodym theorem to $\mu$ and $\mu + \nu$.
With $f = d\mu / d(\mu + \nu)$, the set $S = \{f = 0\}$ is $\mu$-null, and one puts $\nu_s(A) = \nu(A \cap S)$ and $\nu_a(A) = \nu(A \setminus S)$.
Uniqueness holds because a measure that is both absolutely continuous and singular with respect to $\mu$ is zero.

Example: let $\mu$ be Lebesgue measure on $\R$ and $\nu = \mu|_{[0,1]} + \delta_2$, where $\delta_2$ is the point mass at $2$.
Then $\nu_a = \mu|_{[0,1]}$ and $\nu_s = \delta_2$.

On the real line with $\mu$ Lebesgue measure, the singular part splits further into a part made of point masses and a continuous singular part.
The distribution of the Cantor function is an example of a continuous singular measure.

## Explanations

### L1 human

Any reasonable measure can be cut into two pieces relative to a reference measure.
One piece is smooth: it has a density with respect to the reference.
The other piece lives on a set that the reference does not see at all.

### L2 human

Combined with the Radon–Nikodym theorem, it says $\nu = f\mu + \nu_s$ with $f = d\nu_a / d\mu$ and $\nu_s \perp \mu$.
In probability this splits a distribution on $\R$ into a part with a density, a discrete part and a singular continuous part.
The same decomposition holds for finite signed and complex measures, applied to the total variation.
