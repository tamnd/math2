---
tag: 0TPWS0K1BC
kind: statement
role: theorem
name: An algebraic extension of an algebraic extension is algebraic
msc: [12F05]
uses: [09EYMKMSB9, 0DFYTNZ6AM, 0A7KJ68XHT]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_extension
    locator: Properties
---

## Statement

Let $K \subseteq L \subseteq M$ be fields.
If $M/L$ and $L/K$ are [[algebraic|09EYMKMSB9]], then $M/K$ is algebraic.

## Remarks

The proof: let $a \in M$ have minimal polynomial $x^n + c_{n-1} x^{n-1} + \dots + c_0$ over $L$. The field $E = K(c_0, \dots, c_{n-1})$ is finite over $K$, and $E(a)$ is finite over $E$. By the [[tower law|0A7KJ68XHT]], $E(a)/K$ is finite, so $a$ is algebraic over $K$.
Also, if $M/K$ is algebraic, then $M/L$ and $L/K$ are algebraic.

## Explanations

### L1 human

Algebraic extensions can be stacked.
If each step adds only algebraic elements, then the whole tower adds only algebraic elements.
