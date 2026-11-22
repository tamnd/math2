---
tag: 5VYBJYPYMW
kind: statement
role: lemma
name: Basis of a cyclic subspace
aliases: [dimension-of-a-cyclic-subspace]
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
about: [42MMQBTP0M]
uses: [42MMQBTP0M, 0E3MV6E6MG, 0KCQ9Y3QKA, 0ZCWPNZTQ3, XYR7GPH20K, 0KN7EPH7Z0]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Statement

The first few vectors of the orbit $v, Tv, T^2 v, \dots$ form a basis of the cyclic subspace, and the number of them is the degree of the annihilator of $v$.
Let $V$ be a finite-dimensional vector space over a field $F$, let $T \colon V \to V$ be linear, and let $v \in V$.

1. There is a unique monic polynomial $m_v \in F[x]$ of least degree with $m_v(T) v = 0$, the [[$T$-annihilator|42MMQBTP0M]] of $v$.
2. For $f \in F[x]$, we have $f(T) v = 0$ if and only if $m_v$ divides $f$.
3. Let $k = \deg m_v$. Then $v, Tv, \dots, T^{k-1} v$ is a [[basis|0KCQ9Y3QKA]] of the cyclic subspace $Z(v; T)$, so $\dim Z(v; T) = \deg m_v$.
4. $Z(v; T)$ is $T$-invariant, and it is contained in every $T$-invariant subspace that contains $v$.
5. If $v \ne 0$, the matrix of the [[restriction|0KN7EPH7Z0]] $T|_{Z(v; T)}$ in the basis of part 3 is the [[companion matrix|0ZCWPNZTQ3]] $C(m_v)$.
6. The minimal polynomial and the characteristic polynomial of $T|_{Z(v; T)}$ both equal $m_v$.

## Remarks

### A worked case

Let $T$ be the map of $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ on $\mathbb{R}^2$, and let $v = e_2$.
Then $Tv = (1, 1)$, which is not a multiple of $v$, so $k \ge 2$, and $k \le \dim V = 2$ gives $k = 2$.
The next vector depends on the first two:
$$T^2 v = A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} = 2 Tv - v.$$
So $m_v = x^2 - 2x + 1 = (x - 1)^2$, and in the basis $v, Tv$ the matrix of $T$ is
$$C(x^2 - 2x + 1) = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}.$$
Check: this matrix has trace $2$ and determinant $1$, the same as $A$.

### Why each hypothesis is needed

Finite dimension is what makes part 1 work.
On the infinite-dimensional space $F[x]$, the map $f \mapsto x f$ and the vector $v = 1$ give the orbit $1, x, x^2, \dots$, which is independent, so no nonzero polynomial kills $v$.

The case $v = 0$ is allowed but degenerate.
Then $m_v = 1$ and $Z(v; T) = 0$, and part 3 holds with the empty basis.
Part 5 asks for $v \ne 0$ only to avoid a matrix of size $0$.

### What it gives you

Since $Z(v; T) \subseteq V$, part 3 gives $\deg m_v \le \dim V$ for every $v$.
Since $m_T(T) v = 0$ for the [[minimal polynomial|03NDVCSHSB]] $m_T$, part 2 shows that $m_v$ divides $m_T$.
Part 3 also gives the test for cyclic vectors: $v$ is a cyclic vector for $T$ exactly when $\deg m_v = \dim V$.
Parts 5 and 6 explain why companion matrices are the building blocks of the [[rational canonical form|042JWAR3Q0]]: every cyclic piece of $V$ looks like one.

### The converse of part 3

If $v, Tv, \dots, T^{j-1} v$ is a basis of $Z(v; T)$ for some $j$, then $j = \deg m_v$, because every basis of $Z(v; T)$ has $\dim Z(v; T)$ elements.
So the number of steps before the orbit becomes dependent is a property of $v$ alone.

### Generalizations

The same argument works for a module $M$ over $F[x]$ and an element $v$ with a nonzero annihilator, and it gives $F[x] v \cong F[x]/(m_v)$.
Over any principal ideal domain $R$, every cyclic module has the form $R/(a)$.

## Explanations

### L1 human

Start with a vector and apply the map again and again.
At some step the new vector is a combination of the vectors before it.
The lemma says that the vectors before this step form a basis of everything you can reach.
For the shear that sends $(0, 1)$ to $(1, 1)$, two steps are enough to reach the whole plane.
The rule that writes the new vector through the old ones is a polynomial, and the map acts on the basis by "move to the next vector".

### L2 human

Here is a typical use: find a basis of a cyclic subspace that is smaller than the whole space.
Let $A = \operatorname{diag}(1, 1, 2)$ on $\mathbb{Q}^3$ and $v = (1, 1, 1)$.
Then $Av = (1, 1, 2)$, which is not a multiple of $v$.
The next vector is $A^2 v = (1, 1, 4)$, and it depends on the first two:
$$A^2 v = 3 Av - 2v = (3 - 2, 3 - 2, 6 - 2) = (1, 1, 4).$$
So $m_v = x^2 - 3x + 2$, the basis of $Z(v; A)$ is $v, Av$, and $Z(v; A)$ is a plane inside $\mathbb{Q}^3$.
Watch out: the orbit also contains $A^3 v, A^4 v, \dots$, but by part 2 all of them are combinations of $v$ and $Av$, so they add nothing.

### L3 human

In module language the lemma says $Z(v; T) \cong F[x]/(m_v)$ as $F[x]$-modules, with $T$ acting as multiplication by $x$.
The basis of part 3 is the image of the basis $1, x, \dots, x^{k-1}$ of $F[x]/(m_v)$.
The same idea gives the power basis $1, \alpha, \dots, \alpha^{k-1}$ of a simple field extension $F(\alpha) \cong F[x]/(p)$, and the companion matrix $C(p)$ is the matrix of multiplication by $\alpha$.
In numerical linear algebra the spaces $Z(v; A)$, cut off after $j$ steps, are the [[Krylov subspaces|QB45PCGQPV]].
