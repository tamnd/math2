---
tag: GX3PZRZX4B
kind: definition
name: Hankel singular value
msc: [93B11, 93C05, 15A18]
defines: VCPQ0B99MA
uses: [6J9MPVHSMF, 703MCKB5SZ, 9YEW705KHA, 92GVPZH9FT, 0BQAA2BK3Q, P4EKQS312D]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_singular_value
---

## Definition

Let $A \in \R^{n \times n}$, $B \in \R^{n \times m}$ and $C \in \R^{p \times n}$, and assume that every eigenvalue of $A$ has negative real part.
Consider the [[linear time-invariant system|6J9MPVHSMF]] $x' = Ax + Bu$, $y = Cx$.
Its infinite-horizon [[controllability Gramian|703MCKB5SZ]] and [[observability Gramian|9YEW705KHA]] are
$$P = \int_0^\infty e^{At} B B^T e^{A^T t} \, dt, \qquad Q = \int_0^\infty e^{A^T t} C^T C e^{At} \, dt.$$
The [[eigenvalues|0BQAA2BK3Q]] of $PQ$ are real and nonnegative; list them as $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n \ge 0$.
The *Hankel singular values* of the system are the numbers $\sigma_i = \sqrt{\lambda_i}$ for $i = 1, \ldots, n$.

## Remarks

The Gramians are the unique solutions of the [[Lyapunov equations|92GVPZH9FT]] $AP + PA^T + BB^T = 0$ and $A^T Q + QA + C^T C = 0$.
The eigenvalues of $PQ$ are nonnegative because $PQ$ is similar to $P^{1/2} Q P^{1/2}$, which is positive semidefinite.
Under a change of coordinates $x = T^{-1} \tilde{x}$, the Gramians become $TPT^T$ and $T^{-T} Q T^{-1}$, so $PQ$ becomes $T PQ T^{-1}$ and the $\sigma_i$ do not change.
The nonzero $\sigma_i$ are the nonzero singular values of the [[Hankel operator|P4EKQS312D]] of the system, which maps past inputs to future outputs; the largest one, $\sigma_1$, is the Hankel norm.
For a minimal realization all $\sigma_i$ are positive.

Example: for $A = -1$, $B = C = 1$, the Lyapunov equations read $-2P + 1 = 0$ and $-2Q + 1 = 0$.
So $P = Q = 1/2$, $PQ = 1/4$, and the only Hankel singular value is $\sigma_1 = 1/2$.

Non-example: for $A = 1$, $B = C = 1$, the integrand $e^{2t}$ of $P$ is not integrable, so the Gramians and the Hankel singular values are not defined.
Here the hypothesis on the eigenvalues of $A$ fails.
