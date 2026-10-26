---
tag: 0M3PYJ3TSE
kind: statement
role: theorem
name: The number of Sylow subgroups divides the index
msc: [20D20]
uses: [0JWZX6FKSH, 09ZJ6CAK7S, 04DC0SRN2K]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Statement
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime number, and let $P$ be a [[Sylow p-subgroup|0053CQE9Y2]] of $G$.
Then $n_p$ divides the [[index|0DTXBQPA2S]] $[G : P]$.

## Remarks

By [[this formula|09ZJ6CAK7S]], $n_p = [G : N_G(P)]$, and $[G : P] = [G : N_G(P)] \cdot [N_G(P) : P]$.
If $|G| = p^n m$ with $p \nmid m$, then $n_p$ divides $m$.
For example, in a group of order $15$, $n_3$ divides $5$ and $n_3 \equiv 1 \pmod 3$, so $n_3 = 1$.

## Explanations

### L1 human

The number of Sylow subgroups is the size of a conjugation orbit.
Orbit sizes divide the order of the group, and here even the part of the order without $p$.
This gives a strong limit on $n_p$.
