---
tag: 0BRHKKP333
kind: definition
name: Inverse element
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
defines: 0ZNZH0EXFX
uses: [0580ZJSA3Q, 0RQPZZ44T4]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
  - book: isbn:9780471433347
    locator: Section 1.1
inventory: [FEBX9EH0B8]
---

## Definition

Let $S$ be a set with a [[binary operation|0M418FE7BB]] $\ast$ and an [[identity element|07WYQPB8E3]] $e$.
Let $a, b \in S$.
The element $b$ is a left inverse of $a$ when $b \ast a = e$.
The element $b$ is a right inverse of $a$ when $a \ast b = e$.
The element $b$ is an inverse of $a$ (or two-sided inverse) when it is both a left inverse and a right inverse of $a$.
An element that has an inverse is called invertible.

## Notation

The inverse of $a$ is written $a^{-1}$ in multiplicative notation and $-a$ in additive notation.
The notation is used only when the inverse is unique, for example when $\ast$ is associative.

## Remarks

For addition on $\mathbb{Z}$, the inverse of $a$ is $-a$.
For multiplication on $\mathbb{Q}$, each nonzero $a$ has the inverse $1/a$, and $0$ has no inverse.
When $\ast$ is [[associative|0K8F7PVDMX]], an element has at most one inverse: a left inverse $b$ and a right inverse $c$ of $a$ satisfy $b = b \ast (a \ast c) = (b \ast a) \ast c = c$.
The concept page [[inverse element|0ZNZH0EXFX]] gives more examples, the non-examples and the first properties.

## Explanations

### L1 human

An inverse of an element is a second element that cancels the first one.
If you add $5$ and then add $-5$, you come back to $0$, the identity for addition.
For multiplication, the inverse of $2$ is $\tfrac{1}{2}$, because $2 \cdot \tfrac{1}{2} = 1$.

### L2 human

To check that $b$ is an inverse of $a$, compute both $a \ast b$ and $b \ast a$ and check that each is $e$.
To find an inverse, solve $a \ast x = e$ for $x$, and then check the other side.
A trap is to check only one side in a structure where a one-sided inverse need not be two-sided, such as the functions from $\mathbb{N}$ to $\mathbb{N}$ under composition.
