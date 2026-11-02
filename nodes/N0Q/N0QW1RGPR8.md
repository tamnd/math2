---
tag: N0QW1RGPR8
kind: definition
name: Resurgent function
msc: [34M30, "30E15", 40G10]
defines: 37R4QJCARA
uses: [0DG0Z72CQD, 0M3YQJ81NB, 8DJPSYSHGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Resurgent_function
---

## Definition

Let $\Omega$ be a closed discrete subset of $\C$.
A power series $\hat\varphi(\zeta) = \sum_{n \ge 0} c_n \zeta^n$ with positive radius of convergence is *$\Omega$-continuable* if it satisfies both conditions:

1. Its sum is a [[holomorphic function|0DG0Z72CQD]] on a disc $D$ centred at $0$ with $D \cap \Omega \subseteq \set{0}$.
2. It has an [[analytic continuation|0M3YQJ81NB]] along every path in $\C \setminus \Omega$ that starts in $D \setminus \set{0}$.

A formal series $\tilde\varphi(z) = \sum_{n \ge 0} a_n z^{-n-1}$ in the variable $z$ near $\infty$ is an *$\Omega$-resurgent series* if its formal Borel transform
$$\hat\varphi(\zeta) = \sum_{n \ge 0} \frac{a_n}{n!} \zeta^n$$
is $\Omega$-continuable.
The functions $\hat\varphi$ obtained in this way are the *resurgent functions* in the Borel plane.
The series $\tilde\varphi$ is a *resurgent series* if it is $\Omega$-resurgent for some closed discrete $\Omega$.

## Remarks

Example: $\tilde\varphi(z) = \sum_{n \ge 0} (-1)^n n! \, z^{-n-1}$ has Borel transform $\sum_{n \ge 0} (-1)^n \zeta^n = \frac{1}{1 + \zeta}$.
This converges on the unit disc and extends to a holomorphic function on $\C \setminus \set{-1}$, so $\tilde\varphi$ is $\set{-1}$-resurgent.
Non-example: $\sum_{n \ge 0} (n!)^2 z^{-n-1}$ is not resurgent, because its Borel transform $\sum_{n \ge 0} n! \, \zeta^n$ has radius of convergence $0$, so clause 1 fails.
Every convergent series $\sum a_n z^{-n-1}$ is resurgent, since then $\hat\varphi$ is entire.
Écalle's general notion allows the singular set to depend on the path of continuation; it is called endless continuability, and the $\Omega$-continuable germs are a special case.
The Borel transform of the formal product of two resurgent series is the convolution of their Borel transforms, and Écalle showed that resurgence is preserved under this product.
