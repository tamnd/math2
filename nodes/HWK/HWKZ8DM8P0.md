---
tag: HWKZ8DM8P0
kind: statement
role: theorem
name: Similarity is an equivalence relation
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
about: [0E89HQATM8, 0G8VEZ3WTK]
uses: [027KDW2K72, 0SGTMBEWRF]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 2.5
---

## Statement

Let $F$ be a field and let $n \ge 1$.
[[Similarity|027KDW2K72]] is an [[equivalence relation|0SGTMBEWRF]] on the set $M_n(F)$ of $n \times n$ matrices over $F$.
That is, for all $A, B, C \in M_n(F)$:

1. (Reflexive) $A$ is similar to $A$.
2. (Symmetric) If $B$ is similar to $A$, then $A$ is similar to $B$.
3. (Transitive) If $B$ is similar to $A$ and $C$ is similar to $B$, then $C$ is similar to $A$.

In detail, if $B = P^{-1} A P$, then $A = (P^{-1})^{-1} B P^{-1}$.
If also $C = Q^{-1} B Q$, then $C = (PQ)^{-1} A (PQ)$.

## Remarks

### Why each hypothesis is needed

- The matrix $P$ must be invertible, or $P^{-1}$ is not defined.
  If one writes the condition as $PB = AP$ and allows every $P$, then $P = 0$ relates every pair of matrices.
  That relation is an equivalence relation, but it carries no information about $A$ and $B$.
- The matrices must be square of one size $n$, so that $P^{-1} A P$ is defined.
- The ring of scalars may be any commutative ring. The proof uses only that invertible matrices are closed under products and inverses.

### Consequences

- $M_n(F)$ is the disjoint union of the similarity classes.
- The relation "$B$ is similar to $A$" can be stated as "$A$ and $B$ are similar", since the order does not matter.
- Two matrices similar to a third are similar to each other. For example, two matrices similar to one diagonal matrix are similar.

### Converse

The statement has no converse in the usual sense.
In its place, the [[change of basis formula|0MQXVZEBMT]] shows that $A$ and $B$ are similar if and only if they are the matrices of one endomorphism of $F^n$ in two bases.

### Generalizations

- In any group $G$, conjugacy $h = g^{-1} x g$ is an equivalence relation, by the same proof. Similarity is conjugacy in $GL_n(F)$, extended to all of $M_n(F)$.
- For linear maps, $S \colon V \to V$ and $T \colon W \to W$ are similar when $T = \phi S \phi^{-1}$ for an isomorphism $\phi \colon V \to W$. This is also an equivalence relation.

## History

The proof is the standard verification for the conjugation action of a group, written with matrices.

## Explanations

### L1 human

Every matrix is similar to itself, using the identity matrix.
If $B$ comes from $A$ by a change of basis, then $A$ comes from $B$ by the reverse change.
Two changes of basis in a row give one change of basis.

### L2 human

Each axiom uses one property of invertible matrices.
Reflexivity uses $I_n$, symmetry uses the inverse $P^{-1}$, and transitivity uses the product $PQ$ and the rule $(PQ)^{-1} = Q^{-1} P^{-1}$.

### L3 human

The group $GL_n(F)$ acts on $M_n(F)$ by $(P, A) \mapsto P^{-1} A P$, a right action.
For any group action, "being in the same orbit" is an equivalence relation.
The theorem is this general fact for the conjugation action.
