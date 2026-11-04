---
kind: concept
name: Column-stochastic matrix
aliases:
  - probability-vector
  - column-stochastic-matrix
msc:
  - 15B51
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-5.xml#L180
    locator: src/section4-5.xml:180
tag: ~0a4cbee0
uses:
  - 0JXZKX526R
  - JPQCCFCY8X
---

## Summary

A probability vector is a vector whose entries are all nonnegative and whose entries add up to $1$.

A column-stochastic matrix is a [[square matrix|0JXZKX526R]] in which every column is a probability vector. So all entries are nonnegative, as in a [[nonnegative matrix|JPQCCFCY8X]], and each column sums to $1$.

This is the column convention. The node [[transition matrix|0F1KBVY161]] uses the row convention, where each row sums to $1$. The two conventions differ by taking the transpose.
