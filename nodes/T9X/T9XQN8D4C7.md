---
tag: T9XQN8D4C7
kind: statement
role: theorem
name: Chomsky–Schützenberger representation theorem
msc: [68Q45, 68Q42, 68Q70]
uses: [Q56EWEQYE2, B80FATJ43P, 18WVBDCS38, CV013KHVJG]
about: [Q56EWEQYE2]
sources:
  - url: https://en.wikipedia.org/wiki/Chomsky–Schützenberger_representation_theorem
same_as:
  wikidata: Q3527040
  wikipedia: Chomsky–Schützenberger representation theorem
---

## Statement

For $n \ge 1$, let $T_n = \set{[_1, ]_1, \dots, [_n, ]_n}$ be an alphabet of $n$ pairs of brackets.
Let $D_n \subseteq T_n^*$ be the [[Dyck language|B80FATJ43P]] of balanced strings over $T_n$.
Let $\Sigma$ be a finite alphabet and $L \subseteq \Sigma^*$.
Then $L$ is a [[context-free language|Q56EWEQYE2]] if and only if
$$L = h(D_n \cap R)$$
for some $n \ge 1$, some [[regular language|18WVBDCS38]] $R \subseteq T_n^*$ and some homomorphism $h \colon T_n^* \to \Sigma^*$ of [[free monoids|CV013KHVJG]].

## Remarks

The direction "if" holds because $D_n$ is context-free and the context-free languages are closed under intersection with regular languages and under homomorphisms.
For "only if", take a grammar for $L$ in Chomsky normal form and give each rule its own brackets.
A derivation is then encoded as a balanced bracket string.
The regular language $R$ checks the local consistency of the encoding, and $h$ erases the brackets and keeps the letters.
Example: $\set{a^m b^m : m \ge 0} = h(D_1 \cap R)$ with $R = [_1^* \, ]_1^*$, $h([_1) = a$ and $h(]_1) = b$.
Indeed $D_1 \cap R = \set{[_1^m \, ]_1^m : m \ge 0}$.

## Explanations

### L1 human

The theorem says that every context-free language is made of correctly nested brackets, seen through two simple filters.
The first filter is a regular language, which keeps only bracket strings of a certain local shape.
The second filter renames brackets into letters and may erase some of them.
So the Dyck languages are the essence of context-freeness: nesting is all that context-free grammars add to finite automata.

### L2 human

The theorem gives an algebraic description of the context-free languages, without grammars or automata.
It is often used with $D_2$ alone, since each $D_n$ is the inverse image of $D_2$ under a suitable homomorphism, and the class is closed under inverse homomorphisms.
In the language of abstract families of languages, it says that the context-free languages form the smallest full trio containing $D_2$.
