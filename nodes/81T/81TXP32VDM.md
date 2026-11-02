---
tag: 81TXP32VDM
kind: statement
role: theorem
name: Weil conjectures
msc: [14G10, 14G15, 14F20]
uses: [A4H4CZ2V35, SWJYG87QQH, 04SGPNT8R9, RNDDWDAFJ5, P6QD6TKAGS, E1DVHN06CR]
about: [A4H4CZ2V35, SWJYG87QQH]
sources:
  - url: https://en.wikipedia.org/wiki/Weil_conjectures
same_as:
  wikidata: Q1479613
  wikipedia: Weil conjectures
---

## Statement

Let $q$ be a prime power and let $X$ be a smooth, geometrically irreducible [[projective variety|A4H4CZ2V35]] of dimension $n$ over the [[finite field|04SGPNT8R9]] $\F_q$.
For $m \ge 1$ let $N_m$ be the number of [[rational points|SWJYG87QQH]] of $X$ over $\F_{q^m}$.
The zeta function of $X$ is the power series
$$Z(X, t) = \exp\Big(\sum_{m \ge 1} \frac{N_m}{m} t^m\Big),$$
in the ring of formal power series over $\Q$.
Then the following hold.

1. Rationality: $Z(X, t) = \dfrac{P_1(t) P_3(t) \cdots P_{2n-1}(t)}{P_0(t) P_2(t) \cdots P_{2n}(t)}$ with $P_i(t) \in \Z[t]$, $P_0(t) = 1 - t$ and $P_{2n}(t) = 1 - q^n t$.
2. Functional equation: $Z\big(X, \tfrac{1}{q^n t}\big) = \pm\, q^{nE/2} \, t^{E} \, Z(X, t)$, where $E$ is the self-intersection number of the diagonal in $X \times X$.
3. Riemann hypothesis: for $1 \le i \le 2n - 1$, $P_i(t) = \prod_j (1 - \alpha_{ij} t)$, where the $\alpha_{ij}$ are algebraic integers with $\abs{\alpha_{ij}} = q^{i/2}$ for every complex absolute value.
4. Betti numbers: suppose $X$ is the good reduction modulo a prime of a smooth projective variety $Y$ over a number field $K \subset \C$.
   Then $\deg P_i$ is the $i$-th Betti number of the complex manifold $Y(\C)$.

## Remarks

In the proof one takes $P_i(t) = \det(1 - tF \mid H^i(\bar{X}, \Q_\ell))$, where $F$ is the Frobenius acting on [[ℓ-adic cohomology|E1DVHN06CR]].
The [[Grothendieck–Lefschetz trace formula|P6QD6TKAGS]] then gives rationality, Poincaré duality gives the functional equation, and $E$ is the [[Euler characteristic|RNDDWDAFJ5]] of $\bar{X}$.
Dwork proved rationality in 1960 by $p$-adic methods, Grothendieck proved rationality and the functional equation with étale cohomology, and Deligne proved the Riemann hypothesis in 1974.
Example: for an elliptic curve $X$ over $\F_q$, $Z(X, t) = \dfrac{1 - a t + q t^2}{(1 - t)(1 - q t)}$ with $a = q + 1 - N_1$.
The Riemann hypothesis says that the two roots of $1 - a t + q t^2$ have inverses of absolute value $\sqrt{q}$, which is [[Hasse's theorem|7Y26317GJ0]] $\abs{a} \le 2\sqrt{q}$.

## Explanations

### L1 human

Take a system of polynomial equations with integer coefficients and count its solutions in the finite fields with $q$, $q^2$, $q^3, \ldots$ elements.
Weil predicted that these counts are governed by finitely many numbers $\alpha$, with $N_m$ a signed sum of their $m$-th powers.
He also predicted the sizes of these numbers and their link with the shape of the corresponding complex variety.
All four predictions are now theorems.

### L2 human

Point (3) is the analogue of the [[Riemann hypothesis|VCGF9YR36X]] for the zeta function of a variety over a finite field.
It gives sharp estimates of point counts that are used throughout number theory.
Weil proved the conjectures for curves and abelian varieties, and they motivated the creation of étale and $\ell$-adic cohomology.
The local zeta functions $Z(X, t)$ at the primes of a number field are the factors of the [[Hasse–Weil zeta function|37TNNBQ4PK]].
Grothendieck proposed his standard conjectures as a route to point (3), and they would give a second proof of it.
