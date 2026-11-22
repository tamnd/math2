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

We prove the implications $1 \Rightarrow 2$, $2 \Rightarrow 4$, $4 \Rightarrow 3$, $3 \Rightarrow 2$ and $2 \Rightarrow 1$, which together make all four conditions equivalent.
Write $S_i$ for the sum of all $U_j$ with $j \ne i$, and $T_i = U_1 + \cdots + U_{i-1}$ for $i \ge 2$.

1. ($1 \Rightarrow 2$.) Since each $U_i$ is a [[subspace|0EPTJA5QV4]], $0 = 0 + \cdots + 0$ is one expression of $0$.
   If also $0 = u_1 + \cdots + u_k$ with $u_i \in U_i$, then uniqueness gives $u_i = 0$ for each $i$.
2. ($2 \Rightarrow 4$.) Let $x \in U_i \cap S_i$.
   Then $x = \sum_{j \ne i} u_j$ for some $u_j \in U_j$.
3. Moving $x$ to the other side gives an expression of zero,
$$(-x) + \sum_{j \ne i} u_j = 0,$$
   with $-x \in U_i$ in the place $i$.
   By condition 2, $-x = 0$, so $U_i \cap S_i = \{0\}$.
4. ($4 \Rightarrow 3$.) For $i \ge 2$, each vector of $T_i$ is a sum of vectors of $U_1, \dots, U_{i-1}$, and adding zeros in the other places shows $T_i \subseteq S_i$.
   So $U_i \cap T_i \subseteq U_i \cap S_i = \{0\}$.
5. ($3 \Rightarrow 2$.) Assume condition 3, and suppose that $0 = u_1 + \cdots + u_k$ with $u_i \in U_i$ and some $u_i \ne 0$.
   Let $i$ be the largest index with $u_i \ne 0$.
6. If $i = 1$, the equation reads $0 = u_1$, which contradicts $u_1 \ne 0$.
   So $i \ge 2$, and the terms after place $i$ are zero, so
$$u_i = -(u_1 + \cdots + u_{i-1}).$$
7. The left side lies in $U_i$, and the right side lies in $T_i$ because $T_i$ is a subspace.
   So $u_i \in U_i \cap T_i = \{0\}$, which contradicts $u_i \ne 0$.
   Hence all $u_i = 0$, which is condition 2.
8. ($2 \Rightarrow 1$.) Suppose a vector of the [[sum|0RMKABS2S5]] has two expressions $u_1 + \cdots + u_k = u_1' + \cdots + u_k'$ with $u_i, u_i' \in U_i$.
   Subtracting gives $0 = (u_1 - u_1') + \cdots + (u_k - u_k')$ with $u_i - u_i' \in U_i$.
9. By condition 2, $u_i - u_i' = 0$ for each $i$.
   So the two expressions agree, and the sum is [[direct|041JTZCK9Q]].

## Idea

As for two subspaces, uniqueness of all expressions is the same as uniqueness of the expression of $0$.
The new point is how to find the failure when there is a nontrivial expression of $0$.
Look at its last nonzero term: that term lies in its own subspace and also in the sum of the earlier subspaces, so condition 3 rules it out.

## Variants

In finite dimension there is a proof by counting.
The sum is direct if and only if $\dim(U_1 + \cdots + U_k) = \sum_i \dim U_i$, and this follows from condition 3 by induction on $k$, using the [[dimension criterion|P4JG9DJ2HH]] at each step for $T_i$ and $U_i$.
The proof also shows that condition 3 holds for one order of the subspaces exactly when it holds for every order, since it is equivalent to condition 2, which does not depend on the order.
