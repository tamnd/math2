---
tag: CMGKQNMY77
kind: statement
role: lemma
name: Shapley–Folkman lemma
msc: [52A20, 91B50]
uses: [0FQSDC2EQ2, SXS6D87PHE]
about: [SXS6D87PHE, 0FQSDC2EQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Shapley–Folkman_lemma
same_as:
  wikidata: Q3788045
  wikipedia: Shapley–Folkman lemma
---

## Statement

Let $d \ge 1$ and $N \ge 1$, and let $S_1, \dots, S_N$ be subsets of $\R^d$.
Let $S_1 + \cdots + S_N$ be their [[Minkowski sum|SXS6D87PHE]] and let $\operatorname{conv}$ denote the [[convex hull|0FQSDC2EQ2]].
Then every point $x \in \operatorname{conv}(S_1 + \cdots + S_N)$ can be written as $x = x_1 + \cdots + x_N$ with $x_i \in \operatorname{conv}(S_i)$ for each $i$, and with $x_i \in S_i$ for all but at most $d$ indices $i$.

## Remarks

First, $\operatorname{conv}(S_1 + \cdots + S_N) = \operatorname{conv}(S_1) + \cdots + \operatorname{conv}(S_N)$, so $x = \sum_i \sum_j \lambda_{ij} y_{ij}$ with $y_{ij} \in S_i$, $\lambda_{ij} \ge 0$ and $\sum_j \lambda_{ij} = 1$ for each $i$.
Then the point $(x, 1, \dots, 1) \in \R^{d+N}$ is a nonnegative combination of the vectors $(y_{ij}, e_i)$, where $e_i$ is the $i$-th unit vector of $\R^N$.
By the conic form of [[Carathéodory's theorem|0201Q4P2B5]], at most $d + N$ of these vectors are needed.
Each index $i$ needs at least one of them, so at most $d$ indices use two or more, and the other indices use a single point of $S_i$.
Example: $d = 1$ and $S_i = \set{0, 1}$ for all $i$.
The point $x = 2.5$ of $\operatorname{conv}(S_1 + S_2 + S_3) = [0, 3]$ is $1 + 1 + 0.5$, and only one summand is outside its $S_i$.

## Explanations

### L1 human

Adding many sets together makes the sum look almost convex, even if the sets themselves are far from convex.
The lemma makes this precise: a point of the convex hull of the sum can be reached by taking actual points of all but $d$ of the sets.
The number $d$ is the dimension, and it does not grow with the number of sets.

### L2 human

A quantitative consequence, the Shapley–Folkman theorem, bounds the distance between $\operatorname{conv}(S_1 + \cdots + S_N)$ and $S_1 + \cdots + S_N$ in terms of $d$ and the sizes of the $S_i$, independently of $N$.
In mathematical economics this explains why equilibria nearly exist in large markets with nonconvex preferences.
In optimization it bounds the duality gap of separable nonconvex problems with many terms.
