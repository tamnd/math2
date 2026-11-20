---
tag: MVADXMFV59
kind: concept
name: Island of knights and knaves
msc: ["03B05", "00A08"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 0S6GMNJ62Y, 05RSK4Q657]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section I
    note: adopted
    mention: wikipedia://en/76765067#VB7T
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Knights_and_Knaves
    locator: lead section
inventory: [GW406TE0GR]
---

## Summary

The island of knights and knaves is the setting of a family of logic puzzles.
Each inhabitant of the island is either a knight or a knave.
A [[knight|PGNY9Q8HXN]] makes only true statements, and a [[knave|GAXV5SEQ25]] makes only false statements.
A puzzle reports what some inhabitants say and asks for their types, or for another fact that their statements reveal.
The logical core is one rule: if $a$ is the [[proposition|0ZGC7ZESYN]] "inhabitant $A$ is a knight" and $A$ says $S$, then the [[biconditional|0S6GMNJ62Y]] $a \leftrightarrow S$ is true.
So a puzzle is a set of biconditionals, and its solutions are the rows of a [[truth table|05RSK4Q657]] in which all of them are true.
The setting matters as a first exercise in turning sentences into formulas and in reasoning by cases.

## Motivation

Many statements of logic are hard to test because their parts have no visible truth value.
On the island, every statement is tied to the type of its speaker, and the type is a single unknown truth value.
A puzzle therefore becomes a small problem of propositional logic with two to four variables.
The puzzles train the moves that proofs use: assume a case, follow its consequences, and reject the case when it leads to a contradiction.

## Notation

For each inhabitant $A, B, C, \ldots$, the lowercase letter $a, b, c, \ldots$ is the proposition "this inhabitant is a knight".
So $\neg a$ means "$A$ is a knave".
The statement "$A$ says $S$" is translated as $a \leftrightarrow S$.
Truth tables use T and F, with the rows in the standard order.

## Remarks

### Examples

1. [[Knights and knaves puzzles|K17GT0KGZF]]: $A$ says "we are both knaves", solved by a truth table and by cases, and the question that identifies the road to the village.
2. [[Three inhabitants, two statements: "all of us are knaves" and "exactly one of us is a knight"|7FH9D2MCRN]]: a puzzle with $8$ rows and one solution.
3. $A$ says "I am a knave or $B$ is a knight". The translation is $a \leftrightarrow (\neg a \lor b)$. If $a$ were false, the right side would be true, a contradiction. So $a$ is true, then $\neg a \lor b$ is true, so $b$ is true: both are knights.
4. $A$ says "$B$ is a knave". The translation $a \leftrightarrow \neg b$ says that $A$ and $B$ are of different types, but it does not say which is which.

### Non-examples

1. [[No inhabitant of the island can say "I am a knave"|5KXKTWPV3P]]: the translation $a \leftrightarrow \neg a$ is false in every row, so this statement never occurs on the island.
2. An inhabitant who sometimes lies and sometimes tells the truth is not a knight or a knave. Smullyan calls such an inhabitant a normal, and a statement by a normal gives no constraint at all.
3. The sentence "this sentence is false" is not a statement of an inhabitant. It is the [[liar sentence|KBYY281V8T]], and it has no speaker whose type could absorb the paradox.

### Basic properties

1. Every inhabitant can say "I am a knight". The translation $a \leftrightarrow a$ is a tautology, so the statement gives no information.
2. "$A$ says $B$ is a knight" means $a \leftrightarrow b$: $A$ and $B$ are of the same type.
3. To learn the type of $A$, ask a question with a known answer, for example "is $2 + 2 = 4$?". A knight says yes and a knave says no.
4. For any proposition $q$, the question "is it true that you are a knight if and only if $q$?" gets the answer yes exactly when $q$ is true. The answer is yes exactly when $a \leftrightarrow (a \leftrightarrow q)$ is true, and this formula is equivalent to $q$.
5. A puzzle about $n$ inhabitants has a truth table with $2^n$ rows. A puzzle is well posed when exactly one row makes all the biconditionals true, or when all such rows agree on the asked fact.

### History

Raymond Smullyan popularized the island of knights and knaves in his book "What Is the Name of This Book?" of 1978.
Smullyan was a mathematician and logician, and the puzzles of the book lead the reader from riddles to questions of logic.
The truth tables that solve such puzzles go back to the work of Wittgenstein and of Post in 1921.

### Common errors

1. A student takes the statement $S$ of an inhabitant as true. The rule is $a \leftrightarrow S$, and $S$ is true only when the speaker is a knight.
2. A student finds one consistent case and stops. A full solution also rejects the other cases, or the answer may not be unique.
3. A student negates the false statement of a knave wrongly. If a knave says "$A$ and $B$ are knights", then the true fact is "$A$ or $B$ is a knave", by [[De Morgan's laws|09PKJKA6J0]], not "both are knaves".

## Explanations

### L1 human

On the island, knights always tell the truth and knaves always lie.
Suppose an inhabitant says "I am a knight".
A knight would say this, because it is true.
A knave would also say this, because it is a lie.
So this sentence tells us nothing.
But if an inhabitant says "$2 + 2 = 5$", we know at once that this inhabitant is a knave.

### L2 human

We solve: $A$ says "$B$ is a knight", and $B$ says "$A$ and I are of different types".

1. Translate: $a \leftrightarrow b$ and $b \leftrightarrow (a \oplus b)$, where $\oplus$ is the exclusive or.
2. Case $b$ true. Then $a \oplus b$ must be true, so $a$ is false. But $a \leftrightarrow b$ requires $a$ true, a contradiction.
3. Case $b$ false. Then $a \oplus b$ must be false, so $a = b$, so $a$ is false. Then $a \leftrightarrow b$ is true, as required.
4. So both $A$ and $B$ are knaves, and this is the only solution.

The typical use of the island is to practise translation and case analysis on small problems.
A trap is to translate step 1 with $a \land b$ in place of $a \leftrightarrow b$, which forgets that a knave's statement is false.

### L3 human

A knights and knaves puzzle is an instance of propositional satisfiability: the biconditionals form a formula, and the solutions are its satisfying valuations.
The rule $a \leftrightarrow S$ gives each speaker a truth function, and nested reports such as "$A$ says that $B$ says $S$" become nested biconditionals.
Since $\leftrightarrow$ is associative and $a \leftrightarrow a$ is a tautology, many puzzle questions reduce to the identity $a \leftrightarrow (a \leftrightarrow q) \equiv q$.
Variants of the island add other kinds of inhabitants, such as normals, and each kind adds its own rule of translation.
