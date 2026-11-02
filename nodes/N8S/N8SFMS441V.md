---
tag: N8SFMS441V
kind: definition
name: Adjoint of an unbounded operator
msc: [47B25, 47A05]
defines: 86B7HF79PQ
uses: [HM2HHE3J51, BCJHNHKQFG, KRJX5RA0PW, 6HSJBJ8TTQ, VM7B38PA87, 3TWMBFQJJ8, TRC892PJNN]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
    locator: Adjoint
---

## Definition

Let $H$ and $K$ be [[Hilbert spaces|HM2HHE3J51]] over $\C$, with inner products linear in the first argument.
Let $T$ be a [[densely defined operator|BCJHNHKQFG]] from $H$ to $K$ with domain $D(T)$.
The *adjoint* of $T$ is the [[operator|KRJX5RA0PW]] $T^*$ from $K$ to $H$ given as follows.

1. Its domain $D(T^*)$ is the set of $y \in K$ for which there is $z \in H$ with $\ip{Tx}{y} = \ip{x}{z}$ for all $x \in D(T)$.
2. For $y \in D(T^*)$, $T^* y$ is this vector $z$.

## Remarks

The vector $z$ is unique because $D(T)$ is dense: two such vectors differ by a vector orthogonal to $D(T)$, hence to $H$.
Equivalently, $y \in D(T^*)$ if and only if the functional $x \mapsto \ip{Tx}{y}$ is bounded on $D(T)$.
If $T$ is bounded with $D(T) = H$, then $T^*$ is the [[Hilbert space adjoint|6HSJBJ8TTQ]].

The adjoint $T^*$ is always [[closed|VM7B38PA87]].
It is densely defined if and only if $T$ is [[closable|3TWMBFQJJ8]], and then $T^{**}$ is the [[closure|TRC892PJNN]] of $T$.
If $S \subseteq T$, then $T^* \subseteq S^*$.

Example: on $\ell^2$, let $D(T) = \set{x : \sum n^2 \abs{x_n}^2 < \infty}$ and $T(x_n) = (n x_n)$.
For $y \in D(T^*)$ with $T^* y = z$, testing with the unit vector $x = e_n$ gives $n \overline{y_n} = \overline{z_n}$, so $z = (n y_n) \in \ell^2$ and $y \in D(T)$.
Conversely each $y \in D(T)$ lies in $D(T^*)$ with $T^* y = Ty$, so $T^* = T$.

Non-example: if $D(T)$ is not dense, there is a nonzero $w \perp D(T)$, and then $z$ and $z + w$ both satisfy clause 1, so clause 2 does not define a map.
