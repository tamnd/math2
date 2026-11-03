---
tag: 29SCH1KERA
kind: definition
name: Shannon capacity of a graph
msc: [05C69, 94A24, 05C76]
defines: S7QCGGYBDR
uses: [00C0BR7D7H, 08ANQHHG3P]
sources:
  - url: https://en.wikipedia.org/wiki/Shannon_capacity_of_a_graph
---

## Definition

Let $G$ be a finite simple [[graph|00C0BR7D7H]] with vertex set $V$.
Let $\alpha(H)$ denote the largest size of an [[independent set|08ANQHHG3P]] of a graph $H$.

1. For $k \ge 1$, the *strong power* $G^{\boxtimes k}$ is the graph with vertex set $V^k$ defined as follows. Two distinct tuples $(u_1, \dots, u_k)$ and $(v_1, \dots, v_k)$ are adjacent if, for every $i$, either $u_i = v_i$ or $u_i v_i$ is an edge of $G$.
2. The *Shannon capacity* of $G$ is
$$\Theta(G) = \sup_{k \ge 1} \alpha\big(G^{\boxtimes k}\big)^{1/k}.$$

## Remarks

Since $\alpha(G^{\boxtimes (k + l)}) \ge \alpha(G^{\boxtimes k}) \, \alpha(G^{\boxtimes l})$, Fekete's lemma shows that the supremum is also the limit as $k \to \infty$.
In particular $\Theta(G) \ge \alpha(G)$.
Some authors call $\log_2 \Theta(G)$ the zero-error capacity.

Example: let $G$ be the graph on $n$ vertices with no edges.
Then $G^{\boxtimes k}$ also has no edges, so $\alpha(G^{\boxtimes k}) = n^k$ and $\Theta(G) = n$.
For the complete graph $K_n$, every two distinct tuples are adjacent, so $\alpha = 1$ and $\Theta(K_n) = 1$.
For the five-cycle with vertices $0, \dots, 4$ and edges $\set{i, i+1}$ mod $5$, the pairs $(i, 2i \bmod 5)$ for $i = 0, \dots, 4$ form an independent set of size $5$ in $C_5^{\boxtimes 2}$, so $\Theta(C_5) \ge \sqrt5$.

Non-example: if in clause 1 two tuples are declared adjacent only when $u_i v_i$ is an edge for every $i$ (the tensor product), the condition "either $u_i = v_i$" is dropped.
For $G = K_2$ the $k$-th tensor power is a perfect matching on $2^k$ vertices, with independence number $2^{k-1}$, and the resulting growth rate is $2$ instead of $\Theta(K_2) = 1$.
