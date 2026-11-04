---
tag: CE3ZA48YP2
kind: proof
name: Proof that every finite tree with at least two vertices has a leaf, by a longest path
msc: [05C05]
proves: 0H8Q4MANBD
uses: [0MJ0JS72DZ, 0FFAYNMAJZ, 0XNN9Z8E5A, 0VJZM0F9YM, 0JDE56HWQ8, 07CT9RDY7Q, 0PD57PSHNR, 0T0F6CCS9W]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Properties
---

## Proof

We take a longest path and show that its last vertex is a leaf.

1. The [[tree|0MJ0JS72DZ]] $T$ is [[connected|0FFAYNMAJZ]] and [[acyclic|0XNN9Z8E5A]]. Let $n \ge 2$ be its number of vertices.
2. Choose distinct vertices $u \ne v$. By connectedness there is a [[walk|0VJZM0F9YM]] $(w_0, \dots, w_k)$ from $u$ to $v$. Since $u \ne v$, $k \ge 1$.
3. So $w_0 \sim w_1$, and $(w_0, w_1)$ is a [[path|0JDE56HWQ8]] of length $1$.
4. A path has pairwise distinct vertices, so its length is at most $n - 1$. Hence there is a path $P = (v_0, v_1, \dots, v_k)$ of largest length, and $k \ge 1$ by step 3.
5. The vertex $v_{k-1}$ is a neighbour of $v_k$, so $\deg(v_k) \ge 1$. Let $x$ be any neighbour of $v_k$. We show that $x = v_{k-1}$.
6. If $x$ is not a vertex of $P$, then $(v_0, \dots, v_k, x)$ is a path of length $k + 1$. This contradicts the choice of $P$.
7. So $x = v_i$ for some $i$. Since $x \sim v_k$ and no vertex is adjacent to itself, $i \ne k$.
8. Suppose $i \le k - 2$. Consider the closed walk $C = (v_i, v_{i+1}, \dots, v_k, v_i)$ of length $m = k - i + 1 \ge 3$.
9. The vertices of $C$ after the first one are $v_{i+1}, \dots, v_k, v_i$. They are pairwise distinct, since $P$ is a path.
10. The edges $v_j v_{j+1}$ for $i \le j < k$ are distinct, because their vertex pairs differ. The last edge $v_k v_i$ differs from each of them, because $\set{v_k, v_i} = \set{v_j, v_{j+1}}$ would force $i = k - 1$.
11. So $C$ is a [[circuit|0PD57PSHNR]] whose vertices after the first are pairwise distinct. That is, $C$ is a [[cycle|07CT9RDY7Q]] of $T$, which contradicts acyclicity.
12. Hence $i = k - 1$, and $x = v_{k-1}$. So $v_k$ has exactly one neighbour.
13. By the definition of the [[degree|0T0F6CCS9W]], $\deg(v_k) = 1$. So $v_k$ is a vertex of degree $1$ of $T$.

## Idea

Walk along a longest path to its end. The last vertex cannot have a neighbour off the path, or the path would grow. It cannot have a second neighbour on the path either, or the tree would contain a cycle.
