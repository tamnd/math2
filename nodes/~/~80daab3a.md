---
tag: ~80daab3a
kind: definition
name: Multiplication of natural numbers
msc: [03F30]
defines: ~8a70c676
uses: [~6bc69be4, ~717c529c, ~13017306, ~8885364d]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplication
    locator: Product of two natural numbers
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Multiplication
---

## Definition

Let $\mathbb{N}$ be the set of [[natural numbers|~6bc69be4]], let $S$ be the [[successor function|~717c529c]] and let $+$ be the [[addition|~13017306]] of $\mathbb{N}$.
Multiplication is the function $\cdot \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$, $(a, b) \mapsto a \cdot b$, with these two properties for all $a$ and $b$ in $\mathbb{N}$:
$$a \cdot 0 = 0, \qquad a \cdot S(b) = a \cdot b + a.$$

## Remarks

For each $a$, these equations are a [[definition by recursion|~8885364d]] on $b$. Thus exactly one such function exists.
From the definition, $a \cdot 1 = a \cdot 0 + a = a$.
We often write $ab$ for $a \cdot b$.

## Explanations

### L1 human

Multiplication is repeated addition: $3 \cdot 4$ is $3 + 3 + 3 + 3 = 12$.
The definition says this in two rules: zero copies give $0$, and one more copy adds one more $a$.
