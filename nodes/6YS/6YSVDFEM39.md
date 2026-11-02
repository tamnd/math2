---
tag: 6YSVDFEM39
kind: concept
name: Lauricella hypergeometric series
msc: [33C65, 33C70]
sources:
  - url: https://en.wikipedia.org/wiki/Lauricella_hypergeometric_series
same_as:
  wikidata: Q3754612
  wikipedia: Lauricella hypergeometric series
---

## Summary

The Lauricella series $F_A^{(n)}, F_B^{(n)}, F_C^{(n)}, F_D^{(n)}$ are four multiple power series in $n$ variables that extend the [[Appell series|QG9VDK1HN9]] from two variables to any number of variables.
For $n = 2$ they are the Appell series $F_2, F_3, F_4, F_1$, and for $n = 1$ each becomes the Gauss [[hypergeometric series|428M453CR2]].
The series $F_D$ is the most used: it has a one-dimensional Euler-type integral and it describes periods of certain algebraic curves.

## Explanations

### L1 human

The Gauss hypergeometric series has one variable, the Appell series have two, and the Lauricella series allow any number $n$.
The coefficient of $x_1^{m_1} \cdots x_n^{m_n}$ is a ratio of rising factorials that depend either on the single indices $m_i$ or on their total $m_1 + \cdots + m_n$.
For example $F_D$ is what one gets by expanding $\int_0^1 t^{a - 1} (1 - t)^{c - a - 1} \prod_i (1 - x_i t)^{-b_i}\, dt$ in powers of the $x_i$.
Each factor $(1 - x_i t)^{-b_i}$ contributes one variable.
