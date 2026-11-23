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

Pólya's four steps split the work on a problem into four phases: understand the problem, devise a plan, carry out the plan, and look back.
They do not solve anything by themselves, but they tell you what to ask next when you do not know how to start.

Here is a problem where the first phase saves the answer.
A car drives $60$ km at $40$ km/h and then drives back at $60$ km/h; what is its average speed?
The quick answer is the mean of the two speeds, $50$ km/h.
Phase 1 asks what the unknown is, and the unknown is the average speed, which means total distance over total time.
The trip out takes $60/40 = 1.5$ hours and the trip back takes $1$ hour, so
$$\text{average speed} = \frac{60 + 60}{1.5 + 1} = \frac{120}{2.5} = 48 \text{ km/h}.$$
Phase 4 checks the result with an extreme case.
If the return trip took no time at all, the average would be $120/1.5 = 80$ km/h, a finite number, while the mean of the speeds would be infinite.
So the mean of the speeds is the wrong quantity, and $48$ km/h is right.

In general, phase 1 names the unknown, the data and the condition, or, for a statement to prove, the hypothesis and the conclusion.
Phase 2 looks for a connection between the data and the unknown, often through a related problem that is already solved.
Phase 3 carries out the plan and checks each step, and phase 4 checks the result, looks for a second way to reach it, and asks where else the method works.
For each phase George Pólya gave a list of questions, and these lists are the best known collection of [[heuristics|6KCEWEP4WA]] for school and university mathematics.

## Motivation

Many students start to calculate before they know what the problem asks, and many stop as soon as they have a number.
The first habit answers the wrong question, as the quick answer $50$ km/h does, and the second leaves errors in place.
Pólya noticed that a good teacher asks the same few questions again and again: what is the unknown, do you know a related problem, can you check the result.
He wrote these questions down in a fixed order, so that a student can ask them without the teacher.

The phases matter most for a problem whose method you do not know in advance.
For a routine exercise, phases 1 and 2 take a moment, and phase 4 still pays.
For a research problem, phase 2 can take years, and its questions are only a start.
The single heuristics on the later pages, such as [[specialization|FTBJX4G51S]] and [[working backwards|3QTB9S1THS]], are the tools of phase 2.

## Notation

Pólya's English names are "understanding the problem", "devising a plan", "carrying out the plan" and "looking back".
Books also call them the four phases, the four stages or the problem-solving cycle.
The question lists come from the first part of *How to Solve It*, and the longer second part is a "short dictionary of heuristic" with an entry for each single heuristic.

## Remarks

### The questions of each phase

In phase 1 you ask: what is the unknown, what are the data, and what is the condition?
You draw a figure, introduce notation, and ask whether the condition is enough to determine the unknown, too little, or contradictory.
In phase 2 you ask whether you know a problem with the same unknown, and whether you can solve a special case, a more general problem, or a part of the condition.
You also check that the plan uses all the data.
In phase 3 you check each step, and a step that you cannot justify sends you back to phase 2.
In phase 4 you check the result by a special case, by the units, or by a second method, and you ask whether the result or the method solves another problem.

### Pólya's first example

Pólya's own first example asks for the diagonal of a rectangular box with edges $a$, $b$ and $c$.
Phase 2 asks for a solved problem with the same kind of unknown, and the diagonal of a rectangle comes to mind.
That suggests the diagonal of the base, $\sqrt{a^2 + b^2}$, as an extra segment, and then a second right triangle gives
$$d = \sqrt{a^2 + b^2 + c^2}.$$
Phase 4 checks that the formula is symmetric in $a$, $b$ and $c$, and that $c = 0$ gives the diagonal of the rectangle.
[[The diagonal of a rectangular box by the four steps|FGMDA7TF3Q]] writes out every phase.

### A counting problem

How many squares of all sizes lie along the grid lines of a chessboard?
Phase 1 shows that squares of every side from $1$ to $8$ count, not only the $64$ cells.
Phase 2 counts by size, and a square of side $k$ has $(9 - k)^2$ positions, so the total is
$$8^2 + 7^2 + \dots + 1^2 = 204.$$
Phase 4 checks a $2 \times 2$ board, which has $5$ squares, and generalizes to the $n \times n$ board.
[[Counting the squares on a chessboard by the four steps|H817ES7NHH]] gives the details.

### Where the plan gives out

