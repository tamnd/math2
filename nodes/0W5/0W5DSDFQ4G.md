---
tag: 0W5DSDFQ4G
kind: definition
name: Addition of natural numbers
msc: [03F30]
defines: 0S13V32CPB
uses: [0MWKJ44V5A, 0832XVR512, 0DSHAVH45F]
sources:
  - url: https://en.wikipedia.org/wiki/Addition
    locator: Natural numbers
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Addition
---

## Definition

Let $\mathbb{N}$ be the set of [[natural numbers|0MWKJ44V5A]] and let $S$ be the [[successor function|0832XVR512]].
Addition is the function $+ \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$, $(a, b) \mapsto a + b$, with these two properties for all $a$ and $b$ in $\mathbb{N}$:
$$a + 0 = a, \qquad a + S(b) = S(a + b).$$

## Remarks

For each $a$, these equations are a [[definition by recursion|0DSHAVH45F]] on $b$. Thus exactly one such function exists.
With $1 = S(0)$, the second equation gives $a + 1 = S(a)$.
For example, $2 + 2 = S(2 + 1) = S(S(2 + 0)) = S(S(2)) = 4$.

## Explanations

### L1 human

To add $b$ to $a$, you start at $a$ and count up $b$ steps.
The definition says this in two rules: adding $0$ changes nothing, and adding one more step gives the next number.
