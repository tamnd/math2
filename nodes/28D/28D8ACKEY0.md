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
We compute the three [[double-negation translations|QEZR7PZ2DD]] of $A$ and check that intuitionistic [[natural deduction|PAQ4ZX2TX1]] NJ proves each of them.

1. Gödel-Gentzen.
   The second disjunct translates to $(\neg P(x))^N = \neg \neg P(x) \to \bot = \neg \neg \neg P(x)$, so
   $$A^N = \forall x\, \neg (\neg \neg \neg P(x) \wedge \neg \neg \neg \neg P(x)).$$
2. Kolmogorov.
   Here $(\neg P(x))^K = \neg \neg (\neg \neg P(x) \to \bot)$, which is $\neg \neg \neg \neg \neg P(x)$, so
   $$A^K = \neg \neg \forall x\, \neg \neg (\neg \neg P(x) \vee \neg \neg \neg \neg \neg P(x)).$$
3. Kuroda.
   The star map puts $\neg \neg$ after the quantifier, and then one more $\neg \neg$ goes in front:
   $$A^{Ku} = \neg \neg \forall x\, \neg \neg (P(x) \vee \neg P(x)).$$
4. A lemma for any formula $R$: NJ proves $\neg \neg (R \vee \neg R)$.
   Assume $\neg (R \vee \neg R)$ and $R$, so ${\vee}\mathrm{I}$ gives $R \vee \neg R$ and then $\bot$.
5. Discharging $R$ gives $\neg R$, so ${\vee}\mathrm{I}$ gives $R \vee \neg R$ and again $\bot$.
   Discharging $\neg (R \vee \neg R)$ gives $\neg \neg (R \vee \neg R)$.
6. $A^N$ is provable.
   The [[derivation for one atom|F8789WMFC6]] with $P(x)$ in place of $P$ has no open assumptions, so ${\forall}\mathrm{I}$ gives $A^N$.
7. $A^{Ku}$ is provable.
   Step 5 with $R = P(x)$, then ${\forall}\mathrm{I}$, then the NJ theorem $B \to \neg \neg B$ give $A^{Ku}$.
8. $A^K$ is provable.
   Take $R = \neg \neg P(x)$ in step 5, so NJ proves $\neg \neg (R \vee \neg R)$.
9. NJ proves $\neg R \to \neg \neg \neg R$, so $R \vee \neg R$ implies $R \vee \neg \neg \neg R$, and this implication survives under $\neg \neg$.
   So NJ proves $\neg \neg (\neg \neg P(x) \vee \neg \neg \neg \neg \neg P(x))$, and ${\forall}\mathrm{I}$ with $B \to \neg \neg B$ gives $A^K$.

So the three translations are different formulas, and all three are intuitionistically provable.

## Remarks

The three formulas are intuitionistically equivalent, as the [[double-negation translation|HGJVM49PA4]] guarantees in general.
The Gödel-Gentzen form avoids $\vee$ and $\exists$, the Kolmogorov form is the longest, and the Kuroda form keeps the original formula inside.

The formula $A$ itself is not intuitionistically provable.
Neither is $\neg \neg A$, by the [[Kripke model of the prefixed double negation|ZV2MWBRN04]].
So the $\neg \neg$ that Kuroda puts after the quantifier cannot be dropped, and moving it in front of $\forall x$ loses provability.
If $P$ is replaced by a decidable predicate, for example an equation of arithmetic in HA, then $A$ itself becomes provable and all three translations are equivalent to $A$.

## Explanations

### L1 human

The sentence "every object has property $P$ or does not have it" is a classical truth.
There are three standard ways to weaken it so that intuitionistic logic can prove it.
All three insert "it is impossible that not" at certain places.
They differ in where they insert it, but each weakened sentence has a short intuitionistic proof.
For example, Kuroda's form says, for each object, that it is impossible that the object neither has nor lacks $P$.

### L2 human

We check the inner part of the Kuroda translation for one object.
Fix $x$, and assume $\neg (P(x) \vee \neg P(x))$.
If $P(x)$ held, then $P(x) \vee \neg P(x)$ would hold, against the assumption, so $\neg P(x)$.
From $\neg P(x)$ we get $P(x) \vee \neg P(x)$ again, so the assumption gives $\bot$.
Discharging it proves $\neg \neg (P(x) \vee \neg P(x))$ for every $x$, hence $\forall x\, \neg \neg (P(x) \vee \neg P(x))$, and also its double negation.

The point to remember is the place of $\neg \neg$.
Inside the quantifier the proof goes through, one object at a time.
In front of the quantifier, as in $\neg \neg \forall x\, (P(x) \vee \neg P(x))$, it does not, because the argument would need to decide all objects at once.
