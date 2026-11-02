---
tag: 3GNKSCQSCD
kind: statement
role: theorem
name: Hurwitz's automorphisms theorem
msc: [14H37, 30F10]
uses: [5K0N8QMV6Q, NJ787GZS1N, 0K1SCPBNKJ, 42A5ZT6AWN]
about: [0K1SCPBNKJ, 5K0N8QMV6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem
same_as:
  wikidata: Q2226695
  wikipedia: Hurwitz's automorphisms theorem
---

## Statement

Let $X$ be a compact connected [[Riemann surface|5K0N8QMV6Q]] of [[genus|NJ787GZS1N]] $g \ge 2$.
Then the [[automorphism group|0K1SCPBNKJ]] $\Aut(X)$ of biholomorphic self-maps of $X$ is finite, and its order satisfies
$$\abs{\Aut(X)} \le 84 (g - 1).$$

## Remarks

Finiteness is a separate step; a standard proof uses the finite set of Weierstrass points of $X$, which every automorphism permutes.
For the bound, let $G = \Aut(X)$ and apply the [[Riemann–Hurwitz formula|42A5ZT6AWN]] to the quotient map $X \to X / G$, of degree $\abs{G}$.
Here $X/G$ has genus $h$, and the branch values have ramification indices $m_1, \ldots, m_k$.
It gives $2g - 2 = \abs{G} \left( 2h - 2 + \sum_{i=1}^{k} (1 - 1/m_i) \right)$.
The bracket is positive, and its smallest positive value is $1/42$, reached for $h = 0$ and $(m_1, m_2, m_3) = (2, 3, 7)$; this gives $\abs{G} \le 84(g - 1)$.
The hypothesis $g \ge 2$ is needed: a torus $\C / \Lambda$ of genus $1$ has infinitely many automorphisms, the translations, and so does the Riemann sphere.
Example: the Klein quartic $x^3 y + y^3 z + z^3 x = 0$ has genus $3$ and automorphism group of order $168 = 84 \cdot 2$, so the bound is attained.
The bound is not attained for every genus; for $g = 2$ the largest automorphism group has order $48$.

## Explanations

### L1 human

A surface with at least two holes can have only finitely many symmetries that respect its complex structure.
Hurwitz's theorem gives an explicit ceiling: a surface of genus $g$ has at most $84(g - 1)$ such symmetries.
The number $84$ comes from the triangle with angles $\pi/2$, $\pi/3$ and $\pi/7$, the smallest triangle that tiles the hyperbolic plane in this way.

### L2 human

The theorem is a typical application of the Riemann–Hurwitz formula to a quotient by a group action.
The surfaces that reach the bound are called Hurwitz surfaces, and their automorphism groups are the finite quotients of the $(2, 3, 7)$ triangle group, called Hurwitz groups.
The same bound holds for smooth projective curves over an algebraically closed field of characteristic $0$, but in positive characteristic it can fail because of wild ramification.
