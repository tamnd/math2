---
tag: TXMV0YDACG
kind: statement
role: theorem
name: Structure theorem for finitely generated modules over a principal ideal domain
msc: [13C05, 13F10]
uses: [0CMD0BCH8T, 05QY1VEBYD, 0NZ8JA25WK, 0DZ9DKAKZR, 01VH21EV6F, 6PBS6KW0NC]
about: [05QY1VEBYD, 0CMD0BCH8T]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain
same_as:
  wikidata: Q7888360
  wikipedia: Structure theorem for finitely generated modules over a principal ideal domain
---

## Statement

Let $R$ be a [[principal ideal domain|0CMD0BCH8T]] and let $M$ be a [[finitely generated|05QY1VEBYD]] [[$R$-module|0NZ8JA25WK]].

1. (Invariant factors) There are an integer $r \ge 0$ and nonzero non-unit elements $d_1, \ldots, d_k \in R$ with $d_1 \mid d_2 \mid \cdots \mid d_k$ such that
$$M \cong R^r \oplus R/(d_1) \oplus \cdots \oplus R/(d_k).$$
The integer $r$ and the ideals $(d_1), \ldots, (d_k)$ are uniquely determined by $M$.
2. (Elementary divisors) There are an integer $r \ge 0$, [[prime elements|01VH21EV6F]] $p_1, \ldots, p_s \in R$, not necessarily distinct, and integers $e_1, \ldots, e_s \ge 1$ such that
$$M \cong R^r \oplus R/(p_1^{e_1}) \oplus \cdots \oplus R/(p_s^{e_s}).$$
The integer $r$ and the ideals $(p_j^{e_j})$, counted with multiplicity, are uniquely determined by $M$ up to order.

## Remarks

Since $R$ is Noetherian, $M$ has a finite presentation $R^m \xrightarrow{A} R^n \to M \to 0$.
Row and column operations bring the matrix $A$ to Smith normal form, a diagonal matrix with entries $d_1 \mid d_2 \mid \cdots$; this gives part 1.
Part 2 follows from part 1 by the Chinese remainder theorem, which splits $R/(d)$ into $\bigoplus_p R/(p^{e})$ over the prime powers $p^e$ exactly dividing $d$.
The part $R/(d_1) \oplus \cdots \oplus R/(d_k)$ is the [[torsion submodule|6PBS6KW0NC]] of $M$, and $r$ is the rank of the [[free|0DZ9DKAKZR]] quotient $M$ modulo torsion.

Example: over $\Z$, the module $\Z/2\Z \oplus \Z/6\Z$ has invariant factors $2 \mid 6$ and elementary divisors $2, 2, 3$, since $\Z/6\Z \cong \Z/2\Z \oplus \Z/3\Z$.
For $R = \Z$ the theorem is the [[structure theorem for finitely generated abelian groups|0RY0B72XAS]].
For $R = k[x]$ and $M = k^n$ with $x$ acting by a matrix, it gives the rational canonical form and the [[Jordan normal form|085HQ5G5TE]].

The principal ideal hypothesis is necessary.
Over $R = \Z[x]$, the ideal $I = (2, x)$ is a finitely generated torsion-free module.
Any two elements of $I$ are linearly dependent, so a basis would have one element, and $I$ would be principal.
It is not principal, so $I$ is not free and not of the form above.

## Explanations

### L1 human

Over a principal ideal domain, every finitely generated module breaks into simple pieces.
There is a free part, a copy of $R^r$, and a torsion part made of cyclic modules $R/(d)$.
The list of pieces is unique, so it is a complete invariant: two modules are isomorphic exactly when their lists agree.
For abelian groups, this says each finitely generated abelian group is $\Z^r$ times a product of finite cyclic groups.

### L2 human

The theorem unifies two classical results: the classification of finitely generated abelian groups, for $R = \Z$, and the normal forms of matrices, for $R = k[x]$.
In the second case, a matrix $A$ makes $k^n$ a $k[x]$-module, the invariant factors are the invariant polynomials of $A$, and $d_k$ is the minimal polynomial.
The proof by Smith normal form is algorithmic when $R$ is Euclidean.
Over a Dedekind domain that is not principal, the torsion part still decomposes, but the torsion-free part is a sum of ideals rather than a free module.
