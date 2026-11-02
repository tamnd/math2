---
tag: MQCBFACHXH
kind: statement
role: theorem
name: Genus–degree formula
msc: [14H50, 14C40]
uses: [EWS4WFTA7W, 6W8TDV9VVN, H03GKRVBJ1, ZT9A6JK8QF, 0PF6TM8TWT]
about: [EWS4WFTA7W, 6W8TDV9VVN]
sources:
  - url: https://en.wikipedia.org/wiki/Genus%E2%80%93degree_formula
same_as:
  wikidata: Q5533839
  wikipedia: Genus–degree formula
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] and let $C \subset \mathbb{P}^2_k$ be a smooth [[plane curve|EWS4WFTA7W]] of degree $d \ge 1$ in the [[projective plane|ZT9A6JK8QF]].
Then the [[genus|6W8TDV9VVN]] of $C$ is
$$g(C) = \frac{(d - 1)(d - 2)}{2}.$$

## Remarks

One proof uses the adjunction formula: the canonical bundle of $C$ is $\mathcal{O}_C(d - 3)$, of degree $d(d - 3)$, and this equals $2g - 2$.
Another uses the exact sequence $0 \to \mathcal{O}_{\mathbb{P}^2}(-d) \to \mathcal{O}_{\mathbb{P}^2} \to \mathcal{O}_C \to 0$.
It gives $\chi(\mathcal{O}_C) = 1 - (d - 1)(d - 2)/2$, so the [[arithmetic genus|H03GKRVBJ1]] of every plane curve of degree $d$, smooth or not, is $(d - 1)(d - 2)/2$.
Example: lines and conics have genus $0$, smooth cubics have genus $1$, and smooth quartics have genus $3$.
Smoothness is needed: the nodal cubic $y^2 z = x^2(x + z)$ has degree $3$ but geometric genus $0$.
For an irreducible plane curve whose singular points $p$ are ordinary with multiplicities $r_p$, the geometric genus is $(d - 1)(d - 2)/2 - \sum_p r_p (r_p - 1)/2$.

## Explanations

### L1 human

For a smooth curve in the plane, the degree alone fixes the genus.
Degree $1$ and $2$ give spheres, degree $3$ gives a torus, and degree $4$ gives a surface with three handles.
The genus grows roughly like half the square of the degree.

### L2 human

The formula shows that not every genus occurs for smooth plane curves: the values are $0, 1, 3, 6, 10, \ldots$.
So a curve of genus $2$ is never a smooth plane curve, although it can be drawn in the plane with singular points.
The formula is a special case of the adjunction formula, and its singular version is the basic tool to compute the genus of a plane curve from its equation.
