---
tag: PPS9CC6H1Y
kind: statement
role: theorem
name: Gibbard's theorem
msc: [91B14, 91B03, 91A10]
uses: [JGP0Q56FRY, 0FRXBVVR03, 9BF72YM075, TBNSQP89PH]
about: [DTXJQKEHDP, F17C7F17PM]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbard%27s_theorem
same_as:
  wikidata: Q29479399
  wikipedia: Gibbard's theorem
---

## Statement

Let $A$ be a finite set of outcomes and $N = \set{1, \dots, n}$ a finite set of players.
A *game form* consists of nonempty strategy sets $S_1, \dots, S_n$ and an outcome function $g \colon S_1 \times \cdots \times S_n \to A$.
Assume that the image of $g$ has at least $3$ elements.
Assume also that each player $i$ has a [[dominant strategy|9BF72YM075]] for each strict preference $\succ_i$ (a [[linear order|0FRXBVVR03]]) of $A$.
This means some $s_i \in S_i$ such that $g(t_i, s_{-i}) \succ_i g(s_i, s_{-i})$ holds for no $t_i \in S_i$ and no $s_{-i}$.
Then $g$ is dictatorial: some player $d$ can force every outcome in the image of $g$.
That is, for each such outcome $a$ there is $s_d \in S_d$ with $g(s_d, s_{-d}) = a$ for every $s_{-d}$.

## Remarks

The idea of the proof is to fix, for each player and each preference, a dominant strategy.
Composing these choices with $g$ gives a social choice function on profiles of strict preferences, and the dominance property makes it strategyproof.
The [[Gibbard–Satterthwaite theorem|TBNSQP89PH]] then yields a dictator, and one checks that this player controls $g$.

The Gibbard–Satterthwaite theorem is the special case where $S_i = \mathcal{L}(A)$ and truth-telling is the dominant strategy.
Example: in approval voting each voter submits a set of approved candidates, and ties are broken by a fixed order.
With at least $3$ candidates this game form is not dictatorial, so for some preferences some voter has no dominant strategy.

The hypothesis of at least $3$ outcomes is needed.
With two outcomes and an odd number $n \ge 3$ of players, majority voting between them gives every player a dominant strategy without a dictator.

## Explanations

### L1 human

Any procedure for a group decision gives each person some options, such as ballots or bids, and maps the choices to an outcome.
Gibbard's theorem says that if every person always has a single best option no matter what others do, then one person controls the outcome.
So in every fair procedure with three or more outcomes, some people must think about what others will do.

### L2 human

The theorem is the general form of the Gibbard–Satterthwaite theorem, valid for any game form, not only for ranked ballots.
Together with the revelation principle it shows that dominant-strategy implementation without transfers is impossible beyond two outcomes.
