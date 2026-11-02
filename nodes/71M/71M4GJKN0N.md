---
tag: 71M4GJKN0N
kind: definition
name: Massey product
msc: [55S30]
defines: Z761N3D19J
uses: [6N7BC70CX0, JX47MS1R1H, RDT4785M4D, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Massey_product
---

## Definition

Let $X$ be a space and let $R$ be a [[commutative ring|0310REJJY8]].
Let $C^*(X; R)$ be the singular cochain complex, with coboundary $\delta$ and [[cup product|JX47MS1R1H]] $\smile$, so that $\delta(x \smile y) = \delta x \smile y + (-1)^{k} x \smile \delta y$ for $x$ of degree $k$.
Let $u \in H^p(X; R)$, $v \in H^q(X; R)$ and $w \in H^r(X; R)$ be classes in [[singular cohomology|6N7BC70CX0]] with $u \smile v = 0$ and $v \smile w = 0$.

1. Choose cocycles $a, b, c$ representing $u, v, w$.
2. Choose cochains $s$ of degree $p + q - 1$ and $t$ of degree $q + r - 1$ with $\delta s = a \smile b$ and $\delta t = b \smile c$.
3. Then $m = s \smile c + (-1)^{p+1} a \smile t$ is a cocycle of degree $p + q + r - 1$.

The *Massey product* $\langle u, v, w \rangle$ is the set of all classes $[m] \in H^{p+q+r-1}(X; R)$ obtained from all such choices.

## Remarks

The cocycle condition is a direct check: $\delta(s \smile c) = a \smile b \smile c$ and $\delta(a \smile t) = (-1)^p a \smile b \smile c$, so $\delta m = 0$.
Changing $s$ or $t$ by a cocycle changes $[m]$ by an element of $H^{p+q-1}(X; R) \smile w$ or of $u \smile H^{q+r-1}(X; R)$.
So $\langle u, v, w \rangle$ is a coset of the subgroup $u \smile H^{q+r-1}(X; R) + H^{p+q-1}(X; R) \smile w$, called the indeterminacy.
The Massey product is said to vanish if it contains $0$.
Sign conventions differ between books; they change the set only by a sign.

Example: if $u = 0$, take $a = 0$ and $s = 0$; then $m = 0$, so $\langle 0, v, w \rangle$ contains $0$ and vanishes.

Non-example: on the torus $T^2$ with degree-one generators $x, y$, the triple $\langle x, y, x \rangle$ is not defined, because $x \smile y \neq 0$, so clause 2 has no solution $s$.

Higher Massey products $\langle u_1, \ldots, u_n \rangle$ are defined in the same way when the lower ones vanish compatibly.
With rational or real coefficients, all Massey products vanish on formal spaces, such as spheres and compact Kähler manifolds.
