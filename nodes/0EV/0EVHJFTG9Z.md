---
tag: 0EVHJFTG9Z
kind: definition
name: Linear independence
msc: [15A03]
defines: 0CRMGPAH83
uses: [0JB3DP1BMF]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
A family $(v_1, \dots, v_k)$ of vectors of $V$ is *linearly independent* when the only [[linear combination|0V8F3E48E6]] of them that equals $0$ is the trivial one:
$$a_1 v_1 + \cdots + a_k v_k = 0 \implies a_1 = \cdots = a_k = 0$$
for all $a_1, \dots, a_k \in F$.
An arbitrary family $(v_i)_{i \in I}$ is *linearly independent* when each finite subfamily is linearly independent.
A family that is not linearly independent is *linearly dependent*.

## Remarks

The vectors $(1, 0)$ and $(1, 1)$ in $\R^2$ are linearly independent; the vectors $(1, 2)$ and $(2, 4)$ are linearly dependent.
A family that contains the zero vector, or the same vector twice, is linearly dependent.
A family of at least two vectors is linearly dependent if and only if one of its vectors is a linear combination of the others.
In $F^n$, a family of more than $n$ vectors is linearly dependent.

## Explanations

### L1 human

Vectors are linearly independent when none of them is redundant.
No vector can be built from the others, so each one adds a new direction.
Two arrows in the plane are independent exactly when they do not lie on one line.
