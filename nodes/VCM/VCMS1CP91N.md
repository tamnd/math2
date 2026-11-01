---
tag: VCMS1CP91N
kind: statement
role: theorem
name: Hook length formula
msc: [05A17, "05E10", 20C30]
uses: [Q6TH9PH2R7, 096AHMB3P4, 0JV30XN73Z]
about: [Q6TH9PH2R7]
sources:
  - url: https://en.wikipedia.org/wiki/Hook_length_formula
same_as:
  wikidata: Q17163411
  wikipedia: Hook length formula
---

## Statement

Let $\lambda$ be a [[partition|0JV30XN73Z]] of $n$ with [[Young diagram|096AHMB3P4]] $D$.
For a cell $c$ of $D$, let $a(c)$ be the number of cells of $D$ to the right of $c$ in its row.
Let $l(c)$ be the number of cells of $D$ below $c$ in its column.
The hook length of $c$ is $h(c) = a(c) + l(c) + 1$.
Let $f^\lambda$ be the number of standard [[Young tableaux|Q6TH9PH2R7]] of shape $\lambda$.
Then
$$f^\lambda = \frac{n!}{\prod_{c \in D} h(c)}.$$

## Remarks

The formula is due to Frame, Robinson and Thrall.
Let $F(\lambda)$ denote the right-hand side of the formula.
A short proof by Greene, Nijenhuis and Wilf uses a random "hook walk" inside the diagram.
They show that the walk ends at each corner $c$ with probability $F(\lambda \setminus c) / F(\lambda)$, so these ratios add up to $1$.
The largest entry $n$ of a standard tableau sits in a corner.
So $f^\lambda$ is the sum of $f^{\lambda \setminus c}$ over the corners $c$, and $F$ satisfies the same recursion; induction on $n$ finishes the proof.

Example: for $\lambda = (2, 2)$ the hook lengths are $3, 2$ in the first row and $2, 1$ in the second row.
The formula gives $4! / (3 \cdot 2 \cdot 2 \cdot 1) = 2$, and indeed the standard tableaux are $\begin{smallmatrix} 1 & 2 \\ 3 & 4 \end{smallmatrix}$ and $\begin{smallmatrix} 1 & 3 \\ 2 & 4 \end{smallmatrix}$.
For $\lambda = (n)$ the hook lengths are $n, n-1, \dots, 1$ and $f^\lambda = 1$.

## Explanations

### L1 human

The formula counts the ways to fill a Young diagram with $1, \dots, n$ so that rows and columns increase.
Each box has a hook: the box itself, the boxes to its right and the boxes below it.
Divide $n!$ by the product of all hook sizes and the answer is the count.
It is surprising that such a simple product gives an exact count.

### L2 human

The number $f^\lambda$ is the dimension of the irreducible representation of the symmetric group $S_n$ indexed by $\lambda$.
So the hook length formula computes these dimensions directly.
Together with the [[Robinson–Schensted correspondence|1SCF8X47G1]], which gives $\sum_{\lambda} (f^\lambda)^2 = n!$, it is a basic tool of the representation theory of $S_n$.
There are versions for shifted shapes and for trees, and a $q$-analogue that counts tableaux by a statistic.
