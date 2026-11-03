---
tag: WWG959MPXM
kind: definition
name: Parameterized complexity
msc: [68Q27, 68Q25]
defines: X499BMR9MS
uses: [YAVW1XHNFH, T00W8RQT8E, 0AHKWBQSWV, 0BYX1D7C2E]
sources:
  - url: https://en.wikipedia.org/wiki/Parameterized_complexity
---

## Definition

Let $\Sigma$ be a finite alphabet.
A *parameterized problem* is a set $L \subseteq \Sigma^* \times \N$.
In a pair $(x, k)$, the number $k$ is the *parameter*.
The problem $L$ is *fixed-parameter tractable* if there are a computable function $f \colon \N \to \N$, a constant $c$ and an algorithm with these properties.
On input $(x, k)$ it decides whether $(x, k) \in L$.
It runs in time at most $f(k) \cdot \abs{x}^c$.

The class of fixed-parameter tractable problems is called FPT.
*Parameterized complexity* is the study of parameterized problems and of classes such as FPT, the W-hierarchy and XP.

## Remarks

Example: [[vertex cover|0AHKWBQSWV]], with parameter the size $k$ of the cover, is in FPT.
Pick any edge $\set{u, v}$; one of $u$ and $v$ is in the cover.
Branch on the two choices and delete the chosen vertex, with parameter $k - 1$.
The search tree has at most $2^k$ leaves, so the time is $O(2^k \cdot \abs{x})$.

Non-example: the obvious algorithm for $k$-[[clique|0BYX1D7C2E]] tries all $k$-sets of vertices and takes time about $n^k$.
Here the exponent of $n$ grows with $k$, so the bound has not the form $f(k) \cdot n^c$.
The problem is W[1]-complete, and it is believed not to be in FPT.

The class XP consists of the problems solvable in time $\abs{x}^{f(k)}$ for some computable function $f$; it contains FPT.
