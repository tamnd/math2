---
tag: ~c6bd0e8a
kind: statement
role: theorem
name: The rationals are countable
msc: ["03E10"]
uses: [~c69f6aeb, ~5fc8900d, ~fccd21c4]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_number
    locator: Countability
same_as:
  wikidata: Q1244890
  wikipedia: Rational number
---

## Statement

The set $\mathbb{Q}$ of rational numbers is [[countably infinite|~c69f6aeb]].

## Remarks

Proof: each rational number has a unique form $p/q$ with $p \in \mathbb{Z}$, $q \ge 1$ and $\gcd(p, q) = 1$. The map $p/q \mapsto (p, q)$ is an injection into $\mathbb{Z} \times \mathbb{N}$, which is countable. And $\mathbb{Q}$ is infinite.
The rationals are dense in $\mathbb{R}$, but they are countable, and $\mathbb{R}$ is [[not countable|~5d49ab7f]].

## Explanations

### L1 human

Write the fractions $p/q$ in a grid, with $p$ along one side and $q$ along the other.
List the grid diagonal by diagonal, and skip each fraction that is not in lowest terms.
Each rational number appears exactly one time.
