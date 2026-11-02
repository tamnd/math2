---
tag: FFDYRMG5DP
kind: definition
name: Sobolev space
msc: ["46E35"]
defines: M4CEZ5K9HP
uses: [C3EC148VZD, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_space
---

## Definition

Let $U \subseteq \R^n$ be open, let $k \ge 0$ be an integer and let $1 \le p \le \infty$.
The *Sobolev space* $W^{k,p}(U)$ is the set of functions $u \in L^p(U)$ with the following property.
For every multi-index $\alpha$ with $\abs{\alpha} \le k$, the [[weak derivative|C3EC148VZD]] $D^\alpha u$ exists and lies in $L^p(U)$.
Its norm is
$$\norm{u}_{W^{k,p}(U)} = \Big( \sum_{\abs{\alpha} \le k} \int_U \abs{D^\alpha u}^p \, dx \Big)^{1/p} \text{ for } p < \infty, \qquad \norm{u}_{W^{k,\infty}(U)} = \sum_{\abs{\alpha} \le k} \operatorname*{ess\,sup}_U \abs{D^\alpha u}.$$
The space $W^{k,p}_0(U)$ is the closure in $W^{k,p}(U)$ of the space $C_c^\infty(U)$ of test functions.

## Remarks

Here $L^p(U)$ is the [[Lp space|SASP14MA1Z]], and functions equal almost everywhere are identified.
Each $W^{k,p}(U)$ is a Banach space, and $H^k(U) = W^{k,2}(U)$ is a Hilbert space with inner product $\sum_{\abs{\alpha} \le k} \int_U D^\alpha u \, D^\alpha v \, dx$.
For $k = 0$ one gets $W^{0,p}(U) = L^p(U)$.
For $1 \le p < \infty$, the smooth functions in $W^{k,p}(U)$ are dense in it (Meyers–Serrin).

Example: $u(x) = \abs{x}$ lies in $W^{1,p}(-1, 1)$ for all $p$.
Indeed $u$ is bounded, and its weak derivative $\sgn x$ is bounded, so both lie in every $L^p(-1, 1)$.

Non-example: $\sgn x$ is bounded, so it lies in every $L^p(-1, 1)$, but it has no weak derivative on $(-1, 1)$.
So it is in no space $W^{1,p}(-1, 1)$.
