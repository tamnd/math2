---
tag: 0CYRECG2YQ
kind: definition
name: Transitive relation
msc: ["03E20"]
defines: 0GJZW9JFZQ
uses: [08EJC6Q25H]
sources:
  - url: https://en.wikipedia.org/wiki/Transitive_relation
    locator: lead section
inventory: [Q23D46R4C1]
---

## Definition

Let $R$ be a [[binary relation|08EJC6Q25H]] on a set $A$.
The relation $R$ is transitive when, for all $a, b, c \in A$, $a \mathrel{R} b$ and $b \mathrel{R} c$ imply $a \mathrel{R} c$.

## Remarks

The relations $<$, $\le$ and $=$ on $\mathbb{R}$ are transitive, and so is divisibility on $\mathbb{Z}$.
"Is a parent of" is not transitive.
The smallest transitive relation that contains $R$ is the [[transitive closure|0PEJH7AC74]] of $R$.

## Explanations

### L1 human

Transitivity lets you chain steps.
From $2 < 5$ and $5 < 9$ you get $2 < 9$.
In the graph of a transitive relation, each path of two arrows has a direct arrow as a shortcut.
