---
tag: EY4Q36HP8J
kind: counterexample
name: Ellsberg paradox
msc: [91B06, 91B16]
uses: [5KZQYJHB3A, 8C2N37XPJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Ellsberg_paradox
same_as:
  wikidata: Q1332562
  wikipedia: Ellsberg paradox
---

## Counterexample

An urn holds $90$ balls: $30$ are red, and the other $60$ are black or yellow in an unknown proportion.
One ball is drawn, and four bets each pay $100$ euros on some colours and $0$ otherwise.

1. Bet $A$ pays on red.
2. Bet $B$ pays on black.
3. Bet $C$ pays on red or yellow.
4. Bet $D$ pays on black or yellow.

Many people prefer $A$ to $B$ and $D$ to $C$.
No [[subjective expected utility|5KZQYJHB3A]] representation fits these two choices.
Let $P$ be any probability on the colours and $u$ a utility with $u(100) > u(0)$.
The first choice means $P(\text{red}) > P(\text{black})$.
The second choice means $P(\text{black}) + P(\text{yellow}) > P(\text{red}) + P(\text{yellow})$, that is, $P(\text{black}) > P(\text{red})$.
The two inequalities contradict each other.

## Remarks

The choices violate Savage's sure-thing principle P2.
The bets $A$ and $B$ agree on yellow, where both pay $0$, and the bets $C$ and $D$ agree on yellow, where both pay $100$.
On red and black, $A$ agrees with $C$ and $B$ agrees with $D$.
So P2 requires $A \succsim B$ if and only if $C \succsim D$.
The usual explanation is ambiguity aversion: people prefer bets with known probabilities, $1/3$ for red and $2/3$ for black or yellow, to bets with unknown ones.
Models such as maxmin expected utility over a set of priors can represent these choices.

## Explanations

### L1 human

People prefer to bet on a colour whose chance they know over one whose chance is unknown.
Here this preference leads to choices that cannot come from any single belief about the urn.
The paradox, due to Daniel Ellsberg, shows that ambiguity is different from risk, and it is a central example in decision theory.
