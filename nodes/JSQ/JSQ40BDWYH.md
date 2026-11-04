---
tag: JSQ40BDWYH
kind: proof
name: Proof that the sign is a homomorphism
msc: [20B30]
proves: 0JEJJCB0EX
uses: [0SK90238BH, 0XK6FECMW5, 02DTRYKGE8, 0RJMNEN3BJ, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Proof

We concatenate decompositions into transpositions. Products in the [[symmetric group|0RJMNEN3BJ]] $S_n$ are composites of maps, and $n \geq 2$.

1. Let $\sigma, \tau \in S_n$. By the [[decomposition into transpositions|0XK6FECMW5]], write $\sigma = \tau_1 \cdots \tau_m$ and $\tau = \tau'_1 \cdots \tau'_l$, where each $\tau_i$ and each $\tau'_j$ is a [[transposition|02DTRYKGE8]].
2. By the [[definition of the sign|0SK90238BH]], $\operatorname{sgn}(\sigma) = (-1)^m$ and $\operatorname{sgn}(\tau) = (-1)^l$. This does not depend on the chosen decompositions, because the sign is well defined.
3. By associativity, $\sigma \tau = \tau_1 \cdots \tau_m \tau'_1 \cdots \tau'_l$. This is a product of $m + l$ transpositions.
4. By the definition of the sign again, $\operatorname{sgn}(\sigma \tau) = (-1)^{m+l} = (-1)^m (-1)^l = \operatorname{sgn}(\sigma) \operatorname{sgn}(\tau)$.
5. The set $\{1, -1\}$ is a group under multiplication, and step 4 says that $\operatorname{sgn}$ preserves products. So $\operatorname{sgn}$ is a [[group homomorphism|0HV9Y7WG5R]].
6. For surjectivity, the transposition $(1\ 2)$ is a product of one transposition, so $\operatorname{sgn}((1\ 2)) = -1$. This uses $n \geq 2$.
7. The identity $e$ equals $(1\ 2)(1\ 2)$, a product of two transpositions. So $\operatorname{sgn}(e) = (-1)^2 = 1$.
8. By steps 6 and 7, both $1$ and $-1$ are values of $\operatorname{sgn}$. So $\operatorname{sgn} \colon S_n \to \{1, -1\}$ is a surjective group homomorphism.

## Idea

If $\sigma$ uses $m$ transpositions and $\tau$ uses $l$, then writing the two products side by side expresses $\sigma \tau$ with $m + l$ transpositions. Since the parity of the count is well defined, the signs multiply. All the depth is in the well-definedness of the sign, not in this step.
