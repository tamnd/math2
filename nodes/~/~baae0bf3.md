---
tag: ~baae0bf3
kind: definition
name: Nilpotent element
msc: [16N40]
defines: ~3cc37065
uses: [~447242bf]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent
    locator: lead section
---

## Definition

Let $R$ be a [[ring|~447242bf]].
An element $x \in R$ is nilpotent if there is a positive integer $n$ such that $x^n = 0$.

## Remarks

In $\mathbb{Z}/8\mathbb{Z}$, the class of $2$ is nilpotent, because $2^3 = 8 = 0$.
The matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is nilpotent: its square is the zero matrix.
In a nonzero ring, a nilpotent element is a [[zero divisor|~2f380c28]]: if $n$ is the least integer with $x^n = 0$, then $x \cdot x^{n-1} = 0$ and $x^{n-1} \neq 0$.
An [[integral domain|~6bd4a5ff]] has no nilpotent element except $0$.

## Explanations

### L1 human

A nilpotent element is not zero, but some power of it is zero.
Numbers do not behave like this.
In the integers modulo $8$, the element $2$ does: $2 \cdot 2 \cdot 2 = 8$, and $8$ is $0$ modulo $8$.
