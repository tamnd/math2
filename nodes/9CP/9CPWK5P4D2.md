---
tag: 9CPWK5P4D2
kind: problem
name: Stable roommates problem
msc: [91B68, 05C70]
uses: [X201T4TP0Y, 0MJ04A50QW]
about: [0MJ04A50QW]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_roommates_problem
same_as:
  wikidata: Q3406260
  wikipedia: Stable roommates problem
history:
  posed_by: "David Gale and Lloyd Shapley"
  first_stated: "1962"
---

## Problem

Let $P$ be a set of $2n$ people.
Each person $p$ has a strict ranking of the other $2n - 1$ people.
A *matching* is a partition of $P$ into $n$ pairs, a perfect [[matching|0MJ04A50QW]] of the complete graph on $P$.
Two people $p$ and $q$ who are not paired together *block* the matching if each prefers the other to the partner given by the matching.
A matching is *stable* if no two people block it.
The problem is to decide whether a given instance has a stable matching, and to find one if it does.

## Remarks

Unlike the [[stable marriage problem|X201T4TP0Y]], a stable matching need not exist.
Example: let $A$ rank $B > C > D$, let $B$ rank $C > A > D$, let $C$ rank $A > B > D$, and let $D$ rank the others in any order.
Whoever is paired with $D$ forms a blocking pair with the one among the other two who ranks them first.
So $\set{A, D}, \set{B, C}$ is blocked by $(A, C)$, $\set{B, D}, \set{A, C}$ by $(A, B)$, and $\set{C, D}, \set{A, B}$ by $(B, C)$.
Gale and Shapley gave this kind of example in their 1962 paper, where they also posed the stable marriage problem.
Robert Irving found an algorithm in 1985 that decides existence and finds a stable matching when there is one, in time $O(n^2)$.

## Explanations

### L1 human

People who must share two-person rooms each rank everyone else.
A pairing is unstable if two people in different rooms would both rather room together.
With men and women a stable pairing always exists, but here it can fail to exist.
Three people who each prefer the next one in a circle, plus one person nobody wants, leave no stable pairing.
