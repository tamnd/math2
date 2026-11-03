---
tag: SSK0QQYYBP
kind: statement
role: theorem
name: Rental harmony
msc: [91B32, 54H25]
uses: [YX1DJK2QAG, HQG3V5Z6MR, P3GPD0S0J7]
about: [X1X9TZ8GAR]
sources:
  - url: https://en.wikipedia.org/wiki/Rental_harmony
same_as:
  wikidata: Q24964528
  wikipedia: Rental harmony
---

## Statement

Let $n \ge 2$ tenants share a house with $n$ rooms, and let $R > 0$ be the total rent.
A price vector is a point of the [[simplex|YX1DJK2QAG]] $\Delta = \set{p \in \R^n : p_j \ge 0 \text{ for all } j, \ p_1 + \cdots + p_n = R}$, where $p_j$ is the rent of room $j$.
For each tenant $i$ and each $p \in \Delta$, let $A_i(p)$ be a nonempty subset of $\set{1, \dots, n}$.
It is the set of rooms that tenant $i$ likes best at the prices $p$.
Assume the following.

1. Closed preferences: for all $i$ and $j$, the set $\set{p \in \Delta : j \in A_i(p)}$ is closed in $\Delta$.
2. Miserly tenants: if some room is free at $p$, then every room in $A_i(p)$ is free at $p$, that is, $p_j = 0$ for all $j \in A_i(p)$.

Then there are a price vector $p \in \Delta$ and a bijection $\sigma$ from the tenants to the rooms such that $\sigma(i) \in A_i(p)$ for every tenant $i$.

## Remarks

The result is due to Francis Su, who proved it with [[Sperner's lemma|HQG3V5Z6MR]].
Triangulate $\Delta$ finely and give each vertex an owner, so that every small cell has vertices owned by all $n$ tenants.
Label each vertex by a room that its owner likes best there; the miserly condition makes this a Sperner labelling, so some small cell is fully labelled.
Letting the triangulation get finer and using the closed preferences gives the exact prices in the limit.
The resulting division is [[envy-free|P3GPD0S0J7]]: at the prices $p$, no tenant prefers the room of another tenant.
Without the miserly condition the conclusion can fail.
If two tenants like only room $1$ at every price vector, even when room $1$ costs all of $R$, no assignment works.

## Explanations

### L1 human

Housemates must split the rent of a house whose rooms differ in size and comfort.
The theorem says there is always a way to set the rent of each room so that every housemate gets a room they like best at those rents.
The only assumptions are that people prefer a free room to a paid one and that their tastes do not jump suddenly as prices change.

### L2 human

This is a fixed-point style result of [[fair division|X1X9TZ8GAR]], with the price simplex as the space and Sperner's lemma as the engine.
The proof gives an approximate algorithm: on a fine triangulation, ask the owner of each vertex for a favourite room and follow the Sperner path to a fully labelled cell.
It is a dual of envy-free cake-cutting, where the pieces of cake are replaced by prices that sum to a fixed total.
