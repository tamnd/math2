---
tag: P4JG9DJ2HH
kind: statement
role: proposition
name: Dimension criterion for a direct sum
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0XYYT5KNTX]
uses: [041JTZCK9Q, 018W3V3TCT, 05G2G0P224, 0V33SPH7RR]
sources:
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
---

## Statement

In a finite-dimensional space, two subspaces split the space as soon as their dimensions add up correctly and one of the two usual conditions holds.
Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, and let $U$ and $W$ be subspaces of $V$.
Then the following conditions are equivalent.

1. $V = U \oplus W$.
2. $U \cap W = \{0\}$ and $\dim U + \dim W = \dim V$.
3. $U + W = V$ and $\dim U + \dim W = \dim V$.

Here $\dim$ is the [[dimension|05G2G0P224]].

## Remarks

### Why the dimension count is needed

Without the count, neither half of the test is enough.
The $x$-axis and the $y$-axis in $\R^3$ meet only in $0$, but $1 + 1 \ne 3$, and their sum is only the $xy$-plane; see [[the two axes in space|PAJHW0002P]].
The $xy$-plane and the $yz$-plane have sum $\R^3$, but $2 + 2 \ne 3$, and they share the $y$-axis.
With the count, either half implies the other one.

### Why finite dimension is needed

In infinite dimension the count of dimensions carries too little information.
In $F[x]$, let $U$ be spanned by $x^2, x^4, x^6, \dots$ and $W$ by $x, x^3, x^5, \dots$.
Then $U \cap W = \{0\}$, since a polynomial with only even powers and only odd powers is zero.
Both $U$ and $W$ have countably infinite dimension, and so does $F[x]$, so the count holds as an equation of cardinals.
But the constant $1$ is not in $U + W$, so condition 2 holds and condition 1 fails.

### What it gives you

If $V = U \oplus W$, then $\dim W = \dim V - \dim U$, so all [[complements|0M83V17KHX]] of $U$ have the same dimension.
A line and a plane through $0$ in $\R^3$ split the space exactly when the line does not lie in the plane, since $1 + 2 = 3$ and only the intersection is left to check.
For two subspaces of $F^n$ of dimensions $k$ and $n - k$, one check is enough: either a zero intersection or a sum equal to $F^n$.

### Generalizations

For subspaces $U_1, \dots, U_k$ of a finite-dimensional space, the sum is direct if and only if
$$\dim(U_1 + \cdots + U_k) = \dim U_1 + \cdots + \dim U_k.$$
For two subspaces, the criterion is a special case of [[Grassmann's formula|06HTJNCMPA]],
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W,$$
since the formula shows that $U \cap W = \{0\}$ and $U + W = V$ are the same condition once $\dim U + \dim W = \dim V$.

## History

The criterion follows at once from the dimension formula for a sum and an intersection of subspaces, which is named after Hermann Grassmann.

## Explanations

### L1 human

In a space of dimension $n$, two subspaces split the space when they share only the zero vector and their dimensions add up to $n$.
In ordinary space, a line and a plane have dimensions $1$ and $2$, which add up to $3$.
So the line and the plane split space exactly when the line pokes out of the plane.
If the line lies inside the plane, they share more than the origin and the split fails.

### L2 human

Here is a typical use: test $U = \operatorname{span}\{(1, 0, 1)\}$ and $W = \{(x, y, z) : x = z\}$ in $\R^3$.
The dimensions are $1$ and $2$, and $1 + 2 = 3 = \dim \R^3$, so only the intersection is left.
The vector $(1, 0, 1)$ satisfies $x = z$, so $U \subseteq W$ and $U \cap W = U \ne \{0\}$.
So condition 2 fails, and $\R^3 \ne U \oplus W$.
Now change $U$ to $\operatorname{span}\{(1, 0, 0)\}$.
A vector $(t, 0, 0)$ satisfies $x = z$ only for $t = 0$, so $U \cap W = \{0\}$, and the criterion gives $\R^3 = U \oplus W$ with no further work.
Watch out: the count of dimensions in the first step never decides the question alone.

### L3 human

The criterion is an instance of a general principle: an injective linear map between spaces of the same finite dimension is bijective.
It is applied to the addition map $U \times W \to V$, whose source has dimension $\dim U + \dim W$ and whose kernel is zero exactly when $U \cap W = \{0\}$.
The infinite-dimensional failure above is the failure of this principle, in the same way as the shift $x^n \mapsto x^{n+1}$ on $F[x]$ is injective and not surjective.
