---
tag: DYD57G2Y5Z
kind: concept
name: Pólya's four steps
msc: ["00A35", "97E50"]
topics: [X1NSTVGDNQ]
audience: school
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Four phases
  - book: isbn:9780691164076
---

## Summary

Pólya's four steps are a plan for solving a mathematical problem in four phases: understand the problem, devise a plan, carry out the plan, and look back.
In the first phase the solver names the unknown, the data and the condition, or, for a statement to prove, the hypothesis and the conclusion.
In the second phase the solver looks for a connection between the data and the unknown, often through a related problem that is already solved.
In the third phase the solver carries out the plan and checks each step.
In the fourth phase the solver checks the result, looks for another way to reach it, and asks where else the result or the method can be used.
For each phase George Pólya gave a list of questions, and the list is the best known collection of [[heuristics|6KCEWEP4WA]] for school and university mathematics.

## Motivation

Many students start to calculate before they know what the problem asks.
Others stop as soon as they have a number, without a check.
Both habits waste work: the first gives answers to the wrong question, and the second leaves errors in place.
Pólya observed that a good teacher asks the same few questions again and again: what is the unknown, do you know a related problem, can you check the result.
He wrote these questions down in a fixed order, so that a student can ask them without the teacher.
The four phases make the order explicit, and the questions give a start when the solver has no idea.

## Remarks

### The steps

1. Understand the problem. Name the unknown, the data and the condition. Draw a figure and introduce notation. Ask whether the condition is enough to determine the unknown, too little, or contradictory.
2. Devise a plan. Look for a problem with the same unknown that is already solved. Try a special case, a more general problem, an auxiliary problem, or a part of the condition. Check that the plan uses all the data.
3. Carry out the plan. Do each step of the plan, and check that each step is correct. A step that cannot be justified sends the solver back to phase 2.
4. Look back. Check the result by a special case, by the units, or by a second method. Check the argument. Ask whether the result or the method solves another problem.

For a problem to prove, phase 1 names the hypothesis and the conclusion instead of the data and the unknown, and the other phases are the same.

### When it applies

The four steps apply to every problem that is a real problem for the solver, that is, a problem whose method the solver does not know in advance.
For a routine exercise, phases 1 and 2 take a moment, and phase 4 is the part that still pays.
For a research problem, phase 2 can take years, and the questions of phase 2 are only a start.

### Examples

1. [[The diagonal of a rectangular box by the four steps|FGMDA7TF3Q]]: Pólya's own first example; the related problem is the diagonal of a rectangle.
2. [[Counting the squares on a chessboard by the four steps|H817ES7NHH]]: phase 1 finds that squares of every size count, and phase 4 gives the formula for an $n \times n$ board.
3. A speed problem: a car travels $60$ km at $40$ km/h and returns at $60$ km/h. Phase 1 names the unknown as the average speed, total distance over total time; the answer is $\frac{120}{1.5 + 1} = 48$ km/h, not the mean $50$ of the two speeds.
4. A proof problem: to prove that the [[sum of the first n odd numbers|9PESCNHE7Q]] is $n^2$, phase 1 names the hypothesis and conclusion, phase 2 chooses induction, and phase 4 finds a picture proof with squares.

### Non-examples

1. [[The four steps give no plan for the Collatz problem|J50X63VCAK]]: every question of phase 2 can be asked, and none of them has led to a proof.
2. A solution that skips phase 1. In example 3, the answer $50$ km/h comes from averaging the two speeds without asking what the unknown is.
3. A list of formulas to try in turn. That is a search through known methods, and it has no phase 1 and no phase 4.

### Basic properties

1. The four phases are not a strict order. A failed phase 3 sends the solver back to phase 2 or to phase 1.
2. The phases are a [[heuristic|6KCEWEP4WA]] plan, not an algorithm. They organize the search, but they do not produce the idea.
3. Phase 2 contains most of the single heuristics of this topic: [[analogy|7KDT0R1HF2]], [[specialization|FTBJX4G51S]], [[generalization|8NJ0VN9Z97]], [[working backwards|3QTB9S1THS]], [[auxiliary problems|DYSJB93V11]] and the [[variation of the problem|KT5SASGTQ5]].
4. Phase 4 is the source of new problems, as the page [[problem posing|Y896GWYF8A]] explains.

### Related methods

The [[forward-backward method|V8ZB838JY5]] is a plan for phase 2 and phase 3 of a problem to prove.
Schoenfeld's framework adds control: the decision when to stop one plan and to start another.
Mason, Burton and Stacey describe three phases: entry, attack and review.
Entry matches phase 1, attack matches phases 2 and 3, and review matches phase 4.

### History

George Pólya published *How to Solve It* in 1945, with Princeton University Press, from his experience of teaching at ETH Zurich and at Stanford.
The book has a short part on the four phases, a dialogue of a teacher and a class, and a "short dictionary of heuristic" with entries on single heuristics.
A second edition appeared in 1957.
Pólya developed the ideas further in *Mathematics and Plausible Reasoning* (1954) and *Mathematical Discovery* (1962 and 1965).

### Common errors

1. To read the four steps as a recipe. They do not tell what the plan is; they tell what to ask.
2. To skip phase 4 because the answer "looks right". A check by a special case takes a minute and finds many errors.
3. To spend all the time in phase 3 with a bad plan. When a plan fails twice, the solver should return to phase 2.

## Explanations

### L1 human

Pólya's four steps are four questions for any problem.
First: what does the problem ask, and what do we know?
Second: how can we get from what we know to what we want?
Third: do it, carefully.
Fourth: is the answer right, and what did we learn?
For example, to find how many handshakes there are when $5$ people each shake hands once with each other person, we first see that we want the number of pairs.
Each person shakes $4$ hands, which gives $5 \cdot 4 = 20$, but each handshake is counted twice, so the answer is $10$.
To check, we list the pairs for $3$ people: there are $3$, and the rule gives $\frac{3 \cdot 2}{2} = 3$.

### L2 human

We solve a problem with the four steps: find two positive integers whose sum is $20$ and whose product is $96$.

1. Understand. The unknowns are two integers $x$ and $y$. The data are $20$ and $96$. The condition is $x + y = 20$ and $xy = 96$.
2. Plan. A related problem: the roots of $t^2 - st + p = 0$ have sum $s$ and product $p$. So $x$ and $y$ are the roots of $t^2 - 20t + 96 = 0$.
3. Carry out. The discriminant is $400 - 384 = 16$, so $t = \frac{20 \pm 4}{2}$, which gives $t = 12$ or $t = 8$.
4. Look back. Check: $12 + 8 = 20$ and $12 \cdot 8 = 96$. Ask what else the method gives: any sum $s$ and product $p$ with $s^2 - 4p$ a perfect square give integer answers.

The typical use: phase 1 names the condition, which suggests the related problem in phase 2.

A trap: in phase 4 the check confirms that $12$ and $8$ work, but it does not show that they are the only answer; for that, phase 3 must use equivalent steps, as it does here.

### L3 human

The four phases describe a cycle that also appears outside mathematics, for example in engineering design and in the scientific method, where a plan is tested and revised.
Research on problem solving, in particular the work of Alan Schoenfeld, showed that students who learn the names of the heuristics do not use them well without practice in choosing among them.
This led to models that add a control level above the heuristics, and to teaching that makes the solver's decisions visible.
In this topic, the single heuristics of phase 2 have their own pages, and [[proofs and refutations|79P9CTRN0V]] extends phase 4 to the revision of the theorem itself.
The area [[problem solving and competitions|2HNEG88WT8]] treats the training of problem solving as a subject.
