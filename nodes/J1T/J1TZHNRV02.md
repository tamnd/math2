---
tag: J1TZHNRV02
kind: definition
name: Pseudorandom number generator
msc: [65C10, 11K45]
defines: C5FG6ARWVV
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Pseudorandom_number_generator
---

## Definition

A *pseudorandom number generator* is a tuple $(S, s_0, T, U, G)$ where:

1. $S$ is a finite set, the state space;
2. $s_0 \in S$ is the initial state, or seed;
3. $T \colon S \to S$ is a map, the transition function;
4. $U$ is a set, the output space, usually $[0, 1)$ or a set of integers $\set{0, \ldots, m-1}$;
5. $G \colon S \to U$ is a map, the output function.

The generator produces the states $s_i = T(s_{i-1})$ for $i \ge 1$ and the output sequence $u_i = G(s_i)$ for $i \ge 0$.

## Remarks

Example: $S = \set{0, \ldots, 7}$, $T(s) = (5s + 1) \bmod 8$, $U = [0, 1)$, $G(s) = s/8$ and $s_0 = 0$; all five clauses hold, and the outputs are $0, 0.125, 0.75, 0.875, 0.5, 0.625, 0.25, 0.375$, then repeat.
Non-example: the sequence of decimal digits of $\pi$ is not eventually periodic, because $\pi$ is irrational.
It is not the output sequence of any such tuple, since a finite state space as in clause 1 forces the outputs to be eventually periodic.
Since $S$ is finite, the sequence $(s_i)$ is eventually periodic, with period at most $\abs{S}$; if $T$ is a bijection it is purely periodic.
The definition is purely structural; the quality of a generator is judged by its period, by the uniformity of tuples $(u_i, \ldots, u_{i+k-1})$, and by statistical tests.
Generators for cryptography must in addition be unpredictable from past outputs, which is a stronger requirement.
