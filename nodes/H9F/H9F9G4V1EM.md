---
tag: H9F9G4V1EM
kind: statement
role: theorem
name: Double centralizer theorem
msc: [16K20, 16K50]
uses: [5HRKJBAY2V, 62M0NC3E2T, 1735VGRT2P]
about: [5HRKJBAY2V]
sources:
  - url: https://en.wikipedia.org/wiki/Double_centralizer_theorem
same_as:
  wikidata: Q5299981
  wikipedia: Double centralizer theorem
---

## Statement

Let $K$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$.
Let $B$ be a $K$-subalgebra of $A$ that is a [[simple ring|62M0NC3E2T]].
For a subset $S$ of $A$, let $C_A(S) = \set{a \in A : as = sa \text{ for all } s \in S}$ be its centralizer.
Then:

1. $C_A(B)$ is a simple $K$-algebra.
2. $\dim_K B \cdot \dim_K C_A(B) = \dim_K A$.
3. $C_A(C_A(B)) = B$.
4. If $B$ is central simple over $K$, then $A \cong B \otimes_K C_A(B)$.

## Remarks

The proof views $A$ as a module over the simple algebra $B \otimes_K A^{\mathrm{op}}$.
Then $C_A(B)$ is the endomorphism ring of this module, a matrix algebra over a division algebra.
Counting dimensions gives clause 2.
Since $B \subseteq C_A(C_A(B))$ and clause 2 applied twice gives equal dimensions, clause 3 follows.
Example: let $A = M_n(K)$ and $B = K[x]/(p)$, embedded through the companion matrix $C$ of an irreducible polynomial $p$ of degree $n$.
Then $C_A(B)$ consists of the polynomials in $C$, so it equals $B$, and indeed $n \cdot n = n^2$.
Example: for $A = M_2(K) \otimes_K M_3(K)$ and $B = M_2(K) \otimes 1$, the centralizer is $1 \otimes M_3(K)$, and $4 \cdot 9 = 36$.
Simplicity of $B$ is needed for clause 2: in $A = M_3(K)$ let $B$ be spanned by $I$ and the matrix unit $E_{13}$, a subalgebra with the nilpotent ideal $K E_{13}$.
A matrix commutes with $E_{13}$ exactly when its entries in positions $(2,1)$, $(3,1)$, $(3,2)$ vanish and its entries in positions $(1,1)$ and $(3,3)$ agree, so $\dim_K C_A(B) = 5$ and $2 \cdot 5 \ne 9$.

## Explanations

### L1 human

Inside a central simple algebra, take a simple subalgebra and collect everything that commutes with it.
The theorem says that the sizes of the two pieces multiply to the size of the whole algebra.
Doing it twice gives back the subalgebra one started with.

### L2 human

The main use is to subfields: if $L$ is a subfield of $A$ containing $K$, then $[L : K] \cdot \dim_K C_A(L) = \dim_K A$, so $[L : K]$ divides the degree of $A$.
When $C_A(L) = L$, this gives $[L : K]^2 = \dim_K A$, so $L$ is a maximal subfield and splits $A$.
Clause 4 shows that a central simple subalgebra always splits off as a tensor factor.
With the Skolem–Noether theorem it underlies the crossed product description of the Brauer group.
