---
tag: XYZEVGCBXN
kind: definition
name: Recursively enumerable language
msc: [03D25, 68Q45, 68Q04]
defines: 67R1A5Y54R
uses: [W6ESDYBF8Z, 5VRS8PJEFT]
sources:
  - url: https://en.wikipedia.org/wiki/Recursively_enumerable_language
---

## Definition

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$ be a [[formal language|5VRS8PJEFT]].
Let $M$ be a [[Turing machine|W6ESDYBF8Z]] with input alphabet $\Sigma$ and an accepting halting state.
The machine $M$ *recognises* $L$ if, for every $w \in \Sigma^*$, the run of $M$ on $w$ halts in the accepting state exactly when $w \in L$.
On inputs $w \notin L$ the machine may halt in another state or run forever.
The language $L$ is *recursively enumerable*, or *Turing-recognizable*, if some Turing machine recognises it.
The language $L$ is *co-recognizable* if its complement $\Sigma^* \setminus L$ is recursively enumerable.

## Remarks

Equivalently, $L$ is recursively enumerable when it is empty or there is a machine that prints exactly the members of $L$, in some order and possibly with repetitions.
Example: the halting language $H = \set{\langle M, w \rangle : M \text{ halts on } w}$ is recursively enumerable.
A universal machine simulates $M$ on $w$ and accepts if the simulation halts, so it accepts exactly the members of $H$.
Non-example: the complement of $H$ is not recursively enumerable.
If it were, $H$ would be decidable by the [[characterisation of decidable languages|EZ6Z9V91C2]], which contradicts the undecidability of the [[halting problem|Z7TN2B35B0]].
Every [[decidable language|P74SXXT7DX]] is recursively enumerable.
Under a computable bijection between $\Sigma^*$ and $\N$, these languages correspond to the [[computably enumerable sets|TN9G24VABN]].
