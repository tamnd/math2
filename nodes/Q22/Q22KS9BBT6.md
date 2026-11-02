---
tag: Q22KS9BBT6
kind: definition
name: Direct limit of algebras
msc: [08B25, 18A30]
defines: 7SXKJG1Q9B
uses: [QJGPT2W0FT, KBXSZC6BV1, D9RY4667K6, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_limit
---

## Definition

Let $(I, \le)$ be a nonempty [[directed set|D9RY4667K6]].
A *directed system* of algebras over $I$ consists of [[algebras|QJGPT2W0FT]] $\mathbf{A}_i$ of one signature, for $i \in I$, and [[homomorphisms|KBXSZC6BV1]] $f_{ij} \colon \mathbf{A}_i \to \mathbf{A}_j$ for $i \le j$, such that:

1. $f_{ii}$ is the identity of $\mathbf{A}_i$ for each $i$;
2. $f_{jk} \circ f_{ij} = f_{ik}$ whenever $i \le j \le k$.

On the disjoint union of the universes, let $a \sim b$ for $a \in A_i$ and $b \in A_j$ when $f_{ik}(a) = f_{jk}(b)$ for some $k \ge i, j$.
The *direct limit* $\varinjlim \mathbf{A}_i$ has as universe the set of classes $[a]$ of this [[equivalence relation|0G8VEZ3WTK]].
For an $n$-ary operation $f$ and $a_m \in A_{i_m}$, choose $k \ge i_1, \dots, i_n$ and put $f([a_1], \dots, [a_n]) = [f^{\mathbf{A}_k}(f_{i_1 k}(a_1), \dots, f_{i_n k}(a_n))]$.

## Remarks

The relation $\sim$ is transitive and the operations do not depend on the choices of $k$ and representatives, because $I$ is directed and the $f_{ij}$ are homomorphisms.
For a nullary operation $c$, take any $k \in I$ and put $c = [c^{\mathbf{A}_k}]$.
The maps $a \mapsto [a]$ are homomorphisms $\mathbf{A}_i \to \varinjlim \mathbf{A}_i$, and they make the direct limit a colimit of the system.

Example: let $\mathbf{A}_n = \Z/p^n\Z$ for $n \ge 1$, with $f_{nm}(x) = p^{m-n} x$ for $n \le m$.
These maps are injective homomorphisms satisfying clauses 1 and 2, and the direct limit is the Prüfer $p$-group.

Non-example: over $I = \N$, take $\mathbf{A}_n = \Z$ for all $n$ with $f_{nm}(x) = 2x$ for all $n < m$ and $f_{nn} = \id$.
Clause 2 fails, since $f_{12} \circ f_{01}(x) = 4x$ while $f_{02}(x) = 2x$.
Setting instead $f_{nm}(x) = 2^{m-n} x$ gives a directed system with direct limit $\Z[1/2]$.
