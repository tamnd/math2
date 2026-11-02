---
tag: ZEJ9VKKKRG
kind: definition
name: Method of images
msc: [31B10, 35J08, 78A30]
defines: ZSQSPGBN88
uses: [M36SD56MWQ, BSJ8X2XRN9, 02BH3MCBQB, 05D5EGMFYV]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_image_charges
---

## Definition

Let $n \ge 3$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]] with [[boundary|05D5EGMFYV]] $\partial\Omega$.
Let $\sigma_{n-1}$ be the area of the unit sphere, and let $\Phi(z) = \frac{1}{(n-2)\sigma_{n-1}} \abs{z}^{2-n}$ be the [[fundamental solution|BSJ8X2XRN9]] of $-\Delta$.
Fix $x \in \Omega$.
An *image system* for $\Omega$ and $x$ is a finite or countable family of points $x_j \in \R^n \setminus \overline{\Omega}$ and real numbers $c_j$ such that:

1. the series $h(y) = \sum_j c_j \Phi(y - x_j)$ converges to a harmonic function of $y$ on $\Omega$, continuous on $\overline{\Omega}$;
2. $\Phi(y - x) = h(y)$ for every $y \in \partial\Omega$.

The *method of images* is the construction of the [[Green's function|M36SD56MWQ]] of $\Omega$ as $G(x, y) = \Phi(y - x) - h(y)$ from an image system for each $x \in \Omega$.

## Remarks

Example: for the half-space $\Omega = \set{y : y_n > 0}$ and $x = (x', x_n)$, the single point $x_1 = (x', -x_n)$ with $c_1 = 1$ is an image system, since $\abs{y - x} = \abs{y - x_1}$ when $y_n = 0$.
This gives $G(x, y) = \Phi(y - x) - \Phi(y - x_1)$.
For the unit ball and $x \ne 0$, the inverse point $x^* = x/\abs{x}^2$ with $c = \abs{x}^{2-n}$ is an image system.
Non-example: for the half-space, the point $(x', -x_n)$ with $c = -1$ fails clause 2, since then $h = -\Phi(y - x) \ne \Phi(y - x)$ on the boundary.
In the plane the same idea works with $\Phi(z) = \frac{1}{2\pi} \log \frac{1}{\abs{z}}$, where $h$ may also contain an additive constant; for the unit disc this gives the Green's function $\frac{1}{2\pi} \log \abs{\frac{1 - \bar x y}{y - x}}$ in complex notation.
