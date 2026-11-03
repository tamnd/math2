---
tag: 9XYSB8YA1M
kind: definition
name: Killing form
msc: [17B05, 17B20]
defines: TWVQT18JXE
uses: [5JJYBJ6A8K, 54XSPNAM1J, 0KZDNGA561, 0AXZNE5XNH, GMB9ANSTT1, 1ZAT1Z967A]
sources:
  - url: https://en.wikipedia.org/wiki/Killing_form
---

## Definition

Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
For $x \in \mathfrak g$, let $\operatorname{ad} x \colon \mathfrak g \to \mathfrak g$, $y \mapsto [x, y]$, be its image under the [[adjoint representation|54XSPNAM1J]].
The *Killing form* of $\mathfrak g$ is the map $\kappa \colon \mathfrak g \times \mathfrak g \to k$ given by
$$\kappa(x, y) = \tr(\operatorname{ad} x \circ \operatorname{ad} y),$$
where $\tr$ is the [[trace|0KZDNGA561]] of an endomorphism of $\mathfrak g$.

## Remarks

The Killing form is a [[symmetric bilinear form|0AXZNE5XNH]], since $\tr(AB) = \tr(BA)$.
It is [[invariant|GMB9ANSTT1]]: $\kappa([x, y], z) = \kappa(x, [y, z])$, because $\operatorname{ad}[x, y] = [\operatorname{ad} x, \operatorname{ad} y]$ and $\tr([A, B] C) = \tr(A [B, C])$.
It is preserved by every automorphism of $\mathfrak g$.

Example: in the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(k)$ with basis $e, h, f$ and $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$, the matrix of $\operatorname{ad} h$ is $\operatorname{diag}(2, 0, -2)$, so $\kappa(h, h) = 4 + 0 + 4 = 8$.
The map $\operatorname{ad} e \circ \operatorname{ad} f$ sends $e \mapsto 2e$, $h \mapsto 2h$ and $f \mapsto 0$, so $\kappa(e, f) = 4$.
Also $\kappa(e, e) = \kappa(f, f) = \kappa(e, h) = \kappa(f, h) = 0$.
In general $\kappa(x, y) = 4 \tr(xy)$ on $\mathfrak{sl}_2(k)$, and $\kappa(x, y) = 2n \tr(xy)$ on $\mathfrak{sl}_n(k)$.

Non-example: the trace form $\tr(xy)$ on $\mathfrak{sl}_2(k)$ is also invariant and symmetric.
It is not the Killing form when $\operatorname{char} k$ is neither $2$ nor $3$, since it takes the value $2$ at $(h, h)$, not $8$.
