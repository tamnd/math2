---
tag: TDCGM4WR88
kind: definition
name: Tietze transformations
msc: [20F05]
defines: CEZTVHC1KS
uses: [0JGEQXQ4AC, 0KTW26C80J, 6XM4CCVTKE, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Tietze_transformations
---

## Definition

Let $\langle S \mid R \rangle$ be a [[group presentation|0JGEQXQ4AC]], with $R$ a subset of the [[free group|0KTW26C80J]] $F(S)$.
Let $N(R)$ be the [[normal closure|6XM4CCVTKE]] of $R$ in $F(S)$.
The *Tietze transformations* are the following four operations.

1. Add a relation: replace $R$ by $R \cup \set{r}$, where $r \in N(R)$.
2. Remove a relation: replace $R$ by $R \setminus \set{r}$, where $r \in R$ lies in the normal closure of $R \setminus \set{r}$.
3. Add a generator: for a new symbol $x \notin S$ and a word $w \in F(S)$, replace $\langle S \mid R \rangle$ by $\langle S \cup \set{x} \mid R \cup \set{x w^{-1}} \rangle$.
4. Remove a generator: suppose $x \in S$ and $R$ contains a relation $x w^{-1}$, with $w$ a word in $S \setminus \set{x}$. Delete $x$ and this relation, and replace $x$ by $w$ in all other relations.

## Remarks

Each transformation yields a presentation of an [[isomorphic|08MG7H8JW5]] group.
Moves 1 and 2 keep $N(R)$ unchanged, and in moves 3 and 4 the added or removed letter equals an existing element.
Tietze's theorem: two finite presentations define isomorphic groups if and only if one is obtained from the other by a finite sequence of Tietze transformations.
Example: $\langle a, b \mid a b a^{-1} b^{-2},\ b \rangle$ becomes $\langle a \mid a a^{-1} \rangle$ by removing $b$ with $w = 1$, and then $\langle a \mid \ \rangle$ by removing the trivial relation; so it presents $\Z$.
Non-example: replacing $\langle a \mid a^2 \rangle$ by $\langle a \mid a^4 \rangle$ is not a Tietze transformation, since $a^2$ is not in the normal closure of $a^4$; indeed the groups $\Z/2$ and $\Z/4$ differ.
Tietze transformations do not give an algorithm for the [[group isomorphism problem|MP3F49QT3C]], which is undecidable for finite presentations.
