---
tag: HYQPVQF509
kind: example
name: Nim
msc: [91A46]
instance_of: [SHQ800E0J4]
sources:
  - url: https://en.wikipedia.org/wiki/Nim
same_as:
  wikidata: Q724409
  wikipedia: Nim
---

## Example

In *Nim*, there are $k$ heaps of tokens, of sizes $n_1, \dots, n_k \ge 0$.
Two players move alternately; a move removes one or more tokens from a single heap.
Under normal play, the player who takes the last token wins, because the opponent then has no move.
Both players have the same moves in every position, so Nim is an impartial [[combinatorial game|SHQ800E0J4]].
Every play ends, since each move lowers the total number of tokens.

Write $n_1 \oplus \cdots \oplus n_k$ for the *nim-sum*: the binary digits of the $n_i$ are added without carrying, that is, modulo $2$ in each place.
Bouton's theorem (1901) says that the player to move loses, under best play of the opponent, exactly when $n_1 \oplus \cdots \oplus n_k = 0$.

Check with heaps $(1, 2, 3)$: in binary $01 \oplus 10 \oplus 11 = 00$, so the player to move loses.
For instance, if she empties the heap of $3$, the opponent answers with $(1, 1, 0)$, and $1 \oplus 1 = 0$ again.

Check with heaps $(3, 4, 5)$: $011 \oplus 100 \oplus 101 = 010 = 2 \ne 0$, so the player to move wins.
A winning move turns the heap of $3$ into $3 \oplus 2 = 1$, giving $(1, 4, 5)$ with $001 \oplus 100 \oplus 101 = 000$.

## Explanations

### L1 human

Nim is a simple game with piles of matches, where each turn you take as many matches as you like from one pile, and whoever takes the last match wins.
It looks like a game of guessing, but there is a complete recipe for perfect play.
Write the pile sizes in binary and add them without carrying; if the result is zero, the player to move is in trouble.
The winning strategy is always to move so that this "nim-sum" becomes zero.
Nim is important because, by the Sprague–Grundy theorem, every impartial game behaves like a Nim heap.
