---
tag: Y3WXJP6FMB
kind: example
name: An undetermined sentence of independence-friendly logic
msc: ["03B60", "03C80"]
topics: [MDHDYV8QZW]
audience: research
instance_of: [DPMKT2KRB8]
uses: [DPMKT2KRB8, D45Z7HETDA]
sources:
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Semantics
---

## Example

In first-order logic every sentence is true or false in a structure, but in [[independence-friendly logic|DPMKT2KRB8]] a sentence can be neither.
Consider this sentence in a structure $\mathcal{M}$ with domain $M$ and empty vocabulary:
$$\varphi := \forall x \, (\exists y / \set{x}) \, x = y.$$
We show that $\varphi$ is neither true nor false when $M$ has at least two elements.
We also show that $\varphi$ is true when $M$ has one element.

1. In the game for $\varphi$, Abelard first chooses $a \in M$ as the value of $x$.
   Then Eloise chooses $b \in M$ as the value of $y$, and she wins if and only if $a = b$.
2. The slash $/ \set{x}$ hides the value of $x$ from Eloise.
   Her strategy must give the same $b$ in all plays that differ only in the value of $x$.
   So a strategy of Eloise is a constant $b \in M$.
3. Let $M$ have at least two elements, and let Eloise play the constant $b$.
   Abelard chooses some $a \neq b$ and wins.
   So Eloise has no winning strategy, and $\varphi$ is not true.
4. Abelard moves first and sees nothing, so a strategy of Abelard is a constant $a \in M$.
   Against it, the strategy $b = a$ of Eloise wins.
   So Abelard has no winning strategy, and $\varphi$ is not false.
5. By steps 3 and 4, $\varphi$ is undetermined in every structure with at least two elements.
6. If $M = \set{e}$, then $a = b = e$ in every play, so Eloise wins with $b = e$, and $\varphi$ is true.

## Remarks

### A third truth value

The example shows the third truth value of IF logic.
In first-order logic the game has perfect information and finite length, so one of the two players always has a winning strategy.
Here the hidden move breaks this.

The Skolem form of $\varphi$ is $\exists c \, \forall x \, x = c$, because the Skolem function of $y$ has no arguments.
So $\varphi$ is true exactly in the one-element structures.
Without the slash, $\forall x \, \exists y \, x = y$ is true in every structure, because $y$ may copy $x$.

### Excluded middle fails

In $\varphi \lor \neg \varphi$, Eloise first chooses a disjunct.
In $\varphi$ she has no winning strategy, by step 3.
In $\neg \varphi$ the players swap roles.
Eloise chooses $x$, Abelard chooses $y$ without seeing $x$, and Eloise wins if $x \neq y$.
Each strategy of Eloise is a constant $x = a$, and it loses against the constant strategy $y = a$ of Abelard.
So $\varphi \lor \neg \varphi$ is not true in a structure with two elements.

## Explanations

### L1 human

One player hides a coin in the left hand or the right hand.
The other player must name the hand, but cannot see which hand holds the coin.
The guesser has no sure way to win, so we cannot call the sentence "the guesser can find the coin" true.
The hider has no sure way to win either, because a lucky guess finds the coin.
So the sentence is neither true nor false.
With only one hand, the guesser always wins, and the sentence is true.

### L2 human

We check the claims on $M = \set{0, 1}$ by listing all strategies.

1. Eloise has two strategies that respect the slash: always $0$, or always $1$.
2. Abelard has two strategies: $x = 0$, or $x = 1$.
3. The four pairs give the plays $(0, 0)$, $(0, 1)$, $(1, 0)$ and $(1, 1)$, written as (value of $x$, value of $y$).
   Eloise wins exactly in $(0, 0)$ and $(1, 1)$.
4. Each strategy of Eloise loses against one strategy of Abelard.
   Each strategy of Abelard loses against one strategy of Eloise.
5. So neither player has a winning strategy, and $\varphi$ is undetermined in $M$.

Check: in the table of the four plays, every row and every column has one win for each player.
The typical use of this example is to test the semantics: it shows that IF logic has three truth values.
Watch out: Eloise may not use a strategy that depends on $x$, such as $y = x$, because the slash hides $x$.
