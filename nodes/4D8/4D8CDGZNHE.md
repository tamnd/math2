---
tag: 4D8CDGZNHE
kind: definition
name: Partial isometry
msc: [47B02, 47A05]
defines: GGDSF85JPD
uses: [HM2HHE3J51, 079D68S3AW, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_isometry
---

## Definition

Let $H$ and $K$ be [[Hilbert spaces|HM2HHE3J51]] and let $V \colon H \to K$ be a bounded linear operator.
The operator $V$ is a *partial isometry* when
$$\norm{Vx} = \norm{x} \quad \text{for all } x \in (\ker V)^\perp,$$
where $\ker V$ is the [[kernel|02YFME3RGW]] of $V$ and $(\ker V)^\perp$ is its [[orthogonal complement|079D68S3AW]].
The space $(\ker V)^\perp$ is the *initial space* of $V$, and the range of $V$ is its *final space*.

## Remarks

Example: the backward shift $V(x_0, x_1, x_2, \ldots) = (x_1, x_2, \ldots)$ on $\ell^2(\N)$ has kernel spanned by $(1, 0, 0, \ldots)$.
A vector orthogonal to the kernel has $x_0 = 0$, and then $\norm{Vx}^2 = \sum_{n \ge 1} \abs{x_n}^2 = \norm{x}^2$; so $V$ is a partial isometry.

Non-example: $T = 2I$ on $\C$ has kernel $\set{0}$, so its initial space is $\C$, but $\norm{T 1} = 2 \ne 1$.

Equivalent forms: $V$ is a partial isometry if and only if $V^*V$ is an orthogonal projection.
Then $V^*V$ is the projection onto the initial space and $VV^*$ is the projection onto the final space.
Another equivalent condition is $VV^*V = V$.
The final space of a partial isometry is closed.
