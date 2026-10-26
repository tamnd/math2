---
tag: 05FQ3VGAR9
kind: definition
name: Bounded sequence
msc: [40A05]
defines: 0A8JNBGT2Z
uses: [0CTV783HYT]
sources:
  - url: https://en.wikipedia.org/wiki/Sequence
    locator: Bounded
  - url: https://en.wikipedia.org/wiki/Bounded_function
    locator: lead section
---

## Definition

Let $(a_n)$ be a [[real sequence|0CTV783HYT]].
The sequence is bounded above if there is a real number $M$ with $a_n \le M$ for all $n \in \mathbb{N}$.
The sequence is bounded below if there is a real number $m$ with $a_n \ge m$ for all $n \in \mathbb{N}$.
The sequence is bounded if it is bounded above and bounded below.
Equivalently, $(a_n)$ is bounded if there is a real number $K \ge 0$ with $|a_n| \le K$ for all $n \in \mathbb{N}$.

## Remarks

The sequence $a_n = (-1)^n$ is bounded, with $K = 1$.
The sequence $a_n = n$ is bounded below by $0$, but it is not bounded above.
A sequence is a function on $\mathbb{N}$, so a bounded sequence is a bounded function on $\mathbb{N}$.
Each [[convergent sequence|0AZ3R52593]] is bounded, as the node [[convergent sequences are bounded|0S4JF619V7]] states.

## Explanations

### L1 human

A sequence is bounded when all its terms stay inside one fixed interval $[-K, K]$.
The terms can move up and down, but they never escape from that interval.
