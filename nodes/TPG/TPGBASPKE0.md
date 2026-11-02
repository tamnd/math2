---
tag: TPGBASPKE0
kind: example
name: Whitehead link
msc: [57K10, 57K32]
instance_of: [1A5WRCNTM3]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead_link
same_as:
  wikidata: Q2588098
  wikipedia: Whitehead link
---

## Example

Start with a round circle $C_1$ in $\R^3$, and let $D$ be the flat disk that it bounds.
Take a second closed curve $C_2$, disjoint from $C_1$, that goes down through $D$ and then comes back up through $D$, with one twist.
In the standard diagram, $C_2$ has the shape of a figure eight with one self-crossing, and it clasps $C_1$.
The union $C_1 \cup C_2$ is a [[link|1A5WRCNTM3]] with $2$ components, the *Whitehead link*.
Its standard diagram has $5$ crossings: one crossing of $C_2$ with itself, and four crossings between $C_1$ and $C_2$.
The four crossings between the components come in two pairs of opposite signs, so the [[linking number|SFJ329YB9F]] of $C_1$ and $C_2$ is $0$.
Each component on its own is an [[unknot|1TQ06R4Q66]].

## Remarks

Although its linking number is $0$, the Whitehead link is not the unlink of two components: the two curves cannot be separated.
One way to see this uses its complement in $S^3$, which carries a complete hyperbolic metric of finite volume.
The complement of a split link contains a sphere that separates the components.
A hyperbolic complement contains no such sphere.
The complement is built from one regular ideal octahedron, and its volume is about $3.6639$.
Its crossing number is $5$.
It was studied by J. H. C. Whitehead in his work on contractible open $3$-manifolds.
Together with the Hopf link, it shows that the linking number detects some but not all linking.

## Explanations

### L1 human

The Whitehead link has two loops of string, each unknotted on its own.
One loop passes through the other and then hooks back on itself, so that it goes through once in each direction.
Counting with signs, the loops wind around each other zero times, yet they still cannot be pulled apart.
