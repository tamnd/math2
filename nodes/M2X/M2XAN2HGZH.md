---
tag: M2XAN2HGZH
kind: statement
role: theorem
name: Ax–Grothendieck theorem
msc: [03C60, 14A10, 12L12]
uses: [0PF6TM8TWT, 1G0B73WPX8, 09NWETVTNY, 01RVCMSN5N, SKTMN14X5P, 0ZXZ82FTX2]
about: [0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Ax–Grothendieck_theorem
same_as:
  wikidata: Q4830725
  wikipedia: Ax–Grothendieck theorem
---

## Statement

Let $K$ be an [[algebraically closed field|0PF6TM8TWT]], let $n \ge 1$, and let $f_1, \dots, f_n \in K[x_1, \dots, x_n]$ be [[polynomials|1G0B73WPX8]].
Let $F \colon K^n \to K^n$ be the map $F(a) = (f_1(a), \dots, f_n(a))$.
If $F$ is [[injective|09NWETVTNY]], then $F$ is [[surjective|01RVCMSN5N]].

## Remarks

For fixed $n$ and a bound $d$ on the degrees of the $f_i$, the statement is a single first-order sentence in the language of rings.
It holds for every [[finite field|0ZXZ82FTX2]], because an injective map from a finite set to itself is surjective.
It also holds in the algebraic closure $\overline{\F_p}$, the union of the finite fields $\F_{p^k}$.
Given an injective $F$ over $\overline{\F_p}$ and a point $b$, the coefficients of the $f_i$ and the coordinates of $b$ lie in one finite field $\F_{p^k}$.
The map $F$ sends $\F_{p^k}^n$ injectively into itself, so it is onto $\F_{p^k}^n$, and $b$ has a preimage.
By the [[Lefschetz principle|SKTMN14X5P]], it then holds in every algebraically closed field of characteristic $0$, such as $\C$.

Example: over $\C$, the map $F(x, y) = (x, y + x^2)$ is injective, and it is surjective, since $(a, b) = F(a, b - a^2)$.

The hypothesis that $K$ is algebraically closed is necessary.
Over $\Q$, the polynomial map $x \mapsto x^3$ is injective but not surjective, since $2$ is not the cube of a rational number.

## Explanations

### L1 human

Take a map from $n$-dimensional space to itself given by polynomials, over the complex numbers.
If the map never sends two different points to the same point, then it reaches every point.
For finite sets this is obvious, and the theorem carries this simple fact over to the complex numbers.

### L2 human

The theorem was proved by James Ax with model theory and by Alexander Grothendieck with algebraic geometry.
The model-theoretic proof is the standard showcase of the Lefschetz principle: a statement checked over finite fields transfers to $\C$.
The converse fails: a surjective polynomial map need not be injective, as $z \mapsto z^2$ on $\C$ shows.
It is related to the open Jacobian conjecture, which asks whether a polynomial map $\C^n \to \C^n$ with constant nonzero Jacobian determinant has a polynomial inverse.
