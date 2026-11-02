---
tag: GXPDK5Q0HA
kind: definition
name: Cyclic algebra
msc: [16K20, 16S35, 11R52]
defines: D6BM80QYNE
uses: [VFE5B71E7Y, 5HRKJBAY2V, G21MZQCME9, KRNFEZWPY0]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_algebra
---

## Definition

Let $L/K$ be a [[cyclic extension|VFE5B71E7Y]] of degree $n$, and let $\sigma$ be a generator of its Galois group.
Let $a \in K$ be nonzero.
The *cyclic algebra* $(L/K, \sigma, a)$ is the $L$-vector space with basis $1, u, u^2, \dots, u^{n-1}$, with the multiplication determined by
$$u \, x = \sigma(x) \, u \quad (x \in L), \qquad u^n = a.$$

## Remarks

It is the [[crossed product algebra|G21MZQCME9]] for the factor set $f(\sigma^i, \sigma^j) = 1$ if $i + j < n$ and $f(\sigma^i, \sigma^j) = a$ if $i + j \ge n$, for $0 \le i, j < n$.
So it is a [[central simple algebra|5HRKJBAY2V]] over $K$ of degree $n$, split by $L$.
It is isomorphic to $M_n(K)$ if and only if $a$ is a [[norm|KRNFEZWPY0]] from $L$ to $K$, that is, $a = N_{L/K}(b)$ for some $b \in L$.

Example: $L = \C$, $K = \R$, $\sigma$ complex conjugation and $a = -1$ give $\mathbb{H}$.
Since $N_{\C/\R}(z) = \abs{z}^2 \ge 0$, the number $-1$ is not a norm, and $\mathbb{H}$ is not split, as expected.
With $a = 1 = N_{\C/\R}(1)$ one gets $M_2(\R)$.

Non-example: if $L/K$ is Galois but not cyclic, such as $\Q(\sqrt{2}, \sqrt{3})/\Q$, there is no single generator $\sigma$, and the construction does not apply.

If the characteristic of $K$ is not $2$, the quaternion algebra $\left(\frac{a, b}{K}\right)$ is the cyclic algebra $(K(\sqrt{a})/K, \sigma, b)$ when $a$ is not a square in $K$.
