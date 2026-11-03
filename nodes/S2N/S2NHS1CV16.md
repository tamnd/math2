---
tag: S2NHS1CV16
kind: statement
role: theorem
name: Lovász bound on the Shannon capacity
msc: [05C69, 94A24, 90C22]
uses: [S7QCGGYBDR, 00C0BR7D7H, 08ANQHHG3P]
about: [S7QCGGYBDR]
sources:
  - url: https://en.wikipedia.org/wiki/Lov%C3%A1sz_number
---

## Statement

Let $G$ be a finite simple [[graph|00C0BR7D7H]] with vertex set $V$.
An *orthonormal representation* of $G$ is a family of unit vectors $(u_v)_{v \in V}$ in some $\R^d$ such that $u_v \cdot u_w = 0$ whenever $v \ne w$ are not adjacent.
The *Lovász number* of $G$ is $\vartheta(G) = \min_{c, (u_v)} \max_{v \in V} (c \cdot u_v)^{-2}$.
Here the minimum runs over all orthonormal representations $(u_v)$ of $G$ and all unit vectors $c$ in the same space.
Then the [[Shannon capacity|S7QCGGYBDR]] of $G$ satisfies
$$\Theta(G) \le \vartheta(G).$$

## Remarks

The idea of the proof has two steps.
First, $\alpha(G) \le \vartheta(G)$: if $S$ is an [[independent set|08ANQHHG3P]], the vectors $u_v$, $v \in S$, are pairwise orthogonal, so $\sum_{v \in S} (c \cdot u_v)^2 \le 1$, and each term is at least $1/\vartheta(G)$.
Second, $\vartheta(G \boxtimes H) \le \vartheta(G) \, \vartheta(H)$, because the tensor products $u_v \otimes w_x$ form an orthonormal representation of the strong product.
Hence $\alpha(G^{\boxtimes k}) \le \vartheta(G)^k$ for every $k$, and taking $k$-th roots gives the bound.

Example: for the five-cycle $C_5$, an "umbrella" of five unit vectors around a handle $c$ gives $\vartheta(C_5) \le \sqrt5$.
Since $\alpha(C_5^{\boxtimes 2}) = 5$, also $\Theta(C_5) \ge \sqrt5$, and so $\Theta(C_5) = \sqrt5$.
This settled a question left open by Shannon in 1956.

The bound is not always sharp: there are graphs with $\Theta(G) < \vartheta(G)$.

## Explanations

### L1 human

The Shannon capacity of a graph is very hard to compute, because it involves words of every length.
Lovász found a number $\vartheta(G)$, defined with vectors in space, that is always at least as large and that can be computed.
For the five-cycle the two numbers meet, which determined its capacity $\sqrt5$, a case that Shannon had left open.

### L2 human

The Lovász number is the value of a semidefinite program, so it can be computed to any precision in polynomial time.
It is sandwiched as $\alpha(G) \le \vartheta(G) \le \chi(\overline{G})$, where $\chi(\overline G)$ is the chromatic number of the complement; this is Lovász's sandwich theorem.
For perfect graphs, $\alpha(G) = \chi(\overline G)$, so $\vartheta$ computes both, and also $\Theta(G) = \alpha(G)$.
Lovász proved the bound in 1979, and the paper introduced orthonormal representations as a tool in combinatorics.
