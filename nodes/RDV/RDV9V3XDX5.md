---
tag: RDV9V3XDX5
kind: proof
name: Proof of the sign of a cycle
msc: [20B30]
proves: 0V0E04DWX2
uses: [0SK90238BH, 0ZKPH2BD1T, 02DTRYKGE8, 0RJMNEN3BJ]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Proof

We write the cycle as a product of $k - 1$ transpositions. Products in $S_n$ are composites of maps, so the right factor acts first. The sign needs $n \geq 2$.

1. Let $\sigma = (a_1\ a_2\ \dots\ a_k)$ in [[cycle notation|0ZKPH2BD1T]], with $a_1, \dots, a_k$ distinct. So $\sigma(a_i) = a_{i+1}$ for $i < k$, $\sigma(a_k) = a_1$, and $\sigma$ fixes all other points.
2. Case $k = 1$. Then $\sigma$ is the identity $e$. Since $e = (1\ 2)(1\ 2)$ is a product of two [[transpositions|02DTRYKGE8]], the [[definition of the sign|0SK90238BH]] gives $\operatorname{sgn}(\sigma) = (-1)^2 = 1 = (-1)^{0}$.
3. Case $k \geq 2$. Let $\pi = (a_1\ a_k)(a_1\ a_{k-1}) \cdots (a_1\ a_2)$. This is a product of $k - 1$ transpositions. We show $\pi = \sigma$.
4. A point $x$ outside $\{a_1, \dots, a_k\}$ is fixed by each factor, so $\pi(x) = x = \sigma(x)$.
5. The point $a_1$ goes first to $a_2$ under $(a_1\ a_2)$. The later factors $(a_1\ a_j)$ with $j \geq 3$ fix $a_2$. So $\pi(a_1) = a_2 = \sigma(a_1)$.
6. Let $2 \leq i \leq k - 1$. The factors $(a_1\ a_j)$ with $j < i$ fix $a_i$. Then $(a_1\ a_i)$ sends $a_i$ to $a_1$, and $(a_1\ a_{i+1})$ sends $a_1$ to $a_{i+1}$.
7. The factors $(a_1\ a_j)$ with $j > i + 1$ fix $a_{i+1}$. So $\pi(a_i) = a_{i+1} = \sigma(a_i)$.
8. The point $a_k$ is fixed by all factors except the last one applied, $(a_1\ a_k)$, which sends it to $a_1$. So $\pi(a_k) = a_1 = \sigma(a_k)$.
9. By steps 4 to 8, $\pi$ and $\sigma$ agree at every point, so $\sigma = \pi$ is a product of $k - 1$ transpositions.
10. By the definition of the sign, $\operatorname{sgn}(\sigma) = (-1)^{k-1}$. With step 2, this holds for every $k \geq 1$.

## Idea

A $k$-cycle can be built by swapping the first entry successively with the second, third, and so on up to the last. That uses $k - 1$ swaps, so the sign is $(-1)^{k-1}$. In particular, cycles of odd length are even permutations.
