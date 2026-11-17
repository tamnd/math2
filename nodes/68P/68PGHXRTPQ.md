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

For a string $\sigma$, let $l(\sigma)$ be its number of left brackets and $r(\sigma)$ its number of right brackets.
An initial segment of $\sigma$ is a string $\tau$ with $\sigma = \tau\rho$ for some string $\rho$; it is proper when $\rho$ is not empty.
All inductions below are [[inductions on formulas|EDRV3N0SA3]], by the [[definition|TFDYXS3K1N]] of $\mathrm{Form}$.

1. Lemma 1: $l(\varphi) = r(\varphi)$ for each formula $\varphi$. A variable has no brackets, and each formation rule adds one left and one right bracket.
2. Lemma 2: each nonempty proper initial segment $\tau$ of a formula $\varphi$ has $l(\tau) > r(\tau)$. We prove it by induction on $\varphi$.
3. A variable has length $1$, so it has no nonempty proper initial segment, and Lemma 2 holds for it.
4. Let $\varphi = (\neg \psi)$, where $\psi$ has the property of Lemma 2. A nonempty proper initial segment $\tau$ of $\varphi$ is $($, or $(\neg$, or $(\neg \tau'$ with $\tau'$ a nonempty initial segment of $\psi$.
5. In the first two cases $l(\tau) = 1 > 0 = r(\tau)$.
6. In the third case, $l(\tau') \geq r(\tau')$, by Lemma 2 for $\psi$ if $\tau'$ is proper and by Lemma 1 if $\tau' = \psi$. So $l(\tau) = 1 + l(\tau') > r(\tau') = r(\tau)$.
7. Let $\varphi = (\psi \circ \chi)$, where $\psi$ and $\chi$ have the property of Lemma 2. A nonempty proper initial segment $\tau$ of $\varphi$ is $($, or $(\tau'$ with $\tau'$ a nonempty initial segment of $\psi$, or $(\psi \circ$, or $(\psi \circ \tau''$ with $\tau''$ a nonempty initial segment of $\chi$.
8. In the case $($ we have $1 > 0$.
9. In the case $(\tau'$, as in step 6, $l(\tau') \geq r(\tau')$, so $l(\tau) = 1 + l(\tau') > r(\tau') = r(\tau)$.
10. In the case $(\psi \circ$, Lemma 1 gives $l(\psi) = r(\psi)$, so $l(\tau) = 1 + l(\psi) > r(\psi) = r(\tau)$.
11. In the case $(\psi \circ \tau''$, Lemma 1 for $\psi$ and the argument of step 6 for $\tau''$ give $l(\tau) = 1 + l(\psi) + l(\tau'') > r(\psi) + r(\tau'') = r(\tau)$.
12. This proves Lemma 2. Corollary: no nonempty proper initial segment $\tau$ of a formula is a formula, since a formula has $l = r$ by Lemma 1 and $\tau$ has $l(\tau) > r(\tau)$ by Lemma 2.
13. Lemma 3: each formula is nonempty, and its first symbol is a variable or a left bracket. This holds for variables, and both formation rules give strings that begin with $($.
14. Existence of a form. The set $S$ of formulas that have one of the forms 1, 2 or 3 contains the variables and is closed under the formation rules, since each rule produces a string of form 2 or 3. So $S$ is closed, and $\mathrm{Form} \subseteq S$ by the minimality of $\mathrm{Form}$.
15. The forms exclude each other. A variable has length $1$, and strings of forms 2 and 3 have length at least $4$, so form 1 excludes the others.
16. In form 2 the second symbol is $\neg$. In form 3 the second symbol is the first symbol of the formula $\psi$, which is a variable or a left bracket by Lemma 3, and not $\neg$. So forms 2 and 3 exclude each other.
17. Uniqueness in form 2. If $(\neg \psi) = (\neg \psi')$, then removing the first two symbols and the last symbol gives $\psi = \psi'$.
18. Uniqueness in form 3. Let $(\psi \circ \chi) = (\psi' \circ' \chi')$ with $\psi, \chi, \psi', \chi'$ formulas. Remove the first symbol: the string $\psi \circ \chi)$ equals the string $\psi' \circ' \chi')$.
19. So $\psi$ and $\psi'$ are both initial segments of one string, and the shorter one is an initial segment of the longer one.
20. If $\psi \neq \psi'$, the shorter one is a nonempty proper initial segment of the longer one, and both are formulas. This contradicts the corollary of step 12, so $\psi = \psi'$.
21. After $\psi = \psi'$ the next symbols agree, so $\circ = \circ'$. The remaining strings $\chi)$ and $\chi')$ are equal, so $\chi = \chi'$.
22. Steps 14 to 21 show that each formula has exactly one of the three forms, with a unique $\psi$ in form 2 and a unique triple $(\circ, \psi, \chi)$ in form 3.

## Idea

Read a formula from the left and keep the difference between left and right brackets.
This difference is positive inside the formula and returns to $0$ only at the last symbol.
So a formula cannot begin with a shorter formula, and the first formula after the opening bracket ends at a determined place.
That place determines the main connective and both parts.

## Variants

- Parsing algorithm. Enderton gives the theorem as the correctness of an algorithm: remove the outer brackets, find the first position where the bracket count returns to $0$, and split there. The proof of correctness uses the same two lemmas.
- Polish notation. Give each variable weight $1$, the letter $N$ weight $0$, and each binary letter weight $-1$. Induction shows that each formula has weight $1$ and each nonempty proper initial segment has weight at most $0$. The rest of the proof is the same, with weight in place of the bracket difference.
- Free algebra. One can define formulas as abstract trees instead of strings. Then unique readability is built into the definition, and the work moves to the proof that the bracketed strings represent the trees faithfully.
