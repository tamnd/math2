---
tag: GF1RK91VED
kind: statement
role: theorem
name: Rosenberg's classification of maximal clones
msc: [08A40, 03B50]
uses: [PTKR703G6A, EX9NCDFYC7, A0K9EZRM7E, 0QV2JS9RJ3, 0G8VEZ3WTK, 05RWFKVTJ7, DZSZ8ZS554]
about: [EX9NCDFYC7, PTKR703G6A]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Statement

Let $A$ be a finite set with $k = \abs{A} \ge 2$.
A [[clone|PTKR703G6A]] on $A$ is *maximal* if it is a coatom of the [[lattice of clones|EX9NCDFYC7]] on $A$.
For a relation $\rho$ on $A$, let $\operatorname{Pol}(\rho)$ be the clone of all [[polymorphisms|A0K9EZRM7E]] of $\rho$.
A relation $\rho \subseteq A^h$ is *totally symmetric* if it is invariant under all permutations of coordinates.
It is *totally reflexive* if it contains every $h$-tuple with two equal entries.
Then a clone $C$ on $A$ is maximal if and only if $C = \operatorname{Pol}(\rho)$ for a relation $\rho$ of one of the following six types.

1. A [[partial order|0QV2JS9RJ3]] on $A$ with a least and a greatest element.
2. The graph $\set{(a, \sigma(a)) : a \in A}$ of a [[permutation|05RWFKVTJ7]] $\sigma$ of $A$ whose cycles all have the same prime length $p$.
3. The relation $\set{(a, b, c, d) \in A^4 : a + b = c + d}$, where $(A, +)$ is an [[elementary abelian|DZSZ8ZS554]] $p$-group for a prime $p$.
4. An [[equivalence relation|0G8VEZ3WTK]] on $A$ other than equality and $A^2$.
5. A central relation $\rho \subseteq A^h$ with $1 \le h \le k - 1$.
   This means that $\rho \ne A^h$, that $\rho$ is totally symmetric and totally reflexive, and that some $c \in A$ satisfies $(c, a_2, \dots, a_h) \in \rho$ for all $a_2, \dots, a_h \in A$.
   For $h = 1$ it means a nonempty proper subset of $A$.
6. An $h$-regular relation with $3 \le h \le k$.
   This is the relation determined by a family $\theta_1, \dots, \theta_m$ of equivalence relations, $m \ge 1$, each with exactly $h$ blocks.
   The family must be such that any choice of one block of each $\theta_i$ has nonempty intersection.
   The relation consists of the $h$-tuples that, for every $i$, have two entries in the same $\theta_i$-block.

## Remarks

The theorem is due to Ivo Rosenberg.
One direction shows that each listed $\operatorname{Pol}(\rho)$ is a proper clone and that adding any operation outside it generates all operations.
The other direction uses the [[Pol–Inv Galois connection|BQ0AC9QX7E]]: a maximal clone is $\operatorname{Pol}(\rho)$ for a single relation $\rho$, which is then reduced to a minimal form.
For $k = 2$ the list gives the five maximal clones of [[Post's lattice|MA20X7JCET]].
Type 1 gives the monotone operations, type 2 the self-dual ones, and type 3 the affine ones.
Type 5 with $h = 1$ gives the operations preserving $\set{0}$ or preserving $\set{1}$.
Types 4 and 6 do not occur for $k = 2$.
On every finite set, there are therefore only finitely many maximal clones.

## Explanations

### L1 human

A maximal clone is a family of operations that is just one step short of everything.
Adding any single missing operation to it lets one build every operation on the set.
The theorem lists all such families on a finite set.
Each is the set of operations that respect one special relation, such as an order or an equivalence.

### L2 human

The classification gives a completeness test.
A set $F$ of operations on a finite set generates all operations exactly when, for each relation $\rho$ of the six types, some member of $F$ fails to preserve $\rho$.
This extends [[Post's functional completeness theorem|WGBR7JHBV4]] from two elements to any finite set.
It is a basic tool for questions about [[functional completeness|TDZVCWYJ9F]] in many-valued logic.
