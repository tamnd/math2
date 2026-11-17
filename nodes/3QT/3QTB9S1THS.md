---
tag: 3QTB9S1THS
kind: concept
name: Working backwards
msc: ["00A35", "97E50"]
topics: [X1NSTVGDNQ]
audience: school
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - url: https://en.wikipedia.org/wiki/Pappus_of_Alexandria
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Working backwards is a [[heuristic|6KCEWEP4WA]] for a problem with a clear goal: we start from the goal and ask what would come just before it.
Each answer is a new, nearer goal, and the question is repeated until a goal is reached that is already known or given.
For a problem to find (a number, a figure, a sequence of moves), the chain is then reversed to give the solution.
For a problem to prove, the chain is reversed and each step is checked, so that the [[proof|0B94TKFQJX]] runs forward from the hypothesis.
The classical form is the analysis and synthesis of Greek geometry, as described by Pappus of Alexandria.
The heuristic matters because the goal is often a better guide than the data: from the data many roads lead away, but only a few lead to the goal.

## Motivation

A maze is hard to solve from the entrance, where many paths branch, and often easy from the exit, where few paths arrive.
Many problems have the same shape.
In a puzzle with moves, the start allows many moves, but the goal can be reached only from a few states.
In a geometric construction, the data are scattered, but a sketch of the finished figure shows which known figure hides inside it.
In a proof, the hypothesis has many consequences, and the conclusion tells which of them are useful.
Working backwards uses the goal to cut down the search.

## Remarks

### The steps

1. State the goal exactly: the unknown and the condition that it must satisfy.
2. Assume that the goal is reached, and ask: from which state, figure or statement could it follow in one step?
3. Take one answer as the new goal. Keep a record of the step.
4. Repeat steps 2 and 3 until the goal is something given or known to be possible.
5. Reverse the chain. For a problem to find, carry out the steps forward and check that the result meets the condition. For a problem to prove, check that each reversed step is a valid implication.

Step 5 is part of the method.
Pappus called the backward part analysis and the forward part synthesis, and only the synthesis is the solution.

### When it applies

- The goal is stated precisely, and it can be reached in only a few ways.
- The steps can be reversed: a pour, a move in a game, an arithmetic operation, or a logical step that is an equivalence.
- The problem is a construction: the analysis assumes the figure drawn and looks for a known figure inside it.
- A game with perfect information: the positions near the end are easy to classify, as in [[backward induction|JEMK4V2PCW]].
- A proof whose conclusion suggests the last step; for proofs the plan is the [[forward-backward method|V8ZB838JY5]], which works from both ends.

### Examples

1. [[Measuring 6 litres with jugs of 4 and 9 litres|CJJZX90P2M]]: $6 = 9 - 3$, so the last move pours $3$ litres into a small jug that holds $1$ litre, and the chain continues from there.
2. [[Constructing a triangle from two sides and the median|ZKWF9YNS66]]: the analysis doubles the median and finds a triangle with three known sides; the synthesis reverses it.
3. "A number is multiplied by $3$, then $5$ is added, then the result is halved, and the answer is $13$." Backwards: $13 \cdot 2 = 26$, then $26 - 5 = 21$, then $21 / 3 = 7$. Forward check: $(3 \cdot 7 + 5)/2 = 13$.
4. A game: two players take $1$, $2$ or $3$ counters from a pile, and the player who takes the last counter wins. Backwards from the end, a pile of $4$ is lost for the player to move, then $8$, then each multiple of $4$. The page [[a take-away game solved for every number of counters|RNG0PDDXSN]] gives the proof.
5. To show $\sqrt{2} + \sqrt{6} < \sqrt{15}$, work back through equivalences: both sides are positive, so square to get $8 + 2\sqrt{12} < 15$, that is $4\sqrt{3} < 7$, that is $48 < 49$, which is true. Each step is an equivalence, so the chain reverses to a proof.

### Non-examples

1. [[The backward search for 5 litres with jugs of 4 and 6 litres|33P1SJW98J]]: the backward chain only asks for odd amounts and never reaches the start, but only an [[invariant|8NQ190278Y]] proves that the goal is impossible.
2. Solving $\sqrt{x + 2} = x$ by squaring gives $x^2 - x - 2 = 0$, so $x = 2$ or $x = -1$. The step "square both sides" cannot be reversed for $x = -1$, since $\sqrt{1} = 1 \neq -1$. An analysis without synthesis gives a wrong answer.
3. A problem whose goal is not fixed, such as "find a nice property of this sequence". There is no end to work back from, and the heuristic does not apply.

### Basic properties

