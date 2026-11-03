---
tag: XCZZM1QJK9
kind: definition
name: Model order reduction
msc: [93B11, 93C05]
defines: D54SM8Q12V
uses: [6J9MPVHSMF, 86JKV3TRFD, WDVJXWV3RF, QVREFP7BH7]
sources:
  - url: https://en.wikipedia.org/wiki/Model_order_reduction
---

## Definition

Let $(A, B, C, D)$ be a [[linear time-invariant system|6J9MPVHSMF]] of order $n$ with input dimension $m$ and output dimension $p$, and let $G$ be its [[transfer function|86JKV3TRFD]].
Let $1 \le r < n$.
A *reduced-order model* of order $r$ is a system $(A_r, B_r, C_r, D_r)$ with $A_r \in \R^{r \times r}$, $B_r \in \R^{r \times m}$, $C_r \in \R^{p \times r}$, $D_r \in \R^{p \times m}$, with transfer function $G_r$.
*Model order reduction* is the problem of choosing such a model so that the error $G - G_r$ is small in a given system norm.
A common norm is the [[H-infinity norm|QVREFP7BH7]].
Usually the reduced model must also keep properties of the original system, such as stability.

## Remarks

Many methods are projection methods.
One chooses $V, W \in \R^{n \times r}$ with $W^T V = I_r$ and sets $A_r = W^T A V$, $B_r = W^T B$, $C_r = C V$ and $D_r = D$.
This approximates the state by $x \approx V x_r$ and asks the residual of the equation to be orthogonal to the columns of $W$.

Example: $A = \operatorname{diag}(-1, -100)$, $B = (1, 1)^T$, $C = (1, 1)$, $D = 0$ has $G(s) = 1/(s + 1) + 1/(s + 100)$.
The projection with $V = W = (1, 0)^T$ gives $A_r = -1$, $B_r = C_r = 1$, so $G_r(s) = 1/(s + 1)$.
The error $1/(s + 100)$ has H-infinity norm $1/100$, attained at $s = 0$.

Non-example: a [[realization|WDVJXWV3RF]] of the same $G$ of order $n$ obtained by a change of coordinates is not a reduction, since its order is not smaller than $n$.

The same notions are used for nonlinear and parameter-dependent models, with other measures of the error.
