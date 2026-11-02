---
tag: WZKPDWBW2Z
kind: definition
name: Maximal chain
msc: [06A06, 06A07]
defines: 3AX549FFFM
uses: [011C29Q1S1, 0GP9ASVQ1X]
sources:
  - url: https://en.wikipedia.org/wiki/Total_order
    locator: Chains
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
A [[chain|0GP9ASVQ1X]] $C \subseteq P$ is *maximal* when there is no chain $D \subseteq P$ with $C \subsetneq D$.

## Remarks

In the subsets of $\set{1, 2, 3}$ ordered by inclusion, $\set{\emptyset, \set{1}, \set{1, 2}, \set{1, 2, 3}}$ is a maximal chain.
Every other subset is incomparable with one of its members, so no subset can be added.
The chain $\set{\emptyset, \set{1}, \set{1, 2, 3}}$ is not maximal, since adding $\set{1, 2}$ gives a larger chain.
The subsets of $\set{1, \dots, n}$ have exactly $n!$ maximal chains, one for each order in which the elements are added.
A maximal chain is a maximal element of the set of chains ordered by inclusion.
The statement that every chain of a poset lies in a maximal chain is the [[Hausdorff maximal principle|0KM4KVR9MV]], which is equivalent to [[Zorn's lemma|04RXTQA5ZA]].

## Explanations

### L1 human

A maximal chain is a chain that cannot be made longer by adding any element of the poset.
