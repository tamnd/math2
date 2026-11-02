---
tag: NC79GZ12QZ
kind: definition
name: Euler class
msc: [57R20, 55R40, 55R25]
defines: BJX6QS0ANT
uses: [7HACJC0JE2, 6N7BC70CX0, N685RXHDZX]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_class
---

## Definition

Let $\pi \colon E \to B$ be an oriented real vector bundle of rank $n$ over a paracompact space $B$.
Let $s \colon B \to E$ be the zero section and let $E_0 \subset E$ be its complement.
Let $u \in H^n(E, E_0; \Z)$ be the Thom class of $E$.
It is the unique relative class whose restriction to $H^n(E_b, E_b \setminus \set{0}; \Z) \cong \Z$ is the oriented generator, for every $b \in B$.
Its existence and uniqueness is part of the [[Thom isomorphism|N685RXHDZX]] theorem.
The *Euler class* of $E$ is
$$e(E) = s^* j^* u \in H^n(B; \Z),$$
where $j^* \colon H^n(E, E_0; \Z) \to H^n(E; \Z)$ is restriction to absolute [[cohomology|6N7BC70CX0]].

## Remarks

The Euler class is natural under pullback, so it is a [[characteristic class|7HACJC0JE2]] of oriented bundles.
Reversing the orientation changes the sign of $e(E)$.
If $E$ has a nowhere-zero section $\sigma$, then $s$ is homotopic to $\sigma$ as maps into $E$ and $\sigma$ factors through $E_0$, where $j^* u$ restricts to $0$; so $e(E) = 0$.
If $n$ is odd, then $2 e(E) = 0$, because the map $v \mapsto -v$ reverses the orientation.
The reduction of $e(E)$ modulo $2$ is the top [[Stiefel–Whitney class|JQCK7A210W]] $w_n(E)$.

Example: for a closed oriented manifold $M$, $\langle e(TM), [M] \rangle = \chi(M)$.
For $M = S^2$ this gives $e(TS^2) = 2$ times the generator of $H^2(S^2; \Z)$.

Non-example: the Möbius line bundle over $S^1$ is not orientable, so it has no Euler class with integer coefficients in this sense; only its mod $2$ analogue $w_1$ is defined.
