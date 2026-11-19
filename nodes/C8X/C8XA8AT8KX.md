---
tag: C8XA8AT8KX
kind: proof
name: Proof of Gödel's theorem on finite matrices by pigeonhole
msc: ["03B20", "03B50"]
topics: [38EQ20GR7M]
audience: grad
proves: CFCPJA1QF5
uses: [52XCYMK0WW, 5GTQ69W47T, 480TCT5CJ9]
methods: [12MQ2NJ29A, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Many-valued logic
---

## Proof

Part A: item 1.

1. Let $(M, D)$ be a matrix with at most $n$ elements in which every theorem of $\mathsf{IPC}$ is a tautology. Let $v$ be a map from the variables to $M$.
2. The $n + 1$ variables $p_0, \ldots, p_n$ take at most $n$ values. So $v(p_i) = v(p_j)$ for some $i < j$.
3. Let $D_n'$ be the result of replacing $p_j$ by $p_i$ everywhere in $D_n$.
4. The value of a formula depends only on the values of its variables, through the operations of $M$. Since $v(p_j) = v(p_i)$, $D_n$ and $D_n'$ get the same value under $v$, by induction on subformulas.
5. $D_n'$ is a disjunction with the disjunct $p_i \leftrightarrow p_i$.
6. $\mathsf{IPC} \vdash p_i \leftrightarrow p_i$, and axiom 5 of [[the Hilbert system|52XCYMK0WW]] gives $\mathsf{IPC} \vdash D_n'$.
7. By assumption, $v(D_n')$ is designated. By step 4, $v(D_n)$ is designated.
8. As $v$ was arbitrary, $D_n$ is a tautology of $M$.

Part B: item 2.

9. Take the chain $c_1 < c_2 < \cdots < c_n$ as a [[Kripke frame|5GTQ69W47T]]. Its up-sets are $U_k = \set{c_k, \ldots, c_n}$ for $1 \leq k \leq n + 1$, with $U_{n+1} = \emptyset$.
10. Put $V(p_i) = U_{i+1}$ for $0 \leq i \leq n$. These are $n + 1$ different up-sets.
11. Let $i < j$. The world $c_{i+1}$ is in $V(p_i)$ but not in $V(p_j)$.
12. So $c_{i+1} \nVdash p_i \to p_j$, and the root $c_1$ does not force $p_i \leftrightarrow p_j$.
13. No disjunct of $D_n$ is forced at $c_1$, so $c_1 \nVdash D_n$.
14. By [[soundness|480TCT5CJ9]], $\mathsf{IPC} \nvdash D_n$.

Part C: item 3.

15. Suppose a finite matrix with $n$ elements is characteristic for $\mathsf{IPC}$.
16. It has every theorem of $\mathsf{IPC}$ as a tautology. By item 1, $D_n$ is a tautology of it.
17. Since the matrix is characteristic, $\mathsf{IPC} \vdash D_n$. This contradicts item 2.

## Idea

With $n$ truth values and $n + 1$ variables, two variables always share a value.
Then one disjunct of $D_n$ has the value of $p \leftrightarrow p$, a theorem.
But a chain of $n$ worlds has $n + 1$ different up-sets, so in Kripke semantics all variables can differ.

## Variants

1. Part B can be phrased algebraically: in the $(n+1)$-element chain, with distinct values $a_0, \ldots, a_n$, each $a_i \leftrightarrow a_j$ is $\min(a_i, a_j) < 1$, and so is their join.
2. Part A uses no property of the operations of the matrix. It uses only that the matrix validates the theorem $D_n'$.
