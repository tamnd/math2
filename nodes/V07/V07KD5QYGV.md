---
tag: V07KD5QYGV
kind: counterexample
name: Condorcet paradox
msc: [91B12, 91B14]
uses: [WZYEADV8E1, 0GJZW9JFZQ, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Condorcet_paradox
same_as:
  wikidata: Q745768
  wikipedia: Condorcet paradox
---

## Counterexample

Let $A = \set{a, b, c}$ and let three voters have the strict rankings ([[linear orders|0FRXBVVR03]])
$$a \succ_1 b \succ_1 c, \qquad b \succ_2 c \succ_2 a, \qquad c \succ_3 a \succ_3 b.$$
Define the majority relation by $x \mathrel{M} y$ when more voters rank $x$ above $y$ than $y$ above $x$.
Voters $1$ and $3$ rank $a$ above $b$, so $a \mathrel{M} b$.
Voters $1$ and $2$ rank $b$ above $c$, so $b \mathrel{M} c$.
Voters $2$ and $3$ rank $c$ above $a$, so $c \mathrel{M} a$.
If $M$ were [[transitive|0GJZW9JFZQ]], then $a \mathrel{M} b$ and $b \mathrel{M} c$ would give $a \mathrel{M} c$, which contradicts $c \mathrel{M} a$ because $M$ is asymmetric.
So the majority relation of a profile of transitive preferences need not be transitive.
In this profile no candidate beats both others, so there is no Condorcet winner, and a [[Condorcet method|WZYEADV8E1]] must use some other rule.

## Explanations

### L1 human

Each of the three voters has a perfectly sensible ranking.
Yet the group prefers $a$ to $b$, $b$ to $c$ and $c$ to $a$ by majority vote, like rock, paper and scissors.
So "what the majority wants" can go round in a circle, and the order in which pairs are voted on can decide the result.
