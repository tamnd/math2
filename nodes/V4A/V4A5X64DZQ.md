---
tag: V4A5X64DZQ
kind: example
name: The copy-cat strategy wins P or not P
aliases: [copy-cat-strategy, chess-or-not-chess]
msc: ["03B70", "03B47"]
topics: [NJB94B39QK]
audience: research
instance_of: [C7CV0XMSTT]
uses: [C7CV0XMSTT, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Computability_logic
    locator: Semantics
---

## Example

Let $A$ be any static game, and consider the parallel disjunction $A \vee \neg A$ of [[computability logic|C7CV0XMSTT]].
This is a play on two boards.
On board 1 the machine plays $A$ in its own role.
On board 2 it plays $\neg A$, so it plays the environment role of $A$, and the environment plays the machine role of $A$.
The machine wins $A \vee \neg A$ if it wins on at least one board.

Claim: the following *copy-cat strategy* wins $A \vee \neg A$ against every behavior of the environment.
Whenever the environment makes a move on one board, the machine makes the same move on the other board.

1. A move of the environment on board 1 is a move of the environment role of $A$. The machine plays that role on board 2, so the copy is a move of the correct role there.
2. A move of the environment on board 2 is a move of the machine role of $A$. The machine plays that role on board 1, so again the copy is a move of the correct role.
3. Each move is copied after a finite delay. So, in the limit, the two boards carry the same moves of $A$, made by the same roles.
4. The order of moves on the two boards can differ, because each copy comes later than its original. A static game never punishes a player for delaying its own moves. We use this property in the form: the delays of the copy-cat do not change which role wins on either board.
5. Let $\Gamma$ be the common run of $A$ from step 3. Case 1: the machine role of $A$ wins $\Gamma$. Then the machine wins board 1.
6. Case 2: the environment role of $A$ wins $\Gamma$. On board 2 the machine plays the environment role, so the machine wins board 2.
7. In both cases the machine wins at least one board, so it wins $A \vee \neg A$.

The strategy does not depend on $A$, so one machine wins every instance.
So $P \vee \neg P$, with $P$ a general atom, is a valid formula: the form of the [[law of excluded middle|0RYYK8PG4S]] with parallel disjunction.

For chess with ties ruled out, $\text{Chess} \vee \neg \text{Chess}$ is a game on two boards, one played as white and one as black.
The machine copies the opponent's moves from one board to the other, and it wins on at least one board, whoever the opponent is.

## Remarks

The copy-cat strategy never chooses a side, and this is why it works for the parallel disjunction only.
In the choice disjunction $P \sqcup \neg P$ the machine must choose one disjunct, and then it must win that game alone.
This form of excluded middle is not valid; see [[deciding the halting problem as a game|3CBR9YYH4T]].

## Explanations

### L1 human

Play two chess games against a master, one with white and one with black.
Copy each of the master's moves to the other board.
Then the master really plays against itself, and you win one of the two games.

### L2 human

Negation swaps the roles of the players, so the two boards of $A \vee \neg A$ carry the same game from opposite sides.
Copying moves makes the two plays identical, so exactly one role wins, and the machine holds that role on one of the boards.
A trap is to think that this proves $A \sqcup \neg A$: there the machine must say in advance which board it will win, and copy-cat gives no such choice.
