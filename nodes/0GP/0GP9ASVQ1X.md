---
tag: 0GP9ASVQ1X
kind: definition
name: Chain
msc: [06A06]
defines: 0S8FE7ZMFM
uses: [011C29Q1S1, 0316AYH1SC]
sources:
  - url: https://en.wikipedia.org/wiki/Total_order
    locator: Chains
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
A subset $C$ of $P$ is a chain when, for all $a, b \in C$, $a \le b$ or $b \le a$.

## Remarks

So a chain is a subset on which $\le$ is a [[total order|0316AYH1SC]].
In the power set of $\mathbb{N}$, the sets $\{0\} \subseteq \{0, 1\} \subseteq \{0, 1, 2\} \subseteq \dots$ form a chain.
Chains are the key notion in [[Zorn's lemma|04RXTQA5ZA]] and in the [[Hausdorff maximal principle|0KM4KVR9MV]].

## Explanations

### L1 human

A chain is a part of the order that lies on one line.
In the divisors of $12$, the set $\{1, 2, 4, 12\}$ is a chain, but $\{2, 3\}$ is not.
