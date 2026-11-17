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
We verify the contraction axiom $A \to A \wedge A$ under the [[Dialectica interpretation|ZREF8MTYNW]].

1. $A^D = \forall z\, \varphi(z)$: the witness is empty, and the challenge is $z$.
2. $(A \wedge A)^D = \forall z_1, z_2\, (\varphi(z_1) \wedge \varphi(z_2))$: the challenge is the pair $(z_1, z_2)$.
3. By clause 4 of the definition, $(A \to A \wedge A)^D = \exists f\, \forall z_1, z_2\, (\varphi(f z_1 z_2) \to \varphi(z_1) \wedge \varphi(z_2))$.
4. Take $f z_1 z_2 = \mathrm{if}\ \varphi(z_1)\ \mathrm{then}\ z_2\ \mathrm{else}\ z_1$, a definition by cases in [[system T|A4WR995XZP]].
5. If $\varphi(z_1)$ holds, then $f z_1 z_2 = z_2$, and the premise $\varphi(z_2)$ together with $\varphi(z_1)$ gives the conclusion.
6. If $\varphi(z_1)$ fails, then $f z_1 z_2 = z_1$, so the premise $\varphi(z_1)$ is false and the implication holds.
7. T proves $\varphi(z_1) \vee \neg \varphi(z_1)$, so the two cases cover everything.

So $f$ witnesses the contraction axiom for $A$.

## Remarks

The example shows the one place where the [[soundness proof|X79VFTRT8Y]] needs decidability: the premise $A$ can test only one challenge, while the conclusion has two.
Neither projection works in general.
For $f z_1 z_2 = z_1$, take $\varphi(z) = (z \le 10)$, $z_1 = 4$ and $z_2 = 12$: the premise $\varphi(4)$ holds but the conclusion fails.
For $f z_1 z_2 = z_2$, swap the roles of $z_1$ and $z_2$.

## Explanations

### L1 human

The statement "$A$ implies $A$ and $A$" looks empty, but in the game reading it has content.
The opponent offers two tests $z_1$ and $z_2$ for the conclusion, but we may pass only one test to the premise.
The strategy is: if $z_1$ passes, pass on $z_2$; otherwise pass on $z_1$, which already fails.
For example, with the property "$z \le 10$" and the tests $4$ and $12$, we pass on $12$, the test that fails.

### L2 human

We run the witness on three pairs, with $\varphi(z) = (z \le 10)$.

1. For $(z_1, z_2) = (4, 7)$: $\varphi(4)$ holds, so $f = 7$. The premise $\varphi(7)$ is true, and the conclusion $\varphi(4) \wedge \varphi(7)$ is true.
2. For $(4, 12)$: $f = 12$. The premise $\varphi(12)$ is false, so the implication holds.
3. For $(12, 4)$: $\varphi(12)$ fails, so $f = 12$. The premise is false again.

The typical use is the verification of any proof step that uses an assumption twice.
A trap is to choose the challenge without looking at $\varphi$: a fixed choice fails on some pair.
