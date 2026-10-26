---
tag: 07QY5RPFBR
kind: definition
name: Subfield
msc: [12F99]
defines: 0GFGHRT2FJ
uses: [0QA8CHH8MG, 0859D58WPD]
sources:
  - url: https://en.wikipedia.org/wiki/Field_extension
    locator: Subfield
---

## Definition

Let $L$ be a [[field|0QA8CHH8MG]].
A subfield of $L$ is a [[subring|0859D58WPD]] $K \subseteq L$ such that $a^{-1} \in K$ for every nonzero $a \in K$.

## Remarks

Equivalently, $K$ contains $0$ and $1$, and $K$ is closed under addition, negation, multiplication and the inverse of nonzero elements.
A subfield is a field with the operations of $L$ restricted to $K$.
The rationals $\mathbb{Q}$ are a subfield of $\mathbb{R}$, and $\mathbb{R}$ is a subfield of $\mathbb{C}$.
The intersection of any family of subfields of $L$ is a subfield of $L$. The intersection of all of them is the [[prime subfield|0VPFBAY7MW]].

## Explanations

### L1 human

A subfield is a smaller field that sits inside a bigger one.
You can add, subtract, multiply and divide its elements without leaving it.
The integers are a subring of $\mathbb{Q}$, but not a subfield, because $1/2 \notin \mathbb{Z}$.
