---
tag: 6FY0KHMK5A
kind: problem
name: Isoperimetric problem of the calculus of variations
msc: [49K05, 49K21]
uses: [JRQZ803Q5Y, G7T008BEWY, PS0VV149ET, Q7QK3PF806]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
history:
  posed_by: "Jacob Bernoulli"
  first_stated: "1697"
---

## Problem

Let $a < b$ and $A, B, \ell \in \R$, and let $L, G \colon [a, b] \times \R \times \R \to \R$, written $L(x, z, p)$ and $G(x, z, p)$, be of class $C^2$.
Set $J(y) = \int_a^b L(x, y, y') \, dx$ and $K(y) = \int_a^b G(x, y, y') \, dx$, two [[integral functionals|JRQZ803Q5Y]].
The *isoperimetric problem* asks for a minimiser of $J$ among the [[admissible functions|G7T008BEWY]] $y \in C^1([a, b])$ with $y(a) = A$, $y(b) = B$ and the integral constraint $K(y) = \ell$.

## Remarks

The name comes from the classical problem of the largest area enclosed by a curve of given length, the case where $K$ is arc length.
[[Dido's problem|FABJSZ9D3S]] is a version of it.

The basic necessary condition is Euler's multiplier rule.
Let $y_0 \in C^2([a, b])$ be a minimiser, and suppose that $y_0$ does not solve the [[Euler–Lagrange equation|PS0VV149ET]] of $K$.
Then there is $\lambda \in \R$ such that $y_0$ solves the Euler–Lagrange equation of $L - \lambda G$:
$$\frac{d}{dx} \big( L_p - \lambda G_p \big) = L_z - \lambda G_z \quad \text{on } [a, b].$$
It follows from [[Lagrange multipliers on Banach spaces|Q7QK3PF806]] with constraint space $\R$.
If $y_0$ solves the Euler–Lagrange equation of $K$, the rule must be replaced by one with multipliers $(\lambda_0, \lambda) \ne (0, 0)$ for $\lambda_0 L - \lambda G$, where $\lambda_0 = 0$ is possible.

The [[catenary problem|8REBFQD6E0]] is an isoperimetric problem: it minimises potential energy at fixed length.

## Explanations

### L1 human

Many problems ask for the best curve when some total amount is fixed: the length of a fence, the mass of a chain, the area under a graph.
The fixed amount is written as a second integral, and the problem is to minimise the first integral while the second keeps its value.
As for constrained problems in calculus, the answer is found by adding a multiple of the constraint to the functional, with an unknown multiplier.
