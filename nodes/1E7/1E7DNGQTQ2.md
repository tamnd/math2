---
tag: 1E7DNGQTQ2
kind: definition
name: Coalescent theory
msc: [60J90, 92D15, 92D10]
defines: 2W8Y2Y1C8J
uses: [SR4F169EKF, 0Y0JGC2K9T, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Coalescent_theory
---

## Definition

Let a population reproduce in discrete generations, each gene of generation $g$ having exactly one parent gene in generation $g - 1$, as in the [[Wright–Fisher model|SR4F169EKF]].
Take a sample of $n$ genes in the present generation $0$.
For $t \ge 0$, let $A_n(t)$ be the number of distinct ancestors of the sample in generation $-t$.

1. A *coalescence* at time $t$ is the event that two or more ancestral lines in generation $-(t-1)$ have one parent in generation $-t$.
2. The *genealogy* of the sample is a [[rooted tree|0Y0JGC2K9T]] with the $n$ sampled genes as leaves. Its internal vertices are the coalescence events, and its root is the most recent common ancestor.
3. The *coalescent* of the model is the [[stochastic process|0QH5ENKZM1]] that describes this genealogy backward in time, with $A_n(0) = n$ decreasing to $1$.

Coalescent theory is the study of the law of the genealogy and of the data that mutations on its branches produce.

## Remarks

Example: in the haploid Wright–Fisher model with $N$ genes, two lines coalesce in each generation with probability $1/N$ independently.
So the time back to their common ancestor is geometric with mean $N$ generations.
Non-example: with recombination along a chromosome, a sequence may have two parent sequences.
Then the ancestry of a sequence is not a tree, and clause 2 must be replaced by the ancestral recombination graph.
