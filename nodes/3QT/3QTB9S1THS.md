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

Working backwards starts from the goal and asks what would have to come just before it.
From the data many roads lead away, but only a few lead into the goal, so the goal is often the better guide.

Here is a puzzle where this pays off.
You have a $4$-liter jug, a $9$-liter jug, a tap and no marks on the jugs.
You may fill a jug, empty a jug, or pour one jug into the other until the first is empty or the second is full.
How do you get exactly $6$ liters in the large jug?

The natural first attempt runs forward.
Fill the small jug and pour it into the large one, twice, and the large jug holds $8$ liters.
A third pour fills the large jug and leaves $3$ liters in the small one, and now we have $3$ and $9$ liters with no sign of $6$.
Every state allows several moves, and nothing tells us which one leads anywhere.

So we start from the goal instead.
Six liters is a full large jug minus $3$ liters:
$$6 = 9 - 3.$$
A pour from a full large jug removes exactly $3$ liters when the small jug already holds $1$ liter, because then it has room for $3$.
So the new goal is $1$ liter in the small jug, and $1 = 9 - 4 - 4$ is what a full large jug leaves after filling the small jug twice.
Now we reverse the chain and write the moves forward, with states as (small, large):
$$(0, 0) \to (0, 9) \to (4, 5) \to (0, 5) \to (4, 1) \to (0, 1) \to (1, 0) \to (1, 9) \to (4, 6).$$
The large jug holds $6$ liters after $8$ moves, and [[measuring 6 liters with jugs of 4 and 9 liters|CJJZX90P2M]] checks each move.

In general, working backwards replaces the goal by a nearer goal from which it follows, again and again, until it reaches something given or known.
Then the chain is reversed, and only the reversed chain is the solution or the [[proof|0B94TKFQJX]].
Like every heuristic, it is advice about where to start, not an algorithm that always succeeds.

## Motivation

A maze is hard to solve from the entrance, where many paths branch, and often easy from the exit, where few paths arrive.
Many problems have the same shape.
In a puzzle with moves, the start allows many moves, but the goal can be reached from only a few states.
In a geometric construction, a sketch of the finished figure shows which known figure hides inside it.
In a proof, the hypothesis has many consequences, and the conclusion tells you which of them are useful.

The same idea runs through applied mathematics and computing.
In game theory, [[backward induction|JEMK4V2PCW]] finds optimal play by solving the last moves first.
For proofs, the [[forward-backward method|V8ZB838JY5]] works from both ends and meets in the middle.

## Notation

Pólya's term is "working backwards", and he also used Pappus's names: "analysis" for the backward search and "synthesis" for the forward solution.
Computer science calls the same search "backward chaining" or "goal-directed search".
When you write the result, write the synthesis: a solution that starts from the conclusion reads to others as an assumption of what was to be shown.

## Remarks

### Analysis and synthesis

The method has a backward half and a forward half.

1. State the goal exactly: the unknown and the condition it must satisfy.
2. Assume the goal is reached, and ask from which state, figure or statement it could follow in one step.
3. Take one answer as the new goal, record the step, and repeat until the goal is given or known.
4. Reverse the chain, carry out each step forward, and check that the result meets the condition.

Step 4 is not optional.
The backward chain assumes the goal, so it proves nothing until it is reversed, and for proofs each reversed step must be a valid implication.

### When the steps reverse

If every backward step undoes an operation, the synthesis is automatic.
"A number is tripled, then $5$ is added, then the result is halved, and the answer is $13$."
Undo the steps from the end: $13 \cdot 2 = 26$, then $26 - 5 = 21$, then $21 / 3 = 7$, and the check is $(3 \cdot 7 + 5)/2 = 13$.

The same holds for a chain of equivalences.
To show $\sqrt{2} + \sqrt{6} < \sqrt{15}$, note that both sides are positive, so squaring is an equivalence:
$$8 + 2\sqrt{12} < 15 \iff 4\sqrt{3} < 7 \iff 48 < 49.$$
The last statement is true, and each arrow points both ways, so the chain read upward is a proof.

### Constructions and games

The classical home of the method is geometric construction.
In [[constructing a triangle from two sides and the median to the third side|ZKWF9YNS66]], the analysis assumes the triangle drawn, doubles the median, and finds a triangle with three known sides; the synthesis reverses the steps.
The doubled median is an [[auxiliary element|8TKKRAXKFN]], and each new goal of the chain is an [[auxiliary problem|DYSJB93V11]].

In games, the positions near the end are the easiest to classify.
Two players take $1$, $2$ or $3$ counters from a pile, and whoever takes the last counter wins.
A pile of $4$ is lost for the player to move, then $8$, then every multiple of $4$; [[a take-away game solved for every number of counters|RNG0PDDXSN]] proves it.

