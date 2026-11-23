---
tag: DZD5KXKN24
kind: proof
name: Proof outline of Spector's theorem
msc: ["03F10", "03F35"]
topics: [8XY7JYZKFW]
audience: research
proves: DSQJ1RA71N
uses: [WC4TDGEWZR, 6QFRG42QQR, X79VFTRT8Y, 8CCG6F2FAT, ZREF8MTYNW, 3WH3N4GY7W]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Comprehension
  - url: https://en.wikipedia.org/wiki/Bar_recursion
    locator: lead section
---

## Proof

We give the structure of the proof, prove the reduction lemma in full, and cite two results.

### The cited results

Result S1 is the soundness of the [[Dialectica interpretation|ZREF8MTYNW]] for $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$, with witnesses in T.
This is the extension stated in the [[soundness theorem|6QFRG42QQR]].

Result S2 is Spector's main lemma.
For each instance of the double negation shift $\mathrm{DNS}$ there are closed terms of T + BR that satisfy its Dialectica interpretation, provably from the equations of [[bar recursion|8CCG6F2FAT]].
Here $\mathrm{DNS}$ is the schema $\forall n\, \neg \neg B(n) \to \neg \neg \forall n\, B(n)$, for every formula $B$.

### Lemma R

*Lemma R.* For every formula $C$, intuitionistic logic proves $\neg \forall x\, \neg C \leftrightarrow \neg \neg \exists x\, C$.

1. Assume $\neg \forall x\, \neg C$ and $\neg \exists x\, C$.
   From $\neg \exists x\, C$ we get $\forall x\, \neg C$, a contradiction, so $\neg \neg \exists x\, C$.
2. Assume $\neg \neg \exists x\, C$ and $\forall x\, \neg C$.
   From $\forall x\, \neg C$ we get $\neg \exists x\, C$, a contradiction, so $\neg \forall x\, \neg C$.

### Lemma A

*Lemma A.* $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC}^0 + \mathrm{DNS}$ proves $(\mathrm{AC}^0)^N$, the Gödel-Gentzen translation of every instance of $\mathrm{AC}^0$.

3. Fix a formula $A(n, x)$.
   The translation of the instance is $\forall n\, \neg \forall x\, \neg A^N(n, x) \to \neg \forall f\, \neg \forall n\, A^N(n, f\, n)$.
4. Assume $\forall n\, \neg \forall x\, \neg A^N(n, x)$.
   By Lemma R, $\forall n\, \neg \neg \exists x\, A^N(n, x)$.
5. DNS with $B(n) = \exists x\, A^N(n, x)$ gives $\neg \neg \forall n\, \exists x\, A^N(n, x)$.
6. $\mathrm{AC}^0$ for the formula $A^N$ proves $\forall n\, \exists x\, A^N(n, x) \to \exists f\, \forall n\, A^N(n, f\, n)$.
7. If $X \to Y$ is provable, then so is $\neg \neg X \to \neg \neg Y$, by Lemma 2(b) of the [[proof of the translation theorem|3WH3N4GY7W]].
   So $\neg \neg \exists f\, \forall n\, A^N(n, f\, n)$.
8. By Lemma R, $\neg \forall f\, \neg \forall n\, A^N(n, f\, n)$, which is the conclusion of step 3.

### The main proof

9. Assume that $\mathsf{WE}\text{-}\mathsf{PA}^\omega + \mathrm{AC}^0$ proves $\forall n\, \exists m\, \varphi(n, m)$.
10. By the [[Gödel-Gentzen translation theorem|WC4TDGEWZR]] for arithmetic in all finite types, $\mathsf{WE}\text{-}\mathsf{HA}^\omega + (\mathrm{AC}^0)^N$ proves $(\forall n\, \exists m\, \varphi)^N$.
11. By Lemma A, $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC}^0 + \mathrm{DNS}$ proves the same formula.
12. The translation is $\forall n\, \neg \forall m\, \neg \varphi^N$, and $\varphi^N \leftrightarrow \varphi$ since $\varphi$ is decidable.
    By Lemma R it is equivalent to $\forall n\, \neg \neg \exists m\, \varphi(n, m)$.
13. $\mathrm{AC}^0$ is an instance of $\mathrm{AC}$.
    So by S1 and S2, applied by induction on the derivation, the Dialectica interpretation of this formula has a witness in T + BR.
14. The interpretation of $\neg \neg \exists m\, \varphi$ is $\exists m\, \neg \neg \varphi(n, m)$, as in the [[soundness proof|X79VFTRT8Y]].
    With the clause for $\forall$, the interpretation of step 12 is $\exists Y\, \forall n\, \neg \neg \varphi(n, Y\, n)$.
15. So a closed term $t$ of T + BR satisfies $\neg \neg \varphi(n, t\, n)$, provably from the equations of BR.
16. $\varphi$ is decidable, so $\neg \neg \varphi(n, t\, n) \to \varphi(n, t\, n)$, and this proves the theorem.

Step 13 uses that the induction on derivations in the proof of S1 treats each axiom separately, so new axioms with witnesses can be added, and new constants with their equations can be added to T.

## Idea

Classical analysis differs from classical arithmetic in all types by countable choice.
The negative translation of countable choice reduces to choice itself, which the Dialectica interpretation validates, plus the double negation shift.
Bar recursion is exactly what is needed to witness the double negation shift.

## Variants

For dependent choice in place of $\mathrm{AC}^0$ the proof needs more than this outline, and we only cite that extension.
With modified bar recursion, a proof by modified realizability replaces the Dialectica interpretation.
With products of selection functions, the main lemma S2 becomes a statement about optimal strategies in sequential games.
