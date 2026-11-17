---
tag: 28D8ACKEY0
kind: example
name: Three double-negation translations of one formula
msc: ["03F25", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [HGJVM49PA4]
uses: [QEZR7PZ2DD, PAQ4ZX2TX1, Q11N8X99FK]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Equivalent variants
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: First-order logic
---

## Example

Let $P$ be a unary predicate symbol, and let $A = \forall x\, (P(x) \vee \neg P(x))$.
We compute the three [[double-negation translations|QEZR7PZ2DD]] of $A$ and check that each is provable in intuitionistic [[natural deduction|PAQ4ZX2TX1]] NJ.

1. Gödel-Gentzen: $(\neg P(x))^N = \neg \neg \neg P(x)$, so $A^N = \forall x\, \neg (\neg \neg \neg P(x) \wedge \neg \neg \neg \neg P(x))$.
2. Kolmogorov: $(\neg P(x))^K = \neg \neg (\neg \neg P(x) \to \bot)$, which is $\neg \neg \neg \neg \neg P(x)$.
3. So $A^K = \neg \neg \forall x\, \neg \neg (\neg \neg P(x) \vee \neg \neg \neg \neg \neg P(x))$.
4. Kuroda: the star map puts $\neg \neg$ after the quantifier, and then $\neg \neg$ is put in front. So $A^{Ku} = \neg \neg \forall x\, \neg \neg (P(x) \vee \neg P(x))$.
5. $A^N$ is provable: the [[derivation for one atom|F8789WMFC6]] with $P(x)$ has no open assumptions, and ${\forall}\mathrm{I}$ gives $A^N$.
6. For any formula $R$, NJ proves $\neg \neg (R \vee \neg R)$. Assume $\neg (R \vee \neg R)$ and $R$; then ${\vee}\mathrm{I}$ gives $R \vee \neg R$ and $\bot$.
7. ${\to}\mathrm{I}$ gives $\neg R$, then ${\vee}\mathrm{I}$ gives $R \vee \neg R$ and $\bot$. A last ${\to}\mathrm{I}$ gives $\neg \neg (R \vee \neg R)$.
8. $A^{Ku}$ is provable: step 6 with $R = P(x)$, then ${\forall}\mathrm{I}$, then $B \to \neg \neg B$ give $A^{Ku}$.
9. $A^K$ is provable: take $R = \neg \neg P(x)$ in step 6. Then $\neg R \to \neg \neg \neg R$ turns $R \vee \neg R$ into $R \vee \neg \neg \neg R$.
10. Under $\neg \neg$ this implication still holds, so NJ proves $\neg \neg (R \vee \neg \neg \neg R)$. Then ${\forall}\mathrm{I}$ and $B \to \neg \neg B$ give $A^K$.

So the three translations are different formulas, and all three are intuitionistically provable.

## Remarks

The three formulas are intuitionistically equivalent, as the [[double-negation translation|HGJVM49PA4]] page states in general.
The Gödel-Gentzen form avoids $\vee$ and $\exists$, the Kolmogorov form is the longest, and the Kuroda form keeps the original formula inside.
The formula $A$ itself is not intuitionistically provable.
Also $\neg \neg A$ is not intuitionistically provable, by the [[Kripke model of the non-example|ZV2MWBRN04]].
So the $\neg \neg$ after the quantifier in $A^{Ku}$ cannot be dropped.

## Explanations

### L1 human

The sentence "every object has property $P$ or does not have it" is a classical truth.
There are three standard ways to weaken it so that intuitionistic logic can prove it.
All three insert "it is impossible that not" at certain places.
They differ in where they insert it, but each weakened sentence has a short intuitionistic proof.
For example, Kuroda's form says, for each object, that it is impossible that the object neither has nor lacks property $P$.

### L2 human

We check the Kuroda translation for one object in detail.

1. Fix $x$, and assume $\neg (P(x) \vee \neg P(x))$.
2. Assume $P(x)$. Then $P(x) \vee \neg P(x)$, which contradicts step 1. So $\neg P(x)$.
3. From $\neg P(x)$ we get $P(x) \vee \neg P(x)$ again, so step 1 gives $\bot$.
4. Discharge step 1: $\neg \neg (P(x) \vee \neg P(x))$ holds for every $x$.
5. So $\forall x\, \neg \neg (P(x) \vee \neg P(x))$, and also its double negation.

The typical use of the Kuroda form is in proofs that need few double negations, since it puts them only after $\forall$ and at the front.
A trap is to move the inner $\neg \neg$ in front of $\forall x$: the result $\neg \neg \forall x\, (P(x) \vee \neg P(x))$ is not provable.
