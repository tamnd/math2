---
tag: XVQN0GT988
kind: definition
name: Disk algebra
msc: [46J15, 30H50]
defines: DGWYF0B6NT
uses: [8G5ABXRK85, 0P27W9RW0G, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Disk_algebra
---

## Definition

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the open [[unit disc|8G5ABXRK85]] and $\overline{\mathbb{D}}$ its closure.
The *disk algebra* $A(\mathbb{D})$ is the set of functions $f \colon \overline{\mathbb{D}} \to \C$ such that

1. $f$ is [[continuous|0P27W9RW0G]] on $\overline{\mathbb{D}}$, and
2. the restriction of $f$ to $\mathbb{D}$ is [[holomorphic|0DG0Z72CQD]],

with pointwise addition and multiplication and the norm $\norm{f} = \sup_{z \in \overline{\mathbb{D}}} \abs{f(z)}$.

## Remarks

$A(\mathbb{D})$ is a closed subalgebra of $C(\overline{\mathbb{D}})$, hence a commutative Banach algebra with unit.
By the [[maximum modulus principle|048F2P90WR]], the norm equals $\sup_{\abs{z} = 1} \abs{f(z)}$, so $A(\mathbb{D})$ may also be viewed as an algebra of functions on the circle.
The polynomials are dense: $f(rz) \to f(z)$ uniformly as $r \to 1$, and each $f(rz)$ is the uniform limit of its Taylor polynomials on $\overline{\mathbb{D}}$.
The maximal ideals of $A(\mathbb{D})$ are the sets $\set{f : f(a) = 0}$ for $a \in \overline{\mathbb{D}}$.

Example: $f(z) = \sum_{n \ge 1} z^n / n^2$.
The terms are bounded by $1/n^2$ on $\overline{\mathbb{D}}$, so the series converges uniformly there; hence $f$ is continuous on $\overline{\mathbb{D}}$ and holomorphic in $\mathbb{D}$.

Non-example: $S(z) = \exp\left(-\frac{1 + z}{1 - z}\right)$ is bounded and holomorphic in $\mathbb{D}$, but it has no continuous extension to $\overline{\mathbb{D}}$.
Its radial limit at $1$ is $0$, while its radial limits at the points $e^{it} \ne 1$ have modulus $1$, so no continuous extension to $\overline{\mathbb{D}}$ exists.
