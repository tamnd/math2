---
tag: B61GY80PKG
kind: definition
name: Consistency of summability methods
msc: ["40D25", "40C05"]
defines: W3BVN1HDXW
uses: [8X25Q4XYMN, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $A$ and $B$ be [[summability methods|8X25Q4XYMN]] for series of real or complex numbers.
For a series $\sum a_n$ that is $A$-summable, write $A\text{-}\sum a_n$ for the value that $A$ assigns to it, and similarly for $B$.
The methods $A$ and $B$ are *consistent* if for every series $\sum a_n$ that is both $A$-summable and $B$-summable,
$$A\text{-}\sum a_n = B\text{-}\sum a_n.$$

## Remarks

Example: Cesàro summation and Abel summation are consistent.
Indeed, if $\sum a_n$ is Cesàro summable to $s$, then it is Abel summable to the same $s$, so whenever both methods apply their values agree.

Non-example: let $A$ assign to a series the limit of its even [[partial sums|0NB643K60Q]] $s_0, s_2, s_4, \dots$, and let $B$ assign the limit of its odd partial sums $s_1, s_3, s_5, \dots$.
Both methods give the usual sum to every convergent series.
For $1 - 1 + 1 - 1 + \cdots$, the even partial sums are all $1$ and the odd ones are all $0$.
So both methods sum this series, with values $1$ and $0$, and $A$ and $B$ are not consistent.

The same notion applies to methods that act on sequences rather than series, by comparing the values they assign to a common summable sequence.
