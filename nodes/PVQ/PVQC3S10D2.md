---
tag: PVQC3S10D2
kind: statement
role: theorem
name: The number of conjugates of a subgroup is the index of its normaliser
msc: ["20E45"]
topics: [E1506A5A55]
audience: ug1
about: [0H11ZPX4ND, 0YGN3VAA0D]
uses: [0H11ZPX4ND, 0YGN3VAA0D, 0DTXBQPA2S, 03DEH43F4H]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy of subgroups and general subsets
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
    locator: Definitions
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Let $N_G(H) = \{g \in G : gHg^{-1} = H\}$ be the [[normaliser|0YGN3VAA0D]] of $H$ in $G$.
Then the map
$$gN_G(H) \mapsto gHg^{-1}$$
is a well defined bijection from the set of [[left cosets|03DEH43F4H]] of $N_G(H)$ in $G$ to the set of [[conjugate subgroups|0H11ZPX4ND]] of $H$ in $G$.
In particular, the number of conjugates of $H$ in $G$ is the [[index|0DTXBQPA2S]] $[G : N_G(H)]$.

## Remarks

### Why each hypothesis is needed

The statement has no hypothesis on $G$ or $H$.
The group $G$ can be infinite, and then the number of conjugates and the index are equal as cardinal numbers.
The statement needs $H$ to be a subgroup only for the words "conjugate subgroups".
The same proof works for each subset $S$ of $G$, with $N_G(S) = \{g : gSg^{-1} = S\}$.
The normaliser cannot be replaced by $H$.
In $S_3$, the subgroup $A_3$ has index $2$, but it has only $1$ conjugate, because $N_{S_3}(A_3) = S_3$.

### Consequences

- If $G$ is finite, then the number of conjugates of $H$ is $|G| / |N_G(H)|$, by the [[index formula|04DC0SRN2K]] $|G| = [G : K] \, |K|$ for a subgroup $K$.
- Since $H \le N_G(H) \le G$, the number of conjugates of $H$ divides $[G : H]$ when $G$ is finite, by the [[tower law|0ZQJ7KEFQ5]].
- $H$ is [[normal|0CB0DX5BVV]] in $G$ exactly when it has one conjugate, that is, when $N_G(H) = G$.
- The number of Sylow $p$-subgroups of a finite group is the index of the normaliser of one of them, because the Sylow $p$-subgroups are conjugate ([[number of Sylow subgroups|09ZJ6CAK7S]]).

### Converse

The statement is an equality, so it has no separate converse.
It does not say which subgroups are conjugate to $H$.
Two subgroups of the same order need not be conjugate ([[isomorphic but not conjugate subgroups|1VVKMP89VA]]).

### Generalizations

The statement is the [[orbit-stabiliser theorem|0E2HSCKZ6C]] for the action of $G$ on its subgroups by conjugation.
The orbit of $H$ is the set of its conjugates, and the stabiliser of $H$ is $N_G(H)$.
For a single element $a$, the same argument shows that the size of the [[conjugacy class|0DEBXAJ5SA]] of $a$ is the index of its [[centraliser|02YYV36BFM]].

## History

Counts of conjugate subgroups by the index of a normaliser are standard in the theory of finite groups.
They appear in the proofs and in the applications of the Sylow theorems, for example in the count of Sylow subgroups.

## Explanations

### L1 human

Conjugation moves a subgroup to other places in the group.
Some elements do not move it at all, and these elements form the normaliser.
Two elements give the same new place exactly when they differ by an element of the normaliser.
So the number of places is the number of cosets of the normaliser, which is its index.

### L2 human

We count the conjugates of $H = \{e, (1\,2)\}$ in $S_3$, with composition from right to left.
Its normaliser is $H$ itself, so the theorem predicts $[S_3 : H] = 3$ conjugates.
The conjugates are $\{e, (1\,2)\}$, $\{e, (1\,3)\}$ and $\{e, (2\,3)\}$, as in [[the three subgroups of order two of S3 are conjugate|NGZY27YSWE]].
Each conjugate comes from a coset of $H$: for example, all of $(2\,3)H = \{(2\,3), (1\,3\,2)\}$ give $\{e, (1\,3)\}$.

The theorem gives the number of conjugates without a list of them.
In a group of order $60$, a subgroup with normaliser of order $12$ has $5$ conjugates.
A common error is to use $[G : H]$ in place of $[G : N_G(H)]$.
The two numbers agree only when $N_G(H) = H$.

### L3 human

Let $G$ act on the set of its subgroups by $g \cdot H = gHg^{-1}$.
The theorem is the orbit-stabiliser bijection for this action.
The same bijection $G/N_G(H) \to \{gHg^{-1}\}$ is a map of $G$-sets, where $G$ acts on the left cosets by left multiplication.
In algebraic geometry and Lie theory, the conjugates of a subgroup often form a geometric space.
For example, the conjugates of the upper triangular subgroup of $\mathrm{GL}_2(\mathbb{R})$ correspond to the lines through the origin of $\mathbb{R}^2$ ([[conjugate triangular subgroups|MXTMGWMERC]]).
