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

When you intersect two subspaces, the conditions that cut them out add up, so the codimension of the intersection is at most the sum of the two codimensions.
Let $V$ be a vector space over a field $F$, and let $U$ and $W$ be subspaces of $V$ of finite [[codimension|JJCGJ1EGCQ]], that is, with $\dim(V / U)$ and $\dim(V / W)$ finite, where $V / U$ is the [[quotient space|0SVR29SV1V]] and $\dim$ is the [[dimension|05G2G0P224]].
Then the [[intersection|0V33SPH7RR]] $U \cap W$ has finite codimension, and
$$\operatorname{codim}(U \cap W) \le \operatorname{codim} U + \operatorname{codim} W.$$
Equality holds if and only if the [[sum|0RMKABS2S5]] $U + W$ is all of $V$.

## Remarks

### Why each hypothesis is needed

The finiteness of the two codimensions is what makes the conclusion a statement about numbers.
The map in the [[proof|16CSKFCJ6V]] gives the same inequality for infinite cardinals, but then it says little.
In $\R[x]$, the even polynomials $U$ and the odd polynomials $W$ both have infinite codimension, and $U \cap W = \{0\}$ has infinite codimension as well.

The condition $U + W = V$ is needed for equality.
Take $U = W$ to be one line through $0$ in $\R^3$.
Each has codimension $2$, but $U \cap W = U$ has codimension $2$, which is less than $2 + 2 = 4$.
Here $U + W = U$ is only a line, so the two sets of equations repeat each other.

### What it gives you

Apply the inequality $k - 1$ times to $k$ hyperplanes $H_1, \dots, H_k$ of $V$.
Each has codimension $1$, so
$$\operatorname{codim}(H_1 \cap \dots \cap H_k) \le k.$$
For $V = F^n$ this says that a homogeneous system of $k$ linear equations in $n$ unknowns has a solution space of dimension at least $n - k$.
For example, $2$ equations in $5$ unknowns always leave at least $3$ free directions.

Two different hyperplanes $H \ne H'$ meet in a subspace of codimension exactly $2$.
The reason is that $H + H'$ strictly contains $H$, and the only subspace strictly above a hyperplane is $V$ itself, so the equality case applies.

### The exact formula

When $U + W$ also has finite codimension, which always holds here because $U + W \supseteq U$, the inequality sharpens to an equation:
$$\operatorname{codim}(U \cap W) = \operatorname{codim} U + \operatorname{codim} W - \operatorname{codim}(U + W).$$
In finite dimension this is [[Grassmann's formula|06HTJNCMPA]] $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$, rewritten with $\operatorname{codim} X = \dim V - \dim X$ for each of the four subspaces.
The inequality is the case where we drop the last term, and the equality case is the case $\operatorname{codim}(U + W) = 0$.

### Several subspaces

For subspaces $U_1, \dots, U_k$ of finite codimension, the same argument with the map $V \to \prod_i V / U_i$ gives
$$\operatorname{codim} \bigcap_{i=1}^{k} U_i \le \sum_{i=1}^{k} \operatorname{codim} U_i.$$

## History

The inequality is a standard fact of linear algebra, and it is not attached to the name of one author.
In finite dimension it is a rearrangement of Grassmann's formula for the dimensions of a sum and an intersection.

## Explanations

### L1 human

Each subspace of finite codimension is described by a few equations.
The intersection must satisfy all the equations at once, so you need at most the total number of them.
For example, one equation gives a plane in space, a second equation gives a line, and the line misses $1 + 1 = 2$ directions.
You need fewer equations only when some of them repeat information that the others already give.

### L2 human

In $\R^4$, let $U = \{x : x_1 + x_2 + x_3 + x_4 = 0\}$ and $W = \{x : x_1 = x_2\}$, as in [[two hyperplanes in R⁴|7Y08BD14Y6]].

1. Each is the kernel of a nonzero linear form, so each is a hyperplane of codimension $1$.
2. The vector $(1, -1, 0, 0)$ lies in $U$ but not in $W$, so $U \ne W$.
   Then $U + W$ strictly contains the hyperplane $U$, so $U + W = \R^4$.
3. The equality case gives $\operatorname{codim}(U \cap W) = 1 + 1 = 2$, so $\dim(U \cap W) = 4 - 2 = 2$.

Check: $(1, 1, -2, 0)$ and $(1, 1, 0, -2)$ lie in both hyperplanes and are independent, so they form a basis of $U \cap W$.
The typical use is to bound the size of a solution space before you solve anything.
Watch out: you may add codimensions only when $U + W = V$, and with $U = W$ the sum would give $2$ instead of the true value $1$.

### L3 human

The [[proof|16CSKFCJ6V]] uses the linear map $V \to V / U \times V / W$, $v \mapsto (v + U, v + W)$, whose kernel is $U \cap W$.
The equality case says that this map is onto, which is a linear analogue of the Chinese remainder theorem: any two cosets $a + U$ and $b + W$ have a common element exactly when $U + W = V$.
In algebraic geometry the same count appears as the statement that each component of a nonempty subvariety cut out by $k$ equations has codimension at most $k$, a consequence of Krull's height theorem.
