---
tag: NTCD3724BB
kind: example
name: Sierpiński space
msc: [54G20, 54D10]
instance_of: [0CQHFPGJ45, 07SG12TQH3]
uses: [02BH3MCBQB, 0ZCK8DQYN1, 0NW6CH38YR, 0V032VWTHD, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Sierpiński_space
same_as:
  wikidata: Q2119470
  wikipedia: Sierpiński space
---

## Example

Let $S = \set{0, 1}$ with the family of [[open sets|02BH3MCBQB]] $\set{\emptyset, \set{1}, \set{0, 1}}$.
This family contains $\emptyset$ and $S$, and it is closed under unions and intersections, as one checks on its three members.
So $S$ is a [[topological space|0CQHFPGJ45]], the *Sierpiński space*.

- $S$ is a [[T0 space|07SG12TQH3]]: the open set $\set{1}$ contains $1$ but not $0$.
- $S$ is not a [[T1 space|0NW6CH38YR]]: the only open set that contains $0$ is $S$, and it also contains $1$.
- The [[closed sets|0ZCK8DQYN1]] are $\emptyset$, $\set{0}$ and $S$, so the closure of $\set{1}$ is $S$.
- $S$ is [[connected|0V032VWTHD]], since its only clopen sets are $\emptyset$ and $S$.

For any topological space $X$, a map $f \colon X \to S$ is [[continuous|0VGFHTM75Y]] if and only if $f^{-1}(\set{1})$ is open in $X$.
So continuous maps $X \to S$ correspond one to one to open subsets of $X$.

## Explanations

### L1 human

The Sierpiński space is the smallest topological space that is neither discrete nor trivial.
It has two points, and only one of them, the point $1$, forms an open set by itself.
One can read $1$ as "yes, observed" and $0$ as "not yet observed": an open set of any space is the same as a continuous yes-or-no test on it.
This small space is a basic counterexample, since it separates points in one direction only.
