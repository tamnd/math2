---
tag: 5VRS8PJEFT
kind: definition
name: Formal language
msc: [68Q45, 03D05]
defines: 5MFZ4VNY6D
uses: [D9FCP61J44, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_language
---

## Definition

Let $\Sigma$ be an alphabet and let $\Sigma^*$ be the set of [[strings|D9FCP61J44]] over $\Sigma$.
A *formal language* over $\Sigma$ is a [[subset|0FE8Q5S42Y]] $L \subseteq \Sigma^*$.

## Remarks

Example: $L = \set{a^n b^n : n \ge 0} = \set{\varepsilon, ab, aabb, \dots}$ is a language over $\set{a, b}$, since each member is a finite string over $\set{a, b}$.
Non-example: a set that contains the infinite sequence $aaa\cdots$ is not a language over $\set{a}$, since that sequence is not in $\Sigma^*$.
The empty language $\emptyset$ and the language $\set{\varepsilon}$ are different: the first has no strings, the second has one.
Languages are combined by the set operations and by concatenation $L_1 L_2 = \set{uv : u \in L_1, v \in L_2}$.
Since $\Sigma^*$ is countably infinite, there are uncountably many languages over $\Sigma$ but only countably many Turing machines, so most languages are not recursively enumerable.
