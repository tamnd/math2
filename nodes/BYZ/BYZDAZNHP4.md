---
tag: BYZDAZNHP4
kind: statement
role: theorem
name: Grönwall area theorem
msc: [30C50, 30C55]
uses: [R91E83SDBD, 0X3XD2ATB0]
about: [R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/Area_theorem_(conformal_mapping)
same_as:
  wikidata: Q4788680
  wikipedia: Area theorem (conformal mapping)
---

## Statement

Let $g$ be an injective meromorphic function on $\set{z \in \C : \abs{z} > 1}$ with [[Laurent expansion|0X3XD2ATB0]]
$$g(z) = z + b_0 + \sum_{n=1}^{\infty} b_n z^{-n}, \qquad \abs{z} > 1.$$
Then
$$\sum_{n=1}^{\infty} n \abs{b_n}^2 \le 1.$$

## Remarks

For $r > 1$, the image of the circle $\abs{z} = r$ is a Jordan curve, and the bounded region $E_r$ it encloses is the complement of $g(\set{\abs{z} > r})$.
Green's formula gives the area of $E_r$ as $\frac{1}{2i}\oint \bar{w}\, dw$ over this curve, which works out to $\pi\bigl(r^2 - \sum_{n \ge 1} n \abs{b_n}^2 r^{-2n}\bigr)$.
This area is nonnegative, and letting $r \to 1$ gives the inequality.
Equality holds exactly when the complement of $g(\set{\abs{z} > 1})$ has area $0$.
Example: $g(z) = z + 1/z$ maps $\set{\abs{z} > 1}$ onto $\C \setminus [-2, 2]$, and $b_1 = 1$ gives equality.
In particular $\abs{b_1} \le 1$.
Applied to $g(z) = 1/\sqrt{f(1/z^2)}$ for $f$ in the class $S$ of normalised [[univalent functions|R91E83SDBD]], it gives Bieberbach's inequality $\abs{a_2} \le 2$.

## Explanations

### L1 human

The function $g$ maps the outside of the unit disc onto the outside of some compact set in the plane.
That compact set has a nonnegative area, and the area can be written with the coefficients of $g$.
So these coefficients cannot be too large, which is the inequality.

### L2 human

The area theorem is the starting point of the coefficient theory of univalent functions.
Through the substitution $f \mapsto 1/\sqrt{f(1/z^2)}$, it gives $\abs{a_2} \le 2$ for $f \in S$, hence the [[Koebe quarter theorem|WX0HMW4GT7]] and the distortion theorems.
The Grunsky inequalities on the [[Grunsky matrix|XKRR37N916]] refine it to a statement about all the coefficients of $\log\frac{g(z) - g(\zeta)}{z - \zeta}$.
The equality case shows that the bound $\abs{b_1} \le 1$ is attained exactly by maps onto the complement of a segment.
