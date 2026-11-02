---
tag: 2JVB5R0MBW
kind: definition
name: Cancellation property
msc: [08A02, 20M10]
defines: 6CR9A0EWPN
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Cancellation_property
---

## Definition

Let $\ast$ be a [[binary operation|0M418FE7BB]] on a set $S$ and let $a \in S$.

1. The element $a$ is *left cancellable* if $a \ast b = a \ast c$ implies $b = c$, for all $b, c \in S$.
2. The element $a$ is *right cancellable* if $b \ast a = c \ast a$ implies $b = c$, for all $b, c \in S$.
3. The element $a$ is *cancellable* if it is both left and right cancellable.

The pair $(S, \ast)$ is *left cancellative*, *right cancellative* or *cancellative* if every element of $S$ is left cancellable, right cancellable or cancellable.

## Remarks

Example: $(\N, +)$ is cancellative, because $a + b = a + c$ gives $b = c$ by comparing the numbers, and $+$ is commutative.

Non-example: $(\Z, \cdot)$ is not cancellative, because $0 \cdot 1 = 0 \cdot 2$ with $1 \ne 2$, so $0$ is not left cancellable.

An element $a$ is left cancellable if and only if the map $x \mapsto a \ast x$ is injective.
On a set with at least two elements, the operation $a \ast b = b$ is left cancellative but not right cancellative.
