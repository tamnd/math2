---
tag: TPXEFSBQYB
kind: definition
name: Axiom of dependent choice
msc: ["03E25"]
defines: WEMJBN339R
uses: [0SJ3RX9TXA, 08EJC6Q25H, 0QE8STGJH2]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_of_dependent_choice
---

## Definition

The axiom of dependent choice is the following statement.
Let $X$ be a nonempty [[set|0SJ3RX9TXA]] and let $R$ be a [[binary relation|08EJC6Q25H]] on $X$.
Assume that for each $x \in X$ there is $y \in X$ with $x \mathrel{R} y$.
Then there is a [[sequence|0QE8STGJH2]] $(x_n)_{n \in \N}$ of elements of $X$ such that $x_n \mathrel{R} x_{n+1}$ for each $n \in \N$.

## Remarks

Example: let $X = \N$ and let $m \mathrel{R} n$ mean $m < n$.
Each $m$ has $m + 1$ with $m \mathrel{R} (m+1)$, and the sequence $x_n = n$ satisfies the conclusion.
Non-example of the hypothesis: on $X = \set{0, 1}$ with $R = \set{(0, 1)}$, the element $1$ has no $y$ with $1 \mathrel{R} y$.
No sequence with $x_n \mathrel{R} x_{n+1}$ for all $n$ exists, so the hypothesis cannot be dropped.
The axiom is abbreviated DC.
Over ZF, the [[axiom of choice|0HTGB13FE2]] implies DC, and DC implies the axiom of countable choice; neither implication reverses.
Over ZF, DC is equivalent to the [[Baire category theorem|0A7KGAYHGV]] for complete metric spaces.
An equivalent form says that a relation $R$ on a nonempty set is [[well-founded|0230ECX1Q5]] if and only if there is no sequence with $x_{n+1} \mathrel{R} x_n$ for all $n$.
