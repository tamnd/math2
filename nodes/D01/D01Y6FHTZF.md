---
tag: D01Y6FHTZF
kind: statement
role: theorem
name: Strategy-stealing argument
msc: [91A46, 05C65]
uses: [CH2JRZNX7V, 0BBTH3YSZA]
about: [CH2JRZNX7V]
sources:
  - url: https://en.wikipedia.org/wiki/Strategy-stealing_argument
same_as:
  wikidata: Q1158962
  wikipedia: Strategy-stealing argument
---

## Statement

Let $X$ be a [[finite set|0BBTH3YSZA]] and let $\mathcal{F}$ be a family of subsets of $X$, so that $(X, \mathcal{F})$ is a [[hypergraph|CH2JRZNX7V]].
In the *strong positional game* on $(X, \mathcal{F})$, two players alternately claim one element of $X$ not yet claimed, starting with the first player.
The first player to claim all elements of some set in $\mathcal{F}$ wins.
If all of $X$ is claimed and nobody has won, the game is a draw.
Then the second player has no winning strategy.
Equivalently, the first player has a strategy that guarantees at least a draw.

## Remarks

Suppose the second player had a winning strategy $S$.
The first player claims an arbitrary element and then pretends to be the second player, answering with $S$ and ignoring her extra element.
If $S$ tells her to claim the extra element, she claims another arbitrary element instead.
An extra claimed element never hurts in a positional game, so she wins, which is impossible because the two players cannot both have winning strategies.
The game is finite with perfect information.
So by Zermelo's theorem, either one player can force a win, or both players can force at least a draw.

Example: in tic-tac-toe, $X$ is the set of $9$ squares and $\mathcal{F}$ is the set of $8$ lines, so the first player can guarantee at least a draw.
The same idea shows that the first player wins Hex, because Hex cannot end in a draw.
In Chomp on a rectangle larger than $1 \times 1$, the first player wins.
If taking only the corner square opposite the poisoned one were a losing move, its winning reply would also be available as a first move.

The argument is not constructive: it shows that a good strategy exists without describing it.
It needs the symmetry of the rules and the fact that extra moves never hurt.
It fails, for example, in games where a player may be forced to make a bad move.

## Explanations

### L1 human

If the second player had a sure way to win, the first player could steal it.
She makes any first move and then plays as if she were second, following the stolen recipe.
Her extra piece can only help her, so she would win too, which is a contradiction.
So in games like tic-tac-toe or Hex the first player is never at a disadvantage.

### L2 human

Strategy stealing is the standard tool for showing that the first player cannot lose in symmetric games where extra moves never hurt.
It applies to positional games such as tic-tac-toe and its higher-dimensional versions, to Hex, and to Chomp.
Its weakness is that it gives no strategy, and for Hex on large boards no explicit winning strategy is known.
Combined with Zermelo's theorem on finite games of perfect information, it turns "the second player cannot win" into "the first player can win" whenever draws are impossible.
