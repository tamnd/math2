---
tag: YDY12RN2YJ
kind: proof
name: Proof that a product of upper triangular matrices is upper triangular
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: 45RET2Y995
methods: [0WCP0PVET6, 0NTF6DMVAP]
uses: [0MKABWDRNC, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Proof

We write each entry of $AB$ as a sum and find which terms can be nonzero.
Let $A$ and $B$ be upper triangular $n \times n$ matrices over a ring $R$, so $a_{ik} = 0$ for $i > k$ and $b_{kj} = 0$ for $k > j$.

1. By the [[product rule|076JGP6R3T]], for all $i$ and $j$,
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}.$$
2. A term $a_{ik} b_{kj}$ can be nonzero only if $a_{ik} \neq 0$ and $b_{kj} \neq 0$, and by the [[definition|0MKABWDRNC]] of upper triangular this needs $i \le k$ and $k \le j$.
3. Case $i > j$: no index $k$ satisfies $i \le k \le j$, so every term in step 1 is $0$, $(AB)_{ij} = 0$, and $AB$ is upper triangular.
4. Case $i = j$: the only index with $i \le k \le i$ is $k = i$, and all other terms are $0$ by step 2, so $(AB)_{ii} = a_{ii} b_{ii}$.
5. Strict case: now $a_{ik} \neq 0$ needs $i < k$, and $b_{kj} \neq 0$ needs $k < j$; for $i \ge j$ no index satisfies $i < k < j$, so $(AB)_{ij} = 0$, and $AB$ is strictly upper triangular.
6. Steps 3, 4 and 5 are the three claims of the statement.

## Idea

A nonzero term of $(AB)_{ij}$ needs a chain of indices $i \le k \le j$, one step in $A$ and one step in $B$, each going weakly up and to the right.
Below the diagonal there is no such chain, and on the diagonal there is exactly one, which stays at $i$.
The proof never swaps two factors, so it works over any ring.

## Variants

There is a proof without sums.
Let $V_j$ be the span of $e_1, \dots, e_j$ in $R^n$.
A matrix $A$ is upper triangular exactly when its column $Ae_j$ lies in $V_j$ for each $j$, that is, when $A V_j \subseteq V_j$.
Then $AB V_j \subseteq A V_j \subseteq V_j$, so $AB$ is upper triangular.
For the diagonal, $Ae_j$ equals $a_{jj} e_j$ plus a vector of $V_{j-1}$, and so $ABe_j$ equals $a_{jj} b_{jj} e_j$ plus a vector of $V_{j-1}$.
