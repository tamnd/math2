---
tag: TGKPC4GV7R
kind: definition
name: ℓ-adic cohomology
msc: [14F20, 14G15]
defines: E1DVHN06CR
uses: [7YX76G0838, HV6YBS0YDH, GBN9F8FAQ3, CHT5JYM6QW, DZB378CNCK]
sources:
  - url: https://en.wikipedia.org/wiki/%C3%89tale_cohomology
---

## Definition

Let $k$ be a separably closed field and let $X$ be an [[algebraic variety|HV6YBS0YDH]] over $k$.
Let $\ell$ be a prime number different from the characteristic of $k$.
For $i \ge 0$, the *$\ell$-adic cohomology groups* of $X$ are
$$H^i(X, \Z_\ell) = \varprojlim_n H^i_{\text{ét}}(X, \Z/\ell^n\Z), \qquad H^i(X, \Q_\ell) = H^i(X, \Z_\ell) \otimes_{\Z_\ell} \Q_\ell.$$
Here $H^i_{\text{ét}}$ is [[étale cohomology|7YX76G0838]].
The [[inverse limit|DZB378CNCK]] is taken along the maps induced by the reductions $\Z/\ell^{n+1}\Z \to \Z/\ell^n\Z$.
$\Z_\ell$ is the ring of [[$\ell$-adic integers|GBN9F8FAQ3]], and $\Q_\ell$ is the field of [[$\ell$-adic numbers|CHT5JYM6QW]].

## Remarks

Example: let $k$ be algebraically closed and $X = \mathbb{P}^1_k$.
Then $H^0_{\text{ét}}(X, \Z/\ell^n\Z) = \Z/\ell^n\Z$, $H^1_{\text{ét}} = 0$ and $H^2_{\text{ét}} \cong \Z/\ell^n\Z$, compatibly in $n$.
So $H^i(X, \Q_\ell)$ is $\Q_\ell$ for $i = 0, 2$ and $0$ otherwise, as for the sphere $\mathbb{P}^1(\C)$.
Non-example: the condition $\ell \ne \operatorname{char} k$ is needed.
Let $k$ have characteristic $p > 0$ and let $E$ be an elliptic curve over $k$.
Then $H^1(E, \Q_p)$ has dimension $1$ if $E$ is ordinary and $0$ if $E$ is supersingular, not the expected dimension $2$.
For $X$ proper over $k$, the groups $H^i(X, \Q_\ell)$ are finite-dimensional and vanish for $i > 2 \dim X$.
