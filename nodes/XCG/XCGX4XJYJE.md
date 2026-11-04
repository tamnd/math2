---
tag: XCGX4XJYJE
kind: proof
name: Proof that binary trees are counted by Catalan numbers
msc: [05C05]
proves: 0Y97E2DMB7
uses: [02A8EMC83C, 092DRBFKMG, 0EE2V3CHFK, 0VPK4X73Q0, 0GV2573FP4, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Catalan_number
    locator: Applications in combinatorics
---

## Proof

We show that the counts satisfy the Catalan recursion, and conclude by [[strong induction|0KMVFSHFGZ]].

1. For a natural number $m$, let $T_m$ be the set of [[binary trees|02A8EMC83C]] with exactly $m$ nodes.
2. A tree of the form $\operatorname{node}(L, R)$ has at least one node, its root. So the only tree with $0$ nodes is the empty tree, and $T_0$ has $1$ element.
3. Fix a natural number $n$. By the definition, every tree in $T_{n+1}$ is $\operatorname{node}(L, R)$ for a unique pair $(L, R)$ of binary trees.
4. Its number of nodes is $1 + |L| + |R|$, where $|L|$ and $|R|$ are the numbers of nodes. So $|L| = i$ and $|R| = n - i$ for some $0 \le i \le n$.
5. Conversely, for $0 \le i \le n$, $L \in T_i$ and $R \in T_{n-i}$, the tree $\operatorname{node}(L, R)$ has $n + 1$ nodes.
6. By steps 3 to 5, the map $\operatorname{node}(L, R) \mapsto (L, R)$ is a bijection from $T_{n+1}$ onto the disjoint union over $0 \le i \le n$ of the sets $T_i \times T_{n-i}$.
7. We prove by strong induction on $m$ that $T_m$ is finite with $|T_m| = C_m$, where $C_m$ are the [[Catalan numbers|092DRBFKMG]], defined by $C_0 = 1$ and $C_{n+1} = \sum_{i=0}^{n} C_i\, C_{n-i}$.
8. For $m = 0$, step 2 gives $|T_0| = 1 = C_0$.
9. For $m = n + 1$, assume the claim for all $i \le n$. By step 6, the [[bijection principle|0GV2573FP4]], the [[rule of product|0VPK4X73Q0]] and the [[rule of sum|0EE2V3CHFK]], $T_{n+1}$ is finite and $|T_{n+1}| = \sum_{i=0}^{n} C_i\, C_{n-i} = C_{n+1}$.
10. Hence the number of binary trees with exactly $n$ nodes is $C_n$ for every natural number $n$.

## Idea

A nonempty binary tree is a root with a left and a right subtree, whose node counts add up to one less. So the counts obey the same recursion and start value as the Catalan numbers.
