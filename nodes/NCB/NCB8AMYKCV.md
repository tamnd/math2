---
tag: NCB8AMYKCV
kind: definition
name: Operator system
msc: [46L07, 47L07]
defines: 4DSVM5Q17H
sources:
  - url: https://en.wikipedia.org/wiki/Operator_system
---

## Definition

Let $A$ be a unital [[C*-algebra|M2WFY1D3SZ]] with unit $1$ and involution $a \mapsto a^*$.
An *operator system* in $A$ is a linear subspace $S \subseteq A$ such that:

1. $1 \in S$;
2. $a^* \in S$ for every $a \in S$.

## Remarks

Example: in the C*-algebra $C(\mathbb{T})$ of continuous functions on the unit circle $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$, let $S$ be the span of $1, z, \bar z$.
It contains $1$, and $(a + b z + c \bar z)^* = \bar a + \bar c z + \bar b \bar z$ lies in $S$, so $S$ is an operator system.
Non-example: the span of $1$ and $z$ in $C(\mathbb{T})$ contains $1$ but not $\bar z$.
Indeed, if $\bar z = a + b z$ on $\mathbb{T}$, then $z = 1$ and $z = -1$ give $a = 0$ and $b = 1$, but then $z = i$ gives $-i = i$.
Every self-adjoint element $h$ of an operator system $S$ satisfies $-\norm{h} 1 \le h \le \norm{h} 1$, so $S$ is spanned by its positive elements.
Many authors take $A = B(H)$ for a Hilbert space $H$, and some also require $S$ to be norm closed.
