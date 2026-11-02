---
tag: FDARANFQ0B
kind: definition
name: Biholomorphism
msc: [32H02]
defines: FX92PP3HZR
uses: [3MQTWKBBBT, 0J2WAR83WP]
sources:
  - url: https://en.wikipedia.org/wiki/Biholomorphism
---

## Definition

Let $U$ and $V$ be open subsets of $\C^n$.
A *biholomorphism* from $U$ to $V$ is a [[holomorphic map|3MQTWKBBBT]] $F \colon U \to V$ such that:

1. $F$ is a bijection from $U$ onto $V$.
2. The [[inverse map|0J2WAR83WP]] $F^{-1} \colon V \to U$ is holomorphic.

The sets $U$ and $V$ are *biholomorphic*, or biholomorphically equivalent, if there is a biholomorphism from $U$ to $V$.

## Remarks

Example: $F(z_1, z_2) = (2 z_1, \ z_2 + z_1^2)$ is a biholomorphism of $\C^2$, since it is polynomial, bijective, and its inverse $(w_1, w_2) \mapsto (w_1/2, \ w_2 - w_1^2/4)$ is polynomial.
Non-example: $F(z) = z^3$ from $\C$ to $\C$ is holomorphic and onto, but not injective, since $F(1) = F(e^{2\pi i/3})$; so clause 1 fails.
In fact clause 2 follows from clause 1: an injective holomorphic map from an open set $U \subseteq \C^n$ to $\C^n$ has open image and a holomorphic inverse.
This differs from the real case, where $x \mapsto x^3$ is a smooth bijection of $\R$ whose inverse is not differentiable at $0$.
The biholomorphisms of $U$ onto itself form a group, the holomorphic automorphism group $\Aut(U)$.
