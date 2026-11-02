---
tag: QYQ983Z0BK
kind: statement
role: theorem
name: Feichtinger conjecture
msc: [42C15, 46C05, 46L05]
uses: [HM2HHE3J51, ZYDYD7FB1Z]
about: [ZYDYD7FB1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Kadison%E2%80%93Singer_problem
---

## Statement

Let $H$ be a separable [[Hilbert space|HM2HHE3J51]], and let $(f_i)_{i \in \N}$ be a frame of $H$ with $\inf_{i} \norm{f_i} > 0$.
That is, there are constants $0 < A \le B < \infty$ with $A \norm{f}^2 \le \sum_{i} \abs{\ip{f}{f_i}}^2 \le B \norm{f}^2$ for all $f \in H$.
Then $\N$ is the union of finitely many sets $I_1, \dots, I_r$ such that each family $(f_i)_{i \in I_j}$ is a Riesz sequence.
Here a Riesz sequence is a family that is a [[Riesz basis|ZYDYD7FB1Z]] of its closed linear span.

## Remarks

The question is due to Hans Feichtinger, who came to it from time–frequency analysis.
In the 2000s Peter Casazza and coauthors showed that it is equivalent to the [[Kadison–Singer problem|C8TTRMVVS7]].
The positive solution of the Kadison–Singer problem by Marcus, Spielman and Srivastava therefore proves the statement.
The hypothesis $\inf_i \norm{f_i} > 0$ is necessary: a Riesz sequence has norms bounded below, so a frame containing vectors of norm tending to $0$ cannot be split into finitely many Riesz sequences.

Example: the union of two orthonormal bases $(e_n)$ and $(e'_n)$ of $H$ is a frame with $\norm{f_i} = 1$; it splits into the two Riesz sequences $(e_n)$ and $(e'_n)$.

## Explanations

### L1 human

A frame is a redundant spanning family in which every vector can be recovered stably.
A Riesz sequence is a family that is as good as an orthonormal basis of the space it spans, with no redundancy.
The statement says that any frame whose vectors do not shrink to zero can be cut into finitely many pieces, each of them free of redundancy in this strong sense.

### L2 human

The statement lets one replace a redundant frame by finitely many non-redundant pieces, each of which behaves like an orthonormal basis of its span.
The equivalence with the Kadison–Singer problem passes through Anderson's paving conjecture and Weaver's discrepancy conjecture.
The proof of Marcus, Spielman and Srivastava works with sums of random rank-one matrices and interlacing families of polynomials.
