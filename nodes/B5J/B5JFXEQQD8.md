---
tag: B5JFXEQQD8
kind: conjecture
name: Jacobian conjecture
msc: [14R15, 13F20, 14R10]
uses: [0F6ES3BRYP, 0SDC934R52, 047NDTEPCV, 0ZCSMYHTBP]
about: [0ZCSMYHTBP, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobian_conjecture
same_as:
  wikidata: Q2605695
  wikipedia: Jacobian conjecture
history:
  posed_by: "Ott-Heinrich Keller"
  first_stated: "1939"
---

## Statement

Let $k$ be a field of [[characteristic|0F6ES3BRYP]] $0$ and let $n \ge 1$.
Let $F_1, \ldots, F_n \in k[x_1, \ldots, x_n]$ be polynomials, and let $F = (F_1, \ldots, F_n) \colon k^n \to k^n$.
Suppose that the [[Jacobian determinant|0ZCSMYHTBP]] $\det \left( \frac{\partial F_i}{\partial x_j} \right)$ is a nonzero constant in $k$.
Then there are polynomials $G_1, \ldots, G_n \in k[x_1, \ldots, x_n]$ such that $G = (G_1, \ldots, G_n)$ satisfies $G \circ F = F \circ G = \id$.

## Remarks

The converse holds: if $F$ has a polynomial inverse $G$, the chain rule gives $\det J_F \cdot (\det J_G \circ F) = 1$, so $\det J_F$ is a unit of the [[polynomial ring|0SDC934R52]], that is, a nonzero constant.
The conjecture is open for every $n \ge 2$; the case $n = 1$ is easy, since a polynomial with constant nonzero derivative has degree $1$.
The question was posed by Ott-Heinrich Keller in 1939.
Characteristic $0$ is needed: over $\F_p$, the polynomial $F(x) = x - x^p$ has derivative $1$, but it has degree $p$ and is not invertible by a polynomial.
It is known that the conjecture holds when all $F_i$ have degree at most $2$.
Bass, Connell and Wright showed that it suffices to prove it, for all $n$, for maps of the form $F = x + H$ with $H$ homogeneous of degree $3$.

## Explanations

### L1 human

A polynomial map whose Jacobian determinant is a nonzero constant is invertible near each point of $\R^n$ or $\C^n$, by the inverse function theorem.
The conjecture says that it is then invertible everywhere, and that the inverse is again given by polynomials.
For one variable this is clear, but already for two variables nobody knows a proof or a counterexample.
