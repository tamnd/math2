---
tag: 783HAVZ1MV
kind: example
name: Universal quantifiers do not make a polyadic algebra
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: CQ9A86S3J4
    note: universal quantification fails the law p below its quantification
uses: [3GG2T69SSE, W1CR668N0Z]
sources:
  - url: https://en.wikipedia.org/wiki/Polyadic_algebra
---

## Example

Take the Boolean algebra $A = \mathcal{P}(\set{0, 1}^{\set{1, 2}})$ and the substitutions of [[the functional algebra|W1CR668N0Z]].
Replace the existential quantifiers by universal ones: $\forall(J) p = \set{x : y \in p \text{ for every } y \text{ with } y_i = x_i \text{ for } i \notin J}$.

1. A quantifier must satisfy $p \le \exists p$; see [[the definition|3GG2T69SSE]].
2. Take $p = \set{(0, 1)}$ and $J = \set{1}$.
3. The assignment $(0, 1)$ is in $p$, but $(1, 1)$ agrees with it off $J$ and is not in $p$. So $(0, 1) \notin \forall(J) p$.
4. In fact $\forall(J) p = \emptyset$, so $p \not\subseteq \forall(J) p$.

So $(A, I, S, \forall)$ is not a [[polyadic algebra|CQ9A86S3J4]].

## Remarks

1. Universal quantifiers satisfy the dual laws: $\forall 1 = 1$, $\forall p \le p$, and $\forall(p \lor \forall q) = \forall p \lor \forall q$.
2. So $\forall(J) p = \neg \exists(J) \neg p$ recovers the polyadic structure. The choice of $\exists$ as primitive is a convention.
3. Clauses 1 to 6 of the definition hold for $\forall$ in this model; only the quantifier laws fail.

## Explanations

### L1 human

"For all $v_1$" is a stronger claim than the claim itself.
A quantifier in the sense of the definition must give a weaker claim.
So "for all" has the wrong direction, although it is the dual of the right operation.

### L2 human

1. $p = \set{(0, 1)}$ says "$v_1 = 0$ and $v_2 = 1$".
2. "For all $v_1$, ($v_1 = 0$ and $v_2 = 1$)" is false everywhere.
3. So $\forall(\set{1}) p = \emptyset$, which is below $p$, not above it.

The typical use: the example fixes the direction of the quantifier laws.
The trap: one can write the theory with $\forall$ as primitive, but then all laws must be dualized.
