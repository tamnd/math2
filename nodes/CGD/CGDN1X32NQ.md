---
tag: CGDN1X32NQ
kind: statement
role: theorem
name: Hadamard's inequality
msc: [15A45, 15A15]
uses: [00KDZRW4C0, 0V2WP9B1MF, 0Y2X7P2WB7, 0VT6P0GNQR, 01MMVW8CKC]
about: [00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard%27s_inequality
same_as:
  wikidata: Q1365087
  wikipedia: Hadamard's inequality
---

## Statement

Let $A$ be an $n \times n$ complex matrix with columns $v_1, \dots, v_n \in \C^n$.
Let $\norm{v}$ denote the Euclidean [[norm|0V2WP9B1MF]] of $v \in \C^n$.
Then
$$\abs{\det A} \le \prod_{i=1}^{n} \norm{v_i},$$
where $\det$ is the [[determinant|00KDZRW4C0]].
Equality holds if and only if some $v_i$ is $0$ or the vectors $v_1, \dots, v_n$ are pairwise [[orthogonal|0Y2X7P2WB7]].

## Remarks

If the columns are linearly dependent, the left side is $0$.
Otherwise the [[Gram–Schmidt process|0VT6P0GNQR]] gives $A = QR$ with $Q$ unitary and $R$ upper triangular with diagonal entries $r_{ii}$.
Then $\abs{\det A} = \prod_i \abs{r_{ii}}$, and $\abs{r_{ii}}$ is the distance from $v_i$ to the span of $v_1, \dots, v_{i-1}$, so $\abs{r_{ii}} \le \norm{v_i}$.

Example: for $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, the columns are orthogonal with norm $\sqrt{2}$, and indeed $\abs{\det A} = 2 = \sqrt{2} \cdot \sqrt{2}$.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the bound is $1 \cdot \sqrt{2}$, while $\det A = 1$.

An equivalent form: if $P$ is an $n \times n$ [[positive semidefinite|01MMVW8CKC]] matrix, then $\det P \le \prod_i p_{ii}$.
Apply it to $P = A^* A$, whose diagonal entries are $\norm{v_i}^2$.
If all entries of $A$ satisfy $\abs{a_{ij}} \le 1$, the inequality gives $\abs{\det A} \le n^{n/2}$, which is the starting point of [[Hadamard's maximal determinant problem|GCH1Z9YFNG]].

## Explanations

### L1 human

The absolute value of a determinant is the volume of the box spanned by the columns.
A box with given edge lengths has the largest volume when its edges are at right angles.
So the volume is at most the product of the edge lengths, with equality for a rectangular box.

### L2 human

The inequality bounds the size of a determinant without computing it.
It is used to bound the size of integer determinants in algorithms, and it gives the bound $n^{n/2}$ for matrices with entries of absolute value at most $1$.
The positive semidefinite form is a special case of Fischer's inequality for block matrices.
