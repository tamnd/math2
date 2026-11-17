---
tag: DYSJB93V11
kind: concept
name: Auxiliary problem
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, KCK4AQ469Q]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

An auxiliary problem is a second problem that we solve, not for its own sake, but because its solution helps to solve the original problem.
It can be a special case, a more general problem, an analogous problem, a part of the problem, or the same problem in another form.
Two auxiliary problems are equivalent when the solution of each gives the solution of the other; Pólya calls the passage between them a bilateral reduction.
When only one direction holds, the passage is a unilateral reduction: the auxiliary problem is then more ambitious (its solution gives the original solution) or less ambitious (it gives only a part or a bound).
Choosing a good auxiliary problem is one of the main [[heuristics|6KCEWEP4WA]] of problem solving, and the auxiliary problem is often the hidden idea behind a short solution.

## Motivation

Many problems cannot be attacked head-on, because no known method fits them as they are stated.
A change of form can make a known method fit: a quartic equation in $x^2$ is a quadratic equation in disguise.
A count with conditions becomes a count of subsets after a bijection.
Mathematics is full of such passages: a geometry problem becomes an algebra problem in coordinates, and a sum becomes an integral.
The auxiliary problem names this move and asks the solver to look for it on purpose: "If you cannot solve the proposed problem, try to solve first some related problem."

## Notation

Write $P$ for the original problem and $Q$ for the auxiliary problem.
When the problems are statements to prove, a bilateral reduction means $P \Leftrightarrow Q$, and a unilateral reduction means $Q \Rightarrow P$ (a [[stronger statement|KCK4AQ469Q]]) or $P \Rightarrow Q$ (a weaker statement).
When the problems ask for an unknown, the reduction is bilateral if there is a bijection between the solutions of $P$ and of $Q$ that we can compute in both directions.

## Remarks

### The steps

1. Ask whether a known method solves $P$ directly. If not, look for an auxiliary problem.
2. Find a candidate $Q$: introduce a new unknown, reformulate the condition, take a special case or a general case, or take a part of the condition.
3. Decide how $Q$ is related to $P$: equivalent, stronger, or weaker.
4. Solve $Q$.
5. Return to $P$: transfer the solution back, and check what the relation of step 3 allows. An equivalent $Q$ gives the answer; a weaker $Q$ gives only candidates or bounds.

### When it applies

- The unknown appears only through one expression, such as $x^2$ or $3^x$: make that expression the new unknown.
- The objects can be encoded in another way, such as solutions of an equation as rows of stars and bars.
- A condition can be split, so that a part of it defines an easier problem; see [[variation of the problem|KT5SASGTQ5]].
- A known theorem solves a nearby problem, and the task is to bring the problem to that form.

### Examples

1. [[Solving x^4 - 13x^2 + 36 = 0|SCV1PRX55T]]: the auxiliary equation $y^2 - 13y + 36 = 0$ in $y = x^2$ is equivalent to the original equation, together with the condition $y \geq 0$.
2. [[Counting the solutions of x + y + z = 10|5DKC774S00]]: a bijection turns the problem into the choice of $2$ places out of $12$, with answer $66$.
3. To find the distance from the point $(3, 4)$ to the circle $x^2 + y^2 = 1$, solve the auxiliary problem "distance from $(3, 4)$ to the centre", which is $5$. The nearest point of the circle lies on the segment to the centre, so the distance is $5 - 1 = 4$.
4. To prove that $n^5 - n$ is divisible by $30$ for every integer $n$, prove three auxiliary statements: divisibility by $2$, by $3$ and by $5$. Since $2$, $3$ and $5$ are pairwise coprime, together they are equivalent to the original statement; see [[decomposing and recombining|KEZPDNM2NH]].
5. A geometric construction is often reduced to the auxiliary problem of constructing one point, which is then found as the intersection of two loci.

### Non-examples

1. [[Rounding the solution of a linear programming relaxation|R09YNAR948]]: the relaxation drops the integrality condition, so it is only a weaker problem; rounding its answer gives a point that breaks a constraint.
2. Solving $x^2 = 3x$ through the auxiliary equation $x = 3$, obtained by dividing by $x$. The two problems are not equivalent: the solution $x = 0$ is lost.
3. An auxiliary problem that is harder than the original problem and has no solution in view. Replacing "is $2^{31} - 1$ prime?" by "find all primes of the form $2^p - 1$" is a more ambitious problem that is still open.

