---
tag: 0F1D6PK9RZ
kind: definition
name: Well-order
msc: [06A05]
defines: 01CGSJ0GNQ
uses: [0316AYH1SC, 0T2NTJCV83]
sources:
  - url: https://en.wikipedia.org/wiki/Well-order
    locator: lead section
inventory: [WPN6VNJ0WP]
---

## Definition

Let $A$ be a set.
A well-order on $A$ is a [[total order|0316AYH1SC]] $\le$ on $A$ such that each nonempty subset of $A$ has a [[least element|0T2NTJCV83]].
The pair $(A, \le)$ is a well-ordered set.

## Remarks

The usual order on $\mathbb{N}$ is a well-order.
The usual orders on $\mathbb{Z}$ and on $[0, 1]$ are not well-orders: $\mathbb{Z}$ and $(0, 1]$ have no least element.
A total order is a well-order exactly when its strict order $<$ is [[well-founded|0230ECX1Q5]].
The [[well-ordering theorem|0N109NG5ZX]] says that each set has a well-order.

## Explanations

### L1 human

In a well-ordered set, each nonempty part has a first element.
So you can always say "take the smallest element with this property".
