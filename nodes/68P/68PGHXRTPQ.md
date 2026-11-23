---
tag: 68PGHXRTPQ
kind: proof
name: Proof of unique readability by counting brackets
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
proves: 6KBJX91N7G
uses: [TFDYXS3K1N, EDRV3N0SA3]
methods: [12MQ2NJ29A, 0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
    locator: Propositional calculus
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Proof

We show that a formula never begins with a shorter formula, by counting brackets, and then read off the unique form.

For a string $\sigma$, let $l(\sigma)$ be its number of left brackets and $r(\sigma)$ its number of right brackets.
An initial segment of $\sigma$ is a string $\tau$ with $\sigma = \tau\rho$ for some string $\rho$, and it is proper when $\rho$ is not empty.
All inductions below are [[inductions on formulas|EDRV3N0SA3]], based on the [[definition|TFDYXS3K1N]] of $\mathrm{Form}$.

1. Lemma 1: $l(\varphi) = r(\varphi)$ for each formula $\varphi$.
   A variable has no brackets, and each formation rule adds one left and one right bracket.
2. Lemma 2: each nonempty proper initial segment $\tau$ of a formula $\varphi$ has $l(\tau) > r(\tau)$.
   We prove it by induction on $\varphi$.
   A variable has length $1$, so it has no nonempty proper initial segment.
3. Let $\varphi = (\neg \psi)$, where $\psi$ satisfies Lemma 2.
   A nonempty proper initial segment $\tau$ is $($, or $(\neg$, or $(\neg \tau'$ with $\tau'$ a nonempty initial segment of $\psi$.
   In the first two cases $l(\tau) = 1 > 0 = r(\tau)$.
   In the third case $l(\tau') \geq r(\tau')$, by Lemma 2 for $\psi$ if $\tau'$ is proper and by Lemma 1 if $\tau' = \psi$, so
   $$l(\tau) = 1 + l(\tau') > r(\tau') = r(\tau).$$
4. Let $\varphi = (\psi \circ \chi)$, where $\psi$ and $\chi$ satisfy Lemma 2.
   A nonempty proper initial segment $\tau$ is $($, or $(\tau'$ with $\tau'$ a nonempty initial segment of $\psi$, or $(\psi \circ$, or $(\psi \circ \tau''$ with $\tau''$ a nonempty initial segment of $\chi$.
   The case $($ gives $1 > 0$, and the case $(\tau'$ works as in step 3.
   In the case $(\psi \circ$, Lemma 1 gives $l(\tau) = 1 + l(\psi) > r(\psi) = r(\tau)$.
   In the case $(\psi \circ \tau''$, Lemma 1 for $\psi$ and the argument of step 3 for $\tau''$ give
   $$l(\tau) = 1 + l(\psi) + l(\tau'') > r(\psi) + r(\tau'') = r(\tau).$$
5. Corollary: no nonempty proper initial segment of a formula is a formula.
   Such a segment has $l > r$ by Lemma 2, while every formula has $l = r$ by Lemma 1.
6. Lemma 3: each formula is nonempty, and its first symbol is a variable or a left bracket.
   This holds for variables, and both formation rules give strings that begin with $($.
7. Every formula has one of the forms 1, 2 or 3.
   The set of formulas with one of these forms contains the variables and is closed under the formation rules, since each rule produces a string of form 2 or 3.
   So it contains $\mathrm{Form}$, by the minimality of $\mathrm{Form}$.
8. Form 1 excludes the others, because a variable has length $1$ and strings of forms 2 and 3 have length at least $4$.
9. Forms 2 and 3 exclude each other.
   In form 2 the second symbol is $\neg$.
   In form 3 the second symbol is the first symbol of the formula $\psi$, which is a variable or a left bracket by Lemma 3.
10. Uniqueness in form 2: if $(\neg \psi) = (\neg \psi')$, then removing the first two symbols and the last symbol gives $\psi = \psi'$.
11. Uniqueness in form 3: let $(\psi \circ \chi) = (\psi' \circ' \chi')$ with $\psi, \chi, \psi', \chi'$ formulas.
    Removing the first symbol gives the equal strings $\psi \circ \chi)$ and $\psi' \circ' \chi')$.
    So $\psi$ and $\psi'$ are initial segments of one string, and the shorter is an initial segment of the longer.
12. If $\psi \neq \psi'$, the shorter one is a nonempty proper initial segment of the longer one, and both are formulas.
    This contradicts the corollary of step 5, so $\psi = \psi'$.
13. With $\psi = \psi'$ the next symbols agree, so $\circ = \circ'$.
    The remaining strings $\chi)$ and $\chi')$ are equal, so $\chi = \chi'$.

Steps 7 to 13 show that each formula has exactly one of the three forms, with a unique $\psi$ in form 2 and a unique triple $(\circ, \psi, \chi)$ in form 3.

## Idea

Read a formula from the left and keep the difference between left and right brackets.
This difference stays positive inside the formula and returns to $0$ only at the last symbol.
So a formula cannot begin with a shorter formula.
Then, after the opening bracket of $(\psi \circ \chi)$, the first formula $\psi$ must end at one determined place, and that place fixes the main connective and both parts.
For example, in $((p \lor q) \to r)$ the differences after each symbol are $1, 2, 2, 2, 2, 1, 1, 1, 0$, and the first return to $1$ marks the end of $(p \lor q)$.

## Variants

Enderton presents the theorem as the correctness of a parsing algorithm: remove the outer brackets, find the first place where the bracket count returns to $0$, and split there.
The proof of correctness uses the same two lemmas.

For Polish notation, give each variable weight $1$, the letter $N$ weight $0$ and each binary letter weight $-1$.
Induction shows that each formula has weight $1$ and each nonempty proper initial segment has weight at most $0$.
The rest of the proof is the same, with weight in place of the bracket difference.

One can also define formulas as abstract trees instead of strings.
Then unique readability is built into the definition, and the work moves to the proof that the bracketed strings represent the trees faithfully.