### Basic properties

1. If $Q$ is equivalent to $P$, the answer of $Q$ transferred back is exactly the answer of $P$.
2. If $Q \Rightarrow P$, a proof of $Q$ proves $P$, but $Q$ may be false while $P$ is true.
3. If $P \Rightarrow Q$, a solution of $Q$ gives only a necessary condition or a bound for $P$, and the candidates must be checked.
4. A substitution $y = g(x)$ gives an equivalent problem only on the range of $g$; values of $y$ outside the range must be dropped.
5. An auxiliary problem is a guess about a useful detour: it can fail, and the solver may need several attempts.

### Related methods

- [[Specialization|FTBJX4G51S]] and [[generalization as a heuristic|8NJ0VN9Z97]] produce auxiliary problems that are weaker or stronger than the original.
- [[Analogy|7KDT0R1HF2]] produces an auxiliary problem of the same form in another setting.
- The [[inventor's paradox|FVRKDXBJF6]] is the observation that a more ambitious auxiliary problem can be easier.
- [[Auxiliary elements|8TKKRAXKFN]] are the new objects, such as the variable $y$, that an auxiliary problem introduces.
- [[Reduction to a special case|DX2H7AD66G]] is the proof pattern in which the special case is equivalent to the general case.

### History

Pólya gives "auxiliary problem" an entry of the heuristic dictionary in How to Solve It (1945).
He distinguishes there the bilateral reduction, between equivalent problems, from the unilateral reduction, between problems that are more or less ambitious than the original one.
The idea is much older: the Greek analysis that Pappus described reduces a problem to an auxiliary problem step by step; see [[working backwards|3QTB9S1THS]].

### Common errors

1. Treating a weaker auxiliary problem as equivalent, as in the two first non-examples: the answer of the auxiliary problem is taken for the answer of the original.
2. Forgetting the return step: the solution of $y^2 - 13y + 36 = 0$ is $y \in \{4, 9\}$, and the question asked for $x$.
3. Forgetting the range of a new unknown, such as $y = x^2 \geq 0$.

## Explanations

### L1 human

Sometimes a problem is hard as it is asked, but a related problem is easy.
For example, "how far is the point $(3, 4)$ from the circle of radius $1$ around the origin?" is a new kind of question.
But "how far is $(3, 4)$ from the origin?" is easy: it is $5$, by the Pythagorean theorem.
The nearest point of the circle is on the way to the origin, so the answer is $5 - 1 = 4$.
We solved an easier problem first and then used its answer.

### L2 human

We prove that $n^5 - n$ is divisible by $30$ for every integer $n$, through auxiliary problems.

1. Since $30 = 2 \cdot 3 \cdot 5$ with pairwise coprime factors, it suffices, and it is necessary, that $2$, $3$ and $5$ each divide $n^5 - n$.
2. Factor: $n^5 - n = n(n^4 - 1) = (n - 1) n (n + 1)(n^2 + 1)$.
3. Divisibility by $2$: $(n - 1) n$ is a product of two consecutive integers, so one factor is even.
4. Divisibility by $3$: $(n - 1) n (n + 1)$ contains three consecutive integers, so one of them is a multiple of $3$.
5. Divisibility by $5$: if $n \equiv 0, 1, 4 \pmod 5$, one of $n$, $n - 1$, $n + 1$ is divisible by $5$. If $n \equiv 2$ or $3 \pmod 5$, then $n^2 + 1 \equiv 5$ or $10 \equiv 0 \pmod 5$.
6. By step 1, $30$ divides $n^5 - n$.

The typical use: replace one hard question by several easier ones whose answers together are equivalent to it.

A trap: step 1 needs the factors to be pairwise coprime; divisibility by $2$ and by $4$ does not give divisibility by $8$.

### L3 human

Auxiliary problems are the informal side of the notion of reduction, which is exact in other parts of mathematics.
In computability and complexity theory, a reduction of problem $A$ to problem $B$ transforms instances so that a solver for $B$ gives a solver for $A$; NP-completeness is defined this way.
In algebra, an equation over a ring is often studied through its images over residue fields or completions, which are auxiliary problems that are weaker, and local-global principles say when they are together equivalent.
Relaxations in optimization, such as the linear programming relaxation of an integer program, are unilateral reductions that give bounds, and duality gives a second auxiliary problem whose value bounds the first from the other side.
