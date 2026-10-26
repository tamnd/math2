---
tag: 0GNGPF7KS5
kind: definition
name: Antichain
msc: [06A07]
defines: 03HF498P1J
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Antichain
    locator: lead section
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
A subset $A$ of $P$ is an antichain when, for all $a, b \in A$ with $a \neq b$, neither $a \le b$ nor $b \le a$.

## Remarks

In the power set of $\{1, 2, 3\}$, the set $\{\{1\}, \{2\}, \{3\}\}$ is an antichain.
A chain and an antichain have at most one common element.
The largest size of an antichain is the width of the poset.

## Explanations

### L1 human

An antichain is the opposite of a [[chain|0GP9ASVQ1X]]: its elements are side by side.
Under divisibility, the primes form an antichain, because no prime divides another prime.
