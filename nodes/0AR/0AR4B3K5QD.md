---
tag: 0AR4B3K5QD
kind: counterexample
name: Pairwise independent events that are not mutually independent
msc: [60A05]
uses: [0N57D1XY6T, 0GCVEV6BJA]
sources:
  - url: https://en.wikipedia.org/wiki/Pairwise_independence
    locator: Example
---

## Counterexample

Toss a fair coin two times, so $\Omega = \{HH, HT, TH, TT\}$ with probability $1/4$ for each outcome.
Let $A$ be "the first toss is heads", $B$ be "the second toss is heads", and $C$ be "the two tosses are equal".
Then $A = \{HH, HT\}$, $B = \{HH, TH\}$ and $C = \{HH, TT\}$, so $P(A) = P(B) = P(C) = 1/2$.
Each intersection of two of them is $\{HH\}$, with probability $1/4 = \frac12 \cdot \frac12$. So $A$, $B$ and $C$ are [[pairwise independent|0N57D1XY6T]].
But $P(A \cap B \cap C) = P(\{HH\}) = 1/4$, and $P(A) \, P(B) \, P(C) = 1/8$. So $A$, $B$ and $C$ are not [[mutually independent|0GCVEV6BJA]].

## Remarks

Here any two of the events determine the third: if $A$ and $B$ both occur, then $C$ occurs.
The same idea with $n$ fair bits and their sums modulo $2$ gives large pairwise independent families. Such families are useful in computer science.

## Explanations

### L1 human

If you know the first toss, you know nothing about $C$, and the same for the second toss.
But if you know both tosses, you know $C$ exactly. So the three events are not independent as a group.
