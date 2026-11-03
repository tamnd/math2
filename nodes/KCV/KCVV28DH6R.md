---
tag: KCVV28DH6R
kind: problem
name: Fair cake-cutting
msc: [91B32, 91A06]
uses: [X1X9TZ8GAR, P3GPD0S0J7, PR11BZQQPG, 2Z2QVWZ262]
about: [X1X9TZ8GAR]
sources:
  - url: https://en.wikipedia.org/wiki/Fair_cake-cutting
same_as:
  wikidata: Q18206991
  wikipedia: Fair cake-cutting
history:
  posed_by: Hugo Steinhaus
  first_stated: "1948"
---

## Problem

The cake is the interval $C = [0, 1]$, and there are $n$ agents.
Agent $i$ has a valuation $V_i$, a nonatomic probability [[measure|PR11BZQQPG]] on the Borel subsets of $C$.
An example is a measure with a density with respect to [[Lebesgue measure|2Z2QVWZ262]].
The valuations are private: a procedure may only ask agents to evaluate pieces or to cut pieces of a given value.
The problem is to find a procedure that works for all valuations.
It must produce an allocation $(X_1, \dots, X_n)$ of $C$ into measurable pieces with a fairness property, such as:

1. *proportionality*: $V_i(X_i) \ge 1/n$ for every $i$;
2. *[[envy-freeness|P3GPD0S0J7]]*: $V_i(X_i) \ge V_i(X_j)$ for all $i, j$.

## Remarks

For two agents, divide and choose gives an allocation that is both proportional and envy-free.
For any $n$, proportional allocations can be found by finite procedures; the Even–Paz algorithm uses $O(n \log n)$ queries.
For three agents, the Selfridge–Conway procedure gives an envy-free allocation with finitely many cuts.
For every $n$, envy-free allocations exist.
A finite bounded envy-free procedure for every $n$ was given by Aziz and Mackenzie in 2016, and its number of queries grows very fast with $n$.
Many variants are studied: connected pieces, more general valuations, chores with negative value, and efficiency together with fairness.

## Explanations

### L1 human

Several people want to share a cake, but each cares about different parts, say the chocolate or the cherries.
Nobody can read another's mind; each can only say how much she likes a piece, or cut a piece she likes a given amount.
The problem asks for rules that guarantee everyone a fair share by her own taste, whatever the tastes are.