The four steps organize a search, and a search can fail.
The [[Collatz problem|J50X63VCAK]] asks whether repeating $n \mapsto n/2$ for even $n$ and $n \mapsto 3n + 1$ for odd $n$ always reaches $1$.
Every question of phase 2 can be asked, special cases, variants and generalizations, and each answer is informative, but none gives a plan for a proof.
The problem is still open.

A solution can also go wrong by skipping a phase.
The answer $50$ km/h skipped phase 1, and a list of formulas tried one after another skips phases 1 and 4 altogether.

### Watch out

The common error is to read the four steps as a recipe.
They say what to ask, not what the plan is, and they never guarantee that a plan will come.
The phases are also not a strict order: a failed phase 3 sends you back to phase 2 or even to phase 1.

A second error is to skip phase 4 because the answer looks right.
A check with an extreme case, as in the car problem, takes a minute and catches many errors.

### Related frameworks

The [[forward-backward method|V8ZB838JY5]] is a plan for phases 2 and 3 of a problem to prove.
Mason, Burton and Stacey, in *Thinking Mathematically* (1982), describe three phases called entry, attack and review, which match phase 1, phases 2 and 3, and phase 4.
Schoenfeld, in *Mathematical Problem Solving* (1985), added control: the decision when to drop one plan and try another.
Phase 4 is also the source of new questions, as [[problem posing|Y896GWYF8A]] explains.

### History

George Pólya published *How to Solve It* in 1945, and a second edition appeared in 1957.
The book has a short part on the four phases, a dialogue between a teacher and a class, and the dictionary of heuristic.
Pólya developed the ideas further in *Mathematics and Plausible Reasoning* (1954) and *Mathematical Discovery* (1962 and 1965).

### Try it

Two positive integers have sum $20$ and product $96$; find them.
Phase 2 recalls that the roots of $t^2 - 20t + 96 = 0$ have this sum and product, so the numbers are $12$ and $8$, and phase 4 checks $12 + 8 = 20$ and $12 \cdot 8 = 96$.

A cyclist rides up a hill at $10$ km/h and down the same road at $30$ km/h; what is the average speed?
For a road of length $L$ the time is $L/10 + L/30 = 4L/30$, so the average is $2L$ divided by that, which is $15$ km/h, not $20$.

## Explanations

### L1 human

Pólya's four steps are four questions for any problem.
First, what does the problem ask, and what do we know?
Second, how can we get from what we know to what we want?
Third, do it carefully.
Fourth, is the answer right, and what did we learn?
For example, when $5$ people each shake hands once with each other person, we want the number of pairs.
Each person shakes $4$ hands, which gives $5 \cdot 4 = 20$, but that counts each handshake twice, so the answer is $10$.
To check, list the pairs for $3$ people: there are $3$, and the same rule gives $3 \cdot 2 / 2 = 3$.

### L2 human

We find two positive integers with sum $20$ and product $96$ by the four phases.
In phase 1, the unknowns are integers $x$ and $y$, and the condition is $x + y = 20$ and $xy = 96$.
In phase 2 we recall a related problem: the roots of $t^2 - st + p = 0$ have sum $s$ and product $p$.
So $x$ and $y$ are the roots of $t^2 - 20t + 96 = 0$.
In phase 3 the discriminant is $400 - 384 = 16$, so
$$t = \frac{20 \pm 4}{2}, \qquad t = 12 \text{ or } t = 8.$$
In phase 4 we check $12 + 8 = 20$ and $12 \cdot 8 = 96$, and we see that the method works for any sum $s$ and product $p$, with integer answers when $s^2 - 4p$ is a perfect square.
Watch out: the check shows that $12$ and $8$ work, not that they are the only answer.
Uniqueness comes from phase 3, because every step there was an equivalence.

### L3 human

The four phases describe a cycle of planning, trying and revising that also appears in engineering design and in the scientific method.
Research on problem solving, especially Schoenfeld's, found that students who learn the names of the heuristics do not use them well without practice in choosing among them.
This led to models that put a level of control above the heuristics, and to teaching that makes the solver's decisions visible.
[[Proofs and refutations|79P9CTRN0V]] extends phase 4 from the check of an answer to the revision of the theorem itself.
[[Problem solving and competitions|2HNEG88WT8]] treats the training of problem solving as a subject of its own.
