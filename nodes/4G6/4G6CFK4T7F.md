---
tag: 4G6CFK4T7F
kind: definition
name: Homotopy fiber
msc: [55R05, 55P05]
defines: 4F3KWXYXBA
uses: [T9DG8DDE75, 03NAMV1DHJ, 0X3WGX95FE, 0WS9P12FQR, 0GBG8B49AA]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_fiber
---

## Definition

Let $X$ be a topological space, let $(Y, y_0)$ be a [[pointed space|T9DG8DDE75]], and let $f \colon X \to Y$ be a [[continuous map|0X3WGX95FE]].
Let $I = [0, 1]$ and let $Y^I$ be the space of [[paths|03NAMV1DHJ]] $\gamma \colon I \to Y$ with the compact-open topology.
The *homotopy fiber* of $f$ over $y_0$ is
$$F_f = \set{(x, \gamma) \in X \times Y^I : \gamma(0) = f(x), \ \gamma(1) = y_0},$$
with the [[subspace topology|0WS9P12FQR]] of the [[product|0GBG8B49AA]] $X \times Y^I$.

## Remarks

The map $F_f \to X$, $(x, \gamma) \mapsto x$, is a fibration, and its fiber over $x$ is the space of paths from $f(x)$ to $y_0$.
The ordinary fiber $f^{-1}(y_0)$ embeds in $F_f$ by $x \mapsto (x, c_{y_0})$, where $c_{y_0}$ is the constant path.
If $f$ is a [[Serre fibration|PB9JXQ2KC3]], this embedding is a weak homotopy equivalence.

Example: if $X = \set{x_0}$ and $f(x_0) = y_0$, then $F_f$ is the space of paths from $y_0$ to $y_0$, which is the [[loop space|2JFF5F3EGF]] $\Omega Y$.

Non-example: the ordinary fiber need not be a homotopy fiber.
Let $X = \set{x_0}$, $Y = \R$, $f(x_0) = 0$ and $y_0 = 1$.
Then $f^{-1}(1)$ is empty, while $F_f$ is the space of paths in $\R$ from $0$ to $1$, which is nonempty and contractible.

The notations $\operatorname{hofib}(f)$ and $\operatorname{hofib}_{y_0}(f)$ are also used.
