---
tag: B6KFVB1H5F
kind: statement
role: theorem
name: The image of a linear map is a subspace spanned by the images of a spanning set
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0WSFKKT6FF]
uses: [0JB228DCWB, 0EPTJA5QV4, 0BJKVF90Z6, 0HR573CHNM, 0F0RPPJ2TT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9780134860244
    locator: Section 2.1
  - book: isbn:9780321982384
    locator: Section 4.2
---

## Statement

The outputs of a linear map form a subspace, and the outputs of a spanning set already span it.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a linear map.

1. The [[image|0JB228DCWB]] $\im T$ is a [[subspace|0EPTJA5QV4]] of $W$.
2. If a set $S$ [[spans|0BJKVF90Z6]] $V$, then the set $T(S) = \{T(s) : s \in S\}$ spans $\im T$, that is, $\im T = \operatorname{span} T(S)$.
3. For an $m \times n$ matrix $A$ over $F$, the image of $x \mapsto Ax$ is the [[column space|0F0RPPJ2TT]] of $A$.

## Remarks

### Why the hypotheses are needed

Linearity is needed for part 1.
The set of values of $x \mapsto (x, x^2)$ is a parabola, and [[the parabola is not a subspace|YF3Y7THM81]].
Part 2 needs a set that spans all of $V$.
If $S$ spans only a subspace $U$ of $V$, then $T(S)$ spans $T(U)$, which can be smaller than $\im T$.
For the projection $(x, y) \mapsto (x, 0)$ and $S = \{(0, 1)\}$, the set $T(S) = \{(0, 0)\}$ spans only $\{0\}$, while the image is the $x$-axis.

### What it gives you

If $V$ is finite-dimensional, then $\im T$ is finite-dimensional and $\dim \im T \le \dim V$, because a spanning set of $\dim V$ vectors maps to a spanning set of at most $\dim V$ vectors.
So a linear map $\R^2 \to \R^3$ is never surjective.
Part 3 says that the system $Ax = b$ is solvable exactly when $b$ is a combination of the columns of $A$.
Watch out: the images of a basis span the image, but they can be dependent, so they need not be a basis of it.

### The converse

Every subspace $U$ of $W$ is the image of some linear map, for example of the inclusion $U \to W$.
So "image of a linear map into $W$" and "subspace of $W$" describe the same sets.

### Generalizations

For a subspace $U \subseteq V$, the set $T(U)$ is a subspace of $W$, spanned by the images of a spanning set of $U$.
For modules over a ring, the image of a homomorphism is a submodule, with the same proof.

## History

Part 3 together with its consequence for $Ax = b$ is usually stated with ranks, as the Rouché-Capelli theorem of the 19th century.
In different countries the theorem also carries the names of Kronecker, Frobenius and Fontené.

## Explanations

### L1 human

The outputs of a linear map form a subspace.
To describe all outputs, it is enough to know the outputs of a spanning set.
For a matrix, these outputs are its columns.

### L2 human

Let $T \colon \R^2 \to \R^3$ be $T(x, y) = (x, y, x + y)$.

1. The standard vectors $e_1, e_2$ span $\R^2$.
2. Their images are $T(e_1) = (1, 0, 1)$ and $T(e_2) = (0, 1, 1)$.
3. So $\im T$ is the plane spanned by $(1, 0, 1)$ and $(0, 1, 1)$, which is $\{(a, b, c) : c = a + b\}$.

Check: $T(2, 3) = (2, 3, 5) = 2\,(1, 0, 1) + 3\,(0, 1, 1)$, and $5 = 2 + 3$.
