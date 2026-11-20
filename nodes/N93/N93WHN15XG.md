---
tag: N93WHN15XG
kind: proof
name: Proof of the criterion for a direct sum of several subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: FVKY28HHBC
methods: [TFQ1845T84, 0J0XBKG64S]
uses: [041JTZCK9Q, 0EPTJA5QV4, 0RMKABS2S5]
sources:
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780134860244
    locator: Section 5.2
---

## Proof

We prove $1 \Rightarrow 2 \Rightarrow 4 \Rightarrow 3 \Rightarrow 2 \Rightarrow 1$.
Write $S_i$ for the sum of all $U_j$ with $j \ne i$, and $T_i = U_1 + \cdots + U_{i-1}$, with $T_1 = \{0\}$.

1. $1 \Rightarrow 2$. Since each $U_i$ is a [[subspace|0EPTJA5QV4]], $0 = 0 + \cdots + 0$ is one expression of $0$. If also $0 = u_1 + \cdots + u_k$ with $u_i \in U_i$, then uniqueness gives $u_i = 0$ for each $i$.
2. $2 \Rightarrow 4$. Let $x \in U_i \cap S_i$. Then $x = \sum_{j \ne i} u_j$ with $u_j \in U_j$.
3. So $(-x) + \sum_{j \ne i} u_j = 0$, with $-x \in U_i$ in the place $i$. By condition 2, $-x = 0$. Hence $U_i \cap S_i = \{0\}$.
4. $4 \Rightarrow 3$. For $i \ge 2$, each vector of $T_i$ is a sum of vectors of $U_1, \dots, U_{i-1}$. Adding zeros in the other places shows $T_i \subseteq S_i$. So $U_i \cap T_i \subseteq U_i \cap S_i = \{0\}$.
5. $3 \Rightarrow 2$. Assume condition 3, and suppose $0 = u_1 + \cdots + u_k$ with $u_i \in U_i$ and some $u_i \ne 0$.
6. Let $i$ be the largest index with $u_i \ne 0$. If $i = 1$, then $0 = u_1 \ne 0$, which is impossible. So $i \ge 2$.
7. Then $u_i = -(u_1 + \cdots + u_{i-1})$. The left side is in $U_i$ and the right side is in $T_i$, so $u_i \in U_i \cap T_i = \{0\}$.
8. This contradicts $u_i \ne 0$. So all $u_i = 0$, which is condition 2.
9. $2 \Rightarrow 1$. Suppose a vector of the [[sum|0RMKABS2S5]] has two expressions $u_1 + \cdots + u_k = u_1' + \cdots + u_k'$ with $u_i, u_i' \in U_i$.
10. Subtracting gives $0 = (u_1 - u_1') + \cdots + (u_k - u_k')$ with $u_i - u_i' \in U_i$. By condition 2, $u_i = u_i'$ for each $i$. So the sum is [[direct|041JTZCK9Q]].

## Idea

As for two subspaces, uniqueness of all expressions is the same as uniqueness of the expression of $0$.
A nontrivial expression of $0$ has a last nonzero term, and that term lies both in its own subspace and in the sum of the earlier ones.

## Variants

- In finite dimension, the sum is direct if and only if $\dim(U_1 + \cdots + U_k) = \sum_i \dim U_i$. This follows from condition 3 and induction on $k$ with the [[dimension criterion|P4JG9DJ2HH]].
- Condition 3 depends on the order of the subspaces only through its form. The proof shows that it holds for one order if and only if it holds for every order.
