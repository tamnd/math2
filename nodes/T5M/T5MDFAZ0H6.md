---
tag: T5MDFAZ0H6
kind: statement
role: theorem
name: Gårding's inequality
msc: [35J30, 47F10, 35J20]
uses: [XY8GEQSWPR]
about: [XY8GEQSWPR]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%A5rding%27s_inequality
same_as:
  wikidata: Q5625933
  wikipedia: Gårding's inequality
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set and let $k \ge 1$ be an integer.
For multi-indices $\alpha, \beta$ with $\abs{\alpha}, \abs{\beta} \le k$, let $A_{\alpha\beta} \colon \Omega \to \C$ be bounded measurable functions.
Assume that $A_{\alpha\beta}$ is uniformly continuous on $\Omega$ when $\abs{\alpha} = \abs{\beta} = k$.
Assume the uniform ellipticity condition: there is $\theta > 0$ with
$$\operatorname{Re} \sum_{\abs{\alpha} = \abs{\beta} = k} A_{\alpha\beta}(x)\xi^\alpha\xi^\beta \ge \theta\abs{\xi}^{2k} \quad \text{for all } x \in \Omega,\ \xi \in \R^n.$$
For $u, v$ in the [[Sobolev space|M4CEZ5K9HP]] $H^k_0(\Omega)$, let
$$B(u, v) = \sum_{\abs{\alpha}, \abs{\beta} \le k} \int_\Omega A_{\alpha\beta}(x)\, \partial^\beta u(x)\, \overline{\partial^\alpha v(x)} \, dx.$$
Then there are constants $c > 0$ and $G \ge 0$ such that
$$\operatorname{Re} B(u, u) \ge c\norm{u}_{H^k(\Omega)}^2 - G\norm{u}_{L^2(\Omega)}^2 \quad \text{for all } u \in H^k_0(\Omega).$$

## Remarks

The form $B$ is the sesquilinear form of the [[elliptic operator|XY8GEQSWPR]] $Lu = \sum (-1)^{\abs{\alpha}} \partial^\alpha(A_{\alpha\beta}\partial^\beta u)$ in divergence form.
For constant coefficients and only top-order terms, the inequality follows from Plancherel's theorem: the Fourier transform turns $\operatorname{Re} B(u, u)$ into $\int \operatorname{Re}\sigma(\xi)\abs{\hat u(\xi)}^2 \, d\xi \ge \theta \int \abs{\xi}^{2k}\abs{\hat u(\xi)}^2 \, d\xi$.
For variable coefficients, one freezes the coefficients on small pieces of $\Omega$, using uniform continuity, and glues with a partition of unity.
Lower-order terms are absorbed with the interpolation inequality $\norm{u}_{H^j} \le \varepsilon\norm{u}_{H^k} + C_\varepsilon\norm{u}_{L^2}$ for $j < k$.

Example: for $k = 1$ and $B(u, u) = \int_\Omega \abs{\nabla u}^2 \, dx$, the form of $-\Delta$, one has $B(u, u) = \norm{u}_{H^1}^2 - \norm{u}_{L^2}^2$, so $c = 1$ and $G = 1$ work.

Ellipticity cannot be dropped.
In $\R^2$, the form $\int_\Omega \abs{\partial_1 u}^2 \, dx$ is not elliptic, and functions that oscillate fast in the $x_2$ direction make $\norm{u}_{H^1}$ large while the form and $\norm{u}_{L^2}$ stay bounded.

## Explanations

### L1 human

An elliptic operator controls all derivatives of order $k$, not only some of them.
Gårding's inequality makes this precise in terms of energy: the energy $B(u, u)$ bounds the full Sobolev norm of $u$, up to a harmless multiple of $\norm{u}_{L^2}^2$.
It is the basic estimate behind the existence of weak solutions to elliptic boundary problems.

### L2 human

Adding $G$ to the operator, the form $B(u, v) + G\ip{u}{v}$ becomes coercive on $H^k_0(\Omega)$.
The [[Lax–Milgram theorem|85KK79FCN5]] then gives a unique weak solution of $(L + \lambda)u = f$ for every $f$ and every $\lambda \ge G$.
Combined with the compact embedding of $H^k_0(\Omega)$ in $L^2(\Omega)$, this yields the Fredholm alternative and a discrete spectrum for the Dirichlet problem.
The constant $G$ cannot in general be taken to be $0$, because $L$ may have eigenvalues with negative real part.
