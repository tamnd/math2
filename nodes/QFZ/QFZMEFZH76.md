---
tag: QFZMEFZH76
kind: definition
name: Path space fibration
msc: [55R05, 55P35]
defines: D3BN7MBKTR
uses: [T9DG8DDE75, 03NAMV1DHJ, 0WS9P12FQR, 2JFF5F3EGF, 4F3KWXYXBA]
sources:
  - url: https://en.wikipedia.org/wiki/Path_space_fibration
---

## Definition

Let $(X, x_0)$ be a [[pointed space|T9DG8DDE75]] and let $I = [0, 1]$.
The *path space* of $(X, x_0)$ is
$$PX = \set{\gamma \colon I \to X \text{ continuous} : \gamma(0) = x_0},$$
the set of [[paths|03NAMV1DHJ]] starting at $x_0$, with the [[subspace topology|0WS9P12FQR]] of the compact-open topology.
The *path space fibration* is the map
$$p \colon PX \to X, \quad p(\gamma) = \gamma(1).$$

## Remarks

The map $p$ is a Hurewicz fibration, and its fiber $p^{-1}(x_0)$ is the [[loop space|2JFF5F3EGF]] $\Omega X$.
The space $PX$ is contractible: $h_s(\gamma)(t) = \gamma((1 - s) t)$ deforms every path to the constant path at $x_0$.
So the long exact sequence of homotopy groups gives $\pi_n(\Omega X) \cong \pi_{n+1}(X, x_0)$ for $n \ge 0$.

Example: for $X = \R$ and $x_0 = 0$, the fiber over $a \in \R$ is the space of paths from $0$ to $a$, and $p$ is surjective, since the path $t \mapsto t a$ ends at $a$.

Non-example: if $X$ is not path-connected, $p$ is not surjective.
For $X = \set{0, 1}$ with the discrete topology and $x_0 = 0$, every path from $0$ is constant, so $PX$ is a point and $p^{-1}(1)$ is empty.

The fiber of $p$ over $y \in X$ is the [[homotopy fiber|4F3KWXYXBA]] over $y$ of the inclusion $\set{x_0} \to X$.
So $p$ replaces this inclusion by a fibration with a contractible total space.
