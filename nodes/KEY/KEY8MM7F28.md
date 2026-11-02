---
tag: KEY8MM7F28
kind: definition
name: Trace operator
msc: ["46E35"]
defines: Z2T5R88QDB
uses: [M4CEZ5K9HP, SASP14MA1Z, 03TM135G0N, N6NX1VT837]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_operator
---

## Definition

Let $U \subset \R^n$ be a bounded open set with $C^1$ boundary $\partial U$, carrying its surface measure, and let $1 \le p < \infty$.
The *trace operator* is the unique bounded linear map
$$T \colon W^{1,p}(U) \to L^p(\partial U)$$
such that $T u = u|_{\partial U}$ for every $u \in W^{1,p}(U)$ that is continuous on $\overline{U}$.
Here $W^{1,p}(U)$ is the [[Sobolev space|M4CEZ5K9HP]].
The function $T u$ is the *trace* of $u$ on $\partial U$.

## Remarks

The operator exists and is unique.
For $u$ smooth up to the boundary, the divergence theorem gives $\norm{u|_{\partial U}}_{L^p(\partial U)} \le C \norm{u}_{W^{1,p}(U)}$ with $C$ depending on $p$ and $U$.
Such functions are dense in $W^{1,p}(U)$, so restriction extends uniquely to a [[continuous linear map|03TM135G0N]] on all of $W^{1,p}(U)$.

Example: on $U = (0, 1)$ the boundary is $\set{0, 1}$, and every $u \in W^{1,p}(0, 1)$ has a continuous representative.
Its trace is the pair of values $(u(0), u(1))$ of that representative.

Non-example: on $U = (0, 1)$, restriction to the boundary is not bounded for the $L^p$ norm alone.
The functions $u_k(x) = (1 - x)^k$ satisfy $u_k(0) = 1$ while $\norm{u_k}_{L^p(0,1)} \to 0$, so no bounded map $L^p(0, 1) \to \R^2$ extends restriction.
This is why the definition uses $W^{1,p}(U)$.

The kernel of $T$ is $W^{1,p}_0(U)$.
For $1 < p < \infty$, the image of $T$ is the [[fractional Sobolev space|N6NX1VT837]] $W^{1 - 1/p, p}(\partial U)$, a result of Gagliardo.
