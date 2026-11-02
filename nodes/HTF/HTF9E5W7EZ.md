---
tag: HTF9E5W7EZ
kind: definition
name: Curry–Howard correspondence
msc: ["03B40", "03F03", "68N18"]
defines: A77FER1Q5H
uses: [BD756KR8FM, Q11N8X99FK, 6KT3BJZ7D1, 0ZNX6DQ3EJ, 0M28ASWG8T, 0H5GKDTB01]
sources:
  - url: https://en.wikipedia.org/wiki/Curry–Howard_correspondence
---

## Definition

Consider intuitionistic propositional logic in [[natural deduction|6KT3BJZ7D1]], with [[implication|0ZNX6DQ3EJ]], [[conjunction|0M28ASWG8T]] and [[disjunction|0H5GKDTB01]].
Consider the simply typed [[lambda calculus|BD756KR8FM]] with function types $A \to B$, product types $A \times B$ and sum types $A + B$.
The *Curry–Howard correspondence* is the map between the two systems given by these clauses.

1. A formula is read as a type: $A \to B$ as the function type, $A \wedge B$ as $A \times B$, and $A \vee B$ as $A + B$.
2. An assumption $A$ with label $x$ is read as a variable $x : A$.
3. Each introduction rule is read as a term constructor: $\to$-introduction as $\lambda$-abstraction, $\wedge$-introduction as pairing, and $\vee$-introduction as an injection.
4. Each elimination rule is read as a destructor: $\to$-elimination as application, $\wedge$-elimination as a projection, and $\vee$-elimination as case analysis.

Under this map, a derivation of $B$ from assumptions $A_1, \dots, A_n$ corresponds to a term $M$ with $x_1 : A_1, \dots, x_n : A_n \vdash M : B$, and conversely.
A detour in a derivation is an introduction followed at once by an elimination.
It corresponds to a redex, and removing the detour corresponds to one reduction step, such as $(\lambda x.\, M) N \to M[N/x]$.

## Remarks

Example: the term $\lambda f.\, \lambda x.\, f\, (f\, x)$ has type $(A \to A) \to (A \to A)$.
Read as a derivation, it uses $\to$-elimination twice and $\to$-introduction twice, and it proves the formula $(A \to A) \to (A \to A)$.
Non-example: Peirce's law $((A \to B) \to A) \to A$ is a classical tautology but has no closed term of its type in the simply typed lambda calculus.
This matches the fact that it is not provable in [[intuitionistic logic|Q11N8X99FK]].
The correspondence extends to quantifiers with dependent types, and to classical logic with control operators.
