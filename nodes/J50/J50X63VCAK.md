---
tag: J50X63VCAK
kind: example
name: The four steps give no plan for the Collatz problem
msc: ["00A35", "11B83"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: DYD57G2Y5Z
    note: every question of the four steps can be asked about the Collatz problem, but none of them yields a plan that works; the problem is still open
uses: [DYD57G2Y5Z, 6PCQEXEX4N]
sources:
  - url: https://en.wikipedia.org/wiki/Collatz_conjecture
    locator: lead section
---

## Example

Let $T(n) = n/2$ for even $n$ and $T(n) = 3n + 1$ for odd $n$.
The [[Collatz conjecture|6PCQEXEX4N]] says that for every positive integer $n$, repeated use of $T$ reaches $1$.
We follow [[Pólya's four steps|DYD57G2Y5Z]] and watch where they stop.

1. Phase 1 works: the hypothesis is "$n$ is a positive integer", the conclusion is "$T^k(n) = 1$ for some $k \ge 0$", and the statement is precise.
2. We specialize.
   From $6$ we get $6, 3, 10, 5, 16, 8, 4, 2, 1$, which is $8$ steps, and from $7$ we need $16$ steps.
3. We specialize further.
   From $27$ the sequence takes $111$ steps and rises to $9232$ before it falls to $1$, and the cases show no pattern that a proof could follow.
4. We look at a related problem, the map with $3n - 1$ in place of $3n + 1$.
   There the start $5$ gives $5, 14, 7, 20, 10, 5$, a cycle that never reaches $1$, so any proof must use the exact number $+1$.
5. We generalize.
   John Conway showed in 1972 that for a general class of maps of this kind, the question of where the orbits go is undecidable, so the most general version is out of reach.
6. We try a weaker auxiliary problem, "almost every orbit gets small", which has partial answers that do not give the full statement.

Each question of phase 2 was asked, and each answer told us something.
None of them gave a plan for a proof, and the conjecture is still open.
So the four steps organized the search, and the search still failed.

## Remarks

The non-example shows the limit of a [[heuristic|6KCEWEP4WA]] plan.
The four steps say what to ask, not what the answer is, and for an open problem the questions may have no useful answer.
That is why heuristics must not be presented as algorithms.

The search still produced something useful.
The false variant in step 4 is a warning: an argument that does not use the difference between $3n + 1$ and $3n - 1$ cannot prove the conjecture.

## Explanations

### L1 human

Take a number, halve it if it is even, and triple it and add one if it is odd.
Repeat, and the numbers always seem to come down to $1$.
From $27$ they first climb to $9232$, and they need $111$ steps.
Nobody has proved that every starting number comes down to $1$.
Good habits for solving problems help us explore the question, but they have not solved it.

### L2 human

We check the claim about the start $7$ by hand:
$$7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.$$
There are $16$ steps after the start, and the largest value is $52$, more than seven times the start.
Growth like this before the fall is common, so the first few steps give no simple bound on the values.
The four steps produced data, related problems and warnings, which is how research starts.
Watch out: many checked cases do not make the statement true, because checking cases is part of phase 4, not a proof.
