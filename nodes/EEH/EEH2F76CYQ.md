---
tag: EEH2F76CYQ
kind: topic
name: Induction and well-ordering as proof methods
msc: ["00A35", "97E50"]
topics: [SGSVYFDSYK]
---

## Summary

Induction is how mathematics proves infinitely many statements with one finite argument, and this part of [[reasoning and proof|SGSVYFDSYK]] teaches it as a working tool.
It starts with ordinary induction: prove a base case, prove that each case gives the next, and every natural number is covered.
Strong induction lets the step use all earlier cases, and the well-ordering principle says that every nonempty set of natural numbers has a least element.
These three turn out to be one fact about the natural numbers, and a theorem makes that exact over a stated base theory.
From them grow the methods that you meet in every later course.
The minimal counterexample and infinite descent argue from a smallest case, and a strengthened hypothesis rescues a step that is stuck.
Double, forward-backward and structural induction change the order in which the cases are reached, and induction on size picks the right number to induct on.
The story ends with the false proof that all horses have the same color and with the errors that break induction proofs in practice.
The induction axiom of the Peano axioms and transfinite induction are treated in other parts of the library.

## Remarks

### Reading order

1. [[Mathematical induction|0ASJVEFA9J]]: the base case and the step, through the sum of the first $n$ odd numbers and $2^n > n^2$ for $n \ge 5$.
2. [[Strong induction|0KMVFSHFGZ]]: how to use every earlier case, and why every $n \ge 2$ has a prime factor.
3. [[Well-ordering principle|01BX15HSRR]]: how to take a least element, and why the integers and the rationals fail the test.
4. [[Equivalence of induction and well-ordering|J2P9FWBP3Q]]: why the three principles are one fact, and which base theory the claim needs.
5. [[Minimal counterexample|JGRCNPKNGG]]: how to argue from a smallest failure to a smaller one.
6. [[Infinite descent|0EFYCFHYFG]]: Fermat's method, where each solution gives a smaller one inside the natural numbers.
7. [[Strengthening the induction hypothesis|F94KJC2RXP]]: how proving more makes a stuck step work, as in the bound $2 - 1/n$ for the sum of $1/k^2$.
8. [[Double induction|AABX4YPKRR]]: how to run induction on two variables in a safe order.
9. [[Forward-backward induction|QC9FKGZH1V]]: Cauchy's proof of the AM-GM inequality, up through powers of $2$ and then down one at a time.
10. [[Structural induction|12MQ2NJ29A]]: how to prove facts about lists, trees and formulas by following their construction.
11. [[Inductive and recursive definitions|AM4GQQMZ3C]]: how a base and rules define a sequence or the least set closed under the rules.
12. [[Induction on size|B2D8PTFNN1]]: how to choose the parameter for graphs, sets and polynomials, and why you break down instead of building up.
13. [[All horses are the same color|AJ2FDJJGTH]]: a false proof whose step fails from $1$ to $2$, and how to find such a gap.
14. [[Tiling a deficient board with L-trominoes|EXRJ0JF2Q3]]: a picture proof by induction that works wherever the missing square is.
15. [[Errors in induction proofs|V52HDTMPV5]]: the common errors, each with a small case where it fails.

### Prerequisites

1. [[Basic proof methods|958EF46EYJ]] and the general topic of [[proof methods|G9JFJGY4TQ]], for direct proof and proof by contradiction.
2. The [[language of statements|WMY13MXY3W]], for quantifiers and implications.
3. The notion of a [[mathematical proof|0B94TKFQJX]].
4. The [[natural numbers|0MWKJ44V5A]] with their order; the [[Peano axioms|0QFT7Z76N5]] are needed only for the equivalence theorem.
