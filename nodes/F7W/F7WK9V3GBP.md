---
tag: F7WK9V3GBP
kind: statement
role: theorem
name: Saint-Venant compatibility condition
msc: [74A05, 74B05]
uses: [8QS6QMJF5Z, 0QW64ARSHB, 0PBY4E9GQF]
about: [8QS6QMJF5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Saint-Venant%27s_compatibility_condition
same_as:
  wikidata: Q7400838
  wikipedia: Saint-Venant's compatibility condition
---

## Statement

Let $\Omega \subseteq \R^3$ be an open, connected and [[simply connected|0QW64ARSHB]] set.
Let $\varepsilon \colon \Omega \to \R^{3 \times 3}$ be a symmetric matrix field of class $C^2$.
Then the following two conditions are equivalent.

1. There is a displacement field $u \colon \Omega \to \R^3$ of class $C^3$ whose [[strain tensor|8QS6QMJF5Z]] is $\varepsilon$, that is, with the following property.
$$\varepsilon_{ij} = \tfrac12 \left( \frac{\partial u_i}{\partial X_j} + \frac{\partial u_j}{\partial X_i} \right) \quad \text{for all } i, j.$$
2. For all $i, j, k, l \in \set{1, 2, 3}$, the following equation holds on $\Omega$.
$$\frac{\partial^2 \varepsilon_{ij}}{\partial X_k \partial X_l} + \frac{\partial^2 \varepsilon_{kl}}{\partial X_i \partial X_j} - \frac{\partial^2 \varepsilon_{ik}}{\partial X_j \partial X_l} - \frac{\partial^2 \varepsilon_{jl}}{\partial X_i \partial X_k} = 0.$$

In that case $u$ is unique up to an infinitesimal rigid displacement $X \mapsto a + W X$, with $a \in \R^3$ and $W$ a [[skew-symmetric matrix|0PBY4E9GQF]].

## Remarks

Necessity is a direct computation: substituting $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$, all third derivatives of $u$ cancel.
For sufficiency, one first builds the infinitesimal rotation field $\omega$ from $\varepsilon$ by a line integral.
The condition says that the integrand is curl-free, and simple connectivity makes the integral independent of the path.
Then $u$ is recovered from $\varepsilon + \omega$ by a second line integral.
Of the $81$ equations only $6$ are independent; they say that the double curl of $\varepsilon$ vanishes.
Every field $\varepsilon$ whose entries are affine in $X$ is compatible.
The field with $\varepsilon_{11} = X_2^2$ and all other entries $0$ is not: with $i = j = 1$ and $k = l = 2$ the left side is $\partial_2^2 \varepsilon_{11} = 2 \neq 0$.
Without simple connectivity the condition is only locally sufficient; in a hollow cylinder a compatible strain field may correspond to a multivalued displacement, which models a dislocation.

## Explanations

### L1 human

A strain field tells how each tiny piece of a body is stretched and sheared.
Given such a field, one may ask whether some actual displacement of the body produces it.
Saint-Venant's condition answers this: a certain combination of second derivatives must vanish.

### L2 human

In linear elasticity one may solve for stresses first; the compatibility equations then ensure that the corresponding strains come from a displacement.
Written in terms of stresses through Hooke's law, they become the Beltrami–Michell equations.
In two dimensions only one equation remains, $\partial_2^2 \varepsilon_{11} + \partial_1^2 \varepsilon_{22} = 2 \partial_1 \partial_2 \varepsilon_{12}$.
