---
tag: YT2B9KQ0BG
kind: definition
name: Fuchsian equation
msc: [34M03, 34M35]
defines: ZBVH2YE50B
uses: [H96HXG6CA0, QK2J038VB4, 0XDK9CGYKJ, 0J78KBPFZB]
sources:
  - url: https://en.wikipedia.org/wiki/Fuchsian_theory
---

## Definition

Let $p_1, \ldots, p_n$ be [[rational functions|0XDK9CGYKJ]] of $z$ with complex coefficients.
The linear equation
$$y^{(n)} + p_1(z)\, y^{(n-1)} + \cdots + p_n(z)\, y = 0$$
is *Fuchsian* (or of Fuchsian class) if it satisfies the following condition.
Every point of the [[Riemann sphere|0J78KBPFZB]] $\C \cup \set{\infty}$ is an [[ordinary point|QK2J038VB4]] or a [[regular singular point|H96HXG6CA0]] of the equation.

## Remarks

At a finite point $a$, the condition says that each $p_k$ has at most a pole of order $k$ at $a$.
At $\infty$, it says that $z^k p_k(z)$ stays bounded as $z \to \infty$, for each $k$.
Since the $p_k$ are rational, there are only finitely many singular points.

Example: the hypergeometric equation $z (1 - z) y'' + \left( c - (a + b + 1) z \right) y' - a b\, y = 0$ is Fuchsian.
Its normalised coefficients are $p = \frac{c - (a + b + 1) z}{z (1 - z)}$ and $q = \frac{-a b}{z (1 - z)}$.
They have simple poles at $0$ and $1$, and $z p(z) \to a + b + 1$ and $z^2 q(z) \to a b$ as $z \to \infty$.
So the singular points $0$, $1$ and $\infty$ are all regular.

Non-example: the Bessel equation $z^2 y'' + z y' + (z^2 - \nu^2) y = 0$ has $q(z) = 1 - \frac{\nu^2}{z^2}$.
Then $z^2 q(z) = z^2 - \nu^2$ is unbounded as $z \to \infty$, so $\infty$ is an irregular singular point and the equation is not Fuchsian.
