---
tag: QEZR7PZ2DD
kind: definition
name: Double-negation translation
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
uses: [Q11N8X99FK, 0XR7A7RSXB, 0QFT7Z76N5, RXHJPVMPJH, 0RYYK8PG4S]
defines: HGJVM49PA4
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Equivalent variants
---

## Definition

A double-negation translation sends each first-order formula to a formula that is classically equivalent to it and that intuitionistic logic proves whenever classical logic proves the original.

Fix a first-order language, and read $\neg A$ as $A \to \bot$.
The *Gödel-Gentzen negative translation* is the map $A \mapsto A^N$ on formulas defined by these clauses.

1. $\bot^N = \bot$, and $P^N = \neg \neg P$ for every other atomic formula $P$.
2. $(A \wedge B)^N = A^N \wedge B^N$.
3. $(A \vee B)^N = \neg (\neg A^N \wedge \neg B^N)$.
4. $(A \to B)^N = A^N \to B^N$.
5. $(\forall x\, A)^N = \forall x\, A^N$.
6. $(\exists x\, A)^N = \neg \forall x\, \neg A^N$.

For a set of formulas $\Gamma$, let $\Gamma^N = \{ A^N : A \in \Gamma \}$.

The *Kolmogorov translation* $A \mapsto A^K$ puts a double negation in front of every subformula.

1. $\bot^K = \bot$, and $P^K = \neg \neg P$ for every other atomic formula $P$.
2. $(A \circ B)^K = \neg \neg (A^K \circ B^K)$ for each connective $\circ$ among $\wedge$, $\vee$, $\to$.
3. $(\forall x\, A)^K = \neg \neg \forall x\, A^K$ and $(\exists x\, A)^K = \neg \neg \exists x\, A^K$.

The *Kuroda translation* is $A^{Ku} = \neg \neg A^*$, where $A^*$ comes from $A$ by replacing each subformula $\forall x\, B$ by $\forall x\, \neg \neg B$, from the inside out.

A *double-negation translation* is a map $A \mapsto A^*$, obtained by inserting double [[negations|0XR7A7RSXB]], such that $A^*$ is classically equivalent to $A$ and, for every $\Gamma$ and $A$, $\Gamma \vdash A$ in classical logic if and only if $\Gamma^* \vdash A^*$ in [[intuitionistic logic|Q11N8X99FK]].
The three maps $A^N$, $A^K$ and $A^{Ku}$ are double-negation translations, and they are intuitionistically equivalent to each other.

## Remarks

Each clause of the Gödel-Gentzen map has a job.
The clauses for $\wedge$, $\to$ and $\forall$ change nothing, because these connectives already mean the same thing in both logics.
The clauses for $\vee$ and $\exists$ replace a disjunction and an existential by their classical definitions in terms of $\wedge$ and $\forall$, so that the translated formula never claims to know which side holds or which witness works.
The $\neg \neg$ on atoms makes every translated formula stable, that is, $\neg \neg A^N \to A^N$ is intuitionistically provable.

For an example, take the [[law of excluded middle|0RYYK8PG4S]] $P \vee \neg P$ with $P$ atomic.
The clauses give $(P \vee \neg P)^N = \neg (\neg \neg \neg P \wedge \neg \neg \neg \neg P)$.
Since $\neg \neg \neg P$ is intuitionistically equivalent to $\neg P$, this is equivalent to $\neg (\neg P \wedge \neg \neg P)$, which NJ proves by one modus ponens.

A map that fails the definition is the identity $A \mapsto A$.
It keeps $P \vee \neg P$, which classical logic proves and intuitionistic logic does not, so the condition "$\vdash_c A$ implies $\vdash_i A^*$" fails.

For arithmetic, [[Peano arithmetic|0QFT7Z76N5]] proves $A$ if and only if [[Heyting arithmetic|RXHJPVMPJH]] proves $A^N$, and $\bot^N = \bot$ makes PA consistent if HA is.
The atoms of arithmetic are equations, and HA decides them, so in arithmetic one may take $P^N = P$.
Worked examples and the main uses are in the concept [[double-negation translation|HGJVM49PA4]].
