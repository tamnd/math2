---
tag: SEKY67RPX5
kind: definition
name: Loop-erased random walk
msc: [60G50, 82B41, 05C81]
defines: ET73YH2T29
uses: [04VZE3FZXF, 00C0BR7D7H, WND87FBAKC]
sources:
  - url: https://en.wikipedia.org/wiki/Loop-erased_random_walk
---

## Definition

Let $G$ be a [[graph|00C0BR7D7H]] and let $\gamma = (\gamma_0, \ldots, \gamma_n)$ be a finite path in $G$.
Its *loop erasure* $\mathrm{LE}(\gamma) = (\sigma_0, \ldots, \sigma_m)$ is defined inductively.
Let $s_0 = \max \set{k : \gamma_k = \gamma_0}$ and $\sigma_0 = \gamma_0$.
If $s_i < n$, let $\sigma_{i+1} = \gamma_{s_i + 1}$ and $s_{i+1} = \max \set{k : \gamma_k = \sigma_{i+1}}$.
Stop at the first $i = m$ with $s_m = n$.

Let $G$ be connected, let $A$ be a nonempty vertex set, and let $X$ be a simple [[random walk|04VZE3FZXF]] on $G$ from a vertex $x$.
Assume that the hitting time $\tau_A = \min \set{k \ge 0 : X_k \in A}$, a [[stopping time|WND87FBAKC]], is finite almost surely.
The *loop-erased random walk* from $x$ to $A$ is the random path $\mathrm{LE}(X_0, X_1, \ldots, X_{\tau_A})$.

## Remarks

The loop erasure visits each vertex at most once, starts at $\gamma_0$ and ends at $\gamma_n$.
Example: for $\gamma = (0, 1, 2, 1, 2, 3)$ on $\Z$, one gets $s_0 = 0$, $\sigma_1 = 1$, $s_1 = 3$, $\sigma_2 = \gamma_4 = 2$, $s_2 = 4$, $\sigma_3 = \gamma_5 = 3$, $s_3 = 5$, so $\mathrm{LE}(\gamma) = (0, 1, 2, 3)$.
Non-example: the path $(0, 1, 2, 1, 2, 3)$ itself is not a loop erasure of anything, since it visits $1$ and $2$ twice.
On a transient graph, such as $\Z^d$ with $d \ge 3$, one also erases the loops of the infinite walk, since each vertex is visited only finitely often.
Wilson's algorithm builds a uniform spanning tree of a finite connected graph from successive loop-erased random walks.
