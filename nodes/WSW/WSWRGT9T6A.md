---
tag: WSWRGT9T6A
kind: definition
name: Bounded symmetric domain
msc: [32M15, 53C35]
defines: Y7Q2SNKG0C
uses: [FX92PP3HZR]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_symmetric_space
---

## Definition

Let $D \subset \C^n$ be a bounded domain, that is, a bounded connected open set.
The domain $D$ is a *bounded symmetric domain* if for every $p \in D$ there is a [[biholomorphism|FX92PP3HZR]] $s_p \colon D \to D$ such that:

1. $s_p \circ s_p = \id_D$;
2. $p$ is an isolated fixed point of $s_p$.

## Remarks

The map $s_p$ is called the symmetry at $p$, and it is unique.
Its derivative at $p$ is $-\id$.
A bounded symmetric domain is homogeneous: its automorphism group acts transitively.
A bounded domain that is homogeneous and has a symmetry at one point is symmetric.

Example: the unit disc $\Delta = \set{z \in \C : \abs{z} < 1}$.
At $0$ take $s_0(z) = -z$: it is an involution with only the fixed point $0$.
At $a \in \Delta$ take $s_a = \varphi_a \circ s_0 \circ \varphi_a$, where $\varphi_a(z) = (a - z)/(1 - \bar a z)$ is an automorphism of $\Delta$ with $\varphi_a \circ \varphi_a = \id$ and $\varphi_a(a) = 0$.
Then $s_a$ is an involution whose only fixed point is $a$.

Non-example: the annulus $A = \set{z : r < \abs{z} < 1}$ with $0 < r < 1$.
Its automorphisms are the rotations $z \mapsto e^{i\theta} z$ and the maps $z \mapsto r e^{i\theta}/z$.
So each orbit of $\Aut(A)$ is a union of at most two circles, $A$ is not homogeneous, and it cannot be symmetric.

The unit ball of $\C^n$ and the polydisc $\Delta^n$ are bounded symmetric domains, and so is any product of bounded symmetric domains.
