---
tag: 1JCQTY728A
kind: definition
name: Semifield
msc: [12K10, 17A35]
defines: AHH97EJ6VH
uses: [082GHNPJ53, 0EA5BTA0CX, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Semifield
---

## Definition

A *semifield* is a set $S$ with two binary operations $+$ and $\cdot$ such that:

1. $(S, +)$ is an [[abelian group|082GHNPJ53]], with identity element $0$.
2. Both distributive laws hold: $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$ for all $a, b, c \in S$.
3. There is an element $1 \ne 0$ with $1 \cdot a = a \cdot 1 = a$ for all $a \in S$.
4. For all $a, b \in S$ with $a \ne 0$, each of the equations $a x = b$ and $y a = b$ has exactly one solution $x \in S$ and exactly one solution $y \in S$.

Multiplication is not required to be associative or commutative.

## Remarks

Clauses 3 and 4 say that $S \setminus \set{0}$ is a loop under multiplication.
A structure that satisfies clauses 1, 2 and 4 but not necessarily 3 is called a presemifield.
If $S$ is finite, clause 4 is equivalent to the absence of zero divisors: $ab = 0$ implies $a = 0$ or $b = 0$.
An associative semifield is a [[division ring|0EA5BTA0CX]], and a finite associative semifield is a finite [[field|04C5ZBG1WT]] by Wedderburn's little theorem.

Example: every field is a semifield, since it satisfies all four clauses and is moreover associative.
The real octonions are a semifield in which multiplication is not associative.

Non-example: the ring $\Z$ satisfies clauses 1, 2 and 3 but fails clause 4, because $2x = 1$ has no solution $x \in \Z$.

In another usage, found for instance in tropical geometry, a semifield is a commutative semiring in which every nonzero element has a multiplicative inverse, such as $(\R \cup \set{-\infty}, \max, +)$.
