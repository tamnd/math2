---
tag: YM3JZ34PME
kind: statement
role: theorem
name: Rellich–Kondrachov theorem
msc: ["46E35", 47B38]
uses: [M4CEZ5K9HP, SASP14MA1Z, M2NEP1K5AE, B03CA692K3, 0381S8Z5P0]
about: [M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Rellich%E2%80%93Kondrachov_theorem
same_as:
  wikidata: Q3527151
  wikipedia: Rellich–Kondrachov theorem
---

## Statement

Let $n \ge 2$ and let $U \subset \R^n$ be a bounded open set with $C^1$ boundary.

1. Let $1 \le p < n$ and $p^* = \frac{np}{n - p}$. For every $q$ with $1 \le q < p^*$, the inclusion of the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(U)$ into the [[Lp space|SASP14MA1Z]] $L^q(U)$ is compact.
2. Let $n \le p \le \infty$. Then the inclusion of $W^{1,p}(U)$ into $L^p(U)$ is compact.

Here compact means that every bounded sequence in $W^{1,p}(U)$ has a subsequence that converges in $L^q(U)$, respectively in $L^p(U)$.

## Remarks

The inclusion is bounded by the [[Sobolev inequality|B03CA692K3]].
For compactness, one mollifies: the mollified functions $u^\varepsilon$ form an equicontinuous and bounded family for each fixed $\varepsilon$, so the [[Arzelà–Ascoli theorem|0381S8Z5P0]] applies to them.
The error $\norm{u^\varepsilon - u}_{L^1}$ is at most $\varepsilon \norm{\nabla u}_{L^1}$, uniformly on bounded sets, and interpolation with the bound in $L^{p^*}$ gives the same uniform control in $L^q$ for $q < p^*$.
So the inclusion is a [[compact operator|M2NEP1K5AE]].

The hypotheses are needed.
The inclusion into $L^{p^*}(U)$ itself is not compact: the rescaled functions $\lambda^{(n-p)/p} \varphi(\lambda x)$ for a fixed bump $\varphi$ are bounded in $W^{1,p}$ but concentrate at a point as $\lambda \to \infty$.
On an unbounded set, such as $U = \R^n$, translates $\varphi(x - k e_1)$ of a bump are bounded in $W^{1,p}$ but have no convergent subsequence in $L^p$.

## Explanations

### L1 human

A bounded family of functions with bounded slopes cannot oscillate wildly.
The theorem turns this into a compactness statement: from any such sequence one can extract a subsequence that converges in the mean.
It is the infinite-dimensional analogue of the fact that a bounded sequence of numbers has a convergent subsequence.

### L2 human

Compactness is how one passes to the limit in approximations of nonlinear equations: a weak limit in $W^{1,p}$ becomes a strong limit in $L^q$, so nonlinear terms in $u$ converge.
It also implies that the inverse of an elliptic operator such as $-\Delta$ with Dirichlet conditions is compact on $L^2(U)$, which gives a discrete spectrum of eigenvalues.
The Poincaré inequality for functions with zero mean is proved from it by contradiction.
