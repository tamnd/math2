---
tag: 0TXWV1JGG1
kind: statement
role: theorem
name: HN is a subgroup when N is normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0PT52XQZD7, 0CB0DX5BVV]
uses: [0X1JXT47GA, 0CB0DX5BVV, 0PT52XQZD7, 05N4TQKPH0]
sources:
  - url: https://en.wikipedia.org/wiki/Product_of_group_subsets
    locator: Product of subgroups
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Let $HN = \{hn : h \in H, n \in N\}$ and $NH = \{nh : n \in N, h \in H\}$ be the two [[products|0PT52XQZD7]] of $H$ and $N$.
Then the following three claims hold.

1. $HN = NH$.
2. $HN$ is a subgroup of $G$.
3. If $H$ is also a normal subgroup of $G$, then $HN$ is a normal subgroup of $G$.

## Remarks

### Why each hypothesis is needed

The hypothesis that $N$ is normal is needed for claims 1 and 2.
In the [[symmetric group|0515A6D2Y1]] $S_3$, compose permutations from right to left, and let $H = \{e, (1\,2)\}$ and $K = \{e, (1\,3)\}$.
Neither subgroup is normal in $S_3$.
The product $HK$ is $\{e, (1\,2), (1\,3), (1\,2)(1\,3)\}$, and $(1\,2)(1\,3) = (1\,3\,2)$.
Thus $HK$ has $4$ elements.
By [[Lagrange's theorem|3C53TD]], a subgroup of $S_3$ has an order that divides $6$, and $4$ does not divide $6$.
Thus $HK$ is not a subgroup.
Also $KH$ contains $(1\,3)(1\,2) = (1\,2\,3)$, which is not in $HK$, so $HK \ne KH$.

The hypothesis that $H$ is normal is needed for claim 3.
In $S_3$, let $N = \{e\}$, which is normal, and let $H = \{e, (1\,2)\}$.
Then $HN = H$, and $H$ is not normal in $S_3$, because $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$ is not in $H$.

### Consequences

- $HN$ is the smallest subgroup of $G$ that contains $H$ and $N$. Each subgroup that contains $H$ and $N$ contains all products $hn$.
- $N$ is a normal subgroup of $HN$, because $xnx^{-1} \in N$ for all $x \in G$, and thus for all $x \in HN$.
- When $G$ is finite, the [[product formula|08PY4GNAPK]] gives $|HN| = |H|\,|N| / |H \cap N|$.
- The subgroup $HN$ is the top of the diamond in the [[second isomorphism theorem|0PPP2J2DJV]], which gives $H/(H \cap N) \cong HN/N$.
- When $H$ and $N$ are both normal, claim 3 shows that the normal subgroups of $G$ are closed under products.

### Converse

The converse of claim 2 is false.
If $HK$ is a subgroup, then neither $H$ nor $K$ needs to be normal.
In $S_3$, take $H = K = \{e, (1\,2)\}$.
Then $HK = H$ is a subgroup, but $H$ is not normal.
The exact condition is known: for subgroups $H$ and $K$, the set $HK$ is a subgroup if and only if $HK = KH$.

### Generalizations

The proof uses normality only for conjugation by elements of $H$.
Thus claims 1 and 2 hold when $H$ lies in the [[normaliser|0YGN3VAA0D]] of $N$, that is, when $hNh^{-1} = N$ for each $h \in H$.
The same argument works for any finite number of normal subgroups: $N_1 N_2 \cdots N_k$ is a normal subgroup of $G$.

## Explanations

### L1 human

Take one subgroup $H$ and one normal subgroup $N$ of a group.
Multiply each element of $H$ by each element of $N$, and collect all the results.
The theorem says that this collection is again a subgroup.
For example, in the integers with addition, take the multiples of $4$ and the multiples of $6$.
The sums of a multiple of $4$ and a multiple of $6$ are exactly the even numbers, and the even numbers form a subgroup.
Without the normal subgroup, the collection can fail to be a subgroup, as the example in $S_3$ shows.

### L2 human

We compute $HN$ in a group that is not abelian.

1. Let $G = S_4$, composed from right to left, and let $N = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$. This $N$ is a copy of the [[Klein four-group|0PMRQJVTME]], and it is normal in $S_4$.
2. $N$ is normal because conjugation keeps the cycle type, by the [[classification of the conjugacy classes of $S_n$|0J438GAC8K]]. The three elements of type $(2,2)$ are all in $N$.
3. Let $H = \{e, (1\,2)\}$. Then $HN = N \cup (1\,2)N$.
4. We compute $(1\,2)N$. The products are $(1\,2)e = (1\,2)$, $(1\,2)(1\,2)(3\,4) = (3\,4)$, $(1\,2)(1\,3)(2\,4) = (1\,3\,2\,4)$ and $(1\,2)(1\,4)(2\,3) = (1\,4\,2\,3)$.
5. Thus $HN$ has the $8$ elements $e$, $(1\,2)(3\,4)$, $(1\,3)(2\,4)$, $(1\,4)(2\,3)$, $(1\,2)$, $(3\,4)$, $(1\,3\,2\,4)$, $(1\,4\,2\,3)$.
6. The theorem says that these $8$ elements form a subgroup of $S_4$. This subgroup is a copy of the dihedral group of order $8$.

The typical use of the theorem is to build a new subgroup from two known subgroups, for example in the second isomorphism theorem.
A trap is to forget the hypothesis.
For two arbitrary subgroups, the set $HK$ is often not a subgroup, and then its size $|H|\,|K|/|H \cap K|$ need not divide $|G|$.

### L3 human

In the [[lattice of subgroups|0B8BW4YWTF]], the join of $H$ and $K$ is the subgroup that they generate.
The theorem says that the join of $H$ and a normal subgroup $N$ is the plain set of products $HN$, so no longer words are needed.
For abelian groups, all subgroups are normal, and the join is the sum $H + K$, as for subspaces of a vector space.
The normal subgroups of a group form a sublattice of the lattice of subgroups, with meet $M \cap N$ and join $MN$; this sublattice is modular.
The same pattern holds for ideals of a ring, where the sum $I + J$ of two ideals is an ideal.
The theorem is the first step of the [[second isomorphism theorem|0PPP2J2DJV]], and it is used again for products of subgroups in the study of semidirect products and of Sylow subgroups.
