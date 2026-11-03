---
tag: AJZDB279GY
kind: definition
name: Fourier algebra
msc: [43A30, 22D25, 43A20]
defines: 3JA4EF163Q
uses: [AHV05ZBCYW, VVE1P3SM6E, PR8C073VWY, N59BW1QFD1, 2N7CR03Q1X]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_algebra
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with left Haar measure.
Let $\lambda$ be the [[left regular representation|PR8C073VWY]] of $G$ on [[$L^2(G)$|VVE1P3SM6E]], given by $\lambda(y)\xi(x) = \xi(y^{-1}x)$.
The *Fourier algebra* $A(G)$ is the set of functions $u \colon G \to \C$ of the form
$$u(x) = \sum_{n=1}^{\infty} \ip{\lambda(x)\xi_n}{\eta_n},$$
where $\xi_n, \eta_n \in L^2(G)$ and $\sum_n \norm{\xi_n}_2 \norm{\eta_n}_2 < \infty$.
Its norm $\norm{u}_{A}$ is the infimum of $\sum_n \norm{\xi_n}_2 \norm{\eta_n}_2$ over all such representations of $u$.
The product is pointwise multiplication.

## Remarks

By a theorem of Eymard, every $u \in A(G)$ has the form $u(x) = \ip{\lambda(x)\xi}{\eta}$ with a single pair $\xi, \eta \in L^2(G)$, and $\norm{u}_A = \inf \norm{\xi}_2 \norm{\eta}_2$ over such pairs.
With this norm $A(G)$ is a commutative Banach algebra contained in the space $C_0(G)$ of [[continuous functions vanishing at infinity|N59BW1QFD1]], and $\norm{u}_\infty \le \norm{u}_A$.
It is the predual of the [[group von Neumann algebra|2N7CR03Q1X]] of $G$.
Eymard also showed that the Gelfand spectrum of $A(G)$ is $G$, with $x \in G$ giving the character $u \mapsto u(x)$.

Example: $G = \Z$.
The Fourier series isomorphism $\ell^2(\Z) \to L^2(\mathbb{T})$ with $\hat\xi(z) = \sum_k \xi(k) z^k$ turns $\lambda(n)$ into multiplication by $z^n$.
So $\ip{\lambda(n)\xi}{\eta} = \int_{\mathbb{T}} z^{n} \, \hat\xi(z) \overline{\hat\eta(z)} \, dz$ for the normalized Haar measure $dz$, which is the Fourier coefficient of index $-n$ of $\hat\xi \overline{\hat\eta} \in L^1(\mathbb{T})$.
Every function in $L^1(\mathbb{T})$ is such a product, so $A(\Z)$ is the algebra of Fourier coefficient sequences of integrable functions on the circle.
More generally, for abelian $G$, the Fourier transform maps $L^1(\widehat{G})$ isometrically onto $A(G)$.

Non-example: the constant function $1$ on $\R$ is not in $A(\R)$, since it does not vanish at infinity.
For a compact group $G$ with normalized Haar measure, $1 = \ip{\lambda(\cdot)1}{1}$ does lie in $A(G)$.
