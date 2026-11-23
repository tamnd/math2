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

Let $\mathcal{M}$ have domain $\{0, 1\}$, in the signature with equality only.
In [[independence-friendly logic|DPMKT2KRB8]], the formula $\psi = \forall x \, (\exists y / x) \, (x = y)$ means: Abelard picks $x$, and then Eloise picks $y$ without knowing $x$.
We show that neither player has a winning strategy in this game.

1. A strategy of Eloise cannot depend on $x$, so it is a constant $b \in \{0, 1\}$.
2. Against the strategy $b$, Abelard can play $a = 1 - b$.
   Then $x = y$ fails, and Eloise loses, so no strategy of Eloise is winning.
3. A strategy of Abelard is a choice $a \in \{0, 1\}$.
4. Against the strategy $a$, Eloise can play $b = a$, since a constant guess is a legal strategy for her.
   Then $x = y$ holds, and Abelard loses, so no strategy of Abelard is winning.
5. So the game is not [[determined|QXECDPAYTN]].

The condition that fails is perfect information, which every first-order [[evaluation game|D45Z7HETDA]] has.

## Remarks

In the first-order game for $\forall x \, \exists y \, (x = y)$, Eloise sees $x$ and answers $b = a$, so she wins, and the sentence is true.
Hiding information changes the meaning: under game semantics, $\psi$ is neither true nor false in $\mathcal{M}$.
So IF logic does not satisfy the law of excluded middle, since neither $\psi$ nor its game negation has a winning strategy for its verifier.
The size of the domain matters: in a one-element structure, the only constant strategy wins, and $\psi$ is true.

## Explanations

### L1 human

Abelard hides a coin that shows $0$ or $1$, and Eloise must guess it without looking.
No fixed guess always wins, and no fixed way of hiding always wins either.
So neither player has a sure plan, and the statement is neither true nor false.

### L2 human

We list the four plays, with Abelard's move $a$ first and Eloise's move $b$ second.
With $a = 0$, the guess $b = 0$ wins for Eloise and $b = 1$ wins for Abelard.
With $a = 1$, the guess $b = 0$ wins for Abelard and $b = 1$ wins for Eloise.
No single choice of one player wins against both choices of the other.
This failure of determinacy is the first sign that imperfect information leads beyond first-order logic.
Watch out: a mixed strategy, such as a fair coin, does not make the game determined, because game semantics asks for a sure win, and the coin wins only with probability $1/2$.
