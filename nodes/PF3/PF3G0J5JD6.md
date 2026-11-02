---
tag: PF3G0J5JD6
kind: definition
name: Wave front set
msc: [35A18, 35A27, 58J47]
defines: 3T5Q9WVQX8
uses: [DPVM34ADZV, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_front_set
---

## Definition

Let $\Omega$ be an open subset of $\R^n$ and let $u$ be a distribution on $\Omega$.
A *cone* is a set $\Gamma \subseteq \R^n \setminus \set{0}$ such that $t \xi \in \Gamma$ for all $\xi \in \Gamma$ and all $t > 0$.
A point $(x_0, \xi_0) \in \Omega \times (\R^n \setminus \set{0})$ is *microlocally regular* for $u$ if there exist:

1. a test function $\varphi \in C_c^\infty(\Omega)$ with $\varphi(x_0) \ne 0$,
2. an open cone $\Gamma$ with $\xi_0 \in \Gamma$,
3. for each integer $N \ge 0$ a constant $C_N$,

such that the [[Fourier transform|DPVM34ADZV]] of the compactly supported distribution $\varphi u$ satisfies $\abs{\widehat{\varphi u}(\xi)} \le C_N (1 + \abs{\xi})^{-N}$ for all $\xi \in \Gamma$ and all $N$.
The *wave front set* $\operatorname{WF}(u)$ is the set of points of $\Omega \times (\R^n \setminus \set{0})$ that are not microlocally regular for $u$.

## Remarks

Since $\varphi u$ has compact support, $\widehat{\varphi u}$ is a [[smooth function|0V33BNKZ9S]], so the decay condition makes sense pointwise.
By construction $\operatorname{WF}(u)$ is closed, and it is conic: $(x, \xi) \in \operatorname{WF}(u)$ implies $(x, t\xi) \in \operatorname{WF}(u)$ for $t > 0$.
Its projection to $\Omega$ is the singular support of $u$, the complement of the largest open set on which $u$ is smooth.
In particular $\operatorname{WF}(u) = \emptyset$ if and only if $u$ is smooth.

Example: for the [[Dirac delta|0KPHENZ5S7]] $\delta$ at $0$ in $\R^n$, one has $\operatorname{WF}(\delta) = \set{0} \times (\R^n \setminus \set{0})$.
Check: at a point $x_0 \ne 0$ one may take $\varphi$ vanishing near $0$, so $\varphi \delta = 0$.
At $x_0 = 0$, $\widehat{\varphi \delta}(\xi) = \varphi(0)$ is a nonzero constant, which decays in no direction.

Non-example: let $u(x) = H(x_1)$ on $\R^2$, where $H$ is the [[Heaviside step function|09C4JP7Y0M]], and look at the point $(0, (0, 1))$.
Take $\varphi(x) = \chi(x_1) \chi(x_2)$ with $\chi \in C_c^\infty(\R)$ and $\chi(0) \ne 0$.
Then $\widehat{\varphi u}(\xi) = a(\xi_1)\, \hat\chi(\xi_2)$, where $a$ is the Fourier transform of $\chi H$ and is bounded.
In the cone $\abs{\xi_1} < \abs{\xi_2}$ around $(0, 1)$ one has $\abs{\xi} < 2 \abs{\xi_2}$, and $\hat\chi(\xi_2)$ decays faster than any power of $\abs{\xi_2}$.
So the point is microlocally regular, and it is not in $\operatorname{WF}(u)$.
In fact $\operatorname{WF}(u) = \set{x_1 = 0} \times \set{(\xi_1, 0) : \xi_1 \ne 0}$.

The wave front set transforms well under changes of coordinates, as a subset of the cotangent bundle minus its zero section, so the notion extends to distributions on manifolds.
