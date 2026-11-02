---
tag: TY89DBMJYQ
kind: definition
name: Von Neumann–Bernays–Gödel set theory
msc: ["03E30", "03E70"]
defines: JTPZ1HZ9KK
uses: [JRBRNZT680, W473FH7Z0P, 0HE5WDQ9FJ, 0TB16T2C97, 0HTGB13FE2, 6QXBY7J0M5]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann–Bernays–Gödel_set_theory
---

## Definition

*Von Neumann–Bernays–Gödel set theory*, written NBG, is the first-order theory in the language $\set{\in}$ whose variables range over [[classes|W473FH7Z0P]].
A class $X$ is a *set* if $X \in Y$ for some class $Y$, and a *proper class* otherwise.
The axioms of NBG are these.

1. Extensionality: classes with the same elements are equal, as in the [[axiom of extensionality|0TB16T2C97]].
2. Pairing, union, power set and infinity: as in [[ZF|0HE5WDQ9FJ]], stated for sets.
3. Foundation: the [[axiom of regularity|6QXBY7J0M5]], for all nonempty classes.
4. Replacement: if $F$ is a class that is a function and $a$ is a set, then the image $F[a]$ is a set.
5. Class comprehension: for each formula $\varphi(x)$ in which all quantifiers range over sets, possibly with class parameters, there is a class $\set{x : x \text{ is a set and } \varphi(x)}$.
6. Global choice: there is a class function that picks an element from every nonempty set.

## Remarks

Class comprehension can be replaced by finitely many of its instances, so NBG has a finite list of axioms; ZF has no finite axiomatization if it is consistent.
NBG is a conservative extension of ZFC: a statement about sets is provable in NBG if and only if it is provable in ZFC.
Example: the class $V = \set{x : x = x}$ of all sets exists by comprehension, with $\varphi(x)$ the formula $x = x$.
Non-example: $V$ is not a set.
If it were, then comprehension would give the class $R = \set{x : x \notin x}$, which would be a set as a subclass of $V$, and then $R \in R \leftrightarrow R \notin R$.
Morse–Kelley set theory is the stronger theory in which the formula in class comprehension may also quantify over classes.
Some authors drop global choice, or replace it by the [[axiom of choice|0HTGB13FE2]] for sets; NBG without global choice is conservative over ZF.
