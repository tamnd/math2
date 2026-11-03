---
tag: TW8RNRFT9T
kind: definition
name: Social choice theory
msc: [91B14, 91B12, 91B10]
defines: F17C7F17PM
uses: [JGP0Q56FRY, KH8ACT22FR, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Social_choice_theory
---

## Definition

*Social choice theory* is the study of aggregation rules in the following framework.

1. A finite set $N = \set{1, \dots, n}$ of individuals and a set $A$ of alternatives are given.
2. Each individual $i$ has a [[preference relation|JGP0Q56FRY]] $R_i$ on $A$, and the tuple $(R_1, \dots, R_n)$ is a *profile*.
3. An *aggregation rule* assigns a collective outcome to each admissible profile. For a [[social welfare function|KH8ACT22FR]] the outcome is a social ranking of $A$. For a *social choice function* or *correspondence* it is a chosen alternative or set of alternatives.

The theory states properties of aggregation rules as axioms and determines which combinations of axioms some rule satisfies.

## Remarks

Example: plurality voting fits the framework.
The individual preferences are [[linear orders|0FRXBVVR03]] of $A$, and the rule chooses the alternatives ranked first by the largest number of individuals.

Non-example: the Pareto rule ranks $x$ above $y$ exactly when every individual strictly prefers $x$ to $y$.
It is an aggregation rule, but its output is in general not complete, so it is not a social welfare function in the sense of clause 3.
For two individuals with opposite rankings of $x$ and $y$, it neither ranks $x$ above $y$, nor $y$ above $x$, nor declares them indifferent.

Typical axioms are unanimity (Pareto), anonymity, neutrality, independence of irrelevant alternatives and strategyproofness.
