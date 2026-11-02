---
tag: Q19EMZ4CP7
kind: definition
name: Wiener amalgam space
msc: [42B35, "46E30"]
defines: H9H80DM3SX
uses: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_amalgam_space
---

## Definition

Let $d \ge 1$, let $1 \le p, q \le \infty$ and let $Q = [0, 1)^d$.
For a measurable function $f \colon \R^d \to \C$ and $k \in \Z^d$, let $a_k(f) = \norm{f \cdot 1_{k + Q}}_{L^p(\R^d)}$, the norm in the [[Lebesgue space|SASP14MA1Z]] $L^p$ of the restriction of $f$ to the cube $k + Q$.
The *Wiener amalgam space* $W(L^p, \ell^q)(\R^d)$ is the set of measurable $f$ with
$$\norm{f}_{W(L^p, \ell^q)} = \Big( \sum_{k \in \Z^d} a_k(f)^q \Big)^{1/q} < \infty,$$
with the supremum over $k$ in place of the sum when $q = \infty$.
Functions that agree almost everywhere are identified.

## Remarks

$L^p$ is the local component and $\ell^q$ the global component.
In the general theory of Feichtinger, $L^p$ is replaced by a Banach space $B$ of local behaviour.
The space $\ell^q$ is replaced by a solid sequence or function space $C$ of global behaviour, and the sharp cut-off $1_{k + Q}$ by a smooth partition of unity.
Two facts follow from the definition:

1. $W(L^p, \ell^p) = L^p(\R^d)$ with equal norms.
2. If $p_1 \ge p_2$ and $q_1 \le q_2$, then $W(L^{p_1}, \ell^{q_1}) \subseteq W(L^{p_2}, \ell^{q_2})$, since the cube $Q$ has measure $1$.

Example: let $d = 1$ and $f(x) = 1/(1 + \abs{x})$, with $p = \infty$.
On $[k, k+1)$ the supremum of $f$ is $1/(1 + \min(\abs{k}, \abs{k + 1}))$.
These numbers behave like $1/\abs{k}$, so their $q$-th powers have a finite sum for every $q > 1$.
Hence $f \in W(L^\infty, \ell^q)(\R)$ for $q > 1$.

Non-example: the same $f$ is not in $W(L^\infty, \ell^1)(\R)$, because the sum of these numbers is a harmonic series and diverges.
