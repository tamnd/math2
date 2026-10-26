---
tag: 0TZEEFTNCC
kind: definition
name: Maximal element
msc: [06A06]
defines: 072G59HW59
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_and_minimal_elements
    locator: lead section
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]] and let $S$ be a [[subset|0FE8Q5S42Y]] of $P$.
An element $m \in S$ is a maximal element of $S$ when no $s \in S$ satisfies $m < s$.
Equivalently, for each $s \in S$, $m \le s$ implies $s = m$.

## Remarks

A maximal element need not be the [[greatest element|0Z7HDDXX3X]], and a set can have several maximal elements.
In $\{\{1\}, \{2\}, \{1, 2, 3\}, \{4\}\}$ under $\subseteq$, the maximal elements are $\{1, 2, 3\}$ and $\{4\}$.
[[Zorn's lemma|04RXTQA5ZA]] gives maximal elements in many infinite posets.

## Explanations

### L1 human

A maximal element has nothing above it.
It may still be incomparable with other elements, so it is not necessarily above everything.
