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

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ be a subspace of $V$.
Let $U^0 \subseteq V^*$ be the [[annihilator|0R6M158SQ9]] of $U$, and let $\pi \colon V \to V/U$ be the map onto the [[quotient space|0SVR29SV1V]].

1. The map $(V/U)^* \to U^0$, $g \mapsto g \circ \pi$, is a linear isomorphism. So $U^0 \cong (V/U)^*$.
2. The restriction map $r \colon V^* \to U^*$, $f \mapsto f|_U$, is surjective with kernel $U^0$. So $V^*/U^0 \cong U^*$.
3. If $V$ is finite-dimensional, then $\dim U + \dim U^0 = \dim V$, where $\dim$ is the [[dimension|05G2G0P224]].

Parts 1 and 2 hold in any dimension.

## Remarks

### Why each hypothesis is needed

- Part 3 needs finite dimension. For $V = F^{(\N)}$ and $U = \set{0}$, we get $U^0 = V^*$, and $\dim V^* > \dim V$ by the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]]. So $\dim U + \dim U^0 \ne \dim V$.
- In part 2, surjectivity uses that every form on $U$ extends to $V$. This needs a basis of $V$ that extends a basis of $U$, which exists over a field. Over $\Z$, the form $\Z \to \Z$, $x \mapsto x$, on the subgroup $2\Z \cong \Z$ sends $2 \mapsto 1$ and does not extend to $\Z$.

### Consequences

- A subspace $U$ of dimension $k$ in $F^n$ is the solution set of a system of exactly $n - k$ independent linear equations: take a basis of $U^0$.
- For a hyperplane $H$, $\dim H^0 = 1$. This is again the uniqueness of the equation of a hyperplane up to a factor, from the theorem on [[hyperplanes and linear forms|XR0EQN0H8T]].
- With the [[lemma on annihilators|Z71CEX564V]], $U \mapsto U^0$ is an inclusion-reversing bijection between the subspaces of $V$ and those of $V^*$ in finite dimension.
- The [[kernel and image of the dual map|7FA499AW3T]] are computed from part 3.

### Converse

Part 3 characterizes $U^0$ among the subspaces of $V^*$ that vanish on $U$: if $X \subseteq U^0$ and $\dim X = \dim V - \dim U$, then $X = U^0$.

### Generalizations

- Parts 1 and 2 say that duality turns the exact sequence $0 \to U \to V \to V/U \to 0$ into the exact sequence $0 \to (V/U)^* \to V^* \to U^* \to 0$.
- In a normed space, the same isomorphisms hold for the continuous dual and a closed subspace, with norms preserved, by the Hahn-Banach theorem.

## Explanations

### L1 human

The more directions a subspace has, the fewer independent linear forms vanish on it.
In $\R^3$, a line is killed by a plane of forms, and a plane is killed by a line of forms.
The two dimensions always add up to the dimension of the space.

### L2 human

We check part 3 for $U = \set{(x, y, z, w) : x + y = 0,\ z - w = 0}$ in $\R^4$.

1. $U$ is spanned by $(1, -1, 0, 0)$ and $(0, 0, 1, 1)$, so $\dim U = 2$.
2. A form $a x + b y + c z + d w$ vanishes on $U$ exactly when $a - b = 0$ and $c + d = 0$.
3. So $U^0$ is spanned by $x + y$ and $z - w$, and $\dim U^0 = 2$.
4. Then $\dim U + \dim U^0 = 2 + 2 = 4 = \dim \R^4$.

The typical use is to count equations: a subspace of dimension $k$ in an $n$-dimensional space needs exactly $n - k$ independent equations.
A trap: $U^0$ is a subspace of $V^*$, not of $V$, so "$U \oplus U^0 = V$" is meaningless.

### L3 human

Part 1 and part 2 say that the dual functor is exact on vector spaces: it sends short exact sequences to short exact sequences.
This exactness fails for modules over general rings, where $\Hom(-, R)$ is only left exact; the failure of extension in part 2 is measured by the functor $\operatorname{Ext}^1$.
In finite dimension, part 3 is the dimension count behind the equality of row rank and column rank.
