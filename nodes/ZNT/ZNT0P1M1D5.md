---
tag: ZNT0P1M1D5
kind: example
name: Hofstadter sequences
msc: [11B37, 39A05]
illustrates: [7C7FBZGERM]
sources:
  - url: https://en.wikipedia.org/wiki/Hofstadter_sequence
same_as:
  wikidata: Q1623269
  wikipedia: Hofstadter sequence
---

## Example

Hofstadter sequences are integer sequences defined by nested [[nonlinear recurrences|7C7FBZGERM]], in which earlier values decide which earlier terms are used.

1. The *Hofstadter $Q$-sequence* is given by $Q(1) = Q(2) = 1$ and $Q(n) = Q(n - Q(n-1)) + Q(n - Q(n-2))$ for $n > 2$. It begins $1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, \dots$.
2. The *Hofstadter $G$-sequence* is given by $G(0) = 0$ and $G(n) = n - G(G(n-1))$ for $n \ge 1$. It begins $0, 1, 1, 2, 3, 3, 4, 4, 5, \dots$.

Check for $Q$: $Q(3) = Q(2) + Q(2) = 2$, $Q(4) = Q(2) + Q(3) = 3$, $Q(5) = Q(2) + Q(3) = 3$, $Q(6) = Q(3) + Q(3) = 4$.
Check for $G$: $G(1) = 1 - G(0) = 1$, $G(2) = 2 - G(1) = 1$, $G(3) = 3 - G(1) = 2$, $G(4) = 4 - G(2) = 3$.
The $G$-sequence has the closed form $G(n) = \lfloor (n+1)/\varphi \rfloor$, where $\varphi$ is the [[golden ratio|0SC8T7548D]].
The $Q$-sequence behaves erratically, and it is not known whether it is defined for all $n$, that is, whether $n - Q(n-1) \ge 1$ and $n - Q(n-2) \ge 1$ always hold.

## Explanations

### L1 human

These sequences come from Douglas Hofstadter's book *Gödel, Escher, Bach*.
In an ordinary recurrence, you always look back a fixed number of steps.
Here, the values of the sequence tell you how far back to look, which makes the rule self-referential.
Some of these sequences turn out to be tame, like $G$, while others, like $Q$, look chaotic and are still not understood.
