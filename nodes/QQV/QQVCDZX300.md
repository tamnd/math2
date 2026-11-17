---
tag: QQVCDZX300
kind: concept
name: Transversal of a subgroup
aliases: [left-transversal, right-transversal, common-transversal, system-of-coset-representatives]
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: grad
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0DTXBQPA2S, 08WCB90WND, DSBE321XMS, W0SW2ATN1Y, 0ZQJ7KEFQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Transversal_(combinatorics)
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem
    locator: Applications
---

## Summary

Let $G$ be a [[group|G5S1M9]], and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
A left transversal of $H$ in $G$ is a subset $T \subseteq G$ that contains exactly one element of each [[left coset|03DEH43F4H]] of $H$.
A right transversal of $H$ is a subset that contains exactly one element of each [[right coset|0NE1DK7H4T]] of $H$.
A common transversal, or two-sided transversal, is a set that is both a left and a right transversal of $H$.
Each transversal has $[G : H]$ elements, where $[G : H]$ is the [[index|0DTXBQPA2S]].
A transversal turns statements about cosets into statements about elements.
It is the tool behind the transfer and the Schreier generators of a subgroup.

## Motivation

To compute with the cosets of $H$, we need a name for each coset.
The natural name is one element of the coset, its representative.
For $n\mathbb{Z}$ in $\mathbb{Z}$, the remainders $0, 1, \ldots, n - 1$ are the usual names.
A transversal is a full set of names, one for each coset.
With a left transversal $T$, each $g \in G$ has a unique form $g = th$ with $t \in T$ and $h \in H$.
This unique form lets us write the action of $G$ on the cosets as a computation inside $G$.

## Notation

A transversal is also called a system of coset representatives or a set of coset representatives.
For a left transversal $T$ and $g \in G$, many books write $\overline{g}$ for the element of $T$ in the coset $gH$.
Books that use right cosets as the standard often call a right transversal simply a transversal.
In combinatorics, a [[transversal|1ADDR1N29W]] of a family of sets is a set of distinct representatives, one for each set of the family.
A left transversal of $H$ is a transversal, in this sense, of the family of left cosets of $H$.

## Remarks

### Examples

- In $(\mathbb{Z}, +)$, the set $\{0, 1, \ldots, n - 1\}$ is a transversal of $n\mathbb{Z}$, as [[this example|H3RX5PD834]] shows. Each set of $n$ integers with distinct remainders modulo $n$ is also a transversal.
- In the [[symmetric group|0515A6D2Y1]] $S_3$ with $H = \{e, (1\,2)\}$, the set $\{e, (1\,2\,3), (2\,3)\}$ is a left transversal but not a right transversal, as [[this example|XKZN7YVNF8]] shows.
- In $S_3$, the [[alternating group|0Z5905Q73D]] $A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$ is a common transversal of $H = \{e, (1\,2)\}$.
- In the [[direct product|00HF4RJ5QN]] $G = H \times K$, the subgroup $\{e\} \times K$ is a common transversal of $H \times \{e\}$.
- In $(\mathbb{R}, +)$, the interval $[0, 1)$ is a transversal of $\mathbb{Z}$. The coset $x + \mathbb{Z}$ meets $[0, 1)$ only in $x - \lfloor x \rfloor$, where $\lfloor x \rfloor$ is the [[floor|08GR54CKEA]] of $x$.

### Non-examples

- In $S_3$, the set $\{(1\,2\,3), (1\,3\,2), (2\,3)\}$ has $3 = [S_3 : H]$ elements, but it is neither a left nor a right transversal of $H = \{e, (1\,2)\}$, as [[this example|KJBM9C3RF3]] shows.
- In $\mathbb{Z}$, the set $\{0, 1, 3\}$ is not a transversal of $3\mathbb{Z}$. The elements $0$ and $3$ lie in the same coset, and no element lies in $2 + 3\mathbb{Z}$.

### Basic properties

