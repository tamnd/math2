---
tag: 0SZ1KMNWVE
kind: statement
role: proposition
name: Order of the alternating group
msc: [20B30]
uses: [0T13HM377F, 0JEJJCB0EX, 0CXXJNG5B6, 0PCKBBMEXC]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_group
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Parity_of_a_permutation
    locator: Properties
---

## Statement

Let $n \geq 2$.
The [[alternating group|0Z5905Q73D]] $A_n$ has [[order|0B85S2V2DR]] $n!/2$, and $[S_n : A_n] = 2$.

## Remarks

The sign map is a surjective homomorphism onto a group of order $2$ with kernel $A_n$, so $S_n / A_n$ has order $2$.
Another proof: the map $\sigma \mapsto (1\ 2) \sigma$ is a bijection from the even permutations to the odd permutations.
For example, $|A_4| = 12$ and $|A_5| = 60$.

## Explanations

### L1 human

Half of all permutations are even.
To see this, multiply by one fixed swap: this changes each even permutation into an odd one, and back.
So $S_n$ splits into two halves of the same size.
