---
tag: SKJFMANQTW
kind: example
name: Theorems and metatheorems of a Hilbert system
msc: ["03B99", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug2
instance_of: [D9G8M42GKC]
uses: [D9G8M42GKC, 1MGMQX43B8, 9X08XK5RV2]
sources:
  - url: https://en.wikipedia.org/wiki/Metatheorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: lead section
  - book: isbn:9781482237726
---

## Example

We prove that $p \to p$ is a theorem twice, once inside a formal system and once about it, and sort every symbol into the two levels of [[object language and metalanguage|D9G8M42GKC]].
The object language $L$ is propositional logic, with the variables $p, q, r, \dots$, the connectives $\neg$ and $\to$, and parentheses.
The formal system is the [[Hilbert system|1MGMQX43B8]] $H$ with the rule modus ponens and the axiom schemas
$$\begin{aligned} &\text{A1: } \varphi \to (\psi \to \varphi), \\ &\text{A2: } (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ &\text{A3: } (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi). \end{aligned}$$
The metalanguage is mathematical English with the metavariables $\varphi, \psi, \chi, \Gamma$ and the turnstile $\vdash$.

First, the theorem.

1. The string $p \to p$ has three symbols of $L$: the variable $p$, the connective $\to$ and the variable $p$.
   So it is a formula of $L$.
2. It has a derivation in $H$ of five lines: an instance of A2, an instance of A1, modus ponens, another instance of A1, and modus ponens.
   [[Formal system|439M8B4DY2]] writes the lines out.
3. So $p \to p$ is a theorem of $H$, and it is an object of the object language.
4. The sentence "$\vdash p \to p$" is not a formula of $L$, because $\vdash$ is not a symbol of $L$.
   It is a true statement of the metalanguage about $H$.

Second, a metatheorem.

5. The [[deduction theorem|9X08XK5RV2]] says: for every set $\Gamma$ of formulas and all formulas $\varphi$ and $\psi$, if $\Gamma \cup \{ \varphi \} \vdash \psi$, then $\Gamma \vdash \varphi \to \psi$.
6. The words "for every", "if" and "then", the letters $\Gamma, \varphi, \psi$, the set symbols $\cup$ and $\{ \}$, and the turnstile all belong to the metalanguage.
7. The arrow in "$\varphi \to \psi$" is the symbol $\to$ of $L$, and the expression denotes the formula $\ulcorner \varphi \to \psi \urcorner$ built from the values of $\varphi$ and $\psi$.
8. The proof of the deduction theorem is an induction on the length of derivations.
   It is an argument in the metalanguage, not a derivation in $H$.

Third, the metatheorem gives a second proof of the theorem.

9. The one-line list $p$ is a derivation of $p$ from the hypothesis set $\{ p \}$, so $\{ p \} \vdash p$.
10. The deduction theorem with $\Gamma = \emptyset$ and $\varphi = \psi = p$ gives $\emptyset \vdash p \to p$, that is, $\vdash p \to p$.

## Remarks

The two proofs of $\vdash p \to p$ live on different levels.
The first exhibits a derivation in $H$, and the second proves in the metalanguage that a derivation exists.
The proof of the deduction theorem is constructive, so it turns the one-line derivation of step 9 into an explicit derivation of $p \to p$ in $H$.

What changes in a richer system?
In a Hilbert system for first-order logic with the rule of generalization, the deduction theorem needs an extra condition on free variables, as [[generalization on a variable free in a hypothesis|VT4RFH9GNK]] shows.
That change happens in the metatheorem, while the object language only gains quantifiers.

## Explanations

### L1 human

Think of the rules of chess and a book about chess.
A move such as "pawn from e2 to e4" is part of the game.
A sentence in the book such as "a king and a rook can always force checkmate against a lone king" is a fact about the game, proved by reasoning about all possible games.
In logic, a theorem such as "p implies p" is like a move that you can actually make.
A metatheorem such as the deduction theorem is like the fact in the book.

### L2 human

Sort the symbols of the statement $\{ p, p \to q \} \vdash q$.
The letters $p$ and $q$ and the formula $p \to q$ belong to the object language.
The braces, the comma and $\vdash$ belong to the metalanguage, since they form a set of formulas and state derivability.
The statement is true, because the lines $p$, $p \to q$, $q$ form a derivation from the hypotheses, with the last line by modus ponens.
The deduction theorem with $\Gamma = \{ p \}$ then gives $\{ p \} \vdash (p \to q) \to q$, with no new derivation written by hand.
This is the typical use of metatheorems: they shorten work by proving facts about derivations instead of writing derivations.
Watch out for $p \to (\vdash q)$, which puts a turnstile inside a formula and belongs to neither level.
