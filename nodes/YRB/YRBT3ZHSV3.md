---
tag: YRBT3ZHSV3
kind: statement
role: theorem
name: Nevanlinna parametrization of solutions
msc: [44A60, "30E05"]
uses: [TBNCFXTMMW, GCTN4BZ1ET, DYR1QFNGNJ, 0G4F0XB9X2, 0NAHXR1FRH, X6XGGH5FPW]
about: [TBNCFXTMMW, GCTN4BZ1ET]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_function
---

## Statement

Let $(m_n)_{n \ge 0}$ be a sequence of real numbers for which the [[Hamburger moment problem|TBNCFXTMMW]] is [[indeterminate|GCTN4BZ1ET]].
Let $V$ be the set of positive [[Borel measures|DYR1QFNGNJ]] $\mu$ on $\R$ with $\int_\R x^n \, d\mu(x) = m_n$ for all $n \ge 0$.
A Pick function is a [[holomorphic function|0NAHXR1FRH]] $\varphi$ on the [[upper half-plane|X6XGGH5FPW]] $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$ with $\operatorname{Im} \varphi(z) \ge 0$ for all $z \in \mathbb{H}$.
Let $\mathcal{P}$ be the set of Pick functions together with the constant $\infty$.
Then there are four [[entire functions|0G4F0XB9X2]] $A, B, C, D$, real on $\R$ and determined by $(m_n)$, with $A(z) D(z) - B(z) C(z) = 1$ for all $z \in \C$, such that the following holds.
For each $\varphi \in \mathcal{P}$ there is exactly one $\mu_\varphi \in V$ with
$$\int_\R \frac{d\mu_\varphi(x)}{x - z} = -\frac{A(z) \varphi(z) - C(z)}{B(z) \varphi(z) - D(z)} \quad \text{for all } z \in \mathbb{H},$$
where for $\varphi = \infty$ the right side means $-A(z)/B(z)$.
The map $\varphi \mapsto \mu_\varphi$ is a bijection from $\mathcal{P}$ onto $V$.

## Remarks

The functions $A, B, C, D$ are built from the orthonormal polynomials $p_n$ of the moment sequence and the polynomials $q_n$ of the second kind.
For example, $B(z) = -1 + z \sum_{k \ge 0} q_k(0) p_k(z)$ and $D(z) = z \sum_{k \ge 0} p_k(0) p_k(z)$, and these series converge locally uniformly exactly because the problem is indeterminate.
The left side is the Stieltjes transform of $\mu_\varphi$, which determines $\mu_\varphi$ by the [[Stieltjes inversion formula|C0X2A02MRE]].
The parameters $\varphi = t$ with $t \in \R \cup \set{\infty}$ give the N-extremal solutions, for which the polynomials are dense in $L^2(\mu_t)$.
Each $\mu_t$ is a discrete measure supported on the zeros of $B t - D$, or on the zeros of $B$ when $t = \infty$.
The hypothesis of indeterminacy is needed: in the determinate case $V$ has only one element, so there is nothing to parametrize.
Sign conventions for $A, B, C, D$ differ between books.

## Explanations

### L1 human

When a list of moments does not single out one distribution, there are infinitely many distributions with those moments.
The theorem describes all of them at once.
Four fixed functions turn each choice of a free parameter, a Pick function, into exactly one solution, and every solution arises in this way.

### L2 human

The parametrization reduces the study of an indeterminate moment problem to the study of four entire functions, the Nevanlinna matrix.
These entire functions have order at most one and minimal exponential type.
The parameters $t \in \R \cup \set{\infty}$ give solutions that are spectral measures of self-adjoint extensions of the Jacobi operator of the moment sequence.
The Pick functions are the functions of the [[Herglotz representation theorem|9ZBAX4ZPX0]] transplanted from the disc to the upper half-plane, so the parameter set has a concrete integral form.
