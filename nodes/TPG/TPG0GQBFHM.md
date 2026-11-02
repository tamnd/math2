---
tag: TPG0GQBFHM
kind: definition
name: Complex powers of elliptic operators
msc: [58J40, 58J52, 35S05]
defines: MTZCFEV37Y
uses: [MT9P2X85V8, 0NEGN5CRSC, FF27N0BWTP, Z2CP530WDE, VJCJYXGTDY, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Zeta_function_regularization
---

## Definition

Let $M$ be a closed manifold of dimension $n$ with a smooth positive density, and let $E$ be a Hermitian vector bundle over $M$.
Let $A \colon \Gamma(E) \to \Gamma(E)$ be an [[elliptic operator|MT9P2X85V8]] of order $m > 0$ that is formally [[self-adjoint|0NEGN5CRSC]] and positive: $\int_M \ip{Au}{u} > 0$ for every nonzero $u \in \Gamma(E)$.
Then $L^2(E)$ has an orthonormal basis $(\varphi_j)_{j \ge 1}$ of smooth eigensections, $A \varphi_j = \lambda_j \varphi_j$, whose [[eigenvalues|0BQAA2BK3Q]] satisfy $0 < \lambda_1 \le \lambda_2 \le \cdots$ and $\lambda_j \to \infty$.
For $s \in \C$, the *complex power* $A^s$ is the operator
$$A^s u = \sum_{j \ge 1} \lambda_j^{s} \, \ip{u}{\varphi_j} \, \varphi_j, \qquad u \in \Gamma(E),$$
where $\lambda_j^s = e^{s \log \lambda_j}$ with the real logarithm.

## Remarks

The powers satisfy $A^s A^t = A^{s+t}$, $A^0 = \id$ and $A^1 = A$, and $A^{-1}$ is the inverse of $A$.
Seeley proved that $A^s$ is a classical [[pseudo-differential operator|FF27N0BWTP]] of order $ms$.
For $\operatorname{Re} s > n/m$, the operator $A^{-s}$ is [[trace class|Z2CP530WDE]], and the spectral zeta function
$$\zeta_A(s) = \operatorname{tr} A^{-s} = \sum_{j \ge 1} \lambda_j^{-s}$$
is holomorphic there.
It extends to a meromorphic function on $\C$ with at most simple poles, and it is holomorphic at $s = 0$.
This gives the [[zeta-regularized|VJCJYXGTDY]] determinant $\det A = e^{-\zeta_A'(0)}$.
More generally, Seeley defined $A^s$ by a contour integral of $\lambda^s (A - \lambda)^{-1}$ for elliptic $A$ whose principal symbol has no eigenvalues on some ray from $0$, without assuming self-adjointness.

Example: on the circle $S^1 = \R / 2\pi\Z$ with $dx$, let $A = 1 - d^2/dx^2$, which is elliptic of order $2$ and positive.
Its eigensections are $e^{ikx}/\sqrt{2\pi}$, $k \in \Z$, with eigenvalues $1 + k^2$, so $A^{-s} e^{ikx} = (1 + k^2)^{-s} e^{ikx}$.
Then $\zeta_A(s) = \sum_{k \in \Z} (1 + k^2)^{-s}$ converges for $\operatorname{Re} s > \frac{1}{2} = \frac{n}{m}$ with $n = 1$ and $m = 2$.

Non-example: the operator $-d^2/dx^2$ on $S^1$ is elliptic and self-adjoint but not positive, since it kills the constants.
The formula would need $0^s$, which is not defined for all $s$; one first restricts to the orthogonal complement of the kernel.

## Explanations

### L1 human

Complex powers of a positive elliptic operator raise each eigenvalue to the power $s$, keeping the eigenfunctions, just as for a positive matrix.
