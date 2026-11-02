---
tag: GZTT6FT18G
kind: statement
role: theorem
name: Sobolev embedding theorem
msc: ["46E35"]
uses: [SASP14MA1Z, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_inequality
---

## Statement

Let $n \ge 1$ and $1 \le p < \infty$.
Let $W^{1,p}(\R^n)$ be the [[Sobolev space|M4CEZ5K9HP]] of functions $u \in L^p(\R^n)$ whose first [[weak derivatives|C3EC148VZD]] lie in $L^p(\R^n)$.

1. If $p < n$, let $p^* = np/(n - p)$. There is a constant $C = C(n, p)$ such that $\norm{u}_{L^{p^*}} \le C \norm{\nabla u}_{L^p}$ for all $u \in W^{1,p}(\R^n)$. So $W^{1,p}(\R^n)$ embeds continuously in the [[Lp space|SASP14MA1Z]] $L^{p^*}(\R^n)$.
2. If $p > n$, let $\gamma = 1 - n/p$. Each $u \in W^{1,p}(\R^n)$ agrees almost everywhere with a bounded function that is [[Hölder continuous|012PBA0FMD]] with exponent $\gamma$. Its supremum norm and Hölder constant are at most $C(n, p) \norm{u}_{W^{1,p}}$.

## Remarks

Part 1 is the Gagliardo–Nirenberg–Sobolev inequality, and part 2 is Morrey's inequality.
For $p < n$, the space $W^{1,p}(\R^n)$ also embeds in $L^q(\R^n)$ for every $q$ between $p$ and $p^*$, by interpolation.

The exponent $p^*$ is forced by scaling.
For $u_\lambda(x) = u(\lambda x)$, one has $\norm{u_\lambda}_{L^q} = \lambda^{-n/q} \norm{u}_{L^q}$ and $\norm{\nabla u_\lambda}_{L^p} = \lambda^{1 - n/p} \norm{\nabla u}_{L^p}$.
The inequality of part 1 can hold for all $\lambda > 0$ only if $-n/q = 1 - n/p$, that is $q = p^*$.

For $p = n \ge 2$, functions in $W^{1,n}(\R^n)$ need not be bounded.
On the ball $\abs{x} < 1/2$ in $\R^2$, the function $\log \log (1/\abs{x})$ is in $W^{1,2}$ but unbounded near $0$.

## Explanations

### L1 human

If a function and its derivative are both small in an average sense, then the function cannot be too large anywhere on a big set.
The theorem says how much better the function is than its derivative.
With enough integrability of the derivative compared with the dimension, the function is even continuous.

### L2 human

Sobolev embeddings are the main tool to get regularity of weak solutions of partial differential equations.
One first finds a solution in a Sobolev space by energy methods, then uses embeddings to show that it is continuous or smooth.
On bounded domains with regular boundary the same embeddings hold, and the Rellich–Kondrachov theorem makes them compact for $q < p^*$.