1. Each backward step replaces the goal $G$ by a goal $G'$ from which $G$ follows. In a proof, $G'$ must imply $G$; a statement that $G$ only implies cannot replace $G$.
2. If every step is reversible (an equivalence or an invertible operation), the synthesis is automatic: the reversed chain is valid.
3. If some step is not reversible, the analysis only gives necessary conditions, and the synthesis must check each candidate, as in non-example 2.
4. A backward search that finds nothing proves nothing, unless it is complete. An impossibility needs a separate argument, such as an [[invariant|8NQ190278Y]] or a [[proof of impossibility|6F55216R53]].
5. Working backwards is a heuristic: it suggests a plan, and it can fail or lead to dead ends.

### Related methods

- The [[forward-backward method|V8ZB838JY5]] applies the same idea to proofs and works from both ends at once.
- [[Auxiliary elements|8TKKRAXKFN]]: the analysis of a construction often finds an auxiliary point or line, such as the doubled median.
- [[Auxiliary problem|DYSJB93V11]]: each new goal of the backward chain is an auxiliary problem that implies the original one.
- [[Pólya's four steps|DYD57G2Y5Z]]: working backwards is one way to devise a plan.

### History

Pappus of Alexandria worked in the fourth century CE.
In Book 7 of his Collection, he described analysis as the way that takes what is sought as granted and passes back to something admitted.
He described synthesis as the way back, from what is admitted to what is sought.
He distinguished theoretical analysis, which seeks a proof, from problematical analysis, which seeks a construction.
George Pólya included "working backwards" and "Pappus" as entries of the heuristic dictionary in How to Solve It (1945).

### Common errors

1. Stopping after the analysis. The backward chain assumes the goal, so it proves nothing until it is reversed and checked.
2. Using a backward step that cannot be reversed, such as squaring an equation or dividing by a quantity that may be $0$, and not checking the candidates.
3. Writing the backward chain as the final solution, so that the text starts with the conclusion.

## Explanations

### L1 human

To find a route through a maze, it often helps to start at the exit.
Few paths arrive at the exit, so the last part of the route is quickly found.
Then we ask how to reach the start of that path, and so on.
For example: "I think of a number, double it, add $3$ and get $11$; what is my number?"
We undo the steps from the end: $11 - 3 = 8$, and $8 / 2 = 4$.
Then we check forward: $2 \cdot 4 + 3 = 11$.

### L2 human

We work backwards in a game with other moves: two players take $1$, $3$ or $4$ counters in turn, and whoever takes the last counter wins.
Call a pile size losing if the player to move loses against best play, and winning otherwise.

1. A pile of $0$ is losing for the player to move, since the other player has just taken the last counter.
2. Piles of $1$, $3$ and $4$ are winning: take all counters.
3. A pile of $2$ is losing: the only move leaves $1$, a winning pile for the opponent.
4. Piles of $5$ and $6$ are winning: take $3$ or $4$ to leave $2$.
5. A pile of $7$ is losing: the moves leave $6$, $4$ or $3$, all winning. Then $8$, $10$, $11$, $12$, $13$ are winning, and $9$ and $14$ are losing.
6. Conjecture: a pile of $n$ is losing exactly when $n$ leaves remainder $0$ or $2$ on division by $7$.
7. Proof by [[strong induction|0KMVFSHFGZ]]. From remainder $0$ the moves give remainders $6$, $4$, $3$, and from remainder $2$ they give $1$, $6$, $5$; none is $0$ or $2$. From remainders $1$, $3$, $4$, $5$, $6$, taking $1$, $3$, $4$, $3$, $4$ counters gives remainder $0$ or $2$.
8. For $20$ counters, $20 = 2 \cdot 7 + 6$, so the first player takes $4$ and leaves $16$, which has remainder $2$.

The typical use: classify the positions near the goal first, then move outwards.

A trap: the losing piles here are not the multiples of one number, so a guess from steps 1 to 3 alone would be wrong; the pattern became a theorem only through the induction in step 7.

### L3 human

Working backwards is the search direction called backward chaining in automated reasoning and goal-directed search in artificial intelligence.
In a finite state space it can be run as a breadth-first search on the graph of moves with each arrow reversed.
In game theory, backward induction computes optimal play in finite games of perfect information, and in dynamic programming the Bellman equation solves a problem from its last stage.
Pappus's distinction between analysis and synthesis survives in the modern distinction between scratch work and the written proof, treated in the topic [[writing and reading proofs|STSM6PR7TX]].
Its limit is also general: a goal-directed search finds witnesses, but a proof that no witness exists needs a global argument, which links the heuristic to [[invariants|8NQ190278Y]] and to proofs of impossibility.
