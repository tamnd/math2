---
tag: 417PHKB4VC
kind: example
name: Boolean Pythagorean triples problem
aliases: [boolean-pythagorean-triples]
msc: ["05D10", "68V05"]
topics: [1BTHSHST4M]
audience: research
instance_of: [MC18C7BMFT]
uses: [MC18C7BMFT, 0M7ARED5Q7, QN7M1JCGT9, G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_Pythagorean_triples_problem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Boolean_Pythagorean_triples_problem
    locator: Solution
  - url: https://en.wikipedia.org/wiki/Boolean_Pythagorean_triples_problem
    locator: Prize
---

## Example

A [[Pythagorean triple|0M7ARED5Q7]] is a triple $(a, b, c)$ of positive integers with $a^2 + b^2 = c^2$.
The Boolean Pythagorean triples problem asks whether the positive integers can be colored red and blue so that no Pythagorean triple has all three numbers in one color.
In May 2016 Marijn Heule, Oliver Kullmann and Victor Marek answered it.
The set $\{1, \dots, 7824\}$ has such a coloring, and the set $\{1, \dots, 7825\}$ has none, so the answer for all positive integers is no.
We check that their proof is a [[computer-assisted proof|MC18C7BMFT]].

1. The reduction to logic. For each integer $i$ in $\{1, \dots, n\}$ we take a variable $x_i$, true when $i$ is red and false when $i$ is blue.
2. For each Pythagorean triple $(a, b, c)$ with $c \le n$ we write two clauses. The clause $x_a \lor x_b \lor x_c$ says "not all three are blue", and the clause $\lnot x_a \lor \lnot x_b \lor \lnot x_c$ says "not all three are red".
3. A coloring of $\{1, \dots, n\}$ with no one-colored triple is the same thing as an assignment of truth values that makes every clause true. So the problem for a fixed $n$ is an instance of [[satisfiability|QN7M1JCGT9]].
4. A small instance. For $n = 13$ the Pythagorean triples are $(3, 4, 5)$, $(6, 8, 10)$ and $(5, 12, 13)$, so there are $6$ clauses in the $8$ variables $x_3, x_4, x_5, x_6, x_8, x_{10}, x_{12}, x_{13}$.
5. Color $5$ and $10$ blue and all other numbers red. Each triple then has exactly one blue number, namely $5$, $10$ and $5$, so no triple is one-colored and all $6$ clauses are true.
6. The clauses also force colors. If $3$ and $4$ are red, the clause $\lnot x_3 \lor \lnot x_4 \lor \lnot x_5$ forces $5$ to be blue. If in addition $12$ is blue, the clause $x_5 \lor x_{12} \lor x_{13}$ forces $13$ to be red.
7. The case $n = 7824$. A SAT solver found a satisfying assignment, and a short program can test that coloring against every triple, so this half of the result is easy to verify.
8. The case $n = 7825$. There are $2^{7825} \approx 3.63 \cdot 10^{2355}$ colorings, and the proof must exclude all of them. The authors used the cube-and-conquer method: one solver split the problem into many subproblems, and other solvers settled the subproblems in parallel.
9. The search ran for about two days on the Stampede supercomputer, about $4$ years of time on a single processor. The solvers wrote a proof of unsatisfiability in the DRAT format, about $200$ terabytes in size, and a separate checking program verified it.
10. Steps 1 to 3 are a written reduction, and step 8 is a computation that no person could repeat, so the proof is computer-assisted.

## Remarks

The example is the extreme form of a computer-assisted proof: the written part is short and the computer part is enormous.
Trust in the result does not rest on the solvers, which are large and complex programs.
It rests on the proof file and on the checking program, which is small and was written to check exactly this kind of file.
The authors also published a compressed certificate of $68$ gigabytes, from which a reader can rebuild the proof file and check it again.

The paper of Heule, Kullmann and Marek won the best paper award at the SAT 2016 conference.
Ronald Graham had offered a prize of $100$ dollars for the problem in the 1980s, and he paid it to Heule.
The question belongs to [[Ramsey theory|G5TWXV565S]], which asks when a structure must appear inside one color class.
The same question with three or more colors was still open as of 2018.

What happens when $n$ changes?
The answer switches exactly once.
For $n \le 7824$ a coloring exists, because a good coloring of $\{1, \dots, 7824\}$ restricts to a good coloring of every smaller set.
For $n \ge 7825$ none exists, because a good coloring of a larger set would restrict to one of $\{1, \dots, 7825\}$.

## Explanations

### L1 human

Take the numbers $1, 2, 3$ and so on, and paint each one red or blue.
The rule is that no three numbers $a$, $b$, $c$ with $a^2 + b^2 = c^2$, such as $3$, $4$ and $5$, may all get the same color.
For a long time nobody knew how far you can go.
In 2016 three computer scientists showed that you can paint the numbers up to $7824$, but not up to $7825$.
For the second part a computer had to rule out every possible painting, and it wrote a record of its work of about $200$ terabytes.
A separate small program then checked that record, so we do not need to trust the large program that did the search.

### L2 human

We extend the coloring of step 5 to $n = 15$, which adds the triple $(9, 12, 15)$.
The triples with $c \le 15$ are now
$$(3, 4, 5), \quad (6, 8, 10), \quad (5, 12, 13), \quad (9, 12, 15).$$
In the coloring of step 5, the numbers $9$, $12$ and $15$ are all red, so the clause $\lnot x_9 \lor \lnot x_{12} \lor \lnot x_{15}$ is false.
We repair the coloring by making $15$ blue as well.
The first three triples do not contain $15$, so they stay good, and $(9, 12, 15)$ now has two red numbers and one blue one.
So all $8$ clauses for $n = 15$ are true.

The typical use of this encoding is any problem that asks for a coloring or an assignment that avoids forbidden patterns.
Watch out for the answer "unsatisfiable" taken as a proof by itself.
It becomes a proof only when the solver also writes a certificate that an independent checker verifies.
