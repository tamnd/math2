---
tag: 04SJTX9P4N
kind: statement
role: theorem
name: Chinese remainder theorem for non-coprime moduli
msc: [11A07]
uses: [0FNN9B4W64, 02WF878BH1, 09S5SN35DJ]
sources:
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: Generalization to non-coprime moduli
---

## Statement

Let $m$ and $n$ be positive integers, and let $a$ and $b$ be integers. Let $g = \gcd(m, n)$ and $M = \operatorname{lcm}(m, n)$.
The system $x \equiv a \pmod m$, $x \equiv b \pmod n$ has an integer solution if and only if $a \equiv b \pmod g$.
In this case, two solutions are congruent modulo $M$.

## Remarks

When $g = 1$, this is the [[Chinese remainder theorem|0FNN9B4W64]] for two moduli.
The condition is necessary: a solution $x$ gives $a \equiv x \equiv b \pmod g$, since $g$ divides $m$ and $n$.
For $k$ moduli $n_1, \dots, n_k$, the system $x \equiv a_i \pmod{n_i}$ has a solution if and only if $\gcd(n_i, n_j) \mid a_i - a_j$ for all $i \neq j$.
For example, $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 6$ has the solutions $x \equiv 9 \pmod{12}$. But $x \equiv 1 \pmod 4$ and $x \equiv 2 \pmod 6$ has no solution.

## Explanations

### L1 human

When the moduli share a factor $g$, the two conditions both say something about $x$ modulo $g$.
They must agree there. If they agree, there is a solution, and it is unique modulo the lcm.
