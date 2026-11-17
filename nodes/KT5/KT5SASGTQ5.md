---
tag: KT5SASGTQ5
kind: concept
name: Variation of the problem
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 0RVYE75E2M]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

Variation of the problem is a [[heuristic|6KCEWEP4WA]]: when a problem resists, change it into a related problem and use what the new problem teaches.
The change can affect the unknown, the data, or the condition: drop a part of the condition, add a condition, change a number, or exchange hypothesis and conclusion to form the [[converse|0RVYE75E2M]].
Specialization, generalization and analogy are special kinds of variation.
The varied problem is a step, not the goal: its solution must be carried back to the original problem.
The heuristic does not guarantee success, and a variation can be harder than the original or unrelated to it.

## Motivation

A problem that is stuck stays stuck if we keep looking at it in the same form.
A small change can make a known method fit, or reveal how the unknown depends on the data.
If one condition is dropped, the unknown is no longer fixed, and we can watch how it varies.
The family of solutions of the weaker problem is often simple, and the dropped condition then picks the answer from the family.
Variation keeps the mind moving, and it produces a supply of related problems, some of which are solvable.

## Remarks

### The steps

1. State the problem: the unknown, the data and the condition.
2. Change one element. Ask: can the unknown be changed, so that it is nearer to the data? Can the data be changed? Can a part of the condition be dropped?
3. Solve the new problem, or study how its solutions behave.
4. Carry the result back: restore the dropped condition, return to the original data, or use the new result as a step.
5. Check that the solution meets the original problem, since the variation may have changed the answer.

### When it applies

- The condition has several parts, and all parts together are hard to meet, but some of them are easy.
- The unknown is far from the data, and an intermediate unknown would link them.
- A theorem has been proved, and its converse, its generalization or a weaker hypothesis gives a natural new question.
- No plan has come from the problem as stated, and a fresh form is needed.

### Examples

