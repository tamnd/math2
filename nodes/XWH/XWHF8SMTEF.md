---
tag: XWHF8SMTEF
kind: example
name: Dialectica interpretation of contraction for a universal formula
msc: ["03F10", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [HZ17ES9PDY]
uses: [ZREF8MTYNW, A4WR995XZP, X79VFTRT8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Proof translation (soundness)
---

## Example

Let $\varphi(z)$ be a quantifier-free formula, and let $A = \forall z\, \varphi(z)$.
We find a witness for the contraction axiom $A \to A \wedge A$ under the [[Dialectica interpretation|ZREF8MTYNW]].

1. The premise $A$ has an empty witness and the challenge $z$, so $A^D = \forall z\, \varphi(z)$.
2. The conclusion has an empty witness and the pair of challenges $(z_1, z_2)$, so $(A \wedge A)^D = \forall z_1, z_2\, (\varphi(z_1) \wedge \varphi(z_2))$.
3. By the clause for $\to$, we need one function $f$ that turns the two challenges of the conclusion into one challenge of the premise:
   $$(A \to A \wedge A)^D = \exists f\, \forall z_1, z_2\, \bigl( \varphi(f z_1 z_2) \to \varphi(z_1) \wedge \varphi(z_2) \bigr).$$
4. We take $f z_1 z_2 = \mathrm{if}\ \varphi(z_1)\ \mathrm{then}\ z_2\ \mathrm{else}\ z_1$, a definition by cases in [[system T|A4WR995XZP]].
5. If $\varphi(z_1)$ holds, then $f z_1 z_2 = z_2$, and the premise $\varphi(z_2)$ together with $\varphi(z_1)$ gives the conclusion.
6. If $\varphi(z_1)$ fails, then $f z_1 z_2 = z_1$, so the premise $\varphi(z_1)$ is false and the implication holds.
7. T proves $\varphi(z_1) \vee \neg \varphi(z_1)$, because $\varphi$ is quantifier-free, so the two cases cover everything.

So $f$ witnesses the contraction axiom for $A$.

## Remarks

The example shows the one place where the [[soundness proof|X79VFTRT8Y]] needs decidability.
The conclusion offers two tests, but we may pass only one of them to the premise, so we must find out which test is the dangerous one.

Neither fixed choice works.
For $f z_1 z_2 = z_1$, take $\varphi(z) = (z \le 10)$, $z_1 = 4$ and $z_2 = 12$.
Then the premise $\varphi(4)$ holds, but the conclusion $\varphi(4) \wedge \varphi(12)$ fails.
For $f z_1 z_2 = z_2$, swap the two tests, and the same failure appears.

For a general formula $A$ the same trick works with the quantifier-free matrix $A_D(x, y_1)$ in place of $\varphi(z_1)$, and the witness $x$ of the premise is copied into both conjuncts.
The Diller-Nahm variant avoids the case split by passing both tests to the premise as a finite list.

## Explanations

### L1 human

The statement "$A$ implies $A$ and $A$" looks empty, but in the game reading it has content.
The opponent offers two tests $z_1$ and $z_2$ for the conclusion, and we may pass only one test to the premise.
The strategy is this: if $z_1$ passes, pass on $z_2$; otherwise pass on $z_1$, which already fails.
With the property "$z \le 10$" and the tests $4$ and $12$, we pass on $12$, the test that fails.

### L2 human

We run the witness on three pairs, with $\varphi(z) = (z \le 10)$.

1. For $(z_1, z_2) = (4, 7)$: $\varphi(4)$ holds, so $f = 7$.
   The premise $\varphi(7)$ is true, and the conclusion $\varphi(4) \wedge \varphi(7)$ is true.
2. For $(4, 12)$: $\varphi(4)$ holds, so $f = 12$.
   The premise $\varphi(12)$ is false, so the implication holds.
3. For $(12, 4)$: $\varphi(12)$ fails, so $f = 12$, and the premise is false again.

The typical use is in any proof step that uses an assumption twice.
Watch out: a choice of challenge that does not look at $\varphi$ fails on some pair.
