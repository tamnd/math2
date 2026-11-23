---
tag: DTM9GQV88K
kind: proof
name: Proof of the negation of a universal statement
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
proves: 0P3A06QNDP
uses: [0T3DPBG981, 0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB, 0RYYK8PG4S, 0NFAGWH84K]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Proof

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
We prove the two directions separately, with the rules of the quantifiers and of [[negation|0XR7A7RSXB]].
To prove $\neg \varphi$, we assume $\varphi$ and derive a contradiction.

Direction 1: $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$.

1. Assume $\exists x \, \neg P(x)$.
   Reason: hypothesis of the implication.
2. Choose $a \in D$ with $\neg P(a)$.
   Reason: elimination of the [[existential quantifier|0JW2FHW7G3]], with a new name $a$.
3. Assume $\forall x \, P(x)$, to derive a contradiction.
   Reason: this is how a negation is proved.
4. Then $P(a)$.
   Reason: elimination of the [[universal quantifier|0B88PQTJ66]] in step 3, applied to $a$.
5. Steps 2 and 4 give $P(a)$ and $\neg P(a)$, a contradiction.
6. So $\neg \forall x \, P(x)$, which proves direction 1.
   Reason: the assumption of step 3 led to a contradiction.

Direction 2: $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$.

7. Assume $\neg \forall x \, P(x)$.
   Reason: hypothesis of the implication.
8. Assume $\neg \exists x \, \neg P(x)$, to derive a contradiction.
   Reason: [[proof by contradiction|0J0XBKG64S]].
9. Let $b \in D$ be arbitrary, and assume $\neg P(b)$.
   Reason: we prove $\neg \neg P(b)$.
10. Then $\exists x \, \neg P(x)$ with the witness $b$, which contradicts step 8.
    Reason: introduction of $\exists$.
11. So $\neg \neg P(b)$.
    Reason: the assumption of step 9 led to a contradiction.
12. From $\neg \neg P(b)$ we conclude $P(b)$.
    Reason: the [[double negation law|0NFAGWH84K]], which follows from the [[law of excluded middle|0RYYK8PG4S]].
13. Since $b$ was arbitrary, $\forall x \, P(x)$.
    Reason: introduction of $\forall$.
14. Steps 7 and 13 give a contradiction, so $\neg \neg \exists x \, \neg P(x)$.
    Reason: the assumption of step 8 led to a contradiction.
15. From $\neg \neg \exists x \, \neg P(x)$ we conclude $\exists x \, \neg P(x)$, which proves direction 2.
    Reason: the double negation law again.
16. By steps 6 and 15, each side implies the other, so $\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$ in classical logic. $\blacksquare$

Steps 12 and 15 use double negation elimination, which is equivalent to the law of excluded middle.
All other steps are valid in [[intuitionistic logic|Q11N8X99FK]].
So direction 1 holds intuitionistically, and the proof of direction 2 uses excluded middle twice.

## Idea

Direction 1 is direct: a witness $a$ with $\neg P(a)$ contradicts the claim that every element has $P$.
Direction 2 argues by contradiction: if no element fails $P$, then every element has $P$, against the hypothesis.
The step from "no element fails $P$" to "every element has $P$" removes a double negation, and classical logic is needed exactly there.

## Variants

A semantic proof uses truth values.
$\neg \forall x \, P(x)$ is true exactly when some $P(a)$ is not true, which by bivalence means that some $P(a)$ is false, which means that $\exists x \, \neg P(x)$ is true.
The appeal to bivalence plays the role of excluded middle.

A proof by cases applies excluded middle to $\exists x \, \neg P(x)$.
In the first case the conclusion holds.
In the second case, steps 9 to 13 give $\forall x \, P(x)$, which contradicts the hypothesis.

A derivation from the [[negation of an existential statement|05SZQKH75K]] applies it to the predicate $\neg P$, which gives $\neg \exists x \, \neg P(x) \equiv \forall x \, \neg \neg P(x)$.
Taking negations of both sides and removing $\neg \neg$ inside with the double negation law gives the statement.
