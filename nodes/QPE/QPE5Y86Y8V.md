---
tag: QPE5Y86Y8V
kind: statement
role: lemma
name: A vector whose annihilator is the minimal polynomial
aliases: [existence-of-a-vector-of-maximal-annihilator]
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
about: [42MMQBTP0M, 03NDVCSHSB]
uses: [42MMQBTP0M, 5VYBJYPYMW, 03NDVCSHSB, 03FKX7Z5DC]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: lead section
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Statement

Some single vector already needs the whole minimal polynomial before the map sends it to zero.
Let $V$ be a finite-dimensional vector space over a field $F$, and let $T \colon V \to V$ be linear with [[minimal polynomial|03NDVCSHSB]] $m_T$.
Then there is a vector $v \in V$ whose [[$T$-annihilator|42MMQBTP0M]] $m_v$ equals $m_T$.

## Remarks

### A worked case

Let $T = \operatorname{diag}(1, 1, 2)$ on $\mathbb{Q}^3$, so that $m_T = (x - 1)(x - 2)$.
The basis vectors fall short: $m_{e_1} = m_{e_2} = x - 1$ and $m_{e_3} = x - 2$.
The two factors $x - 1$ and $x - 2$ have no common factor, and the proof adds one vector for each, $v = e_1 + e_3$.
Neither factor alone kills $v$:
$$(T - I) v = e_3 \ne 0, \qquad (T - 2I) v = -e_1 \ne 0.$$
Their product does, since $(T - I)(T - 2I) v = (T - I)(-e_1) = 0$, and so $m_v = (x - 1)(x - 2) = m_T$.

### What it gives you

Every $v$ has $m_v \mid m_T$, so the lemma says that the largest possible annihilator is reached, and $m_T$ is the least common multiple of all the $m_v$.
With the [[lemma on cyclic subspaces|5VYBJYPYMW]] it gives $\deg m_T = \dim Z(v; T) \le \dim V$, a bound on the minimal polynomial that does not use the Cayley-Hamilton theorem.
It is also the key step in the proof that $T$ is cyclic [[when $m_T = \chi_T$|RK1QVMYW7H]].
In the [[cyclic decomposition theorem|R3Z20J19BR]], the generator of the largest cyclic summand is such a vector.

### Why each hypothesis is needed

The space must be finite-dimensional, or $m_T$ may not exist.
The map $f \mapsto x f$ on $F[x]$ satisfies no nonzero polynomial at all.
The proof also uses that $F[x]$ has unique factorization, which holds because $F$ is a field.

### Watch out

Adding two vectors does not always multiply their annihilators.
For the Jordan block $J_2(0)$, with $J_2(0) e_1 = 0$ and $J_2(0) e_2 = e_1$, we have $m_{e_1} = x$ and $m_{e_2} = x^2$.
The sum $e_1 + e_2$ has annihilator $x^2$, not $x \cdot x^2 = x^3$, because the two annihilators share the factor $x$.
The product rule holds only for annihilators with no common factor.

### Generalizations

For a finitely generated torsion module over a principal ideal domain, some element has annihilator equal to the annihilator of the whole module.
For a finite abelian group this says that some element has order equal to the exponent of the group.

## Explanations

### L1 human

Each vector has its own polynomial: the shortest rule that sends it to zero under the map.
The minimal polynomial is the shortest rule that sends every vector to zero at once.
The lemma says that one well-chosen vector already needs the full minimal polynomial.
For the map that doubles the second coordinate of a point in the plane, the point $(1, 0)$ needs only $x - 1$ and the point $(0, 1)$ needs only $x - 2$, but the point $(1, 1)$ needs both.

### L2 human

Here is the construction for a power of a polynomial.
Let $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ on $\mathbb{Q}^3$, so that $A^2 = 0$, $A \ne 0$ and $m_A = x^2$.
The proof asks for a vector that $A$ does not kill, because $x^{2-1} = x$ is a proper divisor of $m_A$.
The vector $e_2$ works, since $A e_2 = e_1 \ne 0$ and $A^2 e_2 = 0$, so $m_{e_2} = x^2 = m_A$.
The vectors $e_1$ and $e_3$ do not work, since $A$ kills both of them.
So the right vector is found by testing against the divisor $m_A / x$, one prime factor at a time.

### L3 human

The proof splits $m_T$ into powers $p_j^{e_j}$ of distinct irreducible polynomials, finds a vector with annihilator exactly $p_j^{e_j}$ for each $j$, and adds them.
Annihilators with no common factor multiply under addition, which is the Chinese remainder theorem for $F[x]$ in disguise.
The same argument shows that a finite abelian group has an element whose order is the exponent of the group.
Over an infinite field there is a shorter argument, since a vector space over an infinite field is not a finite union of proper subspaces.
