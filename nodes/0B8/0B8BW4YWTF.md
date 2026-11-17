---
tag: 0B8BW4YWTF
kind: concept
name: Lattice of subgroups
aliases: [subgroup-lattice]
msc: ["20E15", "06C05"]
topics: [BAVE5RN4EE]
audience: ug2
uses: [G5S1M9, 0X1JXT47GA, 0ZTGMDNVTB, 0RP7VWQ0YN, WH4SFAACAS, D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_of_subgroups
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Lattice_of_subgroups
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 2.5
same_as:
  wikidata: Q3538331
  wikipedia: Lattice of subgroups
---

## Summary

Let $G$ be a [[group|G5S1M9]].
The lattice of subgroups of $G$ is the set $\operatorname{Sub}(G)$ of all [[subgroups|0X1JXT47GA]] of $G$, [[partially ordered|0QV2JS9RJ3]] by inclusion.
It is a [[complete lattice|D7A0ZGZT5S]]: each family $(H_i)_{i \in I}$ of subgroups has a greatest lower bound and a least upper bound.
The greatest lower bound (the meet) is the [[intersection|0ZTGMDNVTB]] $\bigcap_i H_i$.
The least upper bound (the join) is the [[subgroup generated|0RP7VWQ0YN]] by the union, $\langle \bigcup_i H_i \rangle$.
The least element is $\{e\}$, and the greatest element is $G$.
The lattice of subgroups shows at one view how all the subgroups of $G$ fit together, and many properties of $G$ can be read from its shape.

## Motivation

A group can have many subgroups, and we want to see how they fit together.
Inclusion is the natural order: one subgroup can lie inside another.
Two subgroups $H$ and $K$ give two new subgroups at once: the largest subgroup inside both, and the smallest subgroup that contains both.
The first is $H \cap K$, and the second is $\langle H \cup K \rangle$.
A partially ordered set in which each pair has such a meet and join is a [[lattice|WH4SFAACAS]].
For a small group we draw the lattice as a [[Hasse diagram|00EYM7MDKS]], and the picture shows the subgroups and their inclusions at once.
For the cyclic group $\mathbb{Z}/12$, the picture is the picture of the divisors of $12$.

## Notation

We write $\operatorname{Sub}(G)$ or $L(G)$ for the lattice of subgroups.
For two subgroups, the meet is $H \wedge K = H \cap K$ and the join is $H \vee K = \langle H, K \rangle = \langle H \cup K \rangle$.
A subgroup $K$ covers a subgroup $H$ when $H < K$ and no subgroup $M$ has $H < M < K$.
In a Hasse diagram, we draw $K$ above $H$ and join them by a line exactly when $K$ covers $H$.
In this node we describe each Hasse diagram by the list of its covering relations $H \prec K$.

## Remarks

### Examples

1. The subgroups of $(\mathbb{Z}, +)$ are the sets $n\mathbb{Z}$ with $n \geq 0$, by [[the classification of the subgroups of the integers|0SRATCFF1W]]. We have $m\mathbb{Z} \subseteq n\mathbb{Z}$ exactly when $n$ divides $m$. The meet is $m\mathbb{Z} \cap n\mathbb{Z} = \operatorname{lcm}(m, n)\mathbb{Z}$, and the join is $m\mathbb{Z} + n\mathbb{Z} = \gcd(m, n)\mathbb{Z}$.
2. [[The lattice of subgroups of $\mathbb{Z}/12$|~5a3b5ce9]] has $6$ elements, one for each divisor of $12$, and it is [[distributive|0HM0HQCK6N]].
3. [[The lattice of subgroups of $S_3$|~d0edf00c]] has $6$ elements: $\{e\}$, four subgroups of prime order, and $S_3$. It is [[modular|QX7WZ92QAK]] but not distributive.
4. [[The lattice of subgroups of $D_4$|~bd61a465]] has $10$ elements, and it is not modular.
5. The [[quaternion group|0NRJGW864D]] $Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ has $6$ subgroups: $\{1\}$, $\{\pm 1\}$, $\langle i \rangle = \{\pm 1, \pm i\}$, $\langle j \rangle$, $\langle k \rangle$ and $Q_8$. The covering relations are $\{1\} \prec \{\pm 1\}$, $\{\pm 1\} \prec \langle i \rangle, \langle j \rangle, \langle k \rangle$, and $\langle i \rangle, \langle j \rangle, \langle k \rangle \prec Q_8$. Each subgroup is normal: $\{\pm 1\}$ is the [[centre|0DZ93493VN]], and the subgroups of order $4$ have index $2$. So the lattice is modular by basic property 4. It is not distributive: $\langle i \rangle \wedge (\langle j \rangle \vee \langle k \rangle) = \langle i \rangle$, but $(\langle i \rangle \wedge \langle j \rangle) \vee (\langle i \rangle \wedge \langle k \rangle) = \{\pm 1\}$.
6. The [[Klein four-group|0PMRQJVTME]] $V = \{e, a, b, c\}$ has $5$ subgroups. The covering relations are $\{e\} \prec \langle a \rangle, \langle b \rangle, \langle c \rangle$ and $\langle a \rangle, \langle b \rangle, \langle c \rangle \prec V$.

### Non-examples

1. [[The cyclic subgroups of the Klein four-group do not form a lattice|~5c428a06]]. Two of the subgroups of order $2$ have no upper bound among the cyclic subgroups.
2. The proper subgroups of $S_3$ do not form a lattice under inclusion. The subgroups $\langle (1\,2) \rangle$ and $\langle (1\,3) \rangle$ have no common upper bound among them, because together they generate $S_3$.
3. The lattice of subgroups is not a sublattice of the lattice of all subsets of $G$, because the join is not the union. In $\mathbb{Z}$, the set $2\mathbb{Z} \cup 3\mathbb{Z}$ is not a subgroup, since $2 + 3 = 5$ is in neither set. The join is $2\mathbb{Z} + 3\mathbb{Z} = \mathbb{Z}$.

### Basic properties

1. $\operatorname{Sub}(G)$ is a complete lattice. An intersection of subgroups is a subgroup, and it is the largest subgroup inside each $H_i$. A subgroup that contains each $H_i$ contains their union, so it contains $\langle \bigcup_i H_i \rangle$, and this makes $\langle \bigcup_i H_i \rangle$ the least upper bound.
2. If the [[product|0PT52XQZD7]] $HK = \{hk : h \in H, \ k \in K\}$ is a subgroup, then $H \vee K = HK$. This holds when $H$ or $K$ is [[normal|0CB0DX5BVV]], and always in an abelian group, where $H \vee K = H + K$.
3. Dedekind's modular law: let $A$, $B$ and $C$ be subgroups of $G$ with $A \leq C$. Then $A(B \cap C) = AB \cap C$ as sets. The proof is below.
4. The normal subgroups of $G$ form a sublattice of $\operatorname{Sub}(G)$, with meet $M \cap N$ and join $MN$. This lattice is modular, by property 3. So $\operatorname{Sub}(G)$ is modular when every subgroup is normal, for example when $G$ is abelian.
5. For a normal subgroup $N$, the [[correspondence theorem|0S9ZVZ34MD]] gives an isomorphism between $\operatorname{Sub}(G/N)$ and the interval of subgroups $H$ with $N \leq H \leq G$.
6. For the cyclic group $\mathbb{Z}/n$, the map $d \mapsto \langle d \rangle$ is a bijection from the positive divisors of $n$ to the subgroups, by the [[fundamental theorem of cyclic groups|0423TXR9AN]]. It reverses divisibility: $\langle d \rangle \leq \langle d' \rangle$ exactly when $d'$ divides $d$.
7. The lattice does not determine the group. For each prime $p$, the lattice of $\mathbb{Z}/p$ has exactly two elements, $\{0\}$ and $\mathbb{Z}/p$.

### Proof of the modular law

Let $A$, $B$ and $C$ be subgroups of $G$ with $A \leq C$.

1. Let $x \in A(B \cap C)$, so $x = ab$ with $a \in A$ and $b \in B \cap C$. Then $x \in AB$.
2. Also $a \in A \subseteq C$ and $b \in C$, so $x = ab \in C$. So $A(B \cap C) \subseteq AB \cap C$.
3. Conversely, let $x \in AB \cap C$, so $x = ab$ with $a \in A$ and $b \in B$, and $x \in C$.
4. Then $b = a^{-1} x$. Here $a^{-1} \in A \subseteq C$ and $x \in C$, so $b \in C$.
5. So $b \in B \cap C$, and $x = ab \in A(B \cap C)$. This gives $AB \cap C \subseteq A(B \cap C)$.
6. Now let $B$ be normal. Then $B \cap C$ is normal in $C$, so $A(B \cap C)$ is a subgroup, and $AB$ is a subgroup. By property 2, $A \vee (B \wedge C) = A(B \cap C)$ and $(A \vee B) \wedge C = AB \cap C$.
7. By steps 1 to 6, $A \vee (B \wedge C) = (A \vee B) \wedge C$. This is the modular law of lattices for these three subgroups.

For three normal subgroups, step 6 applies, so the lattice of normal subgroups is modular.
The set equation of steps 1 to 5 holds for all subgroups, but in general $AB$ is not the join $A \vee B$, and the modular law can fail, as for $D_4$.

### History

Richard Dedekind studied lattices in 1897 and 1900 under the name "Dualgruppen", and he found the modular law in lattices of modules of numbers.
The name "modular" comes from these modules.
Øystein Ore proved in 1938 that a group has a distributive lattice of subgroups exactly when it is [[locally cyclic|RXWA8TF2RM]].

### Common errors

1. A student takes the union of two subgroups as their join. The union is usually not a subgroup, as non-example 3 shows.
2. A student takes the product set $HK$ as the join when neither subgroup is normal. In $S_3$, with products read from right to left, the set $\langle (1\,2) \rangle \langle (1\,3) \rangle = \{e, (1\,2), (1\,3), (1\,3\,2)\}$ has $4$ elements, so it is not a subgroup, by [[Lagrange's theorem|3C53TD]]. The join is $S_3$.
3. A student draws a line in a Hasse diagram for each inclusion. A line goes only from $H$ to a subgroup that covers $H$. The inclusion $\{0\} \leq \mathbb{Z}/12$, for example, has no line of its own.

## Explanations

### L1 human

The subgroups of a group can be drawn as a family tree.
Each subgroup is a dot, and a line goes up from a subgroup to each next larger subgroup that contains it.
Take the hours on a clock with $12$ hours, with addition.
The multiples of $2$, of $3$, of $4$ and of $6$ are subgroups, and so are $\{0\}$ and the whole clock.
The multiples of $6$ lie inside the multiples of $2$ and inside the multiples of $3$.
The picture has $6$ dots, one for each divisor of $12$.
For any two dots, there is a largest dot below both and a smallest dot above both.

### L2 human

We compute the meet and the join of $H = \langle 4 \rangle$ and $K = \langle 6 \rangle$ in $\mathbb{Z}/12$.

1. The multiples of $4$ modulo $12$ are $4, 8, 0$, so $H = \{0, 4, 8\}$.
2. The multiples of $6$ modulo $12$ are $6, 0$, so $K = \{0, 6\}$.
3. The meet is $H \cap K = \{0\}$.
4. The join contains $4$ and $6$, so it contains $6 - 4 = 2$. So $\langle 2 \rangle \leq H \vee K$.
5. Both $4$ and $6$ are multiples of $2$, so $H \vee K \leq \langle 2 \rangle$.
6. So $H \vee K = \langle 2 \rangle = \{0, 2, 4, 6, 8, 10\}$, and $2 = \gcd(4, 6)$.

The typical use of the lattice is a quick overview of all subgroups.
For example, the lattice of $G/N$ is the part of the lattice of $G$ above $N$, and the lattice of a cyclic group is the lattice of divisors.

A trap: the join of two subgroups can be much larger than their union.
In step 6, the union $H \cup K = \{0, 4, 6, 8\}$ has $4$ elements, but the join has $6$.

### L3 human

The lattice of subgroups is a basic example of an algebraic lattice: each element is a join of compact elements, and the compact elements are the finitely generated subgroups.
The lattices of submodules, of ideals and of normal subgroups are modular, by the same argument as Dedekind's law.
In a modular lattice of finite length, all maximal chains have the same length, and this gives a lattice form of the [[Jordan-Hölder theorem|0E088ZP533]] and of the [[Schreier refinement theorem|QQAWHC9X60]].

The shape of $\operatorname{Sub}(G)$ carries information about $G$.
By Ore's theorem, the lattice is distributive exactly when $G$ is locally cyclic.
By the correspondence theorem, the lattice of a quotient $G/N$ is the interval above $N$.
In Galois theory, the lattice of subgroups of a finite Galois group is the lattice of intermediate fields, with the order reversed.
The subgroups that $G$ covers in the Hasse diagram are the [[maximal subgroups|~1e0593e6]].
Their intersection is the [[Frattini subgroup|KXJG5VV340]], which controls the minimal number of generators of a finite $p$-group.
