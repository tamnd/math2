---
tag: BM3TWJ0D4P
kind: statement
role: theorem
name: Langlands decomposition
msc: ["22E46", "22E15"]
uses: [XJS07AJ50Y, 4YDR9Q36DS, Z2FEBW5MQM, DK87YN458D]
about: [Z2FEBW5MQM]
sources:
  - url: https://en.wikipedia.org/wiki/Langlands_decomposition
same_as:
  wikidata: Q6486187
  wikipedia: Langlands decomposition
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite center, with an [[Iwasawa decomposition|4YDR9Q36DS]] $G = KAN$.
Let $\mathfrak{a}$ be the Lie algebra of $A$, and let $\Sigma^+$ be the positive restricted roots used to define $N$.
Let $\Pi \subseteq \Sigma^+$ be the simple ones.
Fix a subset $F \subseteq \Pi$ and let $\Sigma_F$ be the set of restricted roots in the linear span of $F$.
Put $\mathfrak{a}_F = \set{H \in \mathfrak{a} : \alpha(H) = 0 \text{ for all } \alpha \in F}$ and $\mathfrak{n}_F = \bigoplus_{\lambda \in \Sigma^+ \setminus \Sigma_F} \mathfrak{g}_\lambda$.
Let $A_F = \exp \mathfrak{a}_F$, let $N_F = \exp \mathfrak{n}_F$, and let $L_F = Z_G(\mathfrak{a}_F)$ be the centralizer of $\mathfrak{a}_F$ under the adjoint action.
Let $M_F$ be the set of $x \in L_F$ with $\abs{\chi(x)} = 1$ for every continuous homomorphism $\chi \colon L_F \to \R^\times$.
Then $P_F = L_F N_F$ is a [[parabolic subgroup|Z2FEBW5MQM]] of $G$, and:

1. $M_F$ and $A_F$ are closed subgroups that commute with each other, $M_F \cap A_F = \set{e}$, and $L_F = M_F A_F$;
2. $N_F$ is a closed, simply connected, [[nilpotent|DK87YN458D]] normal subgroup of $P_F$;
3. the map $M_F \times A_F \times N_F \to P_F$, $(m, a, n) \mapsto man$, is a diffeomorphism.

The factorization $P_F = M_F A_F N_F$ is the *Langlands decomposition* of $P_F$.

## Remarks

Every parabolic subgroup that contains $MAN$ equals $P_F$ for exactly one $F$, and every parabolic subgroup is conjugate to such a $P_F$.
The group $L_F = M_F A_F$ is a Levi factor of $P_F$; it is reductive, and $A_F$ is a vector group, isomorphic to $\R^k$ with $k = \abs{\Pi \setminus F}$.

For $F = \emptyset$, the group $M_\emptyset$ is $M = Z_K(\mathfrak{a})$ and $P_\emptyset = MAN$ is the minimal parabolic subgroup.
For $F = \Pi$, one gets $\mathfrak{a}_F = 0$, $N_F = \set{e}$ and $P_F = M_F = G$, since a semisimple group has no nontrivial continuous homomorphism to $\R_{>0}$.

Example: in $\mathrm{SL}_n(\R)$, a subset $F$ corresponds to block sizes $n_1 + \cdots + n_r = n$.
Then $P_F$ is the group of block upper triangular matrices, and $N_F$ is the group of block unipotent ones.
The group $A_F$ consists of the matrices $\operatorname{diag}(t_1 I_{n_1}, \dots, t_r I_{n_r})$ with $t_i > 0$ and determinant $1$.
The group $M_F$ consists of the block diagonal matrices of determinant $1$ whose blocks have determinant $\pm 1$.

## Explanations

### L1 human

A parabolic subgroup splits into three pieces in a unique way.
One piece $M$ is a smaller reductive group, similar in kind to $G$.
One piece $A$ is a group of scalings, a copy of $\R^k$.
One piece $N$ is a group of shears, and it is normal.
For block upper triangular matrices, $M$ and $A$ together give the diagonal blocks, and $N$ gives the part above the blocks.

### L2 human

The decomposition is the basis of parabolic induction.
A representation $\sigma$ of $M_F$ and a character $\nu$ of $A_F$ give a representation $\sigma \otimes \nu \otimes 1$ of $P_F$, which one induces to $G$.
The principal series come from $F = \emptyset$, and Langlands used general $F$ to classify the irreducible admissible representations of $G$.
The groups $M_F$ are again reductive groups, which makes induction on the size of the group possible.
