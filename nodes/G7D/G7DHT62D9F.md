---
tag: G7DHT62D9F
kind: statement
role: proposition
name: Codimension of an intersection of subspaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug2
about: [JJCGJ1EGCQ]
uses: [0SVR29SV1V, 0RMKABS2S5, 0V33SPH7RR, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Codimension
    locator: Additivity of codimension and dimension counting
---

## Statement

Let $V$ be a vector space over a field $F$, and let $U$ and $W$ be subspaces of $V$ of finite codimension, that is, with $\dim(V / U)$ and $\dim(V / W)$ finite.
Then the [[intersection|0V33SPH7RR]] $U \cap W$ has finite codimension, and
$$\operatorname{codim}(U \cap W) \le \operatorname{codim} U + \operatorname{codim} W,$$
where $\operatorname{codim} X = \dim(V / X)$ is the [[dimension|05G2G0P224]] of the [[quotient space|0SVR29SV1V]].
Equality holds if and only if the [[sum|0RMKABS2S5]] is $U + W = V$.

## Remarks

### Why each hypothesis is needed

- Finite codimension is needed for the inequality to carry information. In $\R[x]$, the even polynomials $U$ and the odd polynomials $W$ have infinite codimension, and $U \cap W = \{0\}$ has infinite codimension too.
- The equality case needs $U + W = V$. Two lines $U = W$ in $\R^3$ have codimension $2$ each, and $U \cap W = U$ has codimension $2 < 4$.

### Consequences

- The intersection of $k$ hyperplanes has codimension at most $k$. So $k$ linear equations on $F^n$ have a solution space of dimension at least $n - k$.
- In finite dimension, the statement is equivalent to [[Grassmann's formula|06HTJNCMPA]]: $\operatorname{codim}(U \cap W) = \operatorname{codim} U + \operatorname{codim} W - \operatorname{codim}(U + W)$.
- Two different hyperplanes meet in a subspace of codimension exactly $2$, since their sum is $V$.

### Converse

The equality case is already a two-way statement: equality of codimensions forces $U + W = V$.

## History

Counting conditions by codimension is classical in projective geometry, where two hyperplanes of a projective space meet in a subspace of codimension $2$.
The form with quotient spaces is standard in functional analysis, where it applies to closed subspaces of finite codimension.

## Explanations

### L1 human

Each subspace of finite codimension is cut out by a few equations.
The intersection is cut out by all the equations together, so it needs at most the total number.
Fewer are needed exactly when some equations repeat information, which happens when $U + W$ is smaller than $V$.

### L2 human

In $\R^4$, let $U = \{x_1 + x_2 + x_3 + x_4 = 0\}$ and $W = \{x_1 = x_2\}$, as in [[hyperplanes in R⁴|7Y08BD14Y6]].

1. Each is a hyperplane, of codimension $1$.
2. $U \ne W$, since $(1, -1, 0, 0) \in U$ but not in $W$. So $U + W$ is larger than $U$, and $U + W = \R^4$.
3. The statement gives $\operatorname{codim}(U \cap W) = 1 + 1 = 2$, so $\dim(U \cap W) = 2$.

The trap is to add codimensions when $U + W \ne V$, for instance when $U = W$.

### L3 human

The [[proof|16CSKFCJ6V]] uses the map $V \to V / U \times V / W$, $v \mapsto (v + U, v + W)$, whose kernel is $U \cap W$.
The equality case says that this map is surjective, which is the linear analogue of the Chinese remainder theorem.
For several subspaces, the map $V \to \prod_i V / U_i$ gives $\operatorname{codim} \bigcap_i U_i \le \sum_i \operatorname{codim} U_i$.
