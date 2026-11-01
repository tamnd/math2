---
tag: JWSNY03J2Y
kind: definition
name: Bergman kernel
msc: [30C40, "46E22", 32A25]
defines: 8RWDHW0CXC
uses: [GZV7QFA0RZ, 0EWMDD6C14, 0QVNCJXRY3, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_kernel
---

## Definition

Let $\Omega$ be a [[domain|0EWMDD6C14]] in $\C$, and let $A^2(\Omega)$ be its [[Bergman space|GZV7QFA0RZ]] with the [[inner product|0QVNCJXRY3]] $\ip{f}{g} = \int_\Omega f \bar g \, dA$.
For each $w \in \Omega$, the map $f \mapsto f(w)$ is a bounded linear functional on the Hilbert space $A^2(\Omega)$.
By the Riesz representation theorem there is a unique $K_w \in A^2(\Omega)$ with
$$f(w) = \ip{f}{K_w} = \int_\Omega f(z)\, \overline{K_w(z)}\, dA(z) \quad \text{for all } f \in A^2(\Omega).$$
The *Bergman kernel* of $\Omega$ is the function $K \colon \Omega \times \Omega \to \C$ given by $K(z, w) = K_w(z)$.

## Remarks

The kernel satisfies $K(w, z) = \overline{K(z, w)}$, and $K(w, w) = \norm{K_w}^2 > 0$ when $A^2(\Omega) \ne \set{0}$.
For any [[orthonormal basis|0S9GGTR0EX]] $(e_n)$ of $A^2(\Omega)$, $K(z, w) = \sum_n e_n(z)\overline{e_n(w)}$.
Example: on the unit disc the functions $e_n(z) = \sqrt{(n + 1)/\pi}\, z^n$ form an orthonormal basis, so $K(z, w) = \frac{1}{\pi}\sum_{n \ge 0} (n + 1)(z\bar w)^n = \frac{1}{\pi(1 - z\bar w)^2}$.
Non-example: the function $\frac{1}{1 - z\bar w}$ is not the Bergman kernel of the disc.
It is the Szegő kernel, which reproduces values for the inner product of the Hardy space $H^2$ with normalized arc length, not for the area inner product.
For instance, with $w = 0$ it is the constant $1$, while $\int_{\mathbb{D}} f \cdot 1 \, dA = \pi f(0)$, not $f(0)$.
If $\varphi \colon \Omega_1 \to \Omega_2$ is biholomorphic, then $K_1(z, w) = \varphi'(z) K_2(\varphi(z), \varphi(w)) \overline{\varphi'(w)}$.
