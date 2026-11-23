---
tag: 6KCEWEP4WA
kind: concept
name: Heuristics in mathematics
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
uses: [0B94TKFQJX, 5V35SGEN1T]
sources:
  - url: https://en.wikipedia.org/wiki/Heuristic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

A heuristic is a rule of thumb for finding a solution or a proof, such as "try a special case" or "work backwards".
It often leads to an idea, it never guarantees one, and what it finds must still be proved.

Here is a small discovery that shows how heuristics work.
We want a formula for the sum
$$S_n = \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \dots + \frac{1}{n(n+1)}.$$
A first attempt is to put the fractions over a common denominator, but the denominators grow fast and no pattern appears.
So we try small cases instead:
$$S_1 = \frac{1}{2}, \qquad S_2 = \frac{1}{2} + \frac{1}{6} = \frac{2}{3}, \qquad S_3 = \frac{2}{3} + \frac{1}{12} = \frac{3}{4}.$$
The values suggest $S_n = \frac{n}{n+1}$, that is, $1 - S_n = \frac{1}{n+1}$.
A difference of two simple fractions suggests that each term is itself a difference, and indeed
$$\frac{1}{k} - \frac{1}{k+1} = \frac{(k+1) - k}{k(k+1)} = \frac{1}{k(k+1)}.$$
Now the sum telescopes to $1 - \frac{1}{n+1} = \frac{n}{n+1}$, and that line is the proof.
The special cases found the answer and the idea, and only the last computation made the answer certain.

Heuristic reasoning is the provisional reasoning that heuristics produce: a guess, a plan or a partial argument that still needs a [[mathematical proof|0B94TKFQJX]].
A heuristic differs from an algorithm, which always ends with a correct answer, and from a proof, which shows that a statement is true.

## Motivation

A finished proof shows that a theorem is true, but it seldom shows how anyone found it.
A student who reads only finished proofs learns to check arguments, not to make them.
No algorithm finds proofs of all true statements, so the question "how was this found?" has no complete answer.
Still, experienced solvers use the same moves again and again: they look at examples, solve easier problems first, compare the problem with problems they know, and draw figures.

George Pólya collected such moves in *How to Solve It* (1945) and called their study "heuristic", after the Greek verb for "to find".
His aim was to make the moves explicit, so that they can be taught and practiced.
The pages on single heuristics take the moves one by one, from [[specialization|FTBJX4G51S]] to [[working backwards|3QTB9S1THS]], and each one shows a problem that the move solves and a case where it misleads.

## Notation

Pólya uses "heuristic" for the study of the methods of discovery and "heuristic reasoning" for reasoning that is provisional and only plausible.
He also uses "plausible" in a narrow sense, for reasoning that makes a conjecture more credible without proving it; [[plausible reasoning and experimental mathematics|DME0TPC348]] treats that sense.
In computer science and operations research, a heuristic is a fast procedure with no guarantee of an optimal or correct answer, as in [[heuristics and metaheuristics|FQBS45218T]].
Both meanings share the idea "useful but not guaranteed", and here we use the first one.

## Remarks

### Two discoveries worked through

Small cases of the sum of cubes $1^3 + 2^3 + \dots + n^3$ give $1, 9, 36, 100, 225$.
Each value is a square, and the square roots $1, 3, 6, 10, 15$ are the sums $1 + 2 + \dots + n$.
So we guess
$$1^3 + 2^3 + \dots + n^3 = \left( \frac{n(n+1)}{2} \right)^2,$$
test it on $n = 6$, where both sides are $441$, and then prove it by [[induction|0ASJVEFA9J]].
The full story is in [[the sum of the first n cubes found by heuristics|XY7YK4Q3ZZ]].

A second discovery is an estimate.
Since $2^{10} = 1024$ is close to $10^3$, we expect $2^{100}$ to be close to $10^{30}$.
The rounding cannot say which number is larger, but the exact fact $1024 > 1000$ can, and it gives $2^{100} > 10^{30}$.
[[An estimate of 2 to the 100 by rounding|3FG69KFES0]] works out the ratio, about $1.27$.

### The family of heuristics

