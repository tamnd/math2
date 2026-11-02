---
tag: 62PG3KVVVK
kind: definition
name: Homotopy extension property
msc: [55P05]
defines: D42X0F1EG1
uses: [9YA6S6HD9V, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_extension_property
---

## Definition

Let $X$ be a topological space, let $A \subseteq X$ carry the [[subspace topology|0WS9P12FQR]], let $Y$ be a topological space, and let $I = [0, 1]$.
Let $f \colon X \to Y$ be continuous, and let $h \colon A \times I \to Y$ be a [[homotopy|9YA6S6HD9V]] with $h(a, 0) = f(a)$ for all $a \in A$.
An *extension* of $h$ along $f$ is a homotopy $H \colon X \times I \to Y$ such that:

1. $H(x, 0) = f(x)$ for all $x \in X$;
2. $H(a, t) = h(a, t)$ for all $a \in A$ and $t \in I$.

The pair $(X, A)$ has the *homotopy extension property with respect to $Y$* if every such $h$ has an extension along every such $f$.
The pair $(X, A)$ has the *homotopy extension property* if it has it with respect to every topological space $Y$.

## Remarks

If $A$ is closed in $X$, then $(X, A)$ has the homotopy extension property if and only if $X \times \set{0} \cup A \times I$ is a retract of $X \times I$.
Example: $(D^n, S^{n-1})$ has it, because the radial projection from the point $(0, \ldots, 0, 2)$ of $\R^{n+1}$ gives a retraction of $D^n \times I$ onto $D^n \times \set{0} \cup S^{n-1} \times I$.
Non-example: let $X = \set{0} \cup \set{1/n : n \ge 1}$ and $A = \set{0}$.
A retraction $r$ of $X \times I$ onto $X \times \set{0} \cup A \times I$ would fix $(0, 1)$, and would send each connected set $\set{1/n} \times I$ to $(1/n, 0)$.
Then $r(1/n, 1) = (1/n, 0) \to (0, 0) \neq r(0, 1)$, so $r$ is not continuous and the pair fails the property.
Every CW pair has the homotopy extension property.
