---
tag: ~5bdf0fb0
kind: proof
name: Proof that a product of upper triangular matrices is upper triangular
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: ~16a77e22
methods: [0WCP0PVET6, 0NTF6DMVAP]
uses: [0MKABWDRNC, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Proof

Let $A$ and $B$ be upper triangular, so $a_{ik} = 0$ for $i > k$ and $b_{kj} = 0$ for $k > j$.

1. By the [[product rule|076JGP6R3T]], $(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$.
2. A term $a_{ik} b_{kj}$ can be nonzero only if $a_{ik} \neq 0$ and $b_{kj} \neq 0$. By the [[definition|0MKABWDRNC]], this needs $i \le k$ and $k \le j$.
3. Case $i > j$: no $k$ satisfies $i \le k \le j$. So every term is $0$, and $(AB)_{ij} = 0$. Thus $AB$ is upper triangular.
4. Case $i = j$: the only $k$ with $i \le k \le i$ is $k = i$. So $(AB)_{ii} = a_{ii} b_{ii}$.
5. Strict case: now $a_{ik} \neq 0$ needs $i < k$, and $b_{kj} \neq 0$ needs $k < j$. For $i \ge j$, no $k$ satisfies $i < k < j$, so $(AB)_{ij} = 0$.
6. By steps 3 to 5, all claims hold.

## Idea

A nonzero term of $(AB)_{ij}$ needs a path $i \le k \le j$ of indices.
Below the diagonal there is no such path, and on the diagonal there is exactly one.

## Variants

- By maps: $A$ is upper triangular exactly when $A V_j \subseteq V_j$ for $V_j = \langle e_1, \dots, e_j \rangle$. Then $AB V_j \subseteq A V_j \subseteq V_j$, so $AB$ is upper triangular.
- In the map view, $A e_j \equiv a_{jj} e_j$ modulo $V_{j-1}$, so $AB e_j \equiv a_{jj} b_{jj} e_j$ modulo $V_{j-1}$, which gives the diagonal.
