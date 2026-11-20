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

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ matrix over $F$, with [[transpose|09DXWYRD43]] $A^{\top}$.

1. (Solvability) For $b \in F^m$, the [[system|0GT4WWGWH2]] $Ax = b$ has a solution if and only if $y^{\top} b = 0$ for every $y \in F^m$ with $A^{\top} y = 0$.
2. (Alternative form) For each $b \in F^m$, exactly one of the following holds:
   (a) $Ax = b$ has a solution $x \in F^n$;
   (b) there is $y \in F^m$ with $A^{\top} y = 0$ and $y^{\top} b \ne 0$.
3. (Square case) Let $m = n$. Then exactly one of the following two cases holds.
   (a) For every $b \in F^n$, the system $Ax = b$ has exactly one solution $x \in F^n$.
   (b) The [[homogeneous system|04KGXJG1A2]] $Ax = 0$ has a solution $x \ne 0$.
   Case (b) holds if and only if $A^{\top} y = 0$ has a solution $y \ne 0$, and both solution spaces have the same dimension $n - \rank A$.
   In case (b), $Ax = b$ is solvable exactly for the $b$ in part 1.

## Remarks

### Why each hypothesis is needed

- The test uses the null space of $A^{\top}$, not the null space of $A$. For $A = \begin{pmatrix} 1 & 2 \\ 3 & 6 \end{pmatrix}$, the null space of $A$ gives a wrong test. This is the trap in the [[worked example|V8XEQX465M]].
- Part 3 needs a square matrix. For the $1 \times 2$ matrix $A = \begin{pmatrix} 1 & 0 \end{pmatrix}$, every $b$ is reached, but $Ax = 0$ has the solution $x = (0, 1) \ne 0$. So existence for all $b$ does not give uniqueness.
- The space must be finite-dimensional. On the space of sequences, the shift $(x_1, x_2, \dots) \mapsto (0, x_1, x_2, \dots)$ is injective but not surjective.

### Consequences

- For a square matrix, uniqueness of solutions implies existence for every $b$, and existence for every $b$ implies uniqueness.
- The number of independent conditions on $b$ is $\dim \operatorname{Null}(A^{\top}) = m - \rank A$.
- Over $\R$, part 1 says $\operatorname{Col}(A) = \operatorname{Null}(A^{\top})^{\perp}$, by the [[theorem on the orthogonal complement of the column space|J4SZVFBHS5]].

### Converse

Part 1 is an "if and only if".
Part 3 states a dichotomy, so each case is the negation of the other.

### Generalizations

- For $T \colon V \to W$ between finite-dimensional spaces, $T(x) = w$ is solvable if and only if $\varphi(w) = 0$ for every $\varphi \in W^*$ with $T^* \varphi = 0$. Here $T^*$ is the [[dual map|0AZ5ARP287]]; this form belongs to the duality sub-area.
- Fredholm proved the alternative for integral equations $x - Kx = y$. In functional analysis, it holds for $I - K$ with $K$ a compact operator on a Banach space.

## History

The name comes from Fredholm's theory of integral equations, from about 1900, where the same alternative holds for compact perturbations of the identity.

## Explanations

### L1 human

A square linear system behaves in one of two ways.
Either every right side has one and only one solution, or the homogeneous system has a nonzero solution.
In the second case, a simple test tells which right sides work.
The number $y^{\top} b$ must be $0$ for every solution $y$ of the transposed system $A^{\top} y = 0$.

### L2 human

Each solution $y$ of $A^{\top} y = 0$ is a linear relation among the rows of $A$.
If $Ax = b$, the same relation must hold among the entries of $b$.
The theorem says that these relations are the only obstructions.
In dimensions: the column space has dimension $r$, and the conditions cut out a space of dimension $m - (m - r) = r$.

### L3 human

Part 1 says that the column space of $A$ is the annihilator of the null space of $A^{\top}$, when $F^m$ is identified with its dual by the standard basis.
It is the finite-dimensional model for the Fredholm alternative for integral equations and for elliptic boundary value problems.
There the index $\dim \ker T - \dim \operatorname{coker} T$ is $0$, as it is for every square matrix.
