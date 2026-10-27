---
tag: TJ6EBSS3S7
kind: example
name: The alternating group is the kernel of the sign
msc: [20B30]
instance_of: [0W88CEGQP1]
illustrates: [0C9ZKYSPYR]
uses: [0SK90238BH, 0Z5905Q73D, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Example

Let $n \ge 2$. The [[sign|0SK90238BH]] is a homomorphism $\operatorname{sgn} : S_n \to \{1, -1\}$, where $\{1, -1\}$ is a group under multiplication.
A permutation has sign $1$ when it is a product of an even number of transpositions.
Thus the kernel of $\operatorname{sgn}$ is the set of even permutations. This is the [[alternating group|0Z5905Q73D]] $A_n$.
Thus $A_n$ is a [[normal subgroup|0C9ZKYSPYR]] of $S_n$.

## Remarks

The sign is onto, so $A_n$ has index $2$ in $S_n$.
