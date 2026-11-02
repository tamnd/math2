---
tag: PYN08Z14ZP
kind: definition
name: Total variation distance between probability measures
msc: [60B10, 62B10]
defines: 3SZESKX3N5
uses: [059TJN0NZ1, EPBND51CR5, 1NTKG64F7N, 0VKD1TP7F3, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation_distance_of_probability_measures
---

## Definition

Let $P$ and $Q$ be [[probability measures|059TJN0NZ1]] on a measurable space $(\mathcal{X}, \mathcal{F})$.
The *total variation distance* between $P$ and $Q$ is
$$\delta(P, Q) = \sup_{A \in \mathcal{F}} \abs{P(A) - Q(A)}.$$

## Remarks

It lies in $[0, 1]$, and it is a [[metric|0VKD1TP7F3]] on the probability measures on $(\mathcal{X}, \mathcal{F})$.
If $\lambda$ is a measure with densities $p = dP/d\lambda$ and $q = dQ/d\lambda$, then $\delta(P, Q) = \frac{1}{2} \int \abs{p - q} \, d\lambda$, and the supremum is attained at $A = \set{p > q}$.
Equivalently, $\delta(P, Q) = \frac{1}{2} \norm{P - Q}$, where $\norm{\cdot}$ is the [[total variation|EPBND51CR5]] norm of the signed measure $P - Q$.
Some authors call $\norm{P - Q}$ itself the total variation distance, which differs by the factor $2$.

Example: let $P$ and $Q$ be Bernoulli distributions with parameters $p$ and $q$.
The four events are $\emptyset$, $\set{0}$, $\set{1}$ and $\set{0, 1}$, with differences $0$, $\abs{q - p}$, $\abs{p - q}$ and $0$.
So $\delta(P, Q) = \abs{p - q}$.

Non-example: the largest difference over single points, $\sup_x \abs{P(\set{x}) - Q(\set{x})}$, is not the total variation distance.
For the [[normal distributions|05AQE0QR0D]] with means $0$ and $1$ and variance $1$, every point has probability $0$, so this quantity is $0$.
Yet $\delta(P, Q) > 0$, since the two measures are different.
