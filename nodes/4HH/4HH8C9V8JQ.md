---
tag: 4HH8C9V8JQ
kind: statement
role: theorem
name: Fredholm alternative
aliases: [fredholm-alternative-for-matrices]
msc: ["15A06", "47A53"]
topics: [S6559D61BP]
audience: ug1
about: [0GT4WWGWH2, 04KGXJG1A2]
uses: [0JTRMBQ1SA, 06JT7KDHXM, 0W809K6AW0, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_alternative
    locator: Linear algebra
---

## Statement

A linear system $Ax = b$ is solvable exactly when $b$ passes the tests given by the solutions of the transposed system $A^{\top} y = 0$.
Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ matrix over $F$, with [[transpose|09DXWYRD43]] $A^{\top}$.

1. (Solvability) For $b \in F^m$, the [[system|0GT4WWGWH2]] $Ax = b$ has a solution if and only if $y^{\top} b = 0$ for every $y \in F^m$ with $A^{\top} y = 0$.
2. (Alternative form) For each $b \in F^m$, exactly one of the following holds.
   (a) The system $Ax = b$ has a solution $x \in F^n$.
   (b) There is $y \in F^m$ with $A^{\top} y = 0$ and $y^{\top} b \ne 0$.
3. (Square case) Let $m = n$.
   Then exactly one of the following two cases holds.
   (a) For every $b \in F^n$, the system $Ax = b$ has exactly one solution $x \in F^n$.
   (b) The [[homogeneous system|04KGXJG1A2]] $Ax = 0$ has a solution $x \ne 0$.
   Case (b) holds if and only if $A^{\top} y = 0$ has a solution $y \ne 0$, and both solution spaces have the same dimension $n - \rank A$.
   In case (b), $Ax = b$ is solvable exactly for the $b$ described in part 1.

## Remarks

### What it gives you

For a square matrix, uniqueness of solutions implies existence for every $b$, and existence for every $b$ implies uniqueness.
In general, the number of independent conditions on $b$ is $\dim \operatorname{Null}(A^{\top}) = m - \rank A$.
Over $\mathbb{R}$, part 1 says that $b$ lies in the column space of $A$ if and only if $b$ is orthogonal to $\operatorname{Null}(A^{\top})$.
In symbols, $\operatorname{Col}(A) = \operatorname{Null}(A^{\top})^{\perp}$, the [[theorem on the orthogonal complement of the column space|J4SZVFBHS5]].
For $A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}$, the null space of $A^{\top}$ is spanned by $(-3, 1)$, so $Ax = b$ is solvable exactly when $b_2 = 3b_1$.

### Why each hypothesis is needed

The test uses the null space of $A^{\top}$, not the null space of $A$.
For the matrix above, the null space of $A$ is spanned by $(-2, 1)$, and the test $b_2 = 2b_1$ that it suggests is wrong, as the [[worked example|V8XEQX465M]] shows.

Part 3 needs a square matrix.
For the $1 \times 2$ matrix $A = \begin{pmatrix} 1 & 0 \end{pmatrix}$, every $b$ is reached, but $Ax = 0$ has the solution $x = (0, 1) \ne 0$.
So existence for all $b$ does not give uniqueness.

Part 3 also needs finite dimensions, which a matrix provides.
On the space of sequences, the shift $(x_1, x_2, \dots) \mapsto (0, x_1, x_2, \dots)$ is injective but not surjective.

### The converse

Part 1 is already an equivalence.
Part 3 states a dichotomy, so each case is the negation of the other.

### Generalizations

For a linear map $T \colon V \to W$ between finite-dimensional spaces, $T(x) = w$ is solvable if and only if $\varphi(w) = 0$ for every $\varphi \in W^*$ with $T^* \varphi = 0$.
Here $T^*$ is the [[dual map|0AZ5ARP287]].
In functional analysis the alternative holds for $I - K$ with $K$ a compact operator on a Banach space.
The [[proof|Z04Y9W8CSY]] compares the dimensions of the column space and of the space cut out by the tests.

## History

Fredholm studied integral equations of the form $x - Kx = y$ in a paper of 1903, and the name of the alternative comes from that work.

## Explanations

### L1 human

A square linear system behaves in one of two ways.
Either every right side has one and only one solution, or the homogeneous system has a nonzero solution.
In the second case, a test tells which right sides work.
The number $y^{\top} b$ must be $0$ for every solution $y$ of the transposed system $A^{\top} y = 0$.

### L2 human

Each solution $y$ of $A^{\top} y = 0$ is a linear relation among the rows of $A$.
If $Ax = b$, the same relation must hold among the entries of $b$.
The theorem says that these relations are the only obstructions.
In dimensions, the column space has dimension $r = \rank A$, and the $m - r$ independent conditions cut out a space of dimension $m - (m - r) = r$.

### L3 human

Part 1 says that the column space of $A$ is the annihilator of the null space of $A^{\top}$, when $F^m$ is identified with its dual by the standard basis.
It is the finite-dimensional model for the alternative for compact perturbations $I - K$ of the identity.
There the index $\dim \ker T - \dim \operatorname{coker} T$ is $0$, as it is for every square matrix, where both numbers equal $n - \rank A$.