1. [[Inscribing a square in a triangle by dropping one condition|5C38AKJ4N1]]: without the condition on the fourth vertex, the squares form a family related by a [[homothety|0ZG1PNEP35]], and the fourth vertex runs along a ray.
2. [[The least number that leaves remainder 1 on division by 2 to 6 and is divisible by 7|57YGZR5YNR]]: without divisibility by $7$, the solutions are $60k + 1$, and restoring the condition gives $301$.
3. Changing the unknown: to find the diagonal of a box with edges $a$, $b$, $c$, first find the diagonal of the face with edges $a$ and $b$, which is $\sqrt{a^2 + b^2}$. The space diagonal is then the hypotenuse of a right triangle with legs $\sqrt{a^2 + b^2}$ and $c$, so it is $\sqrt{a^2 + b^2 + c^2}$. The page [[the diagonal of a rectangular box by the four steps|FGMDA7TF3Q]] gives the details.
4. Forming the converse: the [[Pythagorean theorem|0VP3A1290K]] says that a right angle at $C$ gives $a^2 + b^2 = c^2$. The converse, that $a^2 + b^2 = c^2$ gives a right angle at $C$, is also true, and Euclid proved it as Book I, Proposition 48.
5. Changing a number in the condition: $a^2 + b^2 = c^2$ has infinitely many solutions in positive integers, but the variation $a^3 + b^3 = c^3$ has none, by the case $n = 3$ of [[Fermat's Last Theorem|0Y5X3SDBCZ]].

### Non-examples

1. [[Taking the converse of Fermat's little theorem as true|ZHMHBFQ2E4]]: the converse is a good question, but it is false, since $2^{340} \equiv 1 \pmod{341}$ and $341 = 11 \cdot 31$.
2. Replacing "find all real solutions of $x^3 = x$" by "find a solution" and reporting $x = 0$. The variation drops the word "all", and its answer is not carried back to the original problem, whose solutions are $-1$, $0$ and $1$.
3. Changing a problem so much that it no longer shares data or unknown with the original. The new problem may be solved, but nothing returns to the original.

### Basic properties

1. Dropping a condition gives a weaker problem, whose solutions include those of the original. Adding a condition gives a stronger problem, whose solutions are among those of the original.
2. A solution of a stronger problem solves the original. A solution of a weaker problem solves the original only after the dropped condition is checked.
3. The converse of a true statement is a new statement. It can be true, as for the Pythagorean theorem, or false, as for Fermat's little theorem.
4. The [[contrapositive|04T1CT7212]] is not a variation in this sense: it is equivalent to the original statement.
5. Variation is a heuristic: it suggests new problems, but it does not say which variation will help.

### Related methods

- [[Specialization|FTBJX4G51S]]: pass to a special case, a variation that adds conditions.
- [[Generalization as a heuristic|8NJ0VN9Z97]]: pass to a more general problem, a variation that removes conditions or replaces numbers by letters.
- [[Analogy|7KDT0R1HF2]]: pass to a similar problem in another setting.
- [[Auxiliary problem|DYSJB93V11]]: the varied problem, when it is used as a step, is an auxiliary problem.
- [[Problem posing|Y896GWYF8A]]: the same changes, made to ask new questions; Brown and Walter's "what if not" strategy changes each attribute of a problem in turn.

### History

George Pólya made "variation of the problem" an entry of the heuristic dictionary in How to Solve It (1945).
The list of questions in that book asks: "Could you restate the problem?"
It advises: "Keep only a part of the condition, drop the other part."
It also asks: "Could you change the unknown or the data, or both if necessary, so that the new unknown and the new data are nearer to each other?"
Euclid already proved converses as separate propositions, as with Book I, Propositions 47 and 48 on the Pythagorean theorem.
Stephen Brown and Marion Walter turned systematic variation into a method for posing new problems in The Art of Problem Posing.

### Common errors

1. Forgetting to return to the original problem, and reporting the answer of the variation.
2. Taking a converse or a generalization as true because it holds in a few cases.
3. Dropping a condition and not checking, at the end, that the chosen solution meets it.
4. Varying several elements at once, so that it is unclear which change made the new problem easier.

## Explanations

### L1 human

When a puzzle is too hard, we can change it a little and try again.
We might ignore one of its rules for a moment, or try smaller numbers, or ask the question backwards.
The changed puzzle is often easier, and solving it shows how the real puzzle works.
Then we put the ignored rule back, or return to the real numbers.
The answer to the changed puzzle is only a step: we must still answer the puzzle we were given.

### L2 human

We solve a problem by dropping a condition and studying the resulting family.
Problem: find a point $X$ on a given line $\ell$ at distance $5$ from $O = (0, 0)$ and at distance $5$ from $A = (8, 0)$, where $\ell$ is the line $y = 3$.

1. Drop the condition "$X$ on $\ell$". The points at distance $5$ from both $O$ and $A$ are the intersections of two circles of radius $5$.
2. Both circles have radius $5$, so these points lie on the perpendicular bisector $x = 4$ of $OA$. Then $16 + y^2 = 25$, so $y = \pm 3$, and the points are $(4, 3)$ and $(4, -3)$.
3. Restore the dropped condition: $X$ must lie on $y = 3$. Only $(4, 3)$ does.
4. Check: the distances from $(4, 3)$ to $O$ and to $A$ are $\sqrt{16 + 9} = 5$.

The typical use: the conditions are loci, each dropped condition leaves a simpler locus, and the answer is an intersection.

A trap: the weaker problem can have solutions when the original has none; if $\ell$ were the line $y = 4$, step 2 would be unchanged, and step 3 would show that no point works.

### L3 human

Systematic variation is standard in research.
A theorem is tested by weakening each hypothesis in turn and looking for a counterexample, which shows which hypotheses are needed.
The converse questions of a field are a source of problems, as in inverse problems, where the data are recovered from a solution.
Deformation theory studies a problem as a member of a family and asks how its solutions change as a parameter varies.
Homotopy continuation in numerical algebraic geometry solves a system of polynomial equations by deforming an easy system into the given one and following the solutions along the path.
These are precise forms of Pólya's advice to drop part of the condition and watch how the unknown varies.
