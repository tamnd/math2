---
tag: ~d9bbcc4a
kind: statement
role: theorem
name: Sign is a homomorphism
msc: [20B30]
uses: [~291ecab2, ~f060c64f]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Statement

Let $n \geq 2$.
The map $\operatorname{sgn} \colon S_n \to \{1, -1\}$ is a surjective [[group homomorphism|~c666c876]], where $\{1, -1\}$ is a group under multiplication.
That is, $\operatorname{sgn}(\sigma \tau) = \operatorname{sgn}(\sigma) \operatorname{sgn}(\tau)$ for all $\sigma, \tau \in S_n$.

## Remarks

If $\sigma$ is a product of $m$ transpositions and $\tau$ is a product of $l$ transpositions, then $\sigma \tau$ is a product of $m + l$ transpositions.
The map is surjective because $\operatorname{sgn}((1\ 2)) = -1$.
Its [[kernel|~695eca04]] is the [[alternating group|~de0bd4cd]] $A_n$.

## Explanations

### L1 human

When you do two permutations one after the other, you join their chains of swaps.
The number of swaps adds, so the signs multiply.
This is exactly the rule of a homomorphism.
