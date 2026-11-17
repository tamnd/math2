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
The Boolean Pythagorean triples problem asks whether the positive integers can be coloured red and blue so that no Pythagorean triple has all three numbers of one colour.
Marijn Heule, Oliver Kullmann and Victor Marek answered it in May 2016: such a colouring of $\{1, \dots, n\}$ exists for $n = 7824$ and does not exist for $n = 7825$.
So the answer for all positive integers is no.
We check that their proof is a [[computer-assisted proof|MC18C7BMFT]].

1. The reduction to logic. For each integer $i$ in $\{1, \dots, n\}$ we take a variable $x_i$, with $x_i$ true when $i$ is red and false when $i$ is blue.
2. For each Pythagorean triple $(a, b, c)$ with $c \le n$ we write two clauses. The clause $x_a \lor x_b \lor x_c$ says "not all three are blue", and the clause $\lnot x_a \lor \lnot x_b \lor \lnot x_c$ says "not all three are red".
3. A colouring of $\{1, \dots, n\}$ without a one-coloured triple is the same thing as an assignment of truth values that makes all clauses true. So the problem for a fixed $n$ is an instance of [[satisfiability|QN7M1JCGT9]].
4. A small instance. For $n = 13$ the Pythagorean triples are $(3, 4, 5)$, $(6, 8, 10)$ and $(5, 12, 13)$, so there are $6$ clauses on the $8$ variables $x_3, x_4, x_5, x_6, x_8, x_{10}, x_{12}, x_{13}$.
5. We colour $5$ and $10$ blue and all other numbers red. Each of the three triples then contains exactly one blue number, namely $5$, $10$ and $5$. So no triple has one colour, and all $6$ clauses are true.
6. The clauses also force colours. If $3$ and $4$ are red, then $5$ must be blue, by the clause $\lnot x_3 \lor \lnot x_4 \lor \lnot x_5$. If in addition $12$ is blue, then $13$ must be red, by the clause $x_5 \lor x_{12} \lor x_{13}$.
7. The case $n = 7824$. A SAT solver found a satisfying assignment. A short program can check the colouring against each triple, so this half of the result is easy to verify.
8. The case $n = 7825$. There are $2^{7825} \approx 3.63 \cdot 10^{2355}$ colourings, and the proof must exclude each of them. The authors used the cube-and-conquer method: a first solver split the problem into about a trillion subproblems, and other solvers solved the subproblems.
9. The computation used about two days on the Stampede supercomputer, about $4$ years of time on one processor. The solvers wrote a proof of unsatisfiability in the DRAT format, of about $200$ terabytes, and a checking program verified it.
10. The condition of a computer-assisted proof holds: steps 1 to 3 are a written reduction, and step 8 is a computation that no person could repeat.

## Remarks

The example shows the most extreme form of a computer-assisted proof: the human part is short and the computer part is enormous.
The trust in the result does not rest on the solvers, which are large and complex programs.
It rests on the proof file and on the checking program, which is small and was written to check exactly this kind of file.
The authors also published a compressed certificate of $68$ gigabytes, from which a reader can rebuild the proof file and check it again.

The paper of Heule, Kullmann and Marek won the best paper award at the SAT 2016 conference.
Ronald Graham had offered a prize of $100$ dollars for the problem in the 1980s, and he awarded it to Heule.
The question belongs to [[Ramsey theory|G5TWXV565S]], which studies when a structure must appear in one colour class.
The same question with three or more colours was still open as of 2018.

When the parameter $n$ changes, the answer changes once.
For $n \le 7824$ a colouring exists, because a colouring of $\{1, \dots, 7824\}$ restricts to each smaller set.
For $n \ge 7825$ no colouring exists, because a colouring of a larger set would restrict to $\{1, \dots, 7825\}$.

## Explanations

### L1 human

Take the numbers $1, 2, 3$ and so on, and paint each one red or blue.
The rule is that no three numbers $a$, $b$, $c$ with $a^2 + b^2 = c^2$, such as $3$, $4$, $5$, may all get the same colour.
For a long time nobody knew how far one can go.
In 2016 three computer scientists showed that one can paint the numbers up to $7824$, but not up to $7825$.
For the second part a computer had to rule out every possible painting, and it wrote a record of its work of about $200$ terabytes.
A separate small program then checked that record, so we do not need to trust the large program that did the search.

### L2 human

We check the colouring of step 5 for $n = 15$, which adds the triple $(9, 12, 15)$.

1. The triples with $c \le 15$ are $(3, 4, 5)$, $(6, 8, 10)$, $(5, 12, 13)$ and $(9, 12, 15)$.
2. In the colouring of step 5, the numbers $9$, $12$ and $15$ are all red. So the clause $\lnot x_9 \lor \lnot x_{12} \lor \lnot x_{15}$ is false.
3. We repair the colouring: we colour $15$ blue as well. The first three triples do not contain $15$, so they stay good.
4. The triple $(9, 12, 15)$ now has two red numbers and one blue number. So all $8$ clauses for $n = 15$ are true.

The typical use of this encoding is any problem that asks for a colouring or an assignment with forbidden patterns.
A trap is to think that a solver's answer "unsatisfiable" is a proof by itself.
It becomes a proof only when the solver also writes a certificate that an independent checker verifies.
