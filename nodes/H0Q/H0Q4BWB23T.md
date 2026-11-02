---
tag: H0Q4BWB23T
kind: concept
name: Partially well-ordered set
msc: [06A06, 06A07]
specializes: [NH25G6GC07, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Well-quasi-ordering
---

## Summary

A partially well-ordered set is a [[partially ordered set|0QV2JS9RJ3]] whose order is a [[well-quasi-ordering|NH25G6GC07]].
Such an order is also called a well-partial-order.
It generalizes a [[well-order|01CGSJ0GNQ]]: the order need not be total, but it is well-founded and every antichain is finite.
One also says that a subset of a preordered set is partially well-ordered when the restricted order has this property.

## Explanations

### L1 human

A well-order lines elements up so that every descent stops.
A partial well-order allows elements that cannot be compared, but only finitely many at a time in any antichain, and still no endless descent.
The set $\N \times \N$ ordered coordinatewise is an example: $(1, 2)$ and $(2, 1)$ are incomparable, yet every antichain is finite.
