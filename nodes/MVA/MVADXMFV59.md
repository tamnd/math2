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

On an island where every inhabitant always tells the truth or always lies, an inhabitant who says "$2 + 2 = 5$" must be a liar.
The island of knights and knaves is the setting of a family of logic puzzles built on this idea.
A [[knight|PGNY9Q8HXN]] makes only true statements, a [[knave|GAXV5SEQ25]] makes only false statements, and every inhabitant is one of the two.
A puzzle reports what some inhabitants say and asks for their types, or for another fact that their statements reveal.
The logical core is one rule: if $a$ is the [[proposition|0ZGC7ZESYN]] "inhabitant $A$ is a knight" and $A$ says $S$, then the [[biconditional|0S6GMNJ62Y]] $a \leftrightarrow S$ is true.
So a puzzle is a set of biconditionals, and its solutions are the rows of a [[truth table|05RSK4Q657]] in which all of them are true.

## Motivation

Many statements of logic are hard to test because their parts have no visible truth value.
On the island, every statement is tied to the type of its speaker, and the type is a single unknown truth value.
A puzzle therefore becomes a small problem of propositional logic with two to four variables.
The puzzles train the moves that proofs use: assume a case, follow its consequences, and reject the case when it leads to a contradiction.
They are also a first exercise in turning sentences into formulas.

## Notation

For each inhabitant $A, B, C, \ldots$, the lowercase letter $a, b, c, \ldots$ is the proposition "this inhabitant is a knight", so $\neg a$ means "$A$ is a knave".
The statement "$A$ says $S$" is translated as $a \leftrightarrow S$.
Truth tables use T and F, with the rows in the standard order.

## Remarks

### A first puzzle on a small table

$A$ says "I am a knave or $B$ is a knight", so the puzzle is $a \leftrightarrow (\neg a \lor b)$.

| $a$ | $b$ | $\neg a \lor b$ | $a \leftrightarrow (\neg a \lor b)$ |
|---|---|---|---|
| T | T | T | T |
| T | F | F | F |
| F | T | T | F |
| F | F | T | F |

Only the first row makes the biconditional true, so $A$ and $B$ are both knights.
By cases: if $A$ were a knave, the part "I am a knave" would make the statement true, which a knave cannot say, so $A$ is a knight, and then $b$ must be true.

### Examples

[[Knights and knaves puzzles|K17GT0KGZF]]: $A$ says "we are both knaves", solved by a truth table and by cases, together with the question that identifies the road to the village.
[[Three inhabitants, two statements|7FH9D2MCRN]]: $A$ says "all of us are knaves" and $B$ says "exactly one of us is a knight", a puzzle with $8$ rows and one solution.
$A$ says "$B$ is a knave": the translation $a \leftrightarrow \neg b$ says that $A$ and $B$ are of different types, but not which is which.

### What does not fit the island

[[No inhabitant of the island can say "I am a knave"|5KXKTWPV3P]]: the translation $a \leftrightarrow \neg a$ is false in every row, so this statement never occurs.
An inhabitant who sometimes lies and sometimes tells the truth is neither a knight nor a knave.
Smullyan calls such an inhabitant a normal, and a statement by a normal gives no constraint at all.
The sentence "this sentence is false" has no speaker whose type could absorb the contradiction, so it is the [[liar sentence|KBYY281V8T]] and not a statement of an inhabitant.

### The rules you can use

Every inhabitant can say "I am a knight", because $a \leftrightarrow a$ is a tautology, so the statement gives no information.
"$A$ says $B$ is a knight" means $a \leftrightarrow b$: $A$ and $B$ are of the same type.
To learn the type of $A$, ask a question with a known answer, such as "is $2 + 2 = 4$?", since a knight says yes and a knave says no.
For any proposition $q$, the question "are you a knight if and only if $q$?" gets the answer yes exactly when $q$ is true, because $a \leftrightarrow (a \leftrightarrow q)$ is equivalent to $q$.
A puzzle about $n$ inhabitants has a truth table with $2^n$ rows, and it is well posed when the rows that make all biconditionals true agree on the fact asked for.

### Watch out

The statement $S$ of an inhabitant is not a fact; the fact is $a \leftrightarrow S$, and $S$ is true only when the speaker is a knight.
One consistent case is not a full solution, because a second consistent case may exist.
If a knave says "$A$ and $B$ are knights", the true fact is "$A$ or $B$ is a knave", by [[De Morgan's laws|09PKJKA6J0]], and not "both are knaves".

### History

Raymond Smullyan popularized the island of knights and knaves in his book What Is the Name of This Book? of 1978.
Smullyan was a mathematician and logician, and the puzzles of the book lead the reader from riddles to questions of logic.
The truth tables that solve such puzzles go back to the work of Wittgenstein and of Post in 1921.

### Try it

Puzzle 1: $A$ says "$B$ is a knight", and $B$ says "$A$ and I are of different types".
What are they?
Both are knaves.
If $B$ were a knight, $A$ would be a knave by the statement of $B$, and the true sentence "$B$ is a knight" would come from a knave, which is impossible.
With $B$ a knave, $A$ and $B$ are of the same type, so $A$ is a knave too, and both statements are false.

Puzzle 2: $A$ says "at least one of us is a knave".
What are $A$ and $B$?
$A$ is a knight and $B$ is a knave: a knave $A$ would make the statement true, so $A$ is a knight, and then $B$ must be the knave.

## Explanations

### L1 human

On the island, knights always tell the truth and knaves always lie.
Suppose an inhabitant says "I am a knight".
A knight would say this, because it is true, and a knave would also say it, because it is a lie.
So this sentence tells us nothing.
But if an inhabitant says "$2 + 2 = 5$", we know at once that this inhabitant is a knave.

### L2 human

Solve: $A$ says "$B$ is a knight", and $B$ says "$A$ and I are of different types".
The translation is $a \leftrightarrow b$ and $b \leftrightarrow (a \oplus b)$, where $\oplus$ is the exclusive or.
If $b$ is true, then $a \oplus b$ must be true, so $a$ is false, while $a \leftrightarrow b$ requires $a$ true, a contradiction.
If $b$ is false, then $a \oplus b$ must be false, so $a$ equals $b$ and is false, and $a \leftrightarrow b$ holds.
So both $A$ and $B$ are knaves, and this is the only solution.
The island is a place to practice translation and case analysis on small problems.
Watch out: translating "$A$ says $B$ is a knight" as $a \land b$ forgets that a knave's statement is false.

### L3 human

A knights and knaves puzzle is an instance of propositional satisfiability: the biconditionals form a formula, and the solutions are its satisfying valuations.
The rule $a \leftrightarrow S$ gives each speaker a truth function, and nested reports such as "$A$ says that $B$ says $S$" become nested biconditionals.
Since $\leftrightarrow$ is associative and $a \leftrightarrow a$ is a tautology, many puzzle questions reduce to the identity $a \leftrightarrow (a \leftrightarrow q) \equiv q$.
Variants of the island add other kinds of inhabitants, such as normals, and each kind adds its own rule of translation.
