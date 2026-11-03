---
tag: TBNSQP89PH
kind: statement
role: theorem
name: Gibbard–Satterthwaite theorem
msc: [91B12, 91B14, 91B03]
uses: [JGP0Q56FRY, 0FRXBVVR03, T1GTBBMHCW, VD8RCR44GQ]
about: [F17C7F17PM, DTXJQKEHDP]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbard%E2%80%93Satterthwaite_theorem
same_as:
  wikidata: Q612021
  wikipedia: Gibbard–Satterthwaite theorem
---

## Statement

Let $A$ be a finite set of alternatives and $N = \set{1, \dots, n}$ a finite set of voters.
Let $\mathcal{L}(A)$ be the set of [[linear orders|0FRXBVVR03]] of $A$.
Let $f \colon \mathcal{L}(A)^n \to A$ be a social choice function whose image has at least $3$ elements.
Call $f$ *strategyproof* if for every voter $i$, every profile $(\succ_1, \dots, \succ_n)$ and every $\succ_i' \in \mathcal{L}(A)$, it is not the case that
$$f(\succ_1, \dots, \succ_i', \dots, \succ_n) \succ_i f(\succ_1, \dots, \succ_i, \dots, \succ_n).$$
If $f$ is strategyproof, then $f$ is dictatorial.
This means that there is a voter $d$ such that, for every profile, $f(\succ_1, \dots, \succ_n)$ is the $\succ_d$-best element of the image of $f$.

## Remarks

Strategyproofness says that no voter can obtain an outcome she strictly prefers by misreporting her ranking; it is dominant-strategy [[incentive compatibility|T1GTBBMHCW]] for voting.
One proof shows that a strategyproof $f$ is monotone and Pareto efficient on its image.
From $f$ one builds a social welfare function satisfying the hypotheses of [[Arrow's impossibility theorem|VD8RCR44GQ]], so it has a dictator, and the dictator of that function dictates $f$.

Example: take candidates $a, b, c$, three voters, and the Borda count with $2, 1, 0$ points and ties broken in favour of $b$, then $a$, then $c$.
This rule is not dictatorial and its image has $3$ elements, so it is manipulable.
Concretely, let two voters report $a \succ b \succ c$ and let the third have $b \succ a \succ c$.
Sincere voting gives $a$ $5$ points and $b$ $4$ points, so $a$ wins.
If the third voter reports $b \succ c \succ a$ instead, $a$ and $b$ both get $4$ points, and the tie-break elects $b$, which she prefers.

The bound $3$ is necessary: with two alternatives, majority rule with an odd number of voters is strategyproof and not dictatorial.
Strategyproof rules exist on restricted domains, for example the median rule for single-peaked preferences.

## Explanations

### L1 human

In almost every election, a voter can sometimes do better by not voting sincerely.
The theorem makes this precise: with three or more possible outcomes, the only voting rules where honesty is always best are dictatorships.
So tactical voting cannot be designed away.

### L2 human

The theorem is the strategic counterpart of Arrow's theorem, and the two can be derived from each other.
It explains why mechanism design relies on money, randomization or restricted preference domains to get truthful reporting.
Gibbard's theorem extends it from voting rules to arbitrary game forms.
