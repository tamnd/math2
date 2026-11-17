---
tag: 0PPP2J2DJV
kind: statement
role: theorem
name: Second isomorphism theorem
aliases: [diamond-isomorphism-theorem]
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0KYX2N69J0, 0CB0DX5BVV, 0PT52XQZD7]
uses: [0X1JXT47GA, 0CB0DX5BVV, 0ZTGMDNVTB, 0TXWV1JGG1, 0KYX2N69J0, 08MG7H8JW5, 0CXXJNG5B6]
formal:
  - system: lean4
    library: mathlib
    decl: QuotientGroup.quotientInfEquivProdNormalQuotient
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem B (groups)
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Note on numbers and names
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$.
Write $H \le G$ and $N \trianglelefteq G$.
Then the following hold.

1. The product $HN = \{hn : h \in H, n \in N\}$ is a subgroup of $G$.
2. $N$ is a normal subgroup of $HN$.
3. The [[intersection|0ZTGMDNVTB]] $H \cap N$ is a normal subgroup of $H$.
4. The formula $h(H \cap N) \mapsto hN$ gives a well defined [[isomorphism|08MG7H8JW5]]
$$H/(H \cap N) \cong HN/N.$$

The proof is in [[the proof of the second isomorphism theorem|3WFXXX5Y2Z]].

## Remarks

The theorem is often drawn as a diamond in the [[lattice of subgroups|0B8BW4YWTF]] of $G$:
$$
\begin{array}{ccccc}
 & & HN & & \\
 & \diagup & & \diagdown & \\
H & & & & N \\
 & \diagdown & & \diagup & \\
 & & H \cap N & &
\end{array}
$$
The theorem says that the two opposite sides $H$ over $H \cap N$ and $HN$ over $N$ give isomorphic quotient groups.
Part 1 is [[this statement|0TXWV1JGG1]].

### Why each hypothesis is needed

