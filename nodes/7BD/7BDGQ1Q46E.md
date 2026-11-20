---
tag: 7BDGQ1Q46E
kind: statement
role: theorem
name: The endomorphisms of a vector space form an associative algebra
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
about: [5JA4CYT1TB]
uses: [0PTF1PTJK0, 0VPCJWGMP9, 1TZSV19D85, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Description
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: History
  - book: isbn:9780135367971
    locator: Section 3.2
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Statement

Let $F$ be a field and let $V$ be a vector space over $F$.
Let $\End(V)$ be the set of [[endomorphisms|0PTF1PTJK0]] of $V$, with the operations of the [[space of linear maps|0VPCJWGMP9]] and with composition $ST = S \circ T$.

1. $\End(V)$ is an [[associative algebra|1TZSV19D85]] over $F$ with unit $\id_V$. So for all $R, S, T \in \End(V)$ and $a \in F$:
   - $(RS)T = R(ST)$ and $\id_V T = T \id_V = T$;
   - $R(S + T) = RS + RT$ and $(R + S)T = RT + ST$;
   - $a(ST) = (aS)T = S(aT)$.
2. Let $\dim V = n$ and let $B$ be a basis of $V$. Then $T \mapsto [T]_B$, the [[matrix of $T$|0YYMY95FWS]] in $B$, is an algebra isomorphism $\End(V) \to M_n(F)$.

## Remarks

### Why each hypothesis is needed

- Left distributivity $R(S + T) = RS + RT$ uses that $R$ is additive. It fails for arbitrary maps, as the [[non-example of all maps|R1SP7B1F0V]] shows.
- The identity $S(aT) = a(ST)$ uses that $S$ is homogeneous.
- Part 2 needs the same basis $B$ on both sides of $T \colon V \to V$. With two different bases, $[ST] = [S][T]$ can fail.

### Consequences

- The $n \times n$ matrices form an associative algebra, and matrix multiplication is associative. Both facts transfer from $\End(V)$ through part 2.
- Polynomials can be evaluated at endomorphisms: $p(T) = a_0 \id + a_1 T + \dots + a_k T^k$. Then $(pq)(T) = p(T)\, q(T)$.
- The automorphisms of $V$ are the units of $\End(V)$, so they form a group.

### Converse

For a set of maps $V \to V$ with pointwise addition and composition, distributivity on the left implies additivity on each element.
Indeed, apply $R(S + T) = RS + RT$ to constant maps $S$ and $T$.
So among all maps $V \to V$, the additive ones are exactly those for which left distributivity holds.

### Generalizations

- For an abelian group $A$, the additive maps $A \to A$ form a ring $\End(A)$ with the same operations.
- For a module $M$ over a commutative ring $R$, $\End_R(M)$ is an associative $R$-algebra.

## History

Cayley introduced matrix notation in 1857.
Peano gave the modern definition of vector spaces and linear maps in 1888.
Part 2 shows that the matrix algebra $M_n(F)$ is the coordinate form of the basis-free algebra $\End(V)$.

## Explanations

### L1 human

Endomorphisms can be added and composed, and these two operations obey the usual laws of a ring.
Composition is associative, and it distributes over addition on both sides.
Only commutativity is missing.

### L2 human

In a basis, part 2 turns each identity in $\End(V)$ into an identity of matrices.
For example, $(T - I)(T + I) = T^2 - I$ holds because $T$ commutes with $I$.
The trap is to expand $(S + T)^2$ as $S^2 + 2ST + T^2$; the correct form is $S^2 + ST + TS + T^2$.

### L3 human

$\End(V)$ is the endomorphism monoid of $V$ in the category of vector spaces, enriched with the vector space structure of $\Hom(V, V)$.
Part 2 is an instance of the equivalence between finite-dimensional spaces with a chosen basis and the coordinate spaces $F^n$.
A different basis $B'$ gives the isomorphism $T \mapsto P^{-1} [T]_B P$, which differs from the first by an inner automorphism of $M_n(F)$.
