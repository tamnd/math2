---
tag: T97B2GX3JJ
kind: definition
name: Outer function
msc: [30H10, 30J99]
defines: KGJD4A4ATY
uses: [8G5ABXRK85, 0DG0Z72CQD, TCYSWCTYYM]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Definition

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]].
Let $\varphi$ be a nonnegative measurable function on the unit circle such that $\log \varphi$ is integrable with respect to Lebesgue measure.
Let $c \in \C$ with $\abs{c} = 1$.
The *outer function* with modulus $\varphi$ and constant $c$ is the function $F \colon \mathbb{D} \to \C$ given by
$$F(z) = c \exp\left(\frac{1}{2\pi} \int_0^{2\pi} \frac{e^{it} + z}{e^{it} - z} \log \varphi(e^{it}) \, dt\right).$$
A holomorphic function on $\mathbb{D}$ is *outer* if it is of this form for some $\varphi$ and $c$.

## Remarks

$F$ is [[holomorphic|0DG0Z72CQD]] and has no zeros, and $\log \abs{F}$ is the [[Poisson integral|TCYSWCTYYM]] of $\log \varphi$.
Its radial limits satisfy $\abs{F^*} = \varphi$ almost everywhere.
For $0 < p \le \infty$, $F$ lies in the Hardy space $H^p$ if and only if $\varphi \in L^p$ (Lp space).

Example: $F(z) = 2 + z$ is outer.
It is holomorphic and has no zeros on a neighbourhood of the closed disc, so $\log \abs{F}$ is harmonic and continuous up to the circle.
Hence $\log \abs{F}$ equals the Poisson integral of $\log \varphi$, where $\varphi = \abs{2 + e^{it}}$.
So $F$ and the outer function with modulus $\varphi$ have the same modulus and no zeros; their quotient is a holomorphic function of constant modulus $1$, hence a constant.

Non-example: $f(z) = z$ is not outer.
Its boundary modulus is $\varphi = 1$, and the outer functions with this modulus are the constants of modulus $1$, which differ from $z$.
