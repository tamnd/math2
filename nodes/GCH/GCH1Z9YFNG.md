---
tag: GCH1Z9YFNG
kind: problem
name: Hadamard's maximal determinant problem
msc: [15B34, 05B20, 15A15]
uses: [00KDZRW4C0, CGDN1X32NQ]
about: [00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard%27s_maximal_determinant_problem
same_as:
  wikidata: Q5637579
  wikipedia: Hadamard's maximal determinant problem
history:
  posed_by: "Jacques Hadamard"
  first_stated: "1893"
---

## Problem

Let $n \ge 1$ be an integer, and let $\det$ denote the [[determinant|00KDZRW4C0]].
Find the largest value of $\det A$ over all $n \times n$ matrices $A$ whose entries are all $1$ or $-1$.

## Remarks

[[Hadamard's inequality|CGDN1X32NQ]] gives $\abs{\det A} \le n^{n/2}$ for such matrices.
Equality holds exactly when the rows of $A$ are pairwise orthogonal, that is, when $A$ is a Hadamard matrix.
A Hadamard matrix of order $n$ can exist only for $n = 1$, $n = 2$ or $n$ divisible by $4$.
The Hadamard conjecture, that one exists for every multiple of $4$, is open.
For other orders the maximum is smaller than $n^{n/2}$, and it is known only for some values of $n$.

The determinant of an $n \times n$ matrix with entries $\pm 1$ is divisible by $2^{n-1}$.
The maximum for $n$ equals $2^{n-1}$ times the maximal determinant of an $(n-1) \times (n-1)$ matrix with entries $0$ and $1$.
So the problem is the same as the maximal determinant problem for $0/1$ matrices.

Small cases: for $n = 2$, the maximum is $2$, reached by $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
For $n = 3$, the bound $3^{3/2} \approx 5.2$ and the divisibility by $4$ show that the maximum is at most $4$, and $4$ is reached.

## Explanations

### L1 human

Fill a square grid with the numbers $1$ and $-1$.
The problem asks how large its determinant can be.
Geometrically, it asks how large the volume of a box can be when its edges join the centre of a cube to corners of the cube.
The best case is when all edges are at right angles, but this is possible only for some sizes.
