---
tag: VDPTQ35JWE
kind: definition
name: Brunn–Minkowski theory
msc: [52A39, 52A40, 52A20]
defines: RNS272QBGT
uses: [437FSG3419, SXS6D87PHE, QB3Q5FBJ08, 2Z2QVWZ262, 9B02RPN7XD]
sources:
  - url: https://en.wikipedia.org/wiki/Brunn%E2%80%93Minkowski_theorem
---

## Definition

Let $n \ge 1$, let $\mathcal{K}^n$ be the set of [[convex bodies|437FSG3419]] in $\R^n$, and let $V$ be the volume, that is, [[Lebesgue measure|2Z2QVWZ262]].
*Brunn–Minkowski theory* is the study of the functionals on $\mathcal{K}^n$ obtained from $V$ and [[Minkowski addition|SXS6D87PHE]] $K + L = \set{x + y : x \in K, \ y \in L}$ together with scaling by nonnegative reals.
Its basis is Minkowski's theorem: for $K_1, \ldots, K_m \in \mathcal{K}^n$ and $\lambda_1, \ldots, \lambda_m \ge 0$,
$$V(\lambda_1 K_1 + \cdots + \lambda_m K_m) = \sum_{i_1, \ldots, i_n = 1}^{m} \lambda_{i_1} \cdots \lambda_{i_n} V(K_{i_1}, \ldots, K_{i_n}),$$
where the coefficients $V(K_{i_1}, \ldots, K_{i_n})$, symmetric in their arguments, are the [[mixed volumes|QB3Q5FBJ08]].
The theory studies the mixed volumes and their special cases, and inequalities between them such as the [[Brunn–Minkowski theorem|9B02RPN7XD]].

## Remarks

Example: take $K_1 = K$ and $K_2 = B$, the unit ball.
Then $V(K + t B)$ is a polynomial of degree $n$ in $t \ge 0$; this is Steiner's formula.
Its coefficients are, up to binomial factors, the quermassintegrals of $K$, among them the volume and a multiple of the surface area.
Non-example: Lutwak's dual Brunn–Minkowski theory replaces Minkowski addition by radial addition of star bodies; it studies sections rather than projections and is a different theory.
The $L_p$ Brunn–Minkowski theory is an extension that replaces Minkowski addition by $L_p$ addition of support functions.
