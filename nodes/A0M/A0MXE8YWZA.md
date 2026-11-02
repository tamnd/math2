---
tag: A0MXE8YWZA
kind: statement
role: theorem
name: Calderón–Vaillancourt theorem
msc: [35S05, 47G30, 42B20]
uses: [FF27N0BWTP, AM4RNWVV4Q, DPVM34ADZV, SASP14MA1Z]
about: [FF27N0BWTP]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-differential_operator
---

## Statement

Let $n \ge 1$ and let $a \colon \R^n \times \R^n \to \C$ be a smooth function such that every derivative of $a$ is bounded: for all multi-indices $\alpha, \beta$,
$$\sup_{x, \xi \in \R^n} \abs{\partial_x^\alpha \partial_\xi^\beta a(x, \xi)} < \infty.$$
That is, $a$ lies in the [[symbol class|AM4RNWVV4Q]] $S^0_{0,0}$.
Let $a(x, D)$ be the [[pseudo-differential operator|FF27N0BWTP]] with symbol $a$, defined on Schwartz functions $u$ by
$$a(x, D) u(x) = (2\pi)^{-n} \int_{\R^n} e^{i x \cdot \xi} a(x, \xi) \, \hat u(\xi) \, d\xi,$$
where $\hat u$ is the [[Fourier transform|DPVM34ADZV]] of $u$.
Then $a(x, D)$ extends to a bounded operator on $L^2(\R^n)$.
Moreover there are a constant $C$ and an integer $N$, depending only on $n$, with
$$\norm{a(x, D)}_{L^2 \to L^2} \le C \max_{\abs{\alpha} \le N,\ \abs{\beta} \le N} \ \sup_{x, \xi} \abs{\partial_x^\alpha \partial_\xi^\beta a(x, \xi)}.$$

## Remarks

One standard proof cuts the symbol into pieces $a_{jk}$ localized near the points $(j, k)$ of the lattice $\Z^n \times \Z^n$ by a smooth partition of unity.
Each piece gives an operator with norm bounded by finitely many derivatives of $a$.
Integration by parts shows that the products $T_{jk}^* T_{j'k'}$ and $T_{jk} T_{j'k'}^*$ decay fast in $\abs{j - j'}$ and $\abs{k - k'}$.
The [[Cotlar–Stein lemma|XBJEDC18B1]] then sums the pieces.

Example: if $a(x, \xi) = m(\xi)$ does not depend on $x$, then $a(x, D)$ is the Fourier multiplier with symbol $m$, and Plancherel's theorem gives the bound $\sup \abs{m}$ directly.
The theorem says that bounded smooth dependence on $x$ costs only finitely many derivatives.
The same conclusion holds for symbols in the classes $S^0_{\rho, \rho}$ with $0 \le \rho < 1$.

For the class $S^0_{1,1}$, which allows $x$-derivatives to grow like $\abs{\xi}$, the operators are in general not bounded on $L^2$.

## Explanations

### L1 human

A pseudo-differential operator acts on a function by changing the strength of each frequency $\xi$, by an amount $a(x, \xi)$ that may also depend on the position $x$.
When $a$ depends only on $\xi$, the operator is bounded on $L^2$ as long as $a$ is bounded.
The Calderón–Vaillancourt theorem says the operator stays bounded on $L^2$ when $a$ depends on both variables, provided $a$ and its derivatives are all bounded.

### L2 human

This is the basic $L^2$ boundedness result of the calculus of pseudo-differential operators.
It shows that operators of order $0$ in the classes $S^0_{\rho,\delta}$ with $\delta \le \rho$ and $\delta < 1$ are bounded on $L^2$.
By composition with $(I - \Delta)^{s/2}$, operators of order $m$ then map the Sobolev space $H^{s+m}$ to $H^s$.
Its proof is a model use of almost orthogonality.
The class $S^0_{0,0}$ is invariant under translations in both $x$ and $\xi$, which makes it natural in phase-space and semiclassical analysis.
