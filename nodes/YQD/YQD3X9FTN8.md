---
tag: YQD3X9FTN8
kind: concept
name: Digital root
aliases: [digital-roots, repeated-digital-sum]
sources:
  - wikipedia: en:8286632@r1368983554
    locator: Digital root
    note: adopted
    mention: wikipedia://en/8286632
    sections: [Summary]
same_as:
  wikidata: Q2532474
  wikipedia: Digital root
inventory: [S7FBZJZVP5]
---

## Summary

The **digital root** (also **repeated digital sum**) of a [[natural number|0MWKJ44V5A]] in a given radix is the (single digit) value obtained by an iterative process of summing digits, on each iteration using the result from the previous iteration to compute a digit sum. The process continues until a single-digit number is reached. For example, in base 10, the digital root of the number 12345 is 6 because the sum of the digits in the number is 1 + 2 + 3 + 4 + 5 = 15, then the addition process is repeated for the resulting number 15, so that the sum of 1 + 5 equals 6, which is the digital root of that number. In base 10, this is equivalent to taking the remainder upon division by 9 (except when the digital root is 9, where the remainder upon division by 9 will be 0), which allows it to be used as a divisibility rule. The formula for the function $\mathrm{dr}_b:\mathbb{N}\rightarrow\mathop{\bigcup}_{k=0}^{b-1}\{k\},\quad b\in\mathbb{N}_{\geqslant2}$ is expressed as:
