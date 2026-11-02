---
tag: 9ZG6HNM84Q
kind: statement
role: theorem
name: Poisson–Jensen formula
msc: [31A10, 30D35]
uses: [0ZZ7ZYDR8W, TCYSWCTYYM, 497K99BQ4Y, 9N6R5ADJXT, 0DEB0JMN0W, Y7A1TP40MB]
about: [0ZZ7ZYDR8W]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen%27s_formula
---

## Statement

Let $0 < R < \infty$ and let $f$ be a [[meromorphic function|0ZZ7ZYDR8W]] on a neighbourhood of the closed disc $\abs{z} \le R$, not identically zero.
Assume that $f$ has no zeros and no poles on the circle $\abs{z} = R$.
Let $a_1, \dots, a_m$ be the zeros and $b_1, \dots, b_n$ the poles of $f$ in $\abs{z} < R$, each listed as often as its multiplicity.
Then, for every $z$ with $\abs{z} < R$ that is neither a zero nor a pole,
$$\log\abs{f(z)} = \frac{1}{2\pi} \int_0^{2\pi} \frac{R^2 - \abs{z}^2}{\abs{R e^{i\theta} - z}^2} \log\abs{f(R e^{i\theta})} \, d\theta - \sum_{\mu = 1}^{m} \log\abs{\frac{R^2 - \bar a_\mu z}{R (z - a_\mu)}} + \sum_{\nu = 1}^{n} \log\abs{\frac{R^2 - \bar b_\nu z}{R (z - b_\nu)}}.$$

## Remarks

Proof idea: each factor $B_a(z) = R(z - a)/(R^2 - \bar a z)$ is a [[Blaschke factor|9N6R5ADJXT]] for the disc of radius $R$: it vanishes only at $a$ and has modulus $1$ on $\abs{z} = R$.
So $g = f \prod_\nu B_{b_\nu} / \prod_\mu B_{a_\mu}$ is holomorphic and zero-free near the closed disc, and $\log\abs{g}$ is [[harmonic|0DEB0JMN0W]].
The Poisson formula, with the [[Poisson kernel|TCYSWCTYYM]] as in the integral, represents $\log\abs{g}$, and $\log\abs{g} = \log\abs{f}$ on the circle.
At $z = 0$ (if $f(0) \ne 0, \infty$) the formula becomes [[Jensen's formula|497K99BQ4Y]]: $\log\abs{f(0)}$ equals the [[circle average|Y7A1TP40MB]] of $\log\abs{f}$ minus $\sum_\mu \log(R/\abs{a_\mu})$ plus $\sum_\nu \log(R/\abs{b_\nu})$.
Example: $f(z) = z$ and $R = 1$; the integral vanishes and the only zero is $a_1 = 0$, so the right side is $-\log\abs{1/z} = \log\abs{z}$.
The formula still holds when $f$ has zeros or poles on the circle, since $\log\abs{f}$ remains integrable there, but the proof needs an extra limit argument.

## Explanations

### L1 human

If one knows the size of a meromorphic function on a circle and where its zeros and poles are inside, one knows its size everywhere inside.
The integral is the harmonic part, and each zero pulls $\log\abs{f}$ down while each pole pushes it up.

### L2 human

The formula is the basic identity of Nevanlinna theory, where it is used to bound the number of zeros of a function by its growth.
It shows that $\log\abs{f}$ for holomorphic $f$ is a harmonic function minus a sum of Green's functions of the disc, one for each zero.
This is a special case of the Riesz decomposition of the subharmonic function $\log\abs{f}$, whose Riesz measure is the sum of point masses at the zeros.