### When working backwards misleads

Some backward steps cannot be reversed.
Solving $\sqrt{x + 2} = x$ by squaring gives $x^2 - x - 2 = 0$, so $x = 2$ or $x = -1$.
The candidate $x = -1$ fails, since $\sqrt{1} = 1 \ne -1$, so an analysis without synthesis gives a wrong answer.

A backward search that finds nothing also proves nothing.
In [[the backward search for 5 liters with jugs of 4 and 6 liters|33P1SJW98J]], the chain keeps asking for odd amounts and never reaches the start.
Only an [[invariant|8NQ190278Y]], "both amounts stay even", shows that the goal is impossible.
And a problem with no fixed goal, such as "find a nice property of this sequence", gives nothing to work back from.

### Watch out

The first error is to stop after the analysis and present it as the solution.
The second is to use a backward step that cannot be reversed, such as squaring an equation or dividing by a quantity that may be $0$, and not to check the candidates.
In the equation above, the fix is to substitute each candidate into $\sqrt{x + 2} = x$.
The third is to write the backward chain as the final proof, so that the text begins with the conclusion; [[scratch work and the final proof|E97XXFW9MV]] shows how to turn it around.

### History

Pappus of Alexandria worked in the fourth century CE.
In Book 7 of his *Collection* he described analysis as the path that takes what is sought as granted and goes back to something admitted, and synthesis as the path forward again.
He separated theoretical analysis, which seeks a proof, from problematical analysis, which seeks a construction.
Pólya gave both "working backwards" and "Pappus" entries in the heuristic dictionary of *How to Solve It* (1945).

### Try it

First, with jugs of $3$ and $5$ liters, get exactly $4$ liters in the large jug.
Work back from $4 = 5 - 1$: a full large jug loses $1$ liter into a small jug that holds $2$, and $2 = 5 - 3$; the moves are $(0,0) \to (0,5) \to (3,2) \to (0,2) \to (2,0) \to (2,5) \to (3,4)$.

Second, I think of a number, square it, subtract $7$ and get $29$; what can my number be?
Undo the steps: $29 + 7 = 36$, and the square roots of $36$ are $6$ and $-6$, so both answers work, since squaring cannot be undone uniquely.

## Explanations

### L1 human

To find a route through a maze, it often helps to start at the exit.
Few paths arrive at the exit, so the last part of the route is quickly found.
Then you ask how to reach the start of that last part, and so on.
For example: "I think of a number, double it, add $3$ and get $11$; what is my number?"
Undo the steps from the end: $11 - 3 = 8$, and $8 / 2 = 4$.
Then check forward: $2 \cdot 4 + 3 = 11$.

### L2 human

We work backwards in a game where two players take $1$, $3$ or $4$ counters in turn, and whoever takes the last counter wins.
Call a pile losing if the player to move loses against best play.
A pile of $0$ is losing, since the other player has just won, and piles of $1$, $3$ and $4$ are winning, since you take everything.
A pile of $2$ is losing, because the only move leaves $1$.
Piles of $5$ and $6$ are winning, since taking $3$ or $4$ leaves $2$, and a pile of $7$ is losing, since every move leaves $6$, $4$ or $3$.
Going on, $9$ and $14$ are losing and $8$, $10$, $11$, $12$ and $13$ are winning.

So we conjecture that $n$ is losing exactly when $n$ leaves remainder $0$ or $2$ on division by $7$, and [[strong induction|0KMVFSHFGZ]] proves it.
From remainder $0$ the moves give remainders $6$, $4$ and $3$, and from remainder $2$ they give $1$, $6$ and $5$, none of them $0$ or $2$.
From remainders $1$, $3$, $4$, $5$ and $6$, taking $1$, $3$, $4$, $3$ and $4$ counters leaves remainder $0$ or $2$.
With $20$ counters, $20 = 2 \cdot 7 + 6$, so the first player takes $4$ and leaves $16$, which has remainder $2$.

This is the typical use: classify the positions near the goal first, then move outward.
Watch out: the losing piles here are not the multiples of one number, so the pattern became a theorem only through the induction.

### L3 human

In automated reasoning, working backwards is backward chaining, and in a finite state space it is a breadth-first search on the graph of moves with every arrow reversed.
In dynamic programming, the Bellman equation solves a problem from its last stage, and backward induction does the same for finite games of perfect information.

Pappus's split between analysis and synthesis survives as the split between scratch work and the written proof, treated in [[writing and reading proofs|STSM6PR7TX]].
Its limit is also general.
A goal-directed search finds witnesses, but a proof that no witness exists needs a global argument, which links the heuristic to invariants and to [[proofs of impossibility|6F55216R53]].
In [[Pólya's four steps|DYD57G2Y5Z]], working backwards is one of the main ways to devise a plan.
