---
tag: P3HMRQN5KT
kind: statement
role: lemma
name: Solutions of a system whose augmented matrix is in reduced row echelon form
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0NNR68BFRY, 0JTRMBQ1SA, 0YCDZ7N8VD, 0BCMGDHZGR]
about: [0WF5AQYTW6]
proofs: [CGHMNHTWGK]
sources:
  - book: isbn:9780321982384
    locator: Section 1.2
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Systems of linear equations
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]], let $R$ be an $m \times n$ matrix over $F$ and let $c \in F^m$.
Assume that the [[augmented matrix|0YCDZ7N8VD]] $[R \mid c]$ is in [[reduced row echelon form|0NNR68BFRY]].

1. If column $n + 1$ of $[R \mid c]$ contains a leading entry, the system $Rx = c$ has no solution.
2. Otherwise, let $p_1 < \dots < p_r$ be the columns of $R$ with a leading entry, and let $f_1 < \dots < f_k$ be the other columns, so $k = n - r$.
3. In case 2, for every $t = (t_1, \dots, t_k) \in F^k$ there is exactly one solution $x$ with $x_{f_l} = t_l$ for all $l$, namely
$$x_{p_i} = c_i - \sum_{l=1}^{k} r_{i f_l}\, t_l \qquad (i = 1, \dots, r).$$
4. In case 2, the map $t \mapsto x$ of part 3 is a bijection from $F^k$ onto the solution set.

## Remarks

### Why each hypothesis is needed

1. The reduced form is needed for the explicit formula. In the echelon form $\left[\begin{array}{cc|c} 1 & 1 & 3 \\ 0 & 1 & 1 \end{array}\right]$, row 1 contains the basic variable $x_2$, and the formula would give $x_1 = 3$ instead of the true $x_1 = 2$.
2. Parts 3 and 4 need the case assumption of part 2. For $\left[\begin{array}{c|c} 0 & 1 \end{array}\right]$ the last column has a leading entry, and the solution set is empty, so it is not the image of $F^1$.

### Consequences

1. A consistent system in RREF has a unique solution exactly when $k = 0$, that is, every column of $R$ has a pivot.
2. Over an infinite field, a consistent system with $k \ge 1$ has infinitely many solutions.
3. Over a field with $q$ elements, a consistent system has exactly $q^k$ solutions, see [[the theorem on finite fields|8QM2Y41P69]].
4. Since every system is equivalent to one in RREF, these facts hold for every system, with $k$ the number of free variables, see [[the existence and uniqueness theorem|BKA191KD1S]].

### Converse

Part 1 has a true converse: if the system has no solution, then column $n + 1$ contains a leading entry, since otherwise part 3 with $t = 0$ gives a solution.

## History

Reading the solution set from the reduced form in this way is the standard method of textbooks such as Lay, Section 1.2.

## Explanations

### L1 human

In the reduced form, every row names one main unknown with coefficient $1$.
The other unknowns in that row are free: we choose them as we like.
Then the row tells us the value of the main unknown.
If a row says $0 = 1$, there is no solution at all.

### L2 human

Take $[R \mid c] = \left[\begin{array}{rrr|r} 1 & 2 & 0 & 5 \\ 0 & 0 & 1 & -1 \end{array}\right]$.

1. The last column has no leading entry, so we are in case 2.
2. The pivot columns are $p_1 = 1$ and $p_2 = 3$, and the free column is $f_1 = 2$.
3. For $t_1 = t$, the formula gives $x_1 = 5 - 2t$ and $x_3 = -1 - 0 \cdot t = -1$.
4. So the solutions are $(5 - 2t, t, -1)$.
5. Check $t = 2$: $(1, 2, -1)$ gives $1 + 4 = 5$ and $x_3 = -1$.

The typical use is the last step of every hand computation.
A trap: the free variables are the columns without pivots, not the variables that happen to be missing from some equation.

### L3 human

Part 4 is a parametrization of the solution set by the affine map $t \mapsto x_0 + Nt$, where $x_0$ is the solution with $t = 0$ and the columns of $N$ span the [[null space|0PHDYNR24D]].
So the lemma computes a basis of the null space and a particular solution at the same time, see [[the parametric form|KQT68YPHD1]].
