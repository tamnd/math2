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

Adding and composing endomorphisms obeys all the rules of a ring, and in a basis these operations become the matrix operations.

Let $F$ be a field and let $V$ be a vector space over $F$.
Let $\End(V)$ be the set of [[endomorphisms|0PTF1PTJK0]] of $V$, with the operations of the [[space of linear maps|0VPCJWGMP9]] and with the product $ST = S \circ T$.

1. $\End(V)$ is an [[associative algebra|1TZSV19D85]] over $F$ with unit $\id_V$.
   So for all $R, S, T \in \End(V)$ and $a \in F$, we have $(RS)T = R(ST)$ and $\id_V T = T \id_V = T$.
   Also $R(S + T) = RS + RT$ and $(R + S)T = RT + ST$.
   Finally $a(ST) = (aS)T = S(aT)$.
2. Let $\dim V = n$ and let $B$ be a basis of $V$.
   Then $T \mapsto [T]_B$, which sends $T$ to its [[matrix|0YYMY95FWS]] in $B$, is an algebra isomorphism $\End(V) \to M_n(F)$.

## Remarks

### Why the hypotheses are needed

Left distributivity $R(S + T) = RS + RT$ uses that $R$ is additive, and it fails for arbitrary maps, as the [[non-example of all maps|R1SP7B1F0V]] shows.
The identity $S(aT) = a(ST)$ uses that $S$ is homogeneous.
Part 2 needs the same basis $B$ on both the source and the target of $T \colon V \to V$.
With two different bases, the rule $[ST] = [S][T]$ can fail.

### What it gives you

Matrix multiplication is associative and distributes over sums, since these facts transfer from $\End(V)$ through part 2.
Polynomials can be evaluated at endomorphisms, as $p(T) = a_0 \id + a_1 T + \dots + a_k T^k$, and then $(pq)(T) = p(T)\, q(T)$.
The automorphisms of $V$ are the units of $\End(V)$, so they form a group.

### The converse

Consider all maps $V \to V$, with pointwise addition and composition.
Left distributivity for a map $R$ forces $R$ to be additive.
Indeed, apply $R(S + T) = RS + RT$ to the constant maps with values $s$ and $t$, which gives $R(s + t) = R(s) + R(t)$.
So among all maps $V \to V$, the additive ones are exactly those for which left distributivity holds.

### Generalizations

For an abelian group $A$, the additive maps $A \to A$ form a ring $\End(A)$ with the same operations.
For a module $M$ over a commutative ring $R$, the endomorphisms form an associative $R$-algebra $\End_R(M)$.

## History

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
Watch out: $(S + T)^2$ expands as $S^2 + ST + TS + T^2$, not as $S^2 + 2ST + T^2$.

### L3 human

The algebra $\End(V)$ is the endomorphism monoid of $V$ in the category of vector spaces, enriched with the vector space structure of $\Hom(V, V)$.
Part 2 reflects the fact that a choice of basis identifies $V$ with the coordinate space $F^n$.
A different basis $B'$ gives the isomorphism $T \mapsto P^{-1} [T]_B P$, where $P$ is the change of basis matrix, and the two differ by an inner automorphism of $M_n(F)$.
