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
Recall that $\neg \varphi$ means "$\varphi$ leads to a contradiction": to prove $\neg \varphi$, we assume $\varphi$ and derive a contradiction.

Direction 1: $\exists x \, \neg P(x) \to \neg \forall x \, P(x)$.

1. Assume $\exists x \, \neg P(x)$. Reason: hypothesis of the implication.
2. Choose $a \in D$ with $\neg P(a)$. Reason: elimination of the [[existential quantifier|0JW2FHW7G3]], with a new name $a$.
3. Assume $\forall x \, P(x)$, to derive a contradiction. Reason: this is how a negation is proved.
4. Then $P(a)$. Reason: elimination of the [[universal quantifier|0B88PQTJ66]] in step 3, applied to $a$.
5. Steps 2 and 4 give $P(a)$ and $\neg P(a)$, a contradiction.
6. So $\neg \forall x \, P(x)$. Reason: the assumption of step 3 led to a contradiction.
7. Steps 1 to 6 prove direction 1.

Direction 2: $\neg \forall x \, P(x) \to \exists x \, \neg P(x)$.

8. Assume $\neg \forall x \, P(x)$. Reason: hypothesis of the implication.
9. Assume $\neg \exists x \, \neg P(x)$, to derive a contradiction. Reason: [[proof by contradiction|0J0XBKG64S]].
10. Let $b \in D$ be arbitrary, and assume $\neg P(b)$. Reason: we prove $\neg \neg P(b)$, so we assume $\neg P(b)$.
11. Then $\exists x \, \neg P(x)$, with witness $b$, and this contradicts step 9. Reason: introduction of $\exists$.
12. So $\neg \neg P(b)$. Reason: the assumption of step 10 led to a contradiction.
13. From $\neg \neg P(b)$ we conclude $P(b)$. Reason: the [[double negation law|0NFAGWH84K]], which follows from the [[law of excluded middle|0RYYK8PG4S]].
14. Since $b$ was arbitrary, $\forall x \, P(x)$. Reason: introduction of $\forall$.
15. Steps 8 and 14 give $\neg \forall x \, P(x)$ and $\forall x \, P(x)$, a contradiction. So $\neg \neg \exists x \, \neg P(x)$. Reason: the assumption of step 9 led to a contradiction.
16. From $\neg \neg \exists x \, \neg P(x)$ we conclude $\exists x \, \neg P(x)$. Reason: the double negation law again.
17. Steps 8 to 16 prove direction 2.

Conclusion.

18. By steps 7 and 17, each side implies the other, so $\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$ in classical logic. $\blacksquare$

Use of excluded middle: steps 13 and 16 use double negation elimination, which is equivalent to the law of excluded middle.
All other steps are valid in [[intuitionistic logic|Q11N8X99FK]].
So direction 1 holds intuitionistically, and the proof of direction 2 uses excluded middle twice.

## Idea

Direction 1 is direct: a witness $a$ with $\neg P(a)$ contradicts the claim that every element has $P$.
Direction 2 argues by contradiction: if no element fails $P$, then every element has $P$, against the hypothesis.
The step from "no element fails $P$" to "every element has $P$" removes a double negation, and this is where classical logic is needed.

## Variants

1. A semantic proof with truth values: $\neg \forall x \, P(x)$ is true exactly when $\forall x \, P(x)$ is false, exactly when some $P(a)$ is not true, exactly when some $P(a)$ is false by bivalence, exactly when $\exists x \, \neg P(x)$ is true. The appeal to bivalence plays the role of excluded middle.
2. A proof by cases with excluded middle: apply $\exists x \, \neg P(x) \lor \neg \exists x \, \neg P(x)$. In the first case the conclusion holds. In the second case, steps 10 to 14 give $\forall x \, P(x)$, which contradicts the hypothesis.
3. A derivation from the [[negation of an existential statement|05SZQKH75K]]: applied to the predicate $\neg P$, it gives $\neg \exists x \, \neg P(x) \equiv \forall x \, \neg \neg P(x)$. Taking negations and removing $\neg \neg$ with the double negation law gives the statement.