The hypothesis that $N$ is normal is needed for part 1.
In the [[symmetric group|0515A6D2Y1]] $S_3$, compose permutations from right to left, and let $H = \{e, (1\,2)\}$ and $N = \{e, (1\,3)\}$.
Then $(1\,2)(1\,3) = (1\,3\,2)$, so $HN = \{e, (1\,2), (1\,3), (1\,3\,2)\}$.
This set has $4$ elements, and $4$ does not divide $6$, so by [[Lagrange's theorem|3C53TD]] it is not a subgroup of $S_3$.

### Consequences

- The [[index|0DTXBQPA2S]] of $N$ in $HN$ equals the index of $H \cap N$ in $H$: $[HN : N] = [H : H \cap N]$.
- If $H$ and $N$ are finite, then $|HN| = |H|\,|N| / |H \cap N|$. This is a special case of the [[product formula|08PY4GNAPK]].
- In the integers, take $H = a\mathbb{Z}$ and $N = b\mathbb{Z}$ for positive integers $a$ and $b$. Then $H + N = d\mathbb{Z}$ with $d = \gcd(a, b)$, and $H \cap N = l\mathbb{Z}$ with $l = \operatorname{lcm}(a, b)$. The theorem gives $a\mathbb{Z}/l\mathbb{Z} \cong d\mathbb{Z}/b\mathbb{Z}$, so $l/a = b/d$ and $ab = \gcd(a, b) \cdot \operatorname{lcm}(a, b)$.
- In $S_4$, the [[Klein four-group|0PMRQJVTME]] $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is normal. With $H$ the copy of $S_3$ that fixes $4$, the theorem gives $S_4/V_4 \cong S_3$ (see L2 below).

### Converse

The converse is false: all four conclusions can hold when $N$ is not normal in $G$.
In $S_3$, take $H = N = \{e, (1\,2)\}$.
Then $HN = N$ is a subgroup, $N$ is normal in $HN$, $H \cap N = H$ is normal in $H$, and both quotients are trivial.
But $N$ is not normal in $S_3$, because $(1\,3)(1\,2)(1\,3)^{-1} = (2\,3)$ is not in $N$.

### Generalizations

The same proof works under the weaker hypothesis that $H$ normalises $N$, that is, $hNh^{-1} = N$ for each $h \in H$.
In other words, $H$ is a subgroup of the [[normaliser|0YGN3VAA0D]] $N_G(N)$.
Then $HN$ is a subgroup, $N \trianglelefteq HN$, $H \cap N \trianglelefteq H$, and $H/(H \cap N) \cong HN/N$.
For example, in $S_4$ the subgroup $N = \{e, (3\,4)\}$ is not normal, but $H = \{e, (1\,2)\}$ normalises it, because $(1\,2)$ and $(3\,4)$ commute.

The same theorem holds for rings, in the form $(S + I)/I \cong S/(S \cap I)$ for a subring $S$ and an ideal $I$.
It holds for modules and vector spaces, in the form $(U + W)/W \cong U/(U \cap W)$.

### Names

Books do not agree on the numbers of the isomorphism theorems, so this theorem can have a different number in other books.
Because of the picture above, it is also called the diamond isomorphism theorem.

## History

Emmy Noether stated the isomorphism theorems in general form, for modules, in a paper of 1927 in Mathematische Annalen.

## Explanations

### L1 human

Start with a subgroup $H$ and a normal subgroup $N$.
The quotient $HN/N$ looks at the elements of $HN$ and ignores the part that comes from $N$.
The quotient $H/(H \cap N)$ looks only at $H$, and ignores the part of $H$ that is also in $N$.
The theorem says that these two views give the same group.
For the integers, with $H = 4\mathbb{Z}$ and $N = 6\mathbb{Z}$, we get $H + N = 2\mathbb{Z}$ and $H \cap N = 12\mathbb{Z}$.
So $4\mathbb{Z}/12\mathbb{Z} \cong 2\mathbb{Z}/6\mathbb{Z}$, and both groups are cyclic of order $3$.

### L2 human

We show $S_4/V_4 \cong S_3$.
Compose permutations from right to left.

1. $V_4$ is normal in $S_4$, because it is the union of $\{e\}$ and the [[conjugacy class|0DEBXAJ5SA]] of $(1\,2)(3\,4)$. A union of conjugacy classes is closed under conjugation.
2. Let $H$ be the set of permutations in $S_4$ that fix $4$. Then $H \cong S_3$, and $|H| = 6$.
3. Each element of $V_4$ other than $e$ moves $4$. So $H \cap V_4 = \{e\}$.
4. By the theorem, $|HV_4| = |H|\,|V_4|/|H \cap V_4| = 6 \cdot 4/1 = 24$. So $HV_4 = S_4$.
5. The theorem gives $S_4/V_4 = HV_4/V_4 \cong H/(H \cap V_4) = H/\{e\} \cong S_3$.

The typical use is to compute a quotient $HN/N$, which can be hard to see, from the quotient $H/(H \cap N)$ of a smaller group.

A common error is to apply the theorem when neither $H$ nor $N$ is normal and $H$ does not normalise $N$.
Then $HN$ need not be a subgroup, as the example with $S_3$ above shows.
A second error is to write $HN/H$ in place of $HN/N$: the subgroup $H$ need not be normal in $HN$.

### L3 human

In the lattice of subgroups, $HN$ is the join $H \vee N$ and $H \cap N$ is the meet, when $N$ is normal.
The theorem then says that the interval from $H \cap N$ to $H$ and the interval from $N$ to $H \vee N$ give isomorphic quotients.
For vector spaces it gives $\dim(U + W) - \dim W = \dim U - \dim(U \cap W)$, which is the dimension formula for a sum of subspaces.
With the [[correspondence theorem|0S9ZVZ34MD]], the theorem shows that the interval from $H \cap N$ to $H$ and the interval from $N$ to $HN$ are isomorphic lattices.
This matches the diamond property of modular lattices, and the normal subgroups of a group form a modular lattice.
The theorem follows from the [[first isomorphism theorem|0CXXJNG5B6]] applied to the map $H \to HN/N$, $h \mapsto hN$.
