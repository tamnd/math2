---
tag: G3WJ3XDJ7M
kind: example
name: Volterra operator
msc: [45D05, 47G10, 47B07]
instance_of: [M2NEP1K5AE, CB5G212Q03]
uses: [SASP14MA1Z, BMKATJ802A, 9V7YQA85PC, QSJKPKPM7H, Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_operator
same_as:
  wikidata: Q5313336
  wikipedia: Volterra operator
---

## Example

The *Volterra operator* is the operator $V$ on the [[Lp space|SASP14MA1Z]] $L^2(0, 1)$ given by
$$(V f)(t) = \int_0^t f(s) \, ds, \quad t \in [0, 1].$$
It is the integral operator of the [[Volterra equation of the first kind|H6ZGEDM4VV]] with kernel $K(t, s) = 1$ for $s \le t$ and $K(t, s) = 0$ for $s > t$.

Check that it is a [[compact operator|M2NEP1K5AE]]: the kernel is square-integrable on $[0, 1]^2$, with $\int_0^1 \int_0^1 \abs{K}^2 = 1/2$.
So $V$ is a [[Hilbert–Schmidt integral operator|CB5G212Q03]], and Hilbert–Schmidt operators are compact.

Check that $V$ has no eigenvalue.
If $V f = 0$, then $\int_0^t f = 0$ for all $t$, so $f = 0$ almost everywhere.
If $V f = \lambda f$ with $\lambda \ne 0$, then $f = \lambda^{-1} V f$ is continuous, hence $V f$ is continuously differentiable, and $f' = f / \lambda$ with $f(0) = 0$; so $f = 0$.

Check that the [[spectrum|BMKATJ802A]] is $\set{0}$.
The power $V^n$ has kernel $(t - s)^{n-1}/(n-1)!$ for $s \le t$, so $\norm{V^n} \le 1/(n-1)!$.
Hence the [[spectral radius|9V7YQA85PC]] $\lim_n \norm{V^n}^{1/n}$ is $0$, while $0$ is in the spectrum because a compact operator on an infinite-dimensional space is not invertible.

## Remarks

The operator norm of $V$ is $2/\pi$.
Its [[singular values|QSJKPKPM7H]] are $2/((2n - 1)\pi)$, $n \ge 1$, which are square-summable but not summable, so $V$ is not a [[trace class operator|Z2CP530WDE]].
The adjoint is $(V^* f)(t) = \int_t^1 f(s) \, ds$, and $V + V^*$ is the rank-one operator $f \mapsto \int_0^1 f$.
The Volterra operator is the standard example of a nonzero quasinilpotent compact operator: its spectrum is the same as that of the zero operator.

## Explanations

### L1 human

The Volterra operator takes a function and returns its running integral from $0$.
It is the most basic integral operator, the continuous version of taking partial sums.
It is a compact operator with no eigenvalues at all, something that cannot happen for a square matrix over the complex numbers.
This is why equations $f - \lambda V f = g$ can be solved for every $\lambda$.
