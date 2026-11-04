---
tag: BQ1D7T0EGD
kind: concept
name: Principle of recursive definition
sources:
  - wikipedia: en:1047605@r1306542381
    locator: Recursive definition, section Form of recursive definitions > Principle of recursive definition
    note: adopted
    mention: wikipedia://en/1047605#MA0E
    sections: [Summary]
inventory: [VNMS423GM9]
---

## Summary

Let $A$ be a set and let $a_{0}$ be an element of $A$. If $\rho$ is a function which assigns to each function $f$ mapping a nonempty section of the positive integers into $A$, an element of $A$, then there exists a unique function $h : \mathbb{Z}_+ \to A$ such that

$$\begin{aligned} h(1) &= a_0 \\ h(i) &= \rho \left(h|_{\{1,2,\ldots,i-1\}}\right) \text{ for } i>1. \end{aligned}$$
