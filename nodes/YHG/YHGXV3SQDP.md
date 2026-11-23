---
tag: YHGXV3SQDP
kind: definition
name: Accessibility relation
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: XBCYFDPS2F
uses: [6BQ71KQ6QT, 05AVARPXA2, 0X8NMST0J2, 061J5VGSPT, 0GJZW9JFZQ, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Accessibility_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Definition

We name the relation of a Kripke frame and the properties of it that modal logic uses most.

Let $\mathfrak{F} = (W, R)$ be a [[Kripke frame|6BQ71KQ6QT]].
The [[binary relation|05AVARPXA2]] $R$ is the *accessibility relation* of $\mathfrak{F}$, and $v$ is *accessible* from $w$ when $w R v$.
For $w \in W$ we write $R[w] = \{ v \in W : w R v \}$.
The relation $R$ is called

1. [[reflexive|0X8NMST0J2]] when $w R w$ for every $w \in W$;
2. *serial* when every $w \in W$ has some $v$ with $w R v$;
3. [[symmetric|061J5VGSPT]] when $w R v$ implies $v R w$;
4. [[transitive|0GJZW9JFZQ]] when $w R v$ and $v R u$ imply $w R u$;
5. *Euclidean* when $w R v$ and $w R u$ imply $v R u$;
6. a *preorder* when it is reflexive and transitive;
7. an [[equivalence relation|0G8VEZ3WTK]] when it is reflexive, symmetric and transitive;
8. *universal* when $R = W \times W$.

## Notation

Frame classes are often named by the logics that they define: reflexive frames are $\mathsf{T}$-frames, preorders are $\mathsf{S4}$-frames, and equivalence relations are $\mathsf{S5}$-frames.
Seriality has its own page, [[seriality|NRNKV2YYWJ]].

## Remarks

### Reading the conditions

Conditions 1 to 5 are each about one or two steps along $R$.
Reflexivity and seriality ask for one successor: the world itself, or any world.
Symmetry and transitivity combine two steps on one path, and the Euclidean property compares two successors of the same world.
Conditions 6 to 8 are combinations, and each of them is stronger than the one before it.

Each of the five basic properties is a first-order condition on $R$, and each matches one axiom: $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$.
[[Common modal axiom schemata|FDFQFWPM4X]] proves the match, and the concept page [[accessibility relation|XBCYFDPS2F]] reads each property in words.

### A case that passes and a case that fails

The relation $R = \{ (a, b), (b, b) \}$ is Euclidean.
The world $a$ has only the successor $b$, so the condition asks for $b R b$, which holds, and the world $b$ gives the same check.
It fails symmetry, because $a R b$ holds and $b R a$ does not.
So a Euclidean relation need not be symmetric; see [[the Euclidean example|NS4AC3W4FM]].

## Explanations

### L1 human

The accessibility relation is the list of arrows between worlds.
Reflexive means every world has an arrow to itself.
Serial means every world has at least one arrow out.
Transitive means that two arrows in a row can be replaced by one arrow.
Euclidean means that two arrows out of the same world end at worlds that see each other.

### L2 human

We check seriality and transitivity for $R = \{ (1, 2), (2, 3), (3, 3) \}$ on $W = \{ 1, 2, 3 \}$.
Every world has a successor, namely $2$, $3$ and $3$, so $R$ is serial.
The path $1 R 2 R 3$ would need $1 R 3$, which is missing, so $R$ is not transitive.
Adding $(1, 3)$ repairs this, and then every path of length two ends at a pair of $R$.
The typical use of the definition is to check which axioms a given frame validates.
Watch out: the Euclidean condition is about two successors of one world, not about a path of two steps.

### L3 human

Seven of the eight properties are universal Horn conditions on $R$, and seriality is a $\forall\exists$ condition.
All eight are preserved under generated subframes.
The Horn conditions are also preserved under intersections of relations on a fixed set, and seriality is not: $\{ (1, 2), (2, 1) \}$ and $\{ (1, 1), (2, 2) \}$ are serial, and their intersection is empty.
