---
tag: G7D6SPTA2C
kind: definition
name: Rotation number
msc: ["37E45", "37E10"]
defines: DP4WWQBJJF
uses: [060W5CBZP6, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_number
---

## Definition

Let $S^1 = \R / \Z$ be the [[circle|060W5CBZP6]], with projection $\pi \colon \R \to S^1$, and let $f \colon S^1 \to S^1$ be an orientation-preserving [[homeomorphism|0QT00PB5G2]].
A *lift* of $f$ is a continuous map $F \colon \R \to \R$ with $\pi \circ F = f \circ \pi$.
Every such lift is increasing and satisfies $F(x + 1) = F(x) + 1$, and two lifts differ by an integer constant.
The *translation number* of a lift $F$ is the limit
$$\rho(F) = \lim_{n \to \infty} \frac{F^n(x) - x}{n},$$
where $F^n$ is the $n$-th iterate of $F$.
The limit exists and does not depend on $x \in \R$.
The *rotation number* of $f$ is $\rho(f) = \rho(F) - \floor{\rho(F)} \in [0, 1)$, which does not depend on the choice of lift $F$.

## Remarks

Example: the rotation $R_\alpha(x) = x + \alpha$ of $S^1$ has the lift $F(x) = x + \alpha$, and $F^n(x) - x = n\alpha$.
So $\rho(F) = \alpha$, and $\rho(R_\alpha)$ is the fractional part of $\alpha$.

Non-example: the doubling map $x \mapsto 2x$ of $S^1$ is not a homeomorphism.
Its lift $F(x) = 2x$ satisfies $F(x + 1) = F(x) + 2$, and $(F^n(x) - x)/n = (2^n - 1) x / n$ has no finite limit for $x \neq 0$, so no rotation number is defined.

The rotation number is invariant under conjugacy: if $h$ is an orientation-preserving homeomorphism of $S^1$, then $\rho(h^{-1} \circ f \circ h) = \rho(f)$.
It depends continuously on $f$ in the uniform topology.
The fractional part is often left out, and $\rho(f)$ is viewed as an element of $\R / \Z$.
