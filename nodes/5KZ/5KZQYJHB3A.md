---
tag: 5KZQYJHB3A
kind: statement
role: theorem
name: Subjective expected utility
msc: [91B06, 91B16]
uses: [8C2N37XPJ8, JGP0Q56FRY, H67ET07G6W, 08QMKTWF9T]
about: [8C2N37XPJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Subjective_expected_utility
same_as:
  wikidata: Q1425777
  wikipedia: Subjective expected utility
---

## Statement

Let $S$ be a set of states, where every subset of $S$ is an event, and let $X$ be a set of consequences.
An act is a function $f \colon S \to X$ with finite range, and $\mathcal{F}$ is the set of acts.
Each consequence $x$ is identified with the constant act with value $x$.
For acts $f, g$ and an event $E$, let $f_E g$ be the act equal to $f$ on $E$ and to $g$ on $S \setminus E$.
Let $\succsim$ be a binary relation on $\mathcal{F}$.
An event $E$ is null if $f_E h \sim g_E h$ for all acts $f, g, h$.
Assume Savage's postulates P1 to P6.

1. P1: $\succsim$ is a [[preference relation|JGP0Q56FRY]] on $\mathcal{F}$.
2. P2 (sure-thing principle): for all acts $f, g, h, h'$ and events $E$, $f_E h \succsim g_E h$ if and only if $f_E h' \succsim g_E h'$.
3. P3: for every non-null event $E$, all consequences $x, y$ and every act $h$, $x_E h \succsim y_E h$ if and only if $x \succsim y$.
4. P4: for all events $A, B$ and consequences $x \succ y$ and $z \succ w$, $x_A y \succsim x_B y$ if and only if $z_A w \succsim z_B w$.
5. P5: there are consequences $x, y$ with $x \succ y$.
6. P6: for all acts $f \succ g$ and every consequence $x$, there is a finite [[partition|08QMKTWF9T]] $E_1, \dots, E_m$ of $S$ such that $x_{E_i} f \succ g$ and $f \succ x_{E_i} g$ for every $i$.

Then there are a unique finitely additive probability $P$ on the subsets of $S$ and a function $u \colon X \to \R$ such that, for all acts $f, g$,
$$f \succsim g \iff \sum_{x \in X} P(f^{-1}(x))\, u(x) \ge \sum_{x \in X} P(g^{-1}(x))\, u(x).$$
The function $u$ is unique up to a change $a u + b$ with $a > 0$ and $b \in \R$.
The probability $P$ is convex-ranged: for every event $A$ and every $\rho \in [0, 1]$ there is an event $B \subseteq A$ with $P(B) = \rho P(A)$.

## Remarks

This is Savage's representation theorem.
The proof first builds $P$ from bets.
By P4, the comparison of $x_A y$ with $x_B y$ defines an order "$A$ is at least as likely as $B$" that does not depend on the stakes.
P6 makes this order fine enough to be represented by a unique probability.
Acts are then turned into lotteries with these probabilities, and the [[von Neumann–Morgenstern utility theorem|H67ET07G6W]] gives $u$.
A seventh postulate, P7, extends the representation to acts with infinite range, and then $u$ is bounded.
The Ellsberg paradox is a pattern of choices that violates P2, so it has no representation of this form.
P6 forces $S$ to be infinite; a finite state space cannot satisfy it.

## Explanations

### L1 human

In many decisions the probabilities are not given, as in a bet on tomorrow's weather.
Savage showed that a person whose choices among such bets are consistent in a few precise ways acts as if they had their own probabilities.
They also act as if they had their own utilities for the outcomes.
They then pick the option with the highest expected utility under these personal probabilities.

### L2 human

This theorem is the foundation of Bayesian decision theory: probability is derived from choice, not assumed.
It combines a qualitative probability construction, driven by P4 and P6, with the [[expected utility|8C2N37XPJ8]] machinery of von Neumann and Morgenstern.
The Anscombe–Aumann framework reaches a similar conclusion more simply by letting acts give objective lotteries as outcomes.
