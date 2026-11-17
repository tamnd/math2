---
tag: 0S9ZVZ34MD
kind: statement
role: theorem
name: Correspondence theorem
aliases: [lattice-theorem, fourth-isomorphism-theorem]
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug2
about: [0KYX2N69J0, 0B8BW4YWTF]
uses: [0X1JXT47GA, 0CB0DX5BVV, 0KYX2N69J0, 0DTXBQPA2S, 0ZTGMDNVTB, 0RP7VWQ0YN, 0B8BW4YWTF]
sources:
  - url: https://en.wikipedia.org/wiki/Correspondence_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem D (groups)
same_as:
  wikidata: Q3527189
  wikipedia: Correspondence theorem
inventory: [Q72ADQWVHM]
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$, and let $\pi \colon G \to G/N$, $\pi(g) = gN$, be the projection to the [[quotient group|0KYX2N69J0]].
For a [[subgroup|0X1JXT47GA]] $M$ of $G$ with $N \subseteq M$, write $M/N = \pi(M) = \{mN : m \in M\}$.
Then the following hold.

1. The map $M \mapsto M/N$ is a bijection from the set of subgroups $M$ of $G$ with $N \subseteq M$ to the set of all subgroups of $G/N$. The inverse map sends a subgroup $Q$ of $G/N$ to its preimage $\pi^{-1}(Q) = \{g \in G : gN \in Q\}$.
2. For subgroups $M$ and $L$ of $G$ that contain $N$, we have $M \subseteq L$ if and only if $M/N \subseteq L/N$.
3. If $N \subseteq M \subseteq L$, then the [[indices|0DTXBQPA2S]] agree: $[L : M] = [L/N : M/N]$.
4. For a subgroup $M$ of $G$ that contains $N$, $M$ is normal in $G$ if and only if $M/N$ is normal in $G/N$.
5. For subgroups $M$ and $L$ of $G$ that contain $N$, we have $(M \cap L)/N = (M/N) \cap (L/N)$ and $\langle M \cup L \rangle/N = \langle (M/N) \cup (L/N) \rangle$.

By parts 2 and 5, the map $M \mapsto M/N$ is an isomorphism from the part of the [[lattice of subgroups|0B8BW4YWTF]] of $G$ above $N$ to the lattice of subgroups of $G/N$.

The proof is in [[the proof of the correspondence theorem|Y4WX4RKWY9]].

## Remarks

In part 5, $M \cap L$ is the [[intersection of subgroups|0ZTGMDNVTB]], and $\langle M \cup L \rangle$ is the [[subgroup generated|0RP7VWQ0YN]] by $M \cup L$.
In part 3, the indices can be infinite, and then the claim is that both indices are infinite.
For a normal subgroup $M$ with $N \subseteq M$, the [[third isomorphism theorem|0TJ1V9DDPC]] adds that $(G/N)/(M/N) \cong G/M$.

### Why each hypothesis is needed

- The condition $N \subseteq M$ is needed for part 1. In the integers, with $N = 2\mathbb{Z}$, the subgroups $3\mathbb{Z}$ and $\mathbb{Z}$ have the same image $\mathbb{Z}/2\mathbb{Z}$, because $3 + 2\mathbb{Z} = 1 + 2\mathbb{Z}$. So the map $M \mapsto \pi(M)$ is not injective on all subgroups.
- The condition $N \subseteq M$ is needed for part 4. In $S_3$, let $N = A_3$ and $M = \{e, (1\,2)\}$. Then $\pi(M)$ is all of $S_3/A_3$, because $(1\,2) \notin A_3$, so $\pi(M)$ is normal in $S_3/A_3$. But $M$ is not normal in $S_3$.
- The condition that $N$ is normal is needed for $G/N$ to be a group.

### Consequences

