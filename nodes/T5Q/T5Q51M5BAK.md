---
tag: T5Q51M5BAK
kind: statement
role: proposition
name: Basic properties of the orthogonal complement
msc: [15A63, 46C05]
topics: [8GQVME4SZZ]
audience: ug1
about: [0XJXTBCB2T]
uses: [079D68S3AW, 0VGSYBWHV2, 0DTY8B9HMS, 0RMKABS2S5]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 6C
  - book: isbn:9780321982384
    locator: Section 6.1
---

## Statement

The orthogonal complement is always a subspace, it only sees the span of a set, it reverses inclusions, and it turns sums into intersections.
Let $V$ be an inner product space over $\R$ or $\C$.
For a subset $S$ of $V$, let $S^\perp$ be its [[orthogonal complement|079D68S3AW]].
Let $S$ and $T$ be subsets of $V$, and let $U$ and $W$ be subspaces of $V$.
Then:

1. $S^\perp$ is a subspace of $V$.
2. If $S \subseteq T$, then $T^\perp \subseteq S^\perp$.
3. $S^\perp = (\operatorname{span} S)^\perp$, where $\operatorname{span} S$ is the [[span|0DTY8B9HMS]] of $S$.
4. $U \cap U^\perp = \{0\}$.
5. $(U + W)^\perp = U^\perp \cap W^\perp$, where $U + W$ is the [[sum of subspaces|0RMKABS2S5]].
6. $\{0\}^\perp = V$ and $V^\perp = \{0\}$.

The [[proof|CD6PQGCSWG]] uses only the axioms of an inner product.

## Remarks

### Why each hypothesis is needed

Parts 1, 2, 3 and 5 use only linearity, so they hold for any bilinear or sesquilinear form, in any dimension.
Parts 4 and 6 are different, because they need positivity.
For the symmetric form $\langle x, y \rangle = x_1 y_1 - x_2 y_2$ on $\R^2$, the vector $(1, 1)$ has $\langle (1, 1), (1, 1) \rangle = 1 - 1 = 0$.
So the line $U = \R(1, 1)$ lies inside its own complement, and $U \cap U^\perp = U \ne \{0\}$, so part 4 fails.

In part 6 the claim $V^\perp = \{0\}$ fails for the form $\langle x, y \rangle = x_1 y_1$ on $\R^2$, which is not positive.
There $(0, 1)$ is orthogonal to every vector, so $V^\perp = \R(0, 1)$.

Part 5 is stated for subspaces, because $U + W$ needs subspaces.
For subsets the same proof gives $(S \cup T)^\perp = S^\perp \cap T^\perp$.

### What it gives you

Part 3 is the rule that makes complements computable.
To find $U^\perp$, test a spanning set of $U$ and nothing else.
In $\R^n$ this makes $U^\perp$ the null space of the matrix whose rows span $U$, as in [[the plane example|38S0WYCSA3]].

Parts 5 and 3 together give $(U_1 + \dots + U_k)^\perp = U_1^\perp \cap \dots \cap U_k^\perp$ for any finite number of subspaces, by induction on $k$.
For example, with $U = \R(1, 0, 0)$ and $W = \R(0, 1, 0)$ in $\R^3$, the complements are the planes $x_1 = 0$ and $x_2 = 0$.
They meet in the $x_3$-axis, and that axis is also the complement of the plane $U + W = \{x_3 = 0\}$.
[[The sum rule for two lines in R3|1JKAGB6W4Z]] checks part 5 with a less symmetric pair.

### The converse

The converse of part 2 is false for subsets.
In $\R^2$ the sets $S = \{(1, 0)\}$ and $T = \{(2, 0)\}$ have the same complement, the $y$-axis, but neither set contains the other.
For subspaces of a finite-dimensional space the converse holds: $W^\perp \subseteq U^\perp$ implies $U \subseteq W$.
To see this, apply part 2 to $W^\perp \subseteq U^\perp$ to get $(U^\perp)^\perp \subseteq (W^\perp)^\perp$, and then use the [[double orthogonal complement|0PXN9G4MX1]] on both sides.

### Generalizations

In finite dimension the dual rule $(U \cap W)^\perp = U^\perp + W^\perp$ also holds.
Apply part 5 to the subspaces $U^\perp$ and $W^\perp$ to get $(U^\perp + W^\perp)^\perp = (U^\perp)^\perp \cap (W^\perp)^\perp = U \cap W$.
Now take complements of both sides and use the double complement once more.
In an infinite-dimensional Hilbert space the dual rule can fail, because $U^\perp + W^\perp$ need not be closed.

## Explanations

### L1 human

The vectors perpendicular to a set always form a flat space through the origin, even if the set itself is not flat.
Adding more vectors to the set makes the complement smaller, because there are more conditions to meet.
A vector that is perpendicular to two lines is also perpendicular to every sum of vectors from those lines.

### L2 human

The typical use is to replace a subspace by a spanning set before a computation.
Take $U = \R(1, 1, 0)$ and $W = \R(0, 0, 1)$ in $\R^3$, and find $(U + W)^\perp$.
By part 5 we intersect the two complements, which are the planes
$$x_1 + x_2 = 0 \quad \text{and} \quad x_3 = 0.$$
Their intersection is the line $\R(1, -1, 0)$.
Check: $(1, -1, 0)$ is orthogonal to $(1, 1, 0)$ and to $(0, 0, 1)$, so it is orthogonal to the whole plane $U + W$.
Watch out: part 4 depends on positivity, so do not use it for the Minkowski form of relativity, where light-like vectors are orthogonal to themselves.

### L3 human

Parts 2 and 3, together with the symmetry of orthogonality, say that $S \mapsto S^\perp$ reverses order and satisfies $S \subseteq (S^\perp)^\perp$.
Such a map, paired with itself, is a Galois connection on the subsets of $V$.
Part 5 says that this map sends joins of subspaces to meets.
The closed elements of the connection are the subspaces with $(U^\perp)^\perp = U$: all subspaces in finite dimension, and the closed subspaces in a Hilbert space.
