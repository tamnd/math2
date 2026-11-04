---
tag: A81YEQ28RM
kind: proof
name: Proof that compact subsets of a metric space are bounded
msc: ["54E45"]
proves: 0R7BTEWCJ2
uses: [063W5JMY85, 00R0X1WGPX, 0P6PMJB4MA, 0DC3MPR7C9, 0B2305GNAZ, 0P953MG05E, 01M6CW9VM6]
sources:
  - url: https://proofwiki.org/wiki/Compact_Subspace_of_Metric_Space_is_Bounded
---

## Proof

We cover $K$ by open balls of growing radius around one point.

1. Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $K$ be a [[compact|00R0X1WGPX]] subset of $X$.
2. If $K = \emptyset$, then $K$ is [[bounded|0P953MG05E]], since the condition on pairs of points is empty. So assume $K \ne \emptyset$ and fix $a \in K$.
3. For each integer $n \ge 1$, let $B(a, n)$ be the [[open ball|0DC3MPR7C9]]. It is open, since [[open balls are open|0B2305GNAZ]].
4. Let $x \in K$. Choose an integer $n > d(a, x)$. Then $x \in B(a, n)$. So the balls $B(a, n)$ with $n \ge 1$ cover $K$.
5. By [[compactness via open covers|0P6PMJB4MA]], there are integers $n_1, \ldots, n_p \ge 1$ with $K \subseteq B(a, n_1) \cup \cdots \cup B(a, n_p)$. Since $K \ne \emptyset$, $p \ge 1$.
6. Let $N = \max(n_1, \ldots, n_p)$. Each $B(a, n_j)$ lies in $B(a, N)$, so $K \subseteq B(a, N)$.
7. Let $x, y \in K$. By the [[triangle inequality|01M6CW9VM6]], $d(x, y) \le d(x, a) + d(a, y) < 2N$.
8. So $d(x, y) \le 2N$ for all $x, y \in K$, and $K$ is bounded.

## Idea

The balls of radius $1, 2, 3, \ldots$ around a point exhaust the whole space.
Compactness keeps only finitely many of them, and the largest one already holds all of $K$.
