---
tag: FQESQA42JE
kind: definition
name: Conley index
msc: [37B30, 37B35]
defines: B3AZ4W0NGT
uses: [0VKD1TP7F3, 0FE2SB8WVJ, BBZP1R872N, WWZTW11664, 0BR3FY5Q8M, T9DG8DDE75, SK0ZJGWXDP]
sources:
  - url: https://en.wikipedia.org/wiki/Conley_index_theory
---

## Definition

Let $X$ be a [[locally compact|0FE2SB8WVJ]] [[metric space|0VKD1TP7F3]] and let $\varphi \colon \R \times X \to X$ be a continuous [[flow|BBZP1R872N]].
For a set $N \subseteq X$, let $\operatorname{Inv}(N) = \set{x \in X : \varphi_t(x) \in N \text{ for all } t \in \R}$, the largest [[invariant set|WWZTW11664]] in $N$.
A compact set $N$ is an *isolating neighbourhood* if $\operatorname{Inv}(N)$ lies in the interior of $N$.
An invariant set $S$ is *isolated* if $S = \operatorname{Inv}(N)$ for some isolating neighbourhood $N$.
An *index pair* for an isolated invariant set $S$ is a pair of compact sets $L \subseteq N \subseteq X$ such that:

1. The closure of $N \setminus L$ is an isolating neighbourhood with $\operatorname{Inv}(\overline{N \setminus L}) = S$.
2. $L$ is positively invariant in $N$: if $x \in L$, $t \ge 0$ and $\varphi_s(x) \in N$ for all $s \in [0, t]$, then $\varphi_t(x) \in L$.
3. $L$ is an exit set for $N$: if $x \in N$ and $\varphi_t(x) \notin N$ for some $t > 0$, then there is $s \in [0, t]$ with $\varphi_s(x) \in L$ and $\varphi_r(x) \in N$ for all $r \in [0, s]$.

Every isolated invariant set has an index pair.
The homotopy type of the [[pointed space|T9DG8DDE75]] $(N/L, [L])$ does not depend on the choice of index pair.
This [[homotopy type|SK0ZJGWXDP]] is the *Conley index* $h(S)$ of $S$.

## Remarks

Here $N/L$ is the [[quotient space|0BR3FY5Q8M]] that collapses $L$ to one point $[L]$; when $L = \emptyset$, one sets $N/L = N \sqcup \set{\ast}$ with base point $\ast$.
Example: let $0$ be a hyperbolic rest point in $\R^n$ with an unstable subspace of dimension $k$.
In adapted coordinates take $N = D^k \times D^{n-k}$, a product of closed balls, and the exit set $L = \partial D^k \times D^{n-k}$.
Then $N/L$ has the homotopy type of $D^k / \partial D^k$, the pointed sphere $S^k$; for an attracting point, $k = 0$ and the index is $S^0$.
Non-example: for the trivial flow $\varphi_t(x) = x$ on $\R$, the invariant set $S = \set{0}$ is not isolated, since every compact $N$ satisfies $\operatorname{Inv}(N) = N$, which is not contained in the interior of $N$.
Ważewski principle: the empty set has index the pointed one-point space, so if $h(S)$ is not that homotopy type, then $S \neq \emptyset$.

## Explanations

### L1 human

The Conley index is the shape left after collapsing the exit of a box around an isolated invariant set.
