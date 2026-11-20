---
tag: ~9c6edc2a
kind: statement
role: lemma
name: Basis of a cyclic subspace
aliases: [dimension-of-a-cyclic-subspace]
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
about: [~33677c91]
uses: [~33677c91, 0E3MV6E6MG, 0KCQ9Y3QKA, 0ZCWPNZTQ3, ~dd227218, 0KN7EPH7Z0]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Statement

Let $V$ be a finite-dimensional vector space over a field $F$, let $T \colon V \to V$ be linear, and let $v \in V$.

1. There is a unique monic polynomial $m_v \in F[x]$ of least degree with $m_v(T) v = 0$, the [[$T$-annihilator|~33677c91]] of $v$.
2. For $f \in F[x]$, $f(T) v = 0$ if and only if $m_v$ divides $f$.
3. Let $k = \deg m_v$. Then $v, Tv, \dots, T^{k-1} v$ is a [[basis|0KCQ9Y3QKA]] of the cyclic subspace $Z(v; T)$, so $\dim Z(v; T) = \deg m_v$.
4. $Z(v; T)$ is $T$-invariant, and it is contained in every $T$-invariant subspace that contains $v$.
5. If $v \ne 0$, the matrix of the [[restriction|0KN7EPH7Z0]] $T|_{Z(v; T)}$ in the basis of part 3 is the [[companion matrix|0ZCWPNZTQ3]] $C(m_v)$.
6. The minimal and the characteristic polynomial of $T|_{Z(v; T)}$ both equal $m_v$.

## Remarks

### Why each hypothesis is needed

If $V$ is infinite-dimensional, part 1 can fail.
For the map $f \mapsto x f$ on $F[x]$ and $v = 1$, no nonzero polynomial kills $v$, and $1, x, x^2, \dots$ are independent.
For $v = 0$ we get $m_v = 1$ and $Z(v; T) = 0$, and part 3 holds with the empty basis; part 5 needs $v \ne 0$ only because a $0 \times 0$ matrix is a degenerate case.

### Consequences

- $\deg m_v \le \dim V$ for every $v$.
- $m_v$ divides the [[minimal polynomial|03NDVCSHSB]] $m_T$, by part 2, since $m_T(T) v = 0$.
- $v$ is a cyclic vector for $T$ if and only if $\deg m_v = \dim V$.

### Converse

Part 3 has a converse.
If $v, Tv, \dots, T^{j-1} v$ is a basis of $Z(v; T)$, then $j = \deg m_v$, since a basis has $\dim Z(v; T)$ elements.

### Generalizations

The same proof works for a module $M$ over $F[x]$ and an element $v$ with nonzero annihilator: $F[x] v \cong F[x]/(m_v)$.
Over a principal ideal domain $R$, every cyclic module is $R/(a)$ for some $a$.

## Explanations

### L1 human

Start with a vector and apply the map again and again.
At some step the new vector is a combination of the earlier vectors.
The lemma says that the vectors before this step form a basis of everything you can reach.
The rule that writes the new vector through the old ones is a polynomial, and the map acts on the basis by "move to the next vector".

### L2 human

Let $T$ be the map of $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ on $\mathbb{R}^2$ and $v = e_2$.

1. $Tv = (1, 1)$, and $v, Tv$ are independent. So $k \ge 2$, and $k \le \dim V = 2$, so $k = 2$.
2. $T^2 v = A(1, 1) = (2, 1) = 2 Tv - v$.
3. So $m_v = x^2 - 2x + 1 = (x - 1)^2$.
4. In the basis $v, Tv$ the matrix of $T$ is $C(x^2 - 2x + 1) = \begin{pmatrix} 0 & -1 \\ 1 & 2 \end{pmatrix}$.

The typical use is to compute a basis in which $T$ has a companion matrix.
The trap is to stop at the first vector that depends on the earlier ones and forget that all later vectors also depend on them.

### L3 human

In module language the lemma says $Z(v; T) \cong F[x]/(m_v)$ as $F[x]$-modules, with $T$ acting as multiplication by $x$.
The basis $1, x, \dots, x^{k-1}$ of $F[x]/(m_v)$ is the image of the basis of part 3.
The same idea gives the power basis of a simple field extension $F(\alpha) \cong F[x]/(p)$, and the companion matrix is the matrix of multiplication by $\alpha$.
