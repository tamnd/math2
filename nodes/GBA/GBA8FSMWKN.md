---
tag: GBA8FSMWKN
kind: example
name: Presburger arithmetic is not essentially undecidable
msc: ["03F30", "03B25"]
topics: [QHCRN4JVG0]
audience: research
not_instance_of:
  - target: Q5MT8WY7JM
    note: Presburger arithmetic is complete and decidable, so it is its own decidable consistent extension and cannot interpret an essentially undecidable theory
uses: [4W0E9G7PPV, 655K8Y7VS8, HWC687ES0Q, TKDKW5MENB]
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: Decidability of a theory
---

## Example

Let $\mathsf{Pr}$ be the set of sentences of the signature $\set{0, S, +, <}$ that are true in $(\N, 0, S, +, <)$.
This is [[Presburger arithmetic|4W0E9G7PPV]], given by its standard model.
It has no multiplication, and it is weak in that sense.
We show that it is not a weak theory of arithmetic in the sense of [[this page|Q5MT8WY7JM]], because it is not essentially undecidable.
We use Presburger's theorem that $\mathsf{Pr}$ is decidable, which rests on quantifier elimination.

1. $\mathsf{Pr}$ is consistent, since it has the model $(\N, 0, S, +, <)$.
2. $\mathsf{Pr}$ is [[complete|655K8Y7VS8]]: for each sentence $\varphi$, either $\varphi$ or $\neg \varphi$ is true in the model, so one of them lies in $\mathsf{Pr}$.
3. Let $T'$ be a consistent theory in the same signature with $\mathsf{Pr} \subseteq T'$.
4. Suppose $T' \vdash \varphi$ with $\varphi \notin \mathsf{Pr}$. By step 2, $\neg \varphi \in \mathsf{Pr} \subseteq T'$, so $T'$ is inconsistent, against step 3.
5. So $T'$ proves exactly the sentences in $\mathsf{Pr}$, and $T'$ is [[decidable|HWC687ES0Q]] by Presburger's theorem.
6. Hence every consistent extension of $\mathsf{Pr}$ is decidable, and $\mathsf{Pr}$ is not essentially undecidable.

## Remarks

The example shows that weakness in expressive power is not the point of the concept.
$\mathsf{Pr}$ has the full induction schema for its language, which $\mathsf{Q}$ lacks.
What it lacks is multiplication, and [[this non-example|TKDKW5MENB]] shows that multiplication is not definable from $0$, $S$, $+$ and $<$.
A consequence: no consistent extension of $\mathsf{Pr}$ interprets $\mathsf{Q}$, since a consistent theory that interprets an essentially undecidable theory is undecidable.
The same steps 1 to 6 work for any complete decidable theory, such as the theory of dense linear orders without endpoints.

## Explanations

### L1 human

Presburger arithmetic knows everything true about adding whole numbers, and a computer program can decide each of its questions.
A theory with this property cannot be a weak theory of arithmetic in our sense, since those theories are exactly the ones that no program can decide, however we extend them.
The reason Presburger arithmetic escapes is that it has no multiplication.

### L2 human

We decide one sentence of $\mathsf{Pr}$ by hand: $\forall x\, \exists y\,(x = y + y \lor x = S(y + y))$, "every number is even or odd".

1. Fix $n \in \N$.
2. If $n$ is even, then $n = 2k$, and $y = k$ gives $n = k + k$.
3. If $n$ is odd, then $n = 2k + 1$, and $y = k$ gives $n = S(k + k)$.
4. So the sentence is true in $(\N, 0, S, +, <)$, and it lies in $\mathsf{Pr}$.

The typical use of this example is as a contrast with $\mathsf{Q}$, which is weaker in proof power but essentially undecidable.
A trap is to think that the induction schema is what makes arithmetic undecidable; $\mathsf{Pr}$ has it and is decidable.
