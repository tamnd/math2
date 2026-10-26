---
tag: 0RJMNEN3BJ
kind: definition
name: Symmetric group
aliases: [permutation-group-of-a-set]
msc: [20B30]
defines: 0515A6D2Y1
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_group
    locator: Definition and first properties
---

## Definition

Let $X$ be a set.
The symmetric group $\operatorname{Sym}(X)$ is the set of all bijections $\sigma \colon X \to X$, with composition of maps as the operation.
For a positive integer $n$, the symmetric group $S_n$ is $\operatorname{Sym}(\{1, 2, \dots, n\})$.
An element of $S_n$ is a permutation of degree $n$.

## Remarks

The identity map is the identity element, and the inverse of $\sigma$ is the inverse map $\sigma^{-1}$.
In this node, the product $\sigma \tau$ means first $\tau$, then $\sigma$.
The group $S_n$ is not [[abelian|082GHNPJ53]] for $n \geq 3$, because $(1\ 2)(2\ 3) \neq (2\ 3)(1\ 2)$.
If $X$ and $Y$ have the same cardinality, then $\operatorname{Sym}(X)$ and $\operatorname{Sym}(Y)$ are [[isomorphic|08MG7H8JW5]].

## Explanations

### L1 human

The symmetric group collects all the ways to shuffle the elements of a set.
Two shuffles combine into one shuffle when you do them one after the other.
Each shuffle can be undone, so the shuffles form a group.
