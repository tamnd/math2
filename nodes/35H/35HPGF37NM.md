---
tag: 35HPGF37NM
kind: proof
name: Proof of the decomposition of a permutation into transpositions
msc: [20B30]
proves: 0XK6FECMW5
uses: [0RJMNEN3BJ, 02DTRYKGE8, 0ZKPH2BD1T, 0YWDAZPRPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Properties
---

## Proof

We write each cycle as a product of transpositions by induction on its length, and then use the disjoint cycle decomposition.

1. Let $n \ge 2$, and let $S_n$ be the [[symmetric group|0RJMNEN3BJ]], with products taken as compositions: $(\alpha\beta)(x) = \alpha(\beta(x))$.
2. Let $k \ge 3$ and let $c = (a_1\ a_2\ \dots\ a_k)$ be a [[cycle|0ZKPH2BD1T]]. We claim $c = (a_1\ a_k)\, c'$, where $c' = (a_1\ a_2\ \dots\ a_{k-1})$ and $(a_1\ a_k)$ is a [[transposition|02DTRYKGE8]].
3. For $1 \le i \le k-2$, $c'(a_i) = a_{i+1}$, which differs from $a_1$ and $a_k$. So $(a_1\ a_k) c'(a_i) = a_{i+1} = c(a_i)$.
4. Next, $c'(a_{k-1}) = a_1$, and $(a_1\ a_k)$ sends $a_1$ to $a_k$. So $(a_1\ a_k) c'(a_{k-1}) = a_k = c(a_{k-1})$.
5. Next, $c'$ fixes $a_k$, and $(a_1\ a_k)$ sends $a_k$ to $a_1$. So $(a_1\ a_k) c'(a_k) = a_1 = c(a_k)$.
6. Every other point is fixed by $c'$, by $(a_1\ a_k)$ and by $c$. With steps 3 to 5, this proves the claim of step 2.
7. A cycle $(a_1\ a_2)$ of length $2$ is itself a transposition. By step 2 and induction on $k \ge 2$, each cycle of length $k$ is a product of $k - 1$ transpositions.
8. Let $\sigma \in S_n$. By the [[decomposition into disjoint cycles|0YWDAZPRPQ]], $\sigma = c_1 \cdots c_r$ with cycles $c_i$ of length at least $2$.
9. If $r \ge 1$, replace each $c_i$ by a product of transpositions, using step 7. This writes $\sigma$ as a product of transpositions.
10. If $r = 0$, then $\sigma$ is the identity. Since $n \ge 2$, the transposition $(1\ 2)$ exists, and $(1\ 2)(1\ 2)$ is the identity.
11. By steps 9 and 10, each permutation in $S_n$ is a product of transpositions.

## Idea

A cycle can be peeled off one point at a time: $(a_1\ \dots\ a_k) = (a_1\ a_k)(a_1\ \dots\ a_{k-1})$. Repeating this writes a cycle of length $k$ as $k - 1$ transpositions. Every permutation is a product of cycles, and the identity is a transposition applied twice.
