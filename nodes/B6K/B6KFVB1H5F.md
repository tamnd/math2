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

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a linear map.

1. The [[image|0JB228DCWB]] $\im T$ is a [[subspace|0EPTJA5QV4]] of $W$.
2. If a set $S$ [[spans|0BJKVF90Z6]] $V$, then the set $T(S) = \{T(s) : s \in S\}$ spans $\im T$. That is, $\im T = \operatorname{span} T(S)$.
3. For an $m \times n$ matrix $A$ over $F$, the image of $x \mapsto Ax$ is the [[column space|0F0RPPJ2TT]] of $A$.

## Remarks

### Why each hypothesis is needed

- Linearity is needed for part 1. The [[image of $x \mapsto (x, x^2)$|YF3Y7THM81]] is a parabola, which is not a subspace.
- Part 2 needs a spanning set of all of $V$. The image of a smaller set spans only the image of its span.

### Consequences

- If $V$ is finite-dimensional, then $\im T$ is finite-dimensional and $\dim \im T \le \dim V$. A spanning set of $\dim V$ vectors maps to a spanning set of at most $\dim V$ vectors.
- A linear map $\R^2 \to \R^3$ is never surjective, since its image has dimension at most $2$.
- The system $Ax = b$ is solvable if and only if $b$ is in the column space of $A$.

### Converse

Every subspace $U$ of $W$ is the image of a linear map, for example of the inclusion $U \to W$.

### Generalizations

- The image of any subspace $U \subseteq V$ is a subspace $T(U)$ of $W$, spanned by the images of a spanning set of $U$.
- For modules over a ring, the image of a homomorphism is a submodule, with the same proof.

## History

Part 3 and its consequence for $Ax = b$ are the content of the Rouché-Capelli theorem of the 19th century.
In different countries the theorem also carries the names of Kronecker, Frobenius and Fontené.

## Explanations

### L1 human

The outputs of a linear map form a subspace.
To describe all outputs, it is enough to know the outputs of a spanning set.
For a matrix, these outputs are the columns.

### L2 human

Let $T \colon \R^2 \to \R^3$ be $T(x, y) = (x, y, x + y)$.

1. The standard vectors $e_1, e_2$ span $\R^2$.
2. $T(e_1) = (1, 0, 1)$ and $T(e_2) = (0, 1, 1)$.
3. So $\im T$ is the plane spanned by $(1, 0, 1)$ and $(0, 1, 1)$, which is $\{(a, b, c) : c = a + b\}$.

The trap is to assume the images of a basis are a basis of the image; they span it, but they can be dependent.