- **Size.** The map $t \mapsto tH$ from a left transversal $T$ to $G/H$ is a bijection, by the definition. Thus $|T| = [G : H]$.
- **Unique factorisation.** Let $T$ be a left transversal. Each $g \in G$ is $g = th$ with unique $t \in T$ and $h \in H$. Here $t$ is the element of $T$ in $gH$, and $h = t^{-1}g$.
- **Inverses.** If $T$ is a left transversal, then $T^{-1} = \{t^{-1} : t \in T\}$ is a right transversal. Indeed, the right coset $Hy$ is the set of inverses of the left coset $y^{-1}H$. The set $y^{-1}H$ contains exactly one $t \in T$, so $Hy$ contains exactly one element $t^{-1}$ of $T^{-1}$.
- **Existence.** Each subgroup has a left transversal. For finite index this needs only finitely many choices. For infinite index the general case uses the [[axiom of choice|0HTGB13FE2]] through a [[choice function|0FWBQ53MPJ]] on the set of cosets.
- **Representative of the identity coset.** If $T$ is a left transversal and $t_0 \in T \cap H$, then $(T \setminus \{t_0\}) \cup \{e\}$ is again a left transversal. Thus we can always choose $e \in T$.
- **Common transversals, finite groups.** Let $G$ be finite. Then each subgroup $H$ has a common transversal. The proof below uses [[Hall's marriage theorem|08WCB90WND]].
- **Common transversals, finite index.** Let $[G : H]$ be finite, with $G$ possibly infinite. Then $H$ has a common transversal. The proof below uses double cosets.

### Proof that a finite group has a common transversal

Let $G$ be finite, let $n = [G : H]$, let $L_1, \ldots, L_n$ be the left cosets and $R_1, \ldots, R_n$ the right cosets of $H$.

1. For each $i$, let $S_i$ be the set of right cosets $R_j$ that meet $L_i$.
2. Let $I \subseteq \{1, \ldots, n\}$ have $k$ elements. Let $U$ be the union of the $L_i$ with $i \in I$. The left cosets are disjoint with $|H|$ elements each, so $|U| = k|H|$.
3. The right cosets that meet $U$ cover $U$, because the right cosets cover $G$. Each has $|H|$ elements.
4. Thus at least $k$ right cosets meet $U$. These are the members of $\bigcup_{i \in I} S_i$, so this union has at least $k$ members.
5. By Hall's marriage theorem, there is an injective map $\sigma$ with $R_{\sigma(i)} \in S_i$ for each $i$. It is a bijection of $\{1, \ldots, n\}$, because it is injective on a finite set.
6. For each $i$, choose $t_i \in L_i \cap R_{\sigma(i)}$. This set is not empty, by step 1 and step 5.
7. The set $T = \{t_1, \ldots, t_n\}$ meets each $L_i$ only in $t_i$, because the left cosets are disjoint.
8. The set $T$ meets each $R_j$ only in $t_{\sigma^{-1}(j)}$, because $\sigma$ is a bijection and the right cosets are disjoint.

Thus $T$ is a common transversal.

### Proof that a subgroup of finite index has a common transversal

Let $n = [G : H]$ be finite.
The step 2 count above fails when $H$ is infinite, so we use the $(H, H)$ [[double cosets|DSBE321XMS]] $D = HgH$.

1. The double cosets partition $G$. Each $D = HgH$ is a union of left cosets $hgH$ and a union of right cosets $Hgh$, with $h \in H$.
2. Each left coset in $D$ meets each right coset in $D$. Indeed, a left coset in $D$ is $h_1gH$ and a right coset in $D$ is $Hgh_2$. Both contain $h_1gh_2$.
3. The left cosets $hgH$ in $D$ are in bijection with $H / (H \cap gHg^{-1})$, because $hgH = h'gH$ exactly when $h^{-1}h' \in gHg^{-1}$.
4. We have $Hgh = Hgh'$ exactly when $h h'^{-1} \in g^{-1}Hg$. Thus the right cosets in $D$ are in bijection with $(H \cap g^{-1}Hg) \backslash H$.
5. Put $K = gHg^{-1}$. Conjugation by $g$ maps the left cosets of $H$ onto the left cosets of $K$, so $[G : K] = n$.
6. By [[Poincaré's theorem|W0SW2ATN1Y]], $[G : H \cap K]$ is finite. The [[tower law|0ZQJ7KEFQ5]] gives $n \, [H : H \cap K] = [G : H \cap K] = n \, [K : H \cap K]$.
7. Thus $[H : H \cap K] = [K : H \cap K]$. Conjugation by $g^{-1}$ maps $K$ to $H$ and $H \cap K$ to $g^{-1}Hg \cap H$, so $[K : H \cap K] = [H : H \cap g^{-1}Hg]$.
8. By steps 3, 4 and 7, $D$ contains the same finite number of left cosets and of right cosets.
9. Pair the left cosets in $D$ with the right cosets in $D$ by any bijection. In each pair choose one element of the intersection, which exists by step 2.
10. Do this for each of the finitely many double cosets, and let $T$ be the set of the chosen elements.
11. Each left coset $L$ lies in exactly one double coset and in exactly one pair. So $L$ contains the element chosen for that pair.
12. Each other chosen element lies in a different left coset, so it is not in $L$. Thus $L$ contains exactly one element of $T$.
13. The same argument holds for each right coset.

Thus $T$ is a common transversal.

### History

Philip Hall proved his marriage theorem in 1935.
The existence of a common transversal of the left and right cosets of a subgroup of finite index is a standard application of it.
Otto Schreier used transversals in 1927 in his proof that each subgroup of a free group is free.

### Common errors

- A set with $[G : H]$ elements is not always a transversal. It must meet each coset, as the non-examples show.
- A left transversal is in general not a right transversal. The two notions agree for each transversal exactly when the left and right cosets are the same sets, that is, when $H$ is [[normal|0CB0DX5BVV]].
- A transversal is in general not a subgroup. A transversal that is a subgroup is a complement of $H$, such as $A_3$ for $\{e, (1\,2)\}$ in $S_3$, and many subgroups have no complement.

## Explanations

### L1 human

Sort the whole numbers by their remainder after division by $5$.
There are five classes.
To talk about the classes, we pick one number from each class as its name.
The usual choice is $0, 1, 2, 3, 4$, but $5, 6, 7, 8, 9$ or $10, 1, 22, 3, 14$ work too.
Such a set of names, one from each class, is a transversal.
The only rule is that each class gets exactly one name.

### L2 human

We find all left transversals of $H = \{e, (1\,2)\}$ in $S_3$ that contain $e$, with permutations composed from right to left.

1. The left cosets are $H$, $(1\,3)H = \{(1\,3), (1\,2\,3)\}$ and $(2\,3)H = \{(2\,3), (1\,3\,2)\}$.
2. A left transversal that contains $e$ takes $e$ from $H$.
3. It takes $(1\,3)$ or $(1\,2\,3)$ from the second coset, and $(2\,3)$ or $(1\,3\,2)$ from the third coset.
4. Thus there are $2 \cdot 2 = 4$ such sets: $\{e, (1\,3), (2\,3)\}$, $\{e, (1\,3), (1\,3\,2)\}$, $\{e, (1\,2\,3), (2\,3)\}$ and $\{e, (1\,2\,3), (1\,3\,2)\}$.
5. The right cosets are $H$, $H(1\,3) = \{(1\,3), (1\,3\,2)\}$ and $H(2\,3) = \{(2\,3), (1\,2\,3)\}$.
6. Thus the first and the fourth set are common transversals.
7. The second and the third set are not right transversals.

The typical use is the unique form $g = th$.
For each $g \in G$ and $t \in T$, the element $gt$ lies in a coset $t'H$, so $gt = t'h$ with $t' \in T$ and $h \in H$.
The map $t \mapsto t'$ is the permutation of $G/H$ given by $g$, and the elements $h$ record the rest of the information.

A trap is to forget that the result can depend on the choice of $T$.
Each construction with a transversal must be checked to be independent of $T$, or the choice must be fixed.

### L3 human

The pairs $(t', h)$ in $gt = t'h$ define a homomorphism from $G$ to the [[wreath product|W1X984PKJ9]] of $H$ with the symmetric group on $G/H$.
This is the monomial representation of $G$ induced from $H$.
Composing it with the map from $H$ to its [[abelianisation|0AQZV0905N]], and multiplying the $n$ factors, gives the [[transfer homomorphism|3R2Y906QAQ]] $G \to H / [H, H]$.
The transfer does not depend on the choice of the transversal, but its computation uses one.

Schreier's lemma is the second main use.
Let $G$ be generated by a set $S$, and let $R$ be a right transversal of $H$ with $e \in R$.
For $g \in G$, let $\overline{g}$ be the element of $R$ in $Hg$.
Then $H$ is generated by the Schreier generators $rs \, (\overline{rs})^{-1}$ with $r \in R$ and $s \in S$.
Thus a subgroup of index $n$ in a group with $d$ generators has at most $nd$ generators, and this leads to the [[Nielsen-Schreier theorem|W97X7WX5G8]].

The existence of common transversals is a matching problem on the bipartite graph of left and right cosets, so it belongs also to combinatorics.
