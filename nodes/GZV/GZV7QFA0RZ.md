---
tag: GZV7QFA0RZ
kind: definition
name: Bergman space
msc: [30H20, 32A36]
defines: 2D619WTPYC
uses: [0EWMDD6C14, 0NAHXR1FRH, 8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_space
---

## Definition

Let $\Omega$ be a [[domain|0EWMDD6C14]] in $\C$, let $dA$ be area measure on $\Omega$, and let $0 < p < \infty$.
The *Bergman space* $A^p(\Omega)$ is the set of [[holomorphic functions|0NAHXR1FRH]] $f \colon \Omega \to \C$ such that
$$\norm{f}_{A^p} = \left( \int_\Omega \abs{f(z)}^p \, dA(z) \right)^{1/p} < \infty.$$

## Remarks

The sub-mean value property of $\abs{f}^p$ gives $\abs{f(z)}^p \le \frac{1}{\pi \delta^2}\int_{\abs{w - z} < \delta} \abs{f(w)}^p \, dA(w)$ whenever the disc of radius $\delta$ about $z$ lies in $\Omega$.
So convergence in $A^p$ implies locally uniform convergence, and for $p \ge 1$ the space $A^p(\Omega)$ is a closed subspace of $L^p(\Omega)$, hence a Banach space.
On the [[unit disc|8G5ABXRK85]] $\mathbb{D}$, the monomials satisfy $\int_{\mathbb{D}} \abs{z}^{2n}\, dA = \int_0^{2\pi}\int_0^1 r^{2n+1}\, dr\, d\theta = \pi/(n + 1)$, so $\norm{\sum a_n z^n}_{A^2}^2 = \pi \sum_n \abs{a_n}^2/(n + 1)$.
Example: $g(z) = 1/(1 - z) = \sum z^n$ on $\mathbb{D}$ has $\abs{g(z)}^p = \abs{1 - z}^{-p}$, which is area-integrable near $z = 1$ exactly when $p < 2$; so $g \in A^p(\mathbb{D})$ for $p < 2$.
Non-example: $g \notin A^2(\mathbb{D})$, as also seen from $\pi \sum 1/(n + 1) = \infty$.
Some authors use the normalized area measure $dA/\pi$ on $\mathbb{D}$, which multiplies the norm by a constant.
