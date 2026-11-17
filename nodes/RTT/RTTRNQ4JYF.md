---
tag: RTTRNQ4JYF
kind: concept
name: Maximal subgroup
msc: ["20E28"]
topics: [BAVE5RN4EE]
audience: ug2
uses: [G5S1M9, 0X1JXT47GA, 0B8BW4YWTF, 0DTXBQPA2S, 3C53TD, 0S9ZVZ34MD, 04RXTQA5ZA, 082DWWXMRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_subgroup
    locator: lead section
---

## Summary

Let $G$ be a [[group|G5S1M9]].
A [[subgroup|0X1JXT47GA]] $M$ of $G$ is maximal if $M \neq G$ and there is no subgroup $H$ with $M \subsetneq H \subsetneq G$.
Equivalently, $M \neq G$, and every subgroup $H$ with $M \subseteq H \subseteq G$ is equal to $M$ or to $G$.
So the maximal subgroups are the maximal elements of the set of proper subgroups of $G$, ordered by inclusion.
In a finite group, every proper subgroup lies in a maximal subgroup, but some infinite groups, such as $(\mathbb{Q}, +)$, have no maximal subgroup.

## Motivation

The [[lattice of subgroups|0B8BW4YWTF]] of a finite group has $G$ at the top.
The maximal subgroups are the subgroups directly below the top.
Many questions about all proper subgroups reduce to questions about the maximal ones, because every proper subgroup of a finite group is inside one of them.
For example, a subset $S$ of a finite group $G$ generates $G$ exactly when $S$ is contained in no maximal subgroup.
To prove that some elements generate $G$, it is enough to check that they do not all lie in one maximal subgroup.

## Notation

There is no standard symbol for a maximal subgroup.
In the language of partially ordered sets, $M$ is covered by $G$ in the lattice of subgroups, and some authors write $M \lessdot G$.
A maximal subgroup is often written $M$, and the set of maximal subgroups of $G$ is sometimes written $\mathcal{M}(G)$.

## Remarks

### Examples

1. [[The maximal subgroups of $\mathbb{Z}/12\mathbb{Z}$ are $\langle 2 \rangle$ and $\langle 3 \rangle$|QJX40B8XBJ]], of orders $6$ and $4$.
2. The maximal subgroups of $(\mathbb{Z}, +)$ are the subgroups $p\mathbb{Z}$ for the primes $p$. Every subgroup of $\mathbb{Z}$ is $n\mathbb{Z}$ for one $n \geq 0$, and $n\mathbb{Z} \subseteq m\mathbb{Z}$ exactly when $m \mid n$. So $n\mathbb{Z}$ is maximal exactly when $n \geq 2$ and the only positive divisors of $n$ are $1$ and $n$.
3. In the [[symmetric group|0515A6D2Y1]] $S_n$ with $n \geq 3$, the alternating group $A_n$ is a maximal subgroup of index $2$, and [[the stabilizer $S_{n-1}$ of the point $n$ is a maximal subgroup|B7BJJBV1S0]] of index $n$.
4. The maximal subgroups of $S_3$ are $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ and the three subgroups $\{e, (i\,j)\}$ of order $2$. So maximal subgroups of one group can have different orders.
5. In a finite group, every subgroup $M$ of prime [[index|0DTXBQPA2S]] $p$ is maximal. If $M \subseteq H \subseteq G$, then by [[Lagrange's theorem|3C53TD]] $|H| / |M|$ is an integer that divides $|G| / |M| = p$, so it is $1$ or $p$, and $H = M$ or $H = G$.

### Non-examples

1. [[The subgroup $4\mathbb{Z}$ of $\mathbb{Z}$ is not maximal|TVFMYCK4AP]], because $4\mathbb{Z} \subsetneq 2\mathbb{Z} \subsetneq \mathbb{Z}$.
2. The group $G$ is never a maximal subgroup of itself, because a maximal subgroup must be proper.
3. In the [[alternating group|0Z5905Q73D]] $A_5$, the trivial subgroup $\{e\}$ is a maximal normal subgroup, because $A_5$ is [[simple|0YMYMNQ0QZ]], but it is not a maximal subgroup, because $\{e\} \subsetneq \langle (1\,2\,3) \rangle \subsetneq A_5$.
4. The group $(\mathbb{Q}, +)$ has no maximal subgroup at all, by property 5 below. The [[Prüfer group|F0XAMM2PPS]] also has none, by the same proof.

### Basic properties

1. Finite groups. Let $G$ be finite and let $H$ be a proper subgroup. Among the proper subgroups of $G$ that contain $H$, choose one, $M$, of the largest order. If $M \subsetneq L \subsetneq G$, then $L$ contains $H$ and $|L| > |M|$, which contradicts the choice of $M$. So $M$ is a maximal subgroup that contains $H$.
2. [[Finitely generated groups|082DWWXMRJ]]. Let $G = \langle s_1, \ldots, s_k \rangle$ and let $H$ be a proper subgroup of $G$. Then $H$ lies in a maximal subgroup. The proof uses [[Zorn's lemma|04RXTQA5ZA]].
   1. Let $P$ be the set of proper subgroups of $G$ that contain $H$, ordered by inclusion. Then $H \in P$, so $P$ is not empty.
   2. Let $C$ be a chain in $P$. If $C$ is empty, then $H$ is an upper bound of $C$ in $P$. Otherwise, let $U$ be the union of the members of $C$.
   3. $U$ is a subgroup. It contains $e$. For $a, b \in U$, choose $K_1, K_2 \in C$ with $a \in K_1$ and $b \in K_2$. Since $C$ is a chain, one of them contains the other, say $K_1 \subseteq K_2$. Then $ab^{-1} \in K_2 \subseteq U$, and the [[subgroup criterion|05N4TQKPH0]] applies.
   4. $U$ contains $H$. Suppose $U = G$. Since $H \neq G$, the group $G$ is not trivial, so $k \geq 1$. Each $s_i$ lies in some $K_i \in C$. The finitely many $K_i$ form a chain, so one of them, $K$, contains all the others. Then $s_1, \ldots, s_k \in K$, so $G = \langle s_1, \ldots, s_k \rangle \subseteq K$. This contradicts $K \neq G$. So $U \neq G$, and $U \in P$ is an upper bound of $C$.
   5. By Zorn's lemma, $P$ has a maximal element $M$. If $M \subsetneq L \subsetneq G$ for a subgroup $L$, then $L \in P$, which contradicts the maximality of $M$ in $P$. So $M$ is a maximal subgroup of $G$ that contains $H$.
3. Normal maximal subgroups. Let $M$ be a [[normal subgroup|0CB0DX5BVV]] of $G$. By the [[correspondence theorem|0S9ZVZ34MD]], the subgroups between $M$ and $G$ correspond to the subgroups of the [[quotient group|0KYX2N69J0]] $G/M$. So $M$ is maximal exactly when $G/M$ is not trivial and has no subgroups other than $\{e\}$ and $G/M$.
4. Abelian groups. Let $G$ be abelian. Then $M$ is a maximal subgroup exactly when $G/M$ is cyclic of prime order.
   1. If $G/M$ has prime order, then by Lagrange's theorem it has no subgroups other than $\{e\}$ and itself. So $M$ is maximal by property 3.
   2. Conversely, let $M$ be maximal, and choose $x \in G/M$ with $x \neq e$. By property 3, $\langle x \rangle = G/M$.
   3. If $x$ had infinite order, then $x^2 \neq e$, so $\langle x^2 \rangle \neq \{e\}$. Also $x \notin \langle x^2 \rangle$, because $x = x^{2k}$ would give $x^{2k-1} = e$ with $2k - 1 \neq 0$. So $\langle x^2 \rangle$ would be a subgroup other than $\{e\}$ and $G/M$. So $x$ has finite order $n \geq 2$.
   4. If $n = ab$ with $1 < a < n$, then $\langle x^a \rangle$ has order $b$ with $1 < b < n$, which is again impossible. So $n$ is prime.
5. Divisible abelian groups have no maximal subgroup.
   1. Suppose $M$ is a maximal subgroup of $(\mathbb{Q}, +)$. By property 4, $\mathbb{Q}/M$ is cyclic of prime order $p$. So $p \cdot (x + M) = M$, that is, $px \in M$, for every $x \in \mathbb{Q}$.
   2. Every $y \in \mathbb{Q}$ is $y = p \cdot (y/p)$, so $y \in M$. Thus $M = \mathbb{Q}$, which contradicts $M \neq \mathbb{Q}$.
   3. The same proof works for every [[divisible group|ZXVBEPMTCN]], such as the Prüfer group, because each element is $p$ times another element.
   4. With property 2, this shows that $\mathbb{Q}$ is not finitely generated.
6. Finite cyclic groups. The maximal subgroups of $\mathbb{Z}/n\mathbb{Z}$ are the subgroups $\langle p \rangle = p\mathbb{Z}/n\mathbb{Z}$ for the primes $p$ that divide $n$, and $\langle p \rangle$ has index $p$. By the [[fundamental theorem of cyclic groups|0423TXR9AN]], every subgroup of $\mathbb{Z}/n\mathbb{Z}$ is $\langle d \rangle$ for a unique positive divisor $d$ of $n$. The quotient $(\mathbb{Z}/n\mathbb{Z})/\langle d \rangle$ has order $d$. So the claim follows from property 4.
7. Generation. Let $G$ be finite or finitely generated, and let $S \subseteq G$. Then $\langle S \rangle = G$ exactly when $S$ lies in no maximal subgroup. If $S \subseteq M$, then $\langle S \rangle \subseteq M \neq G$. If $\langle S \rangle \neq G$, then $\langle S \rangle$ lies in a maximal subgroup by property 1 or 2.
8. Frattini subgroup. The intersection of all maximal subgroups of $G$ is the [[Frattini subgroup|KXJG5VV340]] $\Phi(G)$, with $\Phi(G) = G$ when $G$ has no maximal subgroup. For $\mathbb{Z}/12\mathbb{Z}$, it is $\langle 2 \rangle \cap \langle 3 \rangle = \langle 6 \rangle = \{0, 6\}$.
9. Images under isomorphisms. An [[isomorphism|08MG7H8JW5]] $f : G \to G'$ sends maximal subgroups of $G$ to maximal subgroups of $G'$, because it is a bijection between the subgroups of $G$ and of $G'$ that preserves inclusion. In particular, a conjugate $gMg^{-1}$ of a maximal subgroup is maximal.

### Common errors

1. A student thinks that a maximal subgroup has the largest order among the proper subgroups. The maximal subgroups of $S_4$ have orders $6$, $8$ and $12$, and those of $S_3$ have orders $2$ and $3$.
2. A student confuses "maximal" with "largest". In $\mathbb{Z}/12\mathbb{Z}$, neither of the maximal subgroups $\langle 2 \rangle$ and $\langle 3 \rangle$ contains the other, so there is no largest proper subgroup.
3. A student assumes that every nontrivial group has a maximal subgroup. The group $\mathbb{Q}$ has none.
4. A student assumes that a maximal subgroup is normal. In $S_3$, the subgroup $\{e, (1\,2)\}$ is maximal but not normal, since $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$.

## Explanations

### L1 human

Think of the subgroups of a group as boxes, where a smaller box can fit inside a larger one.
The whole group is the largest box.
A maximal subgroup is a box that is just below the whole group: no other box fits between them.
For example, in the integers, the even numbers form a maximal subgroup, and the multiples of $4$ do not, because the even numbers lie between them and the integers.

### L2 human

We find the maximal subgroups of $G = \mathbb{Z}/72\mathbb{Z}$.

1. The number $72 = 2^3 \cdot 3^2$ has the prime divisors $2$ and $3$.
2. By property 6, the maximal subgroups are $\langle 2 \rangle$, of index $2$ and order $36$, and $\langle 3 \rangle$, of index $3$ and order $24$.
3. The subgroup $\langle 4 \rangle$, of order $18$, is not maximal, because $\langle 4 \rangle \subsetneq \langle 2 \rangle \subsetneq G$.
4. The Frattini subgroup is $\langle 2 \rangle \cap \langle 3 \rangle = \langle 6 \rangle$, of order $12$.
5. By property 7, an element $a$ generates $G$ exactly when $a \notin \langle 2 \rangle$ and $a \notin \langle 3 \rangle$, that is, when $\gcd(a, 72) = 1$.

The typical use of maximal subgroups is in such generation tests, and in inductive proofs about finite groups that pass from $G$ to a maximal subgroup.
A trap: the existence of maximal subgroups needs finiteness or finite generation, and it fails for $\mathbb{Q}$.

### L3 human

Maximal subgroups correspond to primitive actions.
If $G$ acts transitively on a set $X$ with at least two points, then the action is primitive exactly when the stabilizer of a point is a maximal subgroup.
So the study of maximal subgroups of finite simple groups is the study of their [[primitive|Y10S0751KG]] permutation representations.
For the finite classical groups, Aschbacher's theorem divides the maximal subgroups into a small number of geometric classes and one class of almost simple groups.

The existence argument with Zorn's lemma is the same as the proof that a ring with identity has a maximal ideal.
In both cases, finite generation, by the generators or by the element $1$, keeps the union of a chain proper.
In the quotient, property 4 says that $G/M$ is a simple abelian group, just as $R/\mathfrak{m}$ is a field for a maximal ideal $\mathfrak{m}$ of a commutative ring $R$.
The [[Frattini subgroup|KXJG5VV340]] is the set of elements that lie in every maximal subgroup, and for a finitely generated group it is the set of elements that can be removed from every generating set.
