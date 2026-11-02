---
tag: EAEFNBF94A
kind: definition
name: Degree of a central simple algebra
msc: [16K20, 16K50]
defines: NNXSP5KKAC
uses: [5HRKJBAY2V, 1735VGRT2P, 0X6AB5P3G1]
sources:
  - url: https://en.wikipedia.org/wiki/Central_simple_algebra
---

## Definition

Let $K$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$.
The dimension $\dim_K A$ is a perfect square $n^2$ with $n \ge 1$.
The *degree* of $A$ is the integer $n = \sqrt{\dim_K A}$, written $\deg A$.

## Remarks

Let $\bar{K}$ be an [[algebraic closure|0X6AB5P3G1]] of $K$.
The [[tensor product|1735VGRT2P]] $A \otimes_K \bar{K}$ is central simple over $\bar{K}$, hence isomorphic to $M_n(\bar{K})$ for some $n$ by Wedderburn's theorem.
So $\dim_K A = \dim_{\bar{K}} M_n(\bar{K}) = n^2$ is a square.

Example: $\deg M_n(K) = n$, and the quaternion algebra $\mathbb{H}$ over $\R$ has degree $2$, since $\dim_\R \mathbb{H} = 4$.

Non-example: $\C$ has dimension $2$ over $\R$, which is not a square, so it has no degree as an algebra over $\R$; it is not central over $\R$.

If $A \cong M_m(D)$ with $D$ a division algebra, then $\deg A = m \deg D$.
Degree is multiplicative: $\deg(A \otimes_K B) = \deg A \cdot \deg B$.
