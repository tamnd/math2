---
tag: 6X0C4HNMAZ
kind: concept
name: Wynn's epsilon algorithm
msc: [65B05, 65B10, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Shanks_transformation
---

## Summary

Wynn's epsilon algorithm is a recursive scheme that computes the values of the [[Shanks transformation|C0TXDZZMH7]] without evaluating determinants.
Each new entry of its table is computed from three earlier entries by one subtraction, one division and one addition.
It is one of the most widely used nonlinear [[series acceleration|B1S2XJPGYD]] methods.

## Explanations

### L1 human

The Shanks transformation is defined by large determinants, which are expensive and unstable to compute.
Wynn found a short recursion that fills a triangular table column by column.
The even columns of the table contain the Shanks values; the odd columns are only intermediate results.
For example, the second column built from the partial sums $1, \frac23, \frac{13}{15}$ of the Leibniz series gives $\frac{19}{24}$, the first Shanks value.
