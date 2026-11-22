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

Similarity sorts the square matrices of one size into disjoint classes.
Let $F$ be a field and let $n \ge 1$.
[[Similarity|027KDW2K72]] is an [[equivalence relation|0SGTMBEWRF]] on the set $M_n(F)$ of $n \times n$ matrices over $F$.
That is, for all $A, B, C \in M_n(F)$:

1. (Reflexive) $A$ is similar to $A$.
2. (Symmetric) If $B$ is similar to $A$, then $A$ is similar to $B$.
3. (Transitive) If $B$ is similar to $A$ and $C$ is similar to $B$, then $C$ is similar to $A$.

In formulas, if $B = P^{-1}AP$, then $A = (P^{-1})^{-1}BP^{-1}$, and if also $C = Q^{-1}BQ$, then $C = (PQ)^{-1}A(PQ)$.

## Remarks

### Why each hypothesis is needed

The matrix $P$ in the definition must be invertible.
If we wrote the condition as $PB = AP$ and allowed every $P$, then $P = 0$ would relate every pair of matrices.
That relation is still an equivalence relation, but it says nothing about $A$ and $B$.
The invertibility of $P$ is also exactly what the proof uses: the identity for reflexivity, the inverse for symmetry and the product for transitivity.

The matrices must be square of one size $n$, so that $P^{-1}AP$ is defined.
The field is not essential.
Over any commutative ring the same proof works, since it uses only that the invertible matrices are closed under products and inverses and contain $I_n$.

### What it gives you

The set $M_n(F)$ is the disjoint union of the similarity classes.
The order in "$B$ is similar to $A$" does not matter, so we may say "$A$ and $B$ are similar".
Two matrices that are similar to a third are similar to each other.
For example, $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ is similar to $\operatorname{diag}(1, 2)$, which is similar to $\operatorname{diag}(2, 1)$ by the swap matrix, so $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ and $\operatorname{diag}(2, 1)$ are similar.
This is how canonical forms work: to decide whether $A$ and $B$ are similar, bring each to a standard representative of its class and compare.

### The converse

The statement has no converse in the usual sense.
Its companion is the [[change of basis formula|0MQXVZEBMT]], which shows that $A$ and $B$ are similar exactly when they are the matrices of one endomorphism of $F^n$ in two bases.
So each similarity class is the set of all matrices of one endomorphism.

### Generalizations

In any group $G$, conjugacy $h = g^{-1}xg$ is an equivalence relation, by the same proof.
Similarity on invertible matrices is conjugacy in the [[general linear group|0FCHE902D7]] $GL_n(F)$, and on all of $M_n(F)$ it is the orbit relation of the conjugation action of that group.
For linear maps, $S \colon V \to V$ and $T \colon W \to W$ are called similar when $T = \phi S \phi^{-1}$ for a linear isomorphism $\phi \colon V \to W$, and this is again an equivalence relation.

## Explanations

### L1 human

Every matrix is similar to itself, using the identity matrix as the change of basis.
If $B$ comes from $A$ by a change of basis, then $A$ comes from $B$ by the reverse change.
Two changes of basis in a row give one change of basis.
These three facts are the three rules of an equivalence relation.

### L2 human

Each rule uses one property of invertible matrices.
Reflexivity uses $I_n$, symmetry uses the inverse $P^{-1}$, and transitivity uses the product $PQ$ and the rule $(PQ)^{-1} = Q^{-1}P^{-1}$.
For example, with $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ the two steps of the example above combine into one matrix $PQ = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.
Watch out for the order: the matrix of the combined change is $PQ$, not $QP$.

### L3 human

The group $GL_n(F)$ acts on $M_n(F)$ from the right by $A \cdot P = P^{-1}AP$.
For any group action, lying in the same orbit is an equivalence relation, and the theorem is this general fact for the conjugation action.
The classification of the orbits is the subject of the rational and Jordan canonical forms.
