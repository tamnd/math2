---
tag: 3EDRQJJHMT
kind: concept
name: Japaridze's polymodal logic GLP
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
uses: [WJK0YA4GP2, 61THBNS8WE, QQ6PZFGGB3, 1ZRWVDYPX0, 1DMFNR7FZT, NGHWZ9Y7ZV, HACXBCM7SS, 7CVJCQKY41, 4S29X1GTV4, NB485KFXKV, C5E5TG8PGP, QPV0HNP22S, T9NTRY93ZT, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: Language and axiomatization
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: Provability semantics
  - url: https://en.wikipedia.org/wiki/Japaridze%27s_polymodal_logic
    locator: History
---

## Summary

$\mathsf{GLP}$ is provability logic for a ladder of provability notions, one box for each rung.
The box $[0]$ is provability in $\mathsf{PA}$, and $[1]$ is a stronger notion, such as provability with one use of the $\omega$-rule.
A stronger theory can see the consistency facts of a weaker one, so $\langle 0 \rangle \top \to [1] \langle 0 \rangle \top$ is a law.

In exact terms, $\mathsf{GLP}$ has one box $[n]$ for each natural number $n$, with $\langle n \rangle \varphi := \neg [n] \neg \varphi$.
Its axioms are the axioms of $\mathsf{GL}$ for each $[n]$, and two schemas that link the boxes:

$$[m] \varphi \to [n] \varphi \quad (m \leq n), \qquad \langle m \rangle \varphi \to [n] \langle m \rangle \varphi \quad (m < n).$$

Its rules are modus ponens and necessitation for $[0]$.
The box $[n]$ is read as provability with $n$ nested uses of the $\omega$-rule.
Japaridze proved that $\mathsf{GLP}$ is arithmetically complete for this reading, as $\mathsf{GL}$ is for $\mathsf{PA}$ by [[Solovay's theorem|1ZRWVDYPX0]].

## Motivation

[[Provability logic|WJK0YA4GP2]] with one box describes one theory.
Proof theory compares theories of different strength, such as $\mathsf{PA}$ and $\mathsf{PA}$ with [[reflection principles|NB485KFXKV]].
$\mathsf{GLP}$ describes a whole hierarchy of such provability notions at once.
Its consistency formulas $\langle n \rangle \top$ express $n$-consistency, a strengthening of consistency related to [[ω-consistency|4S29X1GTV4]] and to the [[arithmetical hierarchy|7CVJCQKY41]].

Two features make $\mathsf{GLP}$ worth study.
It is not complete for any class of Kripke frames, unlike $\mathsf{GL}$.
And Beklemishev used it for a modal [[ordinal analysis|C5E5TG8PGP]] of $\mathsf{PA}$.

## Notation

We read $[n] \varphi$ as "$\varphi$ is $n$-provable" and $\langle n \rangle \varphi$ as "$\varphi$ is $n$-consistent".
A worm is a formula $\langle n_1 \rangle \langle n_2 \rangle \cdots \langle n_k \rangle \top$, and the empty worm is $\top$.
We write $\langle n \rangle^k \varphi$ for $\langle n \rangle$ applied $k$ times to $\varphi$.
Larger indices mean stronger provability, so $[0] \varphi \to [1] \varphi$ is the correct direction.

## Remarks

### Each box is a provability logic

Each $[n]$ satisfies the theorems of $\mathsf{GL}$, for example $[n] p \to [n][n] p$, by part 1 of [[Löb's axiom in provability logic|QQ6PZFGGB3]].
Necessitation is given only for $[0]$, but it holds for every box.
If $\mathsf{GLP} \vdash \varphi$, necessitation gives $[0] \varphi$, and the axiom $[0] \varphi \to [n] \varphi$ gives $[n] \varphi$.

The monotonicity schema goes only one way.
The schema $[1] \varphi \to [0] \varphi$ is not a theorem.
Its instance with $\varphi = \langle 0 \rangle \top$ would combine with the axiom $\langle 0 \rangle \top \to [1] \langle 0 \rangle \top$ and the $\mathsf{GL}$ theorem $[0] \langle 0 \rangle \top \to [0] \bot$.
Together they give $\mathsf{GLP} \vdash \langle 0 \rangle \top \to [0] \bot$, hence $\mathsf{GLP} \vdash [0] \bot$, which fails by arithmetical soundness.

### Moving consistency inside

The second linking axiom lets a strong box carry a weak consistency fact.
[[The mixing lemma of GLP|ADJA5TD6PZ]] makes this exact for $m < n$:

$$\mathsf{GLP} \vdash \langle n \rangle A \wedge \langle m \rangle B \to \langle n \rangle (A \wedge \langle m \rangle B).$$

With $n = 1$, $m = 0$ and $A = B = \top$, it gives $\langle 1 \rangle \top \wedge \langle 0 \rangle \top \to \langle 1 \rangle \langle 0 \rangle \top$.
A similar computation, repeated by induction, shows that [[1-consistency implies iterated consistency in GLP|670PRKCYFZ]]: $\mathsf{GLP} \vdash \langle 1 \rangle \top \to \langle 0 \rangle^k \top$ for every $k$.

### No Kripke frames fit

A Kripke frame for $\mathsf{GLP}$ has one relation $R_n$ for each box.
[[A bimodal frame that is not a GLP frame|JEA1527ZRE]] shows that two $\mathsf{GL}$ frames $R_0 \supseteq R_1$ on the same worlds need not give a frame of $\mathsf{GLP}$.
The same argument shows that every frame $(W, R_0, R_1, \dots)$ that validates $\mathsf{GLP}$ has $R_1 = \emptyset$.
So $[1] \bot$ is valid on every such frame.

But $\mathsf{GLP} \nvdash [1] \bot$.
The theory $\mathsf{PA}$ with one use of the $\omega$-rule is consistent, because all its theorems are true, and arithmetical soundness does the rest.
So $\mathsf{GLP}$ is not the logic of any class of Kripke frames.

### Arithmetic and ordinals

Japaridze's completeness theorem, which we cite, says this.
$\mathsf{GLP} \vdash \varphi$ holds if and only if $\mathsf{PA}$ proves every realization of $\varphi$, where $[n]$ is realized by the $n$-provability predicate.
$\mathsf{GLP}$ is decidable, and its theorems can be recognized in polynomial space, the class [[PSPACE|T9NTRY93ZT]].

Beklemishev ordered worms by $A <_0 B$ if $\mathsf{GLP} \vdash B \to \langle 0 \rangle A$.
Up to provable equivalence this is a well-order of type $\varepsilon_0$, the ordinal of [[Gentzen's consistency proof|QPV0HNP22S]].
For example, $\langle 0 \rangle^k \top$ has the place $k$, and $\langle 1 \rangle \top$ has the place $\omega$.

### History

Giorgi Japaridze introduced $\mathsf{GLP}$ in his 1986 thesis and proved its arithmetical completeness, published in 1988.
Lev Beklemishev used $\mathsf{GLP}$ in the 2000s, from 2004 on, for ordinal notations up to $\varepsilon_0$ and an ordinal analysis of $\mathsf{PA}$.
He later gave a simplified proof of the completeness theorem.
Ilya Shapirovsky showed in 2008 that $\mathsf{GLP}$ is decidable in polynomial space.

### Watch out

Do not trust a frame just because each relation is a $\mathsf{GL}$ frame.
The frame with $R_0 = R_1 = \{(a, b)\}$ has this property, yet the axiom $\langle 0 \rangle p \to [1] \langle 0 \rangle p$ fails at $a$.
A Kripke countermodel shows that a formula is not in $\mathsf{GLP}$ only if its frame validates all of $\mathsf{GLP}$.

Do not expect the converse either.
A formula valid on every frame of $\mathsf{GLP}$ need not be a theorem, and $[1] \bot$ is the standard case.
Completeness needs more general semantics, such as topological models or special Kripke models.

### Try it

1. Show that $\mathsf{GLP} \vdash \langle 2 \rangle \top \to \langle 0 \rangle \top$.
   Answer: contrapose the axiom $[0] \bot \to [2] \bot$.
2. Apply the mixing lemma with $n = 1$, $m = 0$, $A = \top$ and $B = \langle 0 \rangle \top$.
   Answer: $\langle 1 \rangle \top \wedge \langle 0 \rangle \langle 0 \rangle \top \to \langle 1 \rangle \langle 0 \rangle \langle 0 \rangle \top$.
3. Is one world with every $R_n$ empty a frame of $\mathsf{GLP}$?
   Answer: yes, since every formula $[n] \varphi$ is true there, so each axiom has a true conclusion.

## Explanations

### L1 human

$\mathsf{GLP}$ is a logic with many kinds of "provable".
$[0]$ is ordinary provability, $[1]$ allows stronger arguments, $[2]$ stronger still, and so on.
Each kind follows the laws of ordinary provability logic.
The axioms say that a stronger kind proves everything a weaker one proves, and that a stronger kind can see the consistency facts of a weaker one.
This logic is used to measure the strength of theories of arithmetic.

### L2 human

We derive necessitation for $[1]$ from the rules of $\mathsf{GLP}$, and then use it.
Assume $\mathsf{GLP} \vdash \varphi$.
Necessitation for $[0]$ gives $\mathsf{GLP} \vdash [0] \varphi$.
The axiom $[0] \varphi \to [1] \varphi$ and modus ponens give the result:

$$\mathsf{GLP} \vdash [1] \varphi.$$

For example, from the tautology $\top$ we get $[1] \top$.
This is the base case of the proof that $\langle 1 \rangle \top \to \langle 0 \rangle^k \top$.
The problem shows the typical use: derived rules and the linking axioms turn questions about consistency statements into short modal computations.

### L3 human

$\mathsf{GLP}$ is the polymodal analogue of $\mathsf{GL}$, and its Lindenbaum algebra encodes the proof-theoretic ordinal of $\mathsf{PA}$.
Beklemishev's worms give a purely modal ordinal notation system for $\varepsilon_0$.
The [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ used by Gentzen becomes induction along the order of worms.
The Kripke incompleteness shows that the semantics of [[Kripke completeness of GL|1DMFNR7FZT]] does not extend.
Beklemishev and others use special models and topological semantics instead.
