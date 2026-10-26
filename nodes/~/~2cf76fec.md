---
tag: ~2cf76fec
kind: definition
name: Cartesian product
msc: ["03E20"]
defines: ~b5dfd1b6
uses: [~3c815836]
sources:
  - url: https://en.wikipedia.org/wiki/Cartesian_product
    locator: lead section
---

## Definition

Let $A$ and $B$ be [[sets|~bd92ceee]].
The Cartesian product of $A$ and $B$ is the set
$$A \times B = \{(a, b) \mid a \in A \text{ and } b \in B\}$$
of all [[ordered pairs|~3c815836]] $(a, b)$ with $a \in A$ and $b \in B$.

## Remarks

Example: $\{1, 2\} \times \{x, y\} = \{(1, x), (1, y), (2, x), (2, y)\}$.
For finite sets with $m$ and $n$ elements, $A \times B$ has $mn$ elements.
The plane $\mathbb{R}^2$ is $\mathbb{R} \times \mathbb{R}$.
A [[binary relation|~41fc00d0]] from $A$ to $B$ is a subset of $A \times B$.

## Explanations

### L1 human

Think of a table with a row for each element of $A$ and a column for each element of $B$.
Each cell of the table is one pair $(a, b)$.
The Cartesian product is the set of all the cells.
