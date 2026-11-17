---
tag: ZZBH32V2EY
kind: example
name: An evaluation game with imperfect information is not determined
msc: ["03B60", "91A80"]
topics: [NJDME6F845]
audience: grad
not_instance_of:
  - target: D45Z7HETDA
    note: in the game for the IF formula, Eloise does not see Abelard's move, so the game has imperfect information and is not a first-order evaluation game; it is not determined
uses: [D45Z7HETDA, DPMKT2KRB8, QXECDPAYTN]
sources:
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: lead section
---

## Example

Let $\mathcal{M}$ have domain $\set{0, 1}$, in the signature with equality only.
In [[independence-friendly logic|DPMKT2KRB8]], the formula $\psi = \forall x \, (\exists y / x) \, (x = y)$ means: Abelard picks $x$, and then Eloise picks $y$ without knowing $x$.
We show that neither player has a winning strategy in this game.

1. A strategy of Eloise cannot depend on $x$, so it is a constant $b \in \set{0, 1}$.
2. Against the strategy $b$, Abelard can play $a = 1 - b$. Then $x = y$ fails, and Eloise loses. So Eloise has no winning strategy.
3. A strategy of Abelard is a choice $a \in \set{0, 1}$.
4. Against the strategy $a$, Eloise can play $b = a$, if she happens to choose it. Then $x = y$ holds, and Abelard loses that play. So Abelard has no winning strategy.
5. So the game is not [[determined|QXECDPAYTN]].

The condition that fails is perfect information, which the first-order [[evaluation game|D45Z7HETDA]] has.

## Remarks

In the first-order game for $\forall x \, \exists y \, (x = y)$, Eloise sees $x$ and answers $b = a$, so she wins, and the sentence is true.
The example shows that hiding information changes the meaning: $\psi$ is neither true nor false in $\mathcal{M}$ under game semantics.
So IF logic does not satisfy the law of excluded middle: neither $\psi$ nor its game negation has a winning strategy for its verifier.
In a one-element structure, the constant strategy wins, and $\psi$ is true.

## Explanations

### L1 human

Abelard hides a coin showing $0$ or $1$, and Eloise must guess it without looking.
No fixed guess always wins, and no fixed hiding choice always wins either.
So neither player has a sure plan, and the statement is neither true nor false.

### L2 human

We list the four plays.

1. $a = 0$, $b = 0$: Eloise wins. $a = 0$, $b = 1$: Abelard wins.
2. $a = 1$, $b = 0$: Abelard wins. $a = 1$, $b = 1$: Eloise wins.

No row of choices for one player wins against both choices of the other.
The typical use is to show why imperfect information leads beyond first-order logic.
A trap is to think that a mixed strategy, such as a fair coin, makes the game determined; game semantics asks for a sure win, and the fair coin wins with probability $1/2$ only.
