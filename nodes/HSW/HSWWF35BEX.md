---
tag: HSWWF35BEX
kind: statement
role: theorem
name: Path lifting property
msc: [57M10, 55R05]
uses: [3XZRRE165N, 0Q1D85B8G6]
about: [3XZRRE165N]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Statement

Let $p \colon E \to X$ be a [[covering map|3XZRRE165N]], let $I = [0, 1]$, let $\gamma \colon I \to X$ be a continuous path, and let $e_0 \in E$ with $p(e_0) = \gamma(0)$.
Then there is a unique continuous path $\tilde\gamma \colon I \to E$ with $\tilde\gamma(0) = e_0$ and $p \circ \tilde\gamma = \gamma$.

## Remarks

For existence, cover $X$ by evenly covered open sets.
By the Lebesgue number lemma, there is a subdivision $0 = s_0 < s_1 < \cdots < s_k = 1$ of the [[interval|0Q1D85B8G6]] with each $\gamma([s_{j-1}, s_j])$ in one evenly covered set $U_j$.
The lift is built step by step: on $[s_{j-1}, s_j]$ it is $(p|_{V})^{-1} \circ \gamma$, where $V$ is the sheet over $U_j$ that contains the point already reached.
Uniqueness holds because the set where two lifts agree is open and closed in the connected interval $I$, and it contains $0$.
Example: for $p(t) = e^{2\pi i t}$ from $\R$ to $S^1$ and $\gamma(s) = e^{2\pi i n s}$, the lift starting at $0$ is $\tilde\gamma(s) = ns$, which ends at $n$.
The covering hypothesis is needed: for the local homeomorphism $q = p|_{(0, 2)} \colon (0, 2) \to S^1$, the loop $\gamma(s) = e^{-2\pi i s}$ with $e_0 = 1$ has no lift.
A lift in $(0, 2)$ is also a lift in $\R$, so by uniqueness it would be $s \mapsto 1 - s$, whose value at $s = 1$ is $0 \notin (0, 2)$.

## Explanations

### L1 human

A covering map is like a projection from many stacked floors to a ground floor.
If you walk along a path on the ground floor and choose a floor to start on, there is exactly one way to walk upstairs that stays above your path.
This lets one read off information about loops downstairs from where the lifted path ends upstairs.

### L2 human

The path lifting property, together with its extension to homotopies, is the main tool of covering space theory.
It shows that $p_* \colon \pi_1(E, e_0) \to \pi_1(X, p(e_0))$ is injective, and it computes the [[fundamental group of the circle|6SQXPE0JPN]] through the covering $\R \to S^1$.
The endpoint $\tilde\gamma(1)$ of the lift of a loop defines an action of $\pi_1(X, x_0)$ on the fibre $p^{-1}(x_0)$, which leads to the classification of covering spaces.
