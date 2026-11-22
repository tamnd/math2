---
tag: 06Q1EFVH0Q
kind: statement
role: theorem
name: Dimension of the annihilator
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [0ASHNYF7AG]
uses: [0R6M158SQ9, 05G2G0P224, 0SVR29SV1V, 0M856Q1AMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Duals of quotient spaces
  - url: https://en.wikipedia.org/wiki/Transpose_of_a_linear_map
    locator: Duals of vector subspaces
  - book: isbn:9783031410253
    locator: Section 3F
---

## Statement

A subspace and its annihilator share out the dimension of the space, and behind this count lie two isomorphisms that hold in every dimension.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ be a subspace of $V$.
Let $U^0 \subseteq V^*$ be the [[annihilator|0R6M158SQ9]] of $U$, and let $\pi \colon V \to V/U$ be the projection onto the [[quotient space|0SVR29SV1V]].

1. The map $(V/U)^* \to U^0$, $g \mapsto g \circ \pi$, is a linear isomorphism. So $U^0 \cong (V/U)^*$.
2. The restriction map $r \colon V^* \to U^*$, $f \mapsto f|_U$, is surjective with kernel $U^0$. So $V^*/U^0 \cong U^*$.
3. If $V$ is finite-dimensional, then $\dim U + \dim U^0 = \dim V$, where $\dim$ is the [[dimension|05G2G0P224]].

Parts 1 and 2 hold in every dimension.

## Remarks

### A count in four dimensions

Take $U = \{ (x, y, z, w) : x + y = 0, \ z - w = 0 \}$ in $\mathbb{R}^4$.
Its vectors are $(x, -x, z, z)$, so $U$ is spanned by $(1, -1, 0, 0)$ and $(0, 0, 1, 1)$, and $\dim U = 2$.
A form $ax + by + cz + dw$ vanishes on these two vectors when
$$a - b = 0, \qquad c + d = 0.$$
So $U^0$ is spanned by $x + y$ and $z - w$, and $\dim U^0 = 2$.
Check: $\dim U + \dim U^0 = 2 + 2 = 4 = \dim \mathbb{R}^4$.
The two equations that defined $U$ are exactly a basis of $U^0$.

### Why finite dimension is needed in part 3

In infinite dimension the dimensions are cardinals, and the formula can fail.
For $V = F^{(\mathbb{N})}$ and $U = \{0\}$ we get $U^0 = V^*$.
By the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]], $\dim V^* > \dim V$, so $\dim U + \dim U^0 = \dim V^*$ is not $\dim V$.

### Why the field is needed in part 2

Surjectivity of $r$ says that every form on $U$ extends to $V$.
Over a field this works because a basis of $U$ extends to a basis of $V$.
Over the ring $\mathbb{Z}$ it fails.
The subgroup $2\mathbb{Z}$ of $\mathbb{Z}$ has the homomorphism $\psi(x) = x/2$ to $\mathbb{Z}$, which sends $2$ to $1$.
An extension $g \colon \mathbb{Z} \to \mathbb{Z}$ would satisfy $2 g(1) = g(2) = 1$, and no integer $g(1)$ does that.

### What it gives you

A subspace of dimension $k$ in $F^n$ is the solution set of exactly $n - k$ independent linear equations: take a basis of $U^0$, and the lemma on [[properties of annihilators|Z71CEX564V]] shows that their common solutions form $U$.
For a hyperplane $H$ the count gives $\dim H^0 = 1$, so the equation of a hyperplane is unique up to a factor, as in the theorem on [[hyperplanes and linear forms|XR0EQN0H8T]].

The count also recognizes an annihilator without computing it.
If $X$ is a subspace of $U^0$ with $\dim X = \dim V - \dim U$, then $X = U^0$, since a subspace of the same finite dimension is the whole space.
[[The annihilator of the trace-zero matrices|5QM5REJ243]] uses this with $X$ the line of multiples of the trace.

Later the theorem gives the dimensions of the [[kernel and image of the dual map|7FA499AW3T]], and from them the equality of row rank and column rank.

### Generalizations

Parts 1 and 2 say that the dual turns the [[exact sequence|946YAZNYKX]] $0 \to U \to V \to V/U \to 0$ into the exact sequence $0 \to (V/U)^* \to V^* \to U^* \to 0$.
In a normed space $V$ with a closed subspace $U$, the same two isomorphisms hold for continuous duals, and they preserve norms; the [[Hahn-Banach theorem|QB5AE3VYZZ]] replaces the extension of a basis.

## Explanations

### L1 human

The more directions a subspace has, the fewer independent linear equations hold on it.
In space, a line obeys two independent equations and a plane obeys one.
The number of directions plus the number of independent equations is always the dimension of the whole space.
For a line in space that is $1 + 2 = 3$, and for a plane it is $2 + 1 = 3$.

### L2 human

Here is a typical use: how many equations does it take to describe the polynomials $p$ of degree at most $3$ with $p(1) = 0$ and $p(-1) = 0$?
Let $V$ be the space of real polynomials of degree at most $3$, so $\dim V = 4$.
The subspace $U$ consists of the multiples $(x^2 - 1)(a + bx)$, so it has the basis $x^2 - 1$ and $x^3 - x$, and $\dim U = 2$.
So $\dim U^0 = 4 - 2 = 2$.
The evaluations $p \mapsto p(1)$ and $p \mapsto p(-1)$ lie in $U^0$, and they are independent, since $1$ gives $1$ under both while $x$ gives $1$ and $-1$.
Two independent forms in a space of dimension $2$ span it, so these two equations already give all of $U^0$.
Watch out: $U^0$ is a subspace of $V^*$ and not of $V$, so a statement such as $U \oplus U^0 = V$ has no meaning.

### L3 human

Parts 1 and 2 say that the dual functor $V \mapsto V^*$ is exact on vector spaces: it sends short exact sequences to short exact sequences.
For modules over a general ring $R$ the functor $\operatorname{Hom}(-, R)$ is only left exact, and the failure of extension seen over $\mathbb{Z}$ is measured by the [[Ext functor|4P7GBWJ4RR]].
In finite dimension part 3 also follows from part 1, because $\dim (V/U)^* = \dim (V/U) = \dim V - \dim U$.
The theorem returns in the study of the [[dual map|0AZ5ARP287]], where kernels and images become annihilators.