Most heuristics change the problem.
[[Specialization|FTBJX4G51S]] makes it smaller, [[generalization|8NJ0VN9Z97]] makes it larger, an [[auxiliary problem|DYSJB93V11]] replaces it, and [[variation of the problem|KT5SASGTQ5]] changes its data or its conditions.
Other heuristics change the representation: a [[figure and good notation|6CVYB413ER]], or an [[auxiliary element|8TKKRAXKFN]] such as an extra line.
[[Working backwards|3QTB9S1THS]] changes the order of the work, and [[analogy|7KDT0R1HF2]] borrows a method from a similar problem.
[[Pólya's four steps|DYD57G2Y5Z]] arrange all of them into a plan for a whole solution, and Lakatos's [[proofs and refutations|79P9CTRN0V]] is a heuristic for the growth of a whole theorem.

Several heuristics often work together.
In the telescoping sum above, special cases suggested the answer, and the form of the answer suggested the identity that proves it.

### Heuristics, algorithms and evidence

A heuristic leaves choices to the solver, and it may lead nowhere.
The [[Euclidean algorithm|ZQB1DQR9QS]] is the opposite: it computes $\gcd(1071, 462) = 21$ in three divisions with no choice at any step, and it is correct for every pair of inputs.
So it is an algorithm, not a heuristic.

A table of data is not a heuristic either, although a heuristic may produce it.
The values of $n^2 + n + 41$ for $n = 0, 1, \dots, 39$ are all prime, and they suggest that every value is prime.
The guess fails at $n = 40$:
$$40^2 + 40 + 41 = 1681 = 41^2.$$
Evidence makes a [[conjecture|WMEMMHZ3BH]] plausible, and only a proof or a [[counterexample|0ED72CTBNP]] settles it.

Heuristics also differ from [[proof methods|G9JFJGY4TQ]].
A proof method fixes the logical form of the final argument, such as induction or contradiction, and a heuristic helps to find what goes into it.

### When heuristics help and when they mislead

Heuristics help most when you are stuck at the start: they give you something to do, such as computing a case or drawing a figure.
They mislead when you take their output for a result.
The same advice can solve one problem and fail on the next, because it is advice and not an algorithm.
For this reason, each page on a single heuristic shows a failure next to a success.

### Watch out

The first error is to treat a pattern as a proof.
"The formula holds for $n \le 5$" is a reason to look for a proof, and the polynomial $n^2 + n + 41$ shows how a pattern can hold for forty cases and then fail.

The second error is to treat a list of heuristics as a recipe.
A list gives questions to ask, and you must still choose which one fits, adapt it, and decide when to drop it and try another.

### History

Pappus of Alexandria described the method of analysis and synthesis in Book 7 of his *Collection*, and Descartes and Leibniz both planned a general art of discovery.
Pólya revived the subject for mathematics with *How to Solve It* (1945), *Mathematics and Plausible Reasoning* (1954) and *Mathematical Discovery* (two volumes, 1962 and 1965).
Imre Lakatos analyzed how proofs and counterexamples shape a theorem in *Proofs and Refutations*, first as articles in 1963 to 1964 and as a book in 1976.
Alan Schoenfeld's *Mathematical Problem Solving* (1985) studied how students and experts use heuristics, and argued that knowing the names of heuristics is not enough to use them well.

### Try it

Find a formula for $1 + 3 + 3^2 + \dots + 3^{n-1}$ from small cases.
The values $1, 4, 13, 40$ are each about half of the next power of $3$, which suggests $\frac{3^n - 1}{2}$; multiply the sum by $3$ and subtract it to prove this.

Is $n^2 - n + 41$ prime for every natural number $n$?
It is prime for $n = 1, \dots, 40$, but at $n = 41$ it equals $41^2$, so the answer is no.

## Explanations

### L1 human

A heuristic is a good habit for finding answers, such as "try a small case first" or "draw a picture".
It often helps, but it can fail.
For example, to add $1 + 2 + \dots + 100$, look at a small case first: $1 + 2 + 3 + 4$ pairs as $(1 + 4) + (2 + 3) = 5 + 5$.
The same pairing for $1$ to $100$ gives $50$ pairs that each add to $101$, so the sum is $5050$.
The habit "try a small case" found the idea of pairing, and the pairing argument shows that the answer is right.

### L2 human

How many subsets does a set with $n$ elements have?
A first attempt is to count the subsets of each size and add, but that needs binomial coefficients that we may not know yet.
So we specialize, and list the subsets of small sets:
$$\{\}: 1, \qquad \{a\}: 2, \qquad \{a, b\}: 4, \qquad \{a, b, c\}: 8.$$
The values $1, 2, 4, 8$ suggest $2^n$, and the doubling from one line to the next suggests the reason.
Each subset of $\{a, b, c\}$ either leaves out $c$, and then it is a subset of $\{a, b\}$, or it contains $c$, and then it is a subset of $\{a, b\}$ with $c$ added.
So adding one element doubles the count, and by induction a set with $n$ elements has $2^n$ subsets.
The pattern alone proved nothing, since many sequences start $1, 2, 4, 8$; the doubling argument that we read off a small case is the proof.

### L3 human

Heuristics belong to the [[methodology of mathematics|3FJ3XMV9KD]], which studies how results are found.
The set of theorems of a rich enough formal theory is not decidable, so no algorithm finds all proofs, and some form of guided search is unavoidable for humans and for machines.
Automated provers and proof assistants use heuristics in Pólya's sense: they order a search without changing what counts as a proof.
Schoenfeld's analysis adds that heuristics are one resource of a solver among several, beside knowledge, control over the solving process, and beliefs about mathematics.
Later pages treat [[mathematical intuition|4BT08RE4CR]] and the [[psychology of mathematical invention|XMGGTNSTYC]], and [[plausible reasoning and experimental mathematics|DME0TPC348]] continues with the weighing of evidence for conjectures.