- The subgroups of $\mathbb{Z}/12\mathbb{Z}$ correspond to the subgroups of $\mathbb{Z}$ that contain $12\mathbb{Z}$. These are the subgroups $d\mathbb{Z}$ with $d$ a positive divisor of $12$ ([[subgroups of the integers|0SRATCFF1W]]). So $\mathbb{Z}/12\mathbb{Z}$ has exactly $6$ subgroups, one for each of $d = 1, 2, 3, 4, 6, 12$.
- The quotient $G/N$ is a [[simple group|0YMYMNQ0QZ]] if and only if $N \ne G$ and no normal subgroup $M$ of $G$ satisfies $N \subsetneq M \subsetneq G$. Such an $N$ is called a maximal normal subgroup.
- For a subgroup $M$ of $G$ that does not contain $N$, we get $\pi(M) = MN/N$. So the subgroup of $G/N$ that $M$ gives corresponds to $MN$, the smallest subgroup that contains $M$ and $N$.

### Converse

The subgroups of $G$ that are preimages of subgroups of $G/N$ are exactly the subgroups that contain $N$.
A preimage $\pi^{-1}(Q)$ always contains $\pi^{-1}(\{N\}) = N$.
Conversely, for each subgroup $M$ we get $\pi^{-1}(\pi(M)) = MN$, and this equals $M$ exactly when $N \subseteq M$.

### Generalizations

The same theorem holds for rings, where the ideals of $R/I$ correspond to the ideals of $R$ that contain $I$.
It holds for modules and vector spaces, where the submodules of $V/W$ correspond to the submodules of $V$ that contain $W$.

### Names

The theorem is also called the lattice theorem or the fourth isomorphism theorem.
Some books include it in the third isomorphism theorem.

## Explanations

### L1 human

The subgroups of a quotient group $G/N$ are the same as the subgroups of $G$ that contain $N$.
Passing to the quotient does not make new subgroups, and it does not lose the subgroups above $N$.
So the picture of the subgroups of $G$ above $N$ is a full picture of the subgroups of $G/N$.
The subgroups below $N$ all collapse to the trivial subgroup, and the theorem says nothing about them.

### L2 human

We find all subgroups of $G$ that contain $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$, for $G = S_4$.

1. $V_4$ is normal in $S_4$, and $S_4/V_4 \cong S_3$ by the [[second isomorphism theorem|0PPP2J2DJV]].
2. $S_3$ has exactly $6$ subgroups: the trivial subgroup, three subgroups of order $2$, the subgroup $A_3$ of order $3$, and $S_3$.
3. By part 1, $S_4$ has exactly $6$ subgroups that contain $V_4$.
4. By part 3, a subgroup $M \supseteq V_4$ has order $|M| = 4 \cdot |M/V_4|$. So their orders are $4$, $8$, $8$, $8$, $12$ and $24$.
5. These subgroups are $V_4$, three dihedral subgroups of order $8$, $A_4$ and $S_4$.
6. By part 4, the normal ones are $V_4$, $A_4$ and $S_4$, because the normal subgroups of $S_3$ are $\{e\}$, $A_3$ and $S_3$.

The typical use is to read off the subgroups of a quotient group from the subgroups of $G$, or the subgroups of $G$ above $N$ from a quotient that is easier to see.

A common error is to apply the correspondence to subgroups that do not contain $N$.
Such a subgroup $M$ goes to the same subgroup of $G/N$ as $MN$, so the information on $M$ is lost.

### L3 human

The theorem says that the projection $\pi$ gives a lattice isomorphism from the interval $[N, G]$ of the lattice of subgroups of $G$ to the lattice of subgroups of $G/N$.
It keeps the normal subgroups and the indices, so it is more than an isomorphism of ordered sets.
For any surjective homomorphism $\varphi \colon G \to H$, the same holds with $N = \ker \varphi$, by the [[first isomorphism theorem|0CXXJNG5B6]].
The theorem is the main tool to move between a group and its quotients, for example in the study of composition series.
The same statement holds for rings, modules and other algebraic structures, with the same proof.
