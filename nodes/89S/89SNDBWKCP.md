---
tag: 89SNDBWKCP
kind: definition
name: Reduced K-theory of a space
msc: [55N15, 55R50]
defines: RASZAXBHX0
uses: [A4393CW9G4, P4DZM975BV, T9DG8DDE75, 0TVJZYB6SH, 0S1FJ8VEX9]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_K-theory
    locator: Definitions
---

## Definition

Let $(X, x_0)$ be a [[pointed|T9DG8DDE75]] [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]].
Let $K(X)$ be the [[Grothendieck group of complex vector bundles|A4393CW9G4]] over $X$, and let $i \colon \set{x_0} \to X$ be the inclusion.
The *reduced K-theory* of $X$ is the kernel
$$\tilde{K}(X) = \ker\left(i^* \colon K(X) \to K(\set{x_0}) \cong \Z\right),$$
where $i^*$ restricts bundles to the base point and $K(\set{x_0}) \cong \Z$ by dimension.

## Remarks

The constant map $X \to \set{x_0}$ splits $i^*$, so $K(X) \cong \tilde{K}(X) \oplus \Z$.

Equivalently, call two [[vector bundles|P4DZM975BV]] $E$ and $F$ over $X$ stably equivalent if $E \oplus \C^m \cong F \oplus \C^n$ for some $m, n \ge 0$.
For connected $X$, the stable equivalence classes form a group under direct sum, and $[E] \mapsto [E] - \operatorname{rank}(E)$ identifies it with $\tilde{K}(X)$.

Example: let $X = S^2 = \C P^1$ and let $H$ be the tautological line bundle.
Then $[H] - 1$ restricts to $1 - 1 = 0$ at the base point, so it lies in $\tilde{K}(S^2)$, and it generates $\tilde{K}(S^2) \cong \Z$.

Non-example: the class $[\C] = 1$ of the trivial line bundle is not in $\tilde{K}(X)$, since it restricts to $1 \ne 0$ in $K(\set{x_0})$.
