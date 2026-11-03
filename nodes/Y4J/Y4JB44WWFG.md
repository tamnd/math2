---
tag: Y4JB44WWFG
kind: concept
name: Parity-check matrix
msc: [94B05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Parity-check_matrix
same_as:
  wikidata: Q3100414
  wikipedia: Parity-check matrix
---

## Summary

A parity-check matrix of a [[linear code|E85KREWV60]] $C$ is a matrix $H$ such that a word $x$ lies in $C$ exactly when $Hx^T = 0$.
Each row of $H$ is one linear check that every codeword passes.
It describes the code by equations, while a [[generator matrix|8TXKFC5PRD]] describes it by a basis.
The vector $Hy^T$ of a received word $y$, its syndrome, shows which checks fail and is used in [[syndrome decoding|ZH3QHHP8H7]].

## Explanations

### L1 human

A parity-check matrix is a list of tests for codewords.
Each test adds up some symbols of the word and asks whether the sum is zero.
A word is a codeword when it passes every test.
For example, over $\F_2$ the single row $(1, 1, 1)$ tests whether a word of length $3$ has an even number of ones.
The words that pass are $000$, $011$, $101$, $110$.
