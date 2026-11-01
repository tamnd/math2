---
tag: TMAHZSNTA1
kind: definition
name: Nevanlinna class
msc: [30H15, 30D50]
defines: M3WQTN3FH2
uses: [8G5ABXRK85, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_type_(mathematics)
---

## Definition

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]].
For $x > 0$ let $\log^+ x = \max(\log x, 0)$, and let $\log^+ 0 = 0$.
The *Nevanlinna class* $N$ is the set of [[holomorphic functions|0DG0Z72CQD]] $f \colon \mathbb{D} \to \C$ such that
$$\sup_{0 < r < 1} \frac{1}{2\pi} \int_0^{2\pi} \log^+ \abs{f(r e^{it})} \, dt < \infty.$$

## Remarks

A holomorphic function on $\mathbb{D}$ lies in $N$ if and only if $f = g/h$ with $g$ and $h$ bounded holomorphic on $\mathbb{D}$ and $h$ without zeros.
Such functions are said to be of bounded type.
Since $\log^+ x \le x^p / p$ for $p > 0$, every Hardy space $H^p$ is contained in $N$.

Example: $f(z) = \exp\left(\frac{1}{1 - z}\right)$.
For $z = r e^{it}$ one has $\log \abs{f(z)} = \operatorname{Re} \frac{1}{1 - z} = \frac{1 - r \cos t}{1 - 2r \cos t + r^2} > 0$.
This equals $\frac{1}{2}\left(1 + \frac{1 - r^2}{1 - 2r \cos t + r^2}\right)$, and the Poisson kernel has mean $1$, so the mean of $\log^+ \abs{f}$ on each circle is exactly $1$.
So $f \in N$, although $f$ lies in no $H^p$.

Non-example: $f(z) = \sin\left(\frac{\pi}{1 - z}\right)$ is holomorphic on $\mathbb{D}$ but not in $N$.
Its zeros are $z_k = 1 - 1/k$ for $k \ge 1$, and $\sum_k (1 - \abs{z_k}) = \sum_k 1/k$ diverges.
By Jensen's formula, the zeros of a function in $N$ that is not identically $0$ satisfy the Blaschke condition $\sum (1 - \abs{z_k}) < \infty$.
