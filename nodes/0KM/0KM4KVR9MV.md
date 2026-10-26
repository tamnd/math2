---
tag: 0KM4KVR9MV
kind: statement
role: theorem
name: Hausdorff maximal principle
aliases: [maximal-chain-principle]
msc: ["03E25"]
uses: [0GP9ASVQ1X, 0TZEEFTNCC, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Hausdorff_maximal_principle
    locator: Statement
same_as:
  wikidata: Q738328
  wikipedia: Hausdorff maximal principle
---

## Statement

Assume the [[axiom of choice|0HTGB13FE2]].
Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
Then each [[chain|0GP9ASVQ1X]] of $P$ is a subset of a maximal chain.
A maximal chain is a chain that is not a proper subset of another chain of $P$.

## Remarks

Over ZF, the principle is equivalent to the axiom of choice and to [[Zorn's lemma|04RXTQA5ZA]].
With the empty chain, it says that each partially ordered set has a maximal chain.
Felix Hausdorff proved it in 1914.

## Explanations

### L1 human

Start with any chain in the order.
You can extend it until no element can be added without breaking the chain property.
