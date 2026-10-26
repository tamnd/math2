---
tag: 0ARPRJQWZ2
kind: statement
role: theorem
name: Simplicity of the alternating group
msc: [20B30, 20D06]
uses: [0T13HM377F, 0KFZ0QX83G, 0W77CVBCHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_group
    locator: Basic properties
  - url: https://en.wikipedia.org/wiki/Alternating_group
    locator: Generators and relations
---

## Statement

Let $n \geq 5$.
Then the [[alternating group|0Z5905Q73D]] $A_n$ is simple: its only [[normal subgroups|0CB0DX5BVV]] are $\{e\}$ and $A_n$.

## Remarks

A usual proof shows that a nontrivial normal subgroup of $A_n$ contains a $3$-cycle, then all $3$-cycles, and then uses that the [[3-cycles generate|0KFZ0QX83G]] $A_n$.
The group $A_4$ is not simple, because the Klein four-group $\{e, (1\ 2)(3\ 4), (1\ 3)(2\ 4), (1\ 4)(2\ 3)\}$ is normal in $A_4$.
The group $A_3$ is simple because it has prime order $3$.
For $n \geq 5$, the only normal subgroups of $S_n$ are $\{e\}$, $A_n$ and $S_n$.

## Explanations

### L1 human

A simple group cannot be broken into a normal subgroup and a quotient.
From five symbols on, the even permutations form such an unbreakable group.
This fact is a key step in the proof that there is no general formula in radicals for polynomials of degree $5$ or more.
