---
tag: ~afb5bbca
kind: definition
name: Multiplicity of a root
msc: [13F20]
defines: ~7ede87f9
uses: [~4d191b0b, ~21f58b6e]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicity_(mathematics)
    locator: Multiplicity of a root of a polynomial
---

## Definition

Let $R$ be a [[commutative ring|~79bc52c4]], let $f \in R[x]$ with $f \neq 0$ and let $c \in R$.
The multiplicity of $c$ as a root of $f$ is the largest integer $m \ge 0$ such that $(x - c)^m$ divides $f$.

## Remarks

The integer $m$ exists, because $(x - c)^m$ is monic of degree $m$, so it cannot divide $f$ for $m > \deg f$.
The multiplicity is positive exactly when $c$ is a [[root|~4d191b0b]] of $f$.
A root of multiplicity $1$ is a simple root. A root of multiplicity at least $2$ is a repeated root.
In $\mathbb{Q}[x]$, $f = (x - 1)^3 (x + 2)$ has the root $1$ with multiplicity $3$ and the root $-2$ with multiplicity $1$.

## Explanations

### L1 human

The multiplicity counts how many times the factor $x - c$ appears in $f$.
For $(x - 1)^2 (x + 3)$, the root $1$ counts twice and the root $-3$ counts once.
