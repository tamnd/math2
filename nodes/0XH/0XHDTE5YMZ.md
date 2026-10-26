---
tag: 0XHDTE5YMZ
kind: definition
name: Function
msc: ["03E20"]
defines: 0EPAT51DXQ
uses: [08EJC6Q25H, 0N3ADS4CHH]
sources:
  - url: https://en.wikipedia.org/wiki/Function_(mathematics)
    locator: lead section
---

## Definition

Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
A function from $A$ to $B$ is a [[binary relation|08EJC6Q25H]] $f \subseteq A \times B$ such that, for each $a \in A$, there is exactly one $b \in B$ with $(a, b) \in f$.
This $b$ is the value of $f$ at $a$, written $f(a)$.
The notation $f \colon A \to B$ says that $f$ is a function from $A$ to $B$.

## Remarks

The set $A$ is the [[domain|093CM69AGS]] and the set $B$ is the [[codomain|0F9JHP8AJN]] of $f$.
Many authors take the triple $(A, B, f)$ as the function. Then two functions with the same pairs but different codomains are different.
Two functions $f, g \colon A \to B$ are equal when $f(a) = g(a)$ for each $a \in A$.
Other names are map and mapping.

## Explanations

### L1 human

A function is a machine: you put in an element $a$ of $A$, and it gives back one element $f(a)$ of $B$.
Each input gives exactly one output, but two inputs can give the same output.
For example, $f(x) = x^2$ on $\mathbb{R}$ sends both $2$ and $-2$ to $4$.
