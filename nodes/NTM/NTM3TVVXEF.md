---
tag: NTM3TVVXEF
kind: proof
name: Proof of unique paths in trees
msc: [05C05]
proves: 096B7Q5742
uses: [0MJ0JS72DZ, 0FFAYNMAJZ, 0XNN9Z8E5A, 0J8XE7W68F, 0VJZM0F9YM, 0JDE56HWQ8, 0PD57PSHNR, 07CT9RDY7Q, 09VZBHB33V]
sources:
  - url: https://github.com/oscarlevin/discrete-book/blob/a8e4949bc45daf100930c1182983778f56ab689f/ptx/sec_gt-trees.ptx#L154
---

## Proof

We prove both directions. Step 1 is a fact about closed walks that both directions use.

1. Let $(z_0, z_1, \dots, z_m)$ be a closed walk with $m \ge 3$, $z_m = z_0$, and $z_1, \dots, z_m$ pairwise distinct. Then its $m$ edges are pairwise distinct, so it is a [[circuit|0PD57PSHNR]], and hence a [[cycle|07CT9RDY7Q]].
2. Proof of step 1. Read the indices modulo $m$. The edges are $\set{z_{t-1}, z_t}$ for $t = 1, \dots, m$. Two of them can be equal only if the pairs share both vertices.
3. Since $z_1, \dots, z_m$ are distinct, the equality $\set{z_{s-1}, z_s} = \set{z_{t-1}, z_t}$ with $s \ne t$ forces $z_{s-1} = z_t$ and $z_s = z_{t-1}$. Then $t \equiv s - 1$ and $s \equiv t - 1$, so $2 \equiv 0$ modulo $m$, which is false for $m \ge 3$.
4. ($\Rightarrow$) Let $G$ be a [[tree|0MJ0JS72DZ]]. It is [[connected|0FFAYNMAJZ]], so it has a vertex and any two vertices $u, v$ are joined by a [[walk|0VJZM0F9YM]].
5. By [[every walk contains a path|09VZBHB33V]], there is a [[path|0JDE56HWQ8]] from $u$ to $v$.
6. Suppose $P = (p_0, \dots, p_a)$ and $Q = (q_0, \dots, q_b)$ are different paths from $u$ to $v$.
7. Neither is a proper initial part of the other. For example, if $a < b$ and $p_t = q_t$ for $t \le a$, then $q_a = p_a = v = q_b$, which contradicts the distinct vertices of $Q$.
8. So there is a least index $i$ with $1 \le i \le \min(a, b)$ and $p_i \ne q_i$. Then $p_{i-1} = q_{i-1}$; call this vertex $x$.
9. Let $j \ge i$ be the least index such that $p_j = q_l$ for some $l \ge i$. It exists, because $p_a = v = q_b$ and $b \ge i$.
10. Consider the closed walk $C = (x, p_i, p_{i+1}, \dots, p_j, q_{l-1}, q_{l-2}, \dots, q_i, x)$, where $p_j = q_l$ and $q_{i-1} = x$. Its length is $(j - i + 1) + (l - i + 1)$.
11. The vertices $p_i, \dots, p_j$ are distinct and differ from $x = p_{i-1}$, since $P$ is a path. The vertices $q_{l-1}, \dots, q_i$ are distinct and differ from $x = q_{i-1}$, since $Q$ is a path.
12. No $q_t$ with $i \le t < l$ equals some $p_s$ with $i \le s \le j$. For $s < j$ this follows from the minimality of $j$, and for $s = j$ from $p_j = q_l$ and $t \ne l$.
13. So the vertices of $C$ after the first are pairwise distinct. If the length were $2$, then $j = l = i$ and $p_i = q_i$, which is false. So the length is at least $3$.
14. By step 1, $C$ is a cycle in $G$. This contradicts that $G$ is [[acyclic|0XNN9Z8E5A]]. Hence the path from $u$ to $v$ is unique.
15. ($\Leftarrow$) Suppose $G$ has a vertex, and any two vertices are joined by exactly one path.
16. A path is a walk, so any two vertices are [[reachable|0J8XE7W68F]] from each other. So $G$ is connected.
17. Suppose $G$ has a cycle $(w_0, w_1, \dots, w_k)$. Its length $k$ is at least $3$: $k = 1$ needs a loop, and $k = 2$ uses the edge $w_0 w_1$ twice.
18. Then $(w_0, w_1)$ and $(w_k, w_{k-1}, \dots, w_1)$ are paths from $w_0 = w_k$ to $w_1$. The second has distinct vertices because $w_1, \dots, w_k$ are distinct.
19. These two paths have lengths $1$ and $k - 1 \ge 2$, so they are different. This contradicts uniqueness, so $G$ is acyclic.
20. By steps 16 and 19, $G$ is a tree.

## Idea

Two different routes between the same two vertices must split apart at some vertex and later meet again. The two pieces between the split and the first meeting point form a cycle. Conversely, a cycle gives two different routes between neighbouring vertices on it.
