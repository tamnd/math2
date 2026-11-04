---
tag: "~d571badb"
kind: concept
name: Coefficient of determination of a least-squares solution
msc: [62J05]
uses: [0BYTQ4X1HC, 03Y6AQ2S0J]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-5.xml#L954
    locator: src/section6-5.xml:954
---

## Summary

Let $A\mathbf{x} = \mathbf{b}$ be a system with a data vector $\mathbf{b}$, and let $\hat{\mathbf{x}}$ be a [[least squares|0BYTQ4X1HC]] solution of it.
The vector $A\hat{\mathbf{x}}$ is the fit to the data.

Demeaning $\mathbf{b}$ means subtracting the [[mean|03Y6AQ2S0J]] of its entries from each entry.
Call the resulting vector $\tilde{\mathbf{b}}$.

The *coefficient of determination* of the fit is the number
$$R^2 = 1 - \frac{\|\mathbf{b} - A\hat{\mathbf{x}}\|^2}{\|\tilde{\mathbf{b}}\|^2}.$$

The numerator is the squared length of the error of the fit.
The denominator is the squared length of the demeaned data, which is the total variation of $\mathbf{b}$ about its mean.
