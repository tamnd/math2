---
tag: 93STGYCSTS
kind: problem
name: Bargaining problem
msc: [91B26, 91A12]
uses: [02AS45T3H9, 0R6EWFKRCF]
about: [39HGM44CFZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cooperative_bargaining
same_as:
  wikidata: Q1516247
  wikipedia: Cooperative bargaining
history:
  posed_by: "John Nash"
  first_stated: "1950"
---

## Problem

A *two-person bargaining problem* is a pair $(F, d)$ where:

1. $F \subseteq \R^2$ is a [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]], the set of feasible utility pairs;
2. $d = (d_1, d_2) \in F$ is the disagreement point, the utilities the two players get if they fail to agree;
3. there is a point $x \in F$ with $x_1 > d_1$ and $x_2 > d_2$.

A *bargaining solution* is a rule $f$ that assigns to every bargaining problem $(F, d)$ a point $f(F, d) \in F$.
The problem is to find a bargaining solution that describes a reasonable agreement between the two players.

## Remarks

John Nash formulated the problem in this form in his 1950 paper "The Bargaining Problem".
He answered it by listing axioms that a solution should satisfy and showing that exactly one solution satisfies them, the Nash bargaining solution.
Other sets of axioms lead to other solutions, such as the Kalai–Smorodinsky bargaining solution.
Example: two players dividing one dollar, with utility equal to money and nothing on disagreement, give $F = \set{x \in \R^2 : x_1, x_2 \ge 0, \ x_1 + x_2 \le 1}$ and $d = (0, 0)$.
The model extends to $n$ players with $F \subseteq \R^n$.

## Explanations

### L1 human

Two people can share a gain if they agree, and get a fallback amount if they do not.
The bargaining problem asks which agreement they should reach.
The model records only what they can achieve together and what happens if talks break down.
