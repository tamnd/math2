---
tag: 0HV1SKWPMS
kind: statement
role: theorem
name: Rouché–Capelli theorem
aliases: [kronecker-capelli-theorem, rouche-frobenius-theorem, rouche-fontene-theorem]
msc: [15A06]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0JTRMBQ1SA, 0YCDZ7N8VD, 0EWQEYRVA8]
proofs: [Q7FMCDJRET, ~403d5028]
sources:
  - url: https://en.wikipedia.org/wiki/Rouché–Capelli_theorem
    locator: lead section
same_as:
  wikidata: Q2071632
  wikipedia: Rouché–Capelli theorem
inventory: [CHV02TF7SA]
---

## Statement

Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $b \in F^m$.
The [[system|0GT4WWGWH2]] $Ax = b$ has a solution if and only if $\rank A = \rank [A \mid b]$, where $[A \mid b]$ is the [[augmented matrix|0T6MWGZSXA]] and $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]].
If a solution exists, then the solution set is an affine subspace of $F^n$ of dimension $n - \rank A$.
In particular, the solution is unique if and only if $\rank A = n$.

## Remarks

If $\rank [A \mid b] = \rank A + 1$, then the system is [[inconsistent|0X6V9B1V10]]; these are the only two cases, because adding one column raises the rank by at most $1$.
The dimension $n - \rank A$ is the number of free variables.

### Why each hypothesis is needed

1. The coefficients must lie in a field, and the solutions are taken in the same field.
Over $\mathbb{Q}$ the equation $2x = 1$ has $\rank A = \rank [A \mid b] = 1$, but it has no solution in $\mathbb{Z}$.
2. The dimension claim needs a solution: an inconsistent system has the empty solution set, which has no dimension as an affine subspace.

### Consequences

1. A system with $\rank A = m$ is consistent for every $b$, because $\rank [A \mid b] \le m$.
2. A square system has a unique solution for every $b$ if and only if $\rank A = n$, that is, $A$ is invertible.
3. Over a field with $q$ elements, a consistent system has $q^{n - \rank A}$ solutions, see [[the theorem on finite fields|~b461276f]].

### Converse

The first claim is an equivalence, and the dimension claim determines the size of the solution set, so the converses are included.

### Generalizations

1. For a linear map $T \colon V \to W$, the equation $T(x) = w$ is solvable if and only if $w \in \im T$.
2. The pivot form of the same facts is [[the existence and uniqueness theorem|BKA191KD1S]]; the two are equivalent because the rank is the number of pivots.
3. The [[Fredholm alternative|4HH8C9V8JQ]] gives a related test for consistency by the solutions of the transposed homogeneous system.

### History

The theorem is named after Rouché and Capelli, and other names honour Kronecker, Fontené and Frobenius.
The name varies by country: Kronecker-Capelli in Russia and Poland, Rouché-Fontené in France, Rouché-Frobenius in Spain and much of Latin America, and Frobenius in the Czech Republic and Slovakia.

## Explanations

### L1 human

The theorem says that a system has a solution exactly when the right side adds no new independent information.
If adding the column $b$ raises the rank, then $b$ is not a combination of the columns of $A$, and no solution exists.
When solutions exist, each unknown without a pivot is free, and it adds one dimension to the solution set.

### L2 human

We use [[the example with a parameter in the right side|~8027660c]]: $x + y + z = 1$, $x + 2y + 3z = 2$, $x + 3y + 5z = a$ over $\R$.

1. Row reduction gives the rows $(1, 1, 1 \mid 1)$, $(0, 1, 2 \mid 1)$ and $(0, 0, 0 \mid a - 3)$.
2. So $\rank A = 2$ for every $a$.
3. If $a \neq 3$, then $\rank [A \mid b] = 3 \neq 2$, so there is no solution.
4. If $a = 3$, then $\rank [A \mid b] = 2$, so there are solutions, and they form a line, since $3 - 2 = 1$.

The typical use is to decide consistency, and the number of free parameters, for a system with a parameter in it.
A trap: comparing $\rank A$ with $n$ instead of with $\rank [A \mid b]$ answers uniqueness, not existence.

### L3 human

The rank condition says that $b$ lies in the column space, since adding $b$ keeps the span exactly when $b$ is already in it.
The dimension claim is the rank-nullity theorem for $x \mapsto Ax$, together with [[the structure of the solution set|~a01a76ca]].
