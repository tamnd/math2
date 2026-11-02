---
tag: EYXNKYMJJH
kind: statement
role: corollary
name: Lidskii's trace formula for integral operators
msc: [45C05, 47B10, 47G10]
uses: [3JVT83K8A1, Z2CP530WDE, 4NSACSWRJZ, QD23PJR6RP, SASP14MA1Z, PKGADWXPYH]
about: [3JVT83K8A1]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_class
---

## Statement

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be continuous, and let $T$ be the integral operator $(T x)(s) = \int_a^b K(s, t) \, x(t) \, dt$ on the [[Lp space|SASP14MA1Z]] $L^2(a, b)$.
Assume that $T$ is a [[trace class operator|Z2CP530WDE]].
Let $(\lambda_n)$ be the nonzero eigenvalues of $T$, each repeated according to its algebraic multiplicity.
Then $\sum_n \abs{\lambda_n} < \infty$ and
$$\sum_n \lambda_n = \int_a^b K(s, s) \, ds.$$

## Remarks

The proof has two steps.
First, for a trace class integral operator with continuous kernel, the operator trace equals the [[trace of the kernel|3JVT83K8A1]] $\int_a^b K(s, s) \, ds$.
Second, [[Lidskii's theorem|QD23PJR6RP]] says that the operator trace equals the sum of the eigenvalues, counted with algebraic multiplicity.

Example: on $[0, 1]$ let $K(s, t) = \min(s, t)$.
The [[eigenfunctions|4NSACSWRJZ]] are $\sin((n - \tfrac12)\pi s)$ with eigenvalues $\lambda_n = 1/((n - \tfrac12)^2 \pi^2)$, $n \ge 1$.
Since $K$ is a positive kernel and $\sum_n \lambda_n < \infty$, the operator is trace class.
The formula reads $\sum_{n \ge 1} \frac{4}{(2n - 1)^2 \pi^2} = \int_0^1 s \, ds = \frac12$, which is the identity $\sum_{n \ge 1} (2n-1)^{-2} = \pi^2/8$.

The trace class hypothesis cannot be dropped.
There are continuous kernels whose operators are not trace class, and for them the sum of the eigenvalues need not converge absolutely.
Take the Volterra kernel $K(s, t) = 1$ for $t \le s$ and $K(s, t) = 0$ otherwise.
Its operator has no nonzero eigenvalue, while the diagonal integral is $b - a$.
There is no contradiction: this kernel is not continuous, and the operator is not trace class.

## Explanations

### L1 human

For a matrix, the sum of the eigenvalues equals the sum of the diagonal entries.
For an integral operator, the diagonal entries become the values $K(s, s)$, and the sum becomes an integral.
The formula says that, for good enough kernels, the sum of all eigenvalues equals this integral.

### L2 human

For a continuous Hermitian kernel of positive type, the formula follows from [[Mercer's theorem|PKGADWXPYH]] by integrating the expansion $K(s, s) = \sum_n \lambda_n \abs{\varphi_n(s)}^2$.
Lidskii's theorem extends it to kernels that are not self-adjoint, where the eigenvalues may be complex and the eigenfunctions need not form a basis.
The formula is the first case of the trace identities $\sum_n \lambda_n^m = \int_a^b K_m(s, s) \, ds$ for the iterated kernels $K_m$, which hold for every continuous kernel when $m \ge 2$, since then $T^m$ is trace class.
