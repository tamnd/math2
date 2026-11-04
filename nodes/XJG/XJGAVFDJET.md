---
tag: XJGAVFDJET
kind: proof
name: Proof that a set is open if and only if its complement is closed
msc: [54A05]
proves: 0K67Q60Z8P
uses: [0CNQXVBHCX, 01ZQQDCERP, 0G5AV9Q4RR, 0B1FSS1VZW]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_set
---

## Proof

1. Let $X$ be a [[topological space|0CNQXVBHCX]] and let $U \subseteq X$.
2. By the definition of a [[closed set|0G5AV9Q4RR]], the set $X \setminus U$ is closed if and only if its [[complement|0B1FSS1VZW]] $X \setminus (X \setminus U)$ is [[open|01ZQQDCERP]].
3. A point $x \in X$ lies in $X \setminus (X \setminus U)$ exactly when it is not outside $U$, that is, when $x \in U$. So $X \setminus (X \setminus U) = U$.
4. By steps 2 and 3, $X \setminus U$ is closed if and only if $U$ is open.

## Idea

A set is closed when its complement is open. Taking the complement twice gives back the set, so the statement is the definition read the other way round.
