---
tag: PPT1ZSSHBN
kind: definition
name: Reproducing kernel Hilbert space
msc: ["46E22"]
defines: 4CK2GSRAGD
uses: [HM2HHE3J51, 03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space
---

## Definition

Let $X$ be a nonempty set and let $\mathbb{K}$ be $\R$ or $\C$.
Let $H$ be a vector space of functions $X \to \mathbb{K}$, with pointwise operations, that is a [[Hilbert space|HM2HHE3J51]] for some inner product.
The space $H$ is a *reproducing kernel Hilbert space* if the following holds.
For every $x \in X$, the evaluation map $f \mapsto f(x)$ is a [[continuous linear map|03TM135G0N]] from $H$ to $\mathbb{K}$.

## Remarks

For each $x$ there is then a unique $k_x \in H$ with $f(x) = \ip{f}{k_x}$ for all $f \in H$.
The function $K(x, y) = k_y(x) = \ip{k_y}{k_x}$ on $X \times X$ is the *reproducing kernel* of $H$.

Example: $H = \ell^2(\N)$, seen as functions on $X = \N$.
Evaluation at $n$ is $f \mapsto f(n)$, and $\abs{f(n)} \le \norm{f}_2$, so it is continuous.
Here $k_n$ is the unit vector $e_n$ and $K(m, n) = 1$ if $m = n$ and $0$ otherwise.

Non-example: $L^2([0, 1])$ is not a reproducing kernel Hilbert space.
Its elements are classes of functions equal almost everywhere, so $f \mapsto f(x)$ is not even defined on it.
The continuous functions on $[0, 1]$ with the $L^2$ inner product are not one either, because this space is not complete.

The Hardy space of the unit disc is a reproducing kernel Hilbert space with kernel $K(z, w) = 1/(1 - z \bar{w})$.
