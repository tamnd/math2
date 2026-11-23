---
tag: FVRKDXBJF6
kind: concept
name: Inventor's paradox
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 8NJ0VN9Z97, F94KJC2RXP]
sources:
  - url: https://en.wikipedia.org/wiki/Inventor%27s_paradox
    locator: lead section
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

The inventor's paradox is the observation that a more ambitious problem can be easier to solve than the problem that was asked.
A stronger statement says more, so it should be harder to prove, yet it often gives the proof more to work with.

Here is the standard case.
We want to show that for every $n \ge 1$,
$$1 + \frac{1}{4} + \frac{1}{9} + \cdots + \frac{1}{n^2} < 2.$$
Write $S_n$ for the sum, and try [[induction|0ASJVEFA9J]] on the claim $S_n < 2$.
The base case $S_1 = 1 < 2$ holds, but the step fails: from $S_n < 2$ we only get
$$S_{n+1} = S_n + \frac{1}{(n + 1)^2} < 2 + \frac{1}{(n + 1)^2},$$
which is not below $2$.
The hypothesis "$S_n < 2$" is too weak, because it allows $S_n$ to sit just below $2$, where the next term pushes it over.

So we ask for more, and we prove the sharper bound $S_n \le 2 - \frac{1}{n}$.
The base case is $S_1 = 1 = 2 - 1$.
For the step, assume $S_n \le 2 - \frac{1}{n}$; then we need
$$2 - \frac{1}{n} + \frac{1}{(n + 1)^2} \le 2 - \frac{1}{n + 1}, \quad \text{that is,} \quad \frac{1}{(n + 1)^2} \le \frac{1}{n} - \frac{1}{n + 1} = \frac{1}{n(n + 1)},$$
which holds because $n(n + 1) < (n + 1)^2$.
So $S_n \le 2 - \frac{1}{n} < 2$ for every $n$, and the harder-looking claim was the one we could prove.
The full example is [[the sum of 1/k² is at most 2 - 1/n|DFVCKA01PN]], and [[a direct induction on the bound 2|MZXYW75TC3]] shows the stuck attempt in detail.

As a heuristic, the inventor's paradox tells a solver who is stuck to try a stronger or more general problem as well as a weaker one.
It is a suggestion, not a law: sometimes the stronger problem is easier, and sometimes it is far harder.

## Motivation

A solver who cannot prove a statement usually tries to weaken it or to add hypotheses.
That is often right, but sometimes the obstacle is the opposite one: the statement is too weak to carry its own proof.
In an induction, the statement for $n$ is the hypothesis of the step, so a weak statement gives a weak hypothesis.
In a problem about one number, the number may hide a pattern that a general $n$ shows.
The paradox names this case, so that the solver remembers to try the stronger problem too.
Inside induction proofs it becomes the technique of [[strengthening the induction hypothesis|F94KJC2RXP]], and in general it explains why [[generalization|8NJ0VN9Z97]] can succeed.

## Notation

"Inventor's paradox" is Pólya's term, and "inventor" here means the person who finds a solution.
In books on induction the same move is called strengthening or loading the induction hypothesis.
In automated theorem proving it is called generalization of the goal.

## Remarks

### Why a stronger claim can be easier

A stronger statement is a stronger hypothesis and a stronger conclusion at once.
The method works when the gain in the hypothesis outweighs the extra demand in the conclusion.
In the opening problem, the hypothesis $S_n \le 2 - \frac{1}{n}$ leaves a gap of $\frac{1}{n}$ below $2$.
The step only has to show that the next term $\frac{1}{(n + 1)^2}$ is at most $\frac{1}{n} - \frac{1}{n + 1}$, the amount by which the gap is allowed to shrink.
The same pattern proves [[the product of (2k - 1)/(2k) is at most 1/√(3n + 1)|MC068WVGWS]], where the bound $\frac{1}{\sqrt{3n}}$ does not support an induction and $\frac{1}{\sqrt{3n + 1}}$ does.

### Solving for every n instead of one n

A question about one number often becomes easier when it is asked for every number.
In [[a take-away game solved for every number of counters|RNG0PDDXSN]], the game with $21$ counters is decided by finding all losing positions, the multiples of $4$, by induction.
In [[products of consecutive integers by the integrality of binomial coefficients|8G1BXJ7ZJM]], the claim that $24$ divides every product of four consecutive integers follows from the claim that $k!$ divides every product of $k$ consecutive integers.
That general claim says that a [[binomial coefficient|0GBZM0MT0F]] is an integer, which Pascal's rule proves for all $k$ at once.

### When the paradox fails

The ambitious problem is not always easier.
In [[Fermat's Last Theorem for n = 4 is easier than the general theorem|672544QRJC]], the exponent $4$ has a short proof by infinite descent, and the theorem for every exponent waited more than three centuries.
A strengthening can also be false.
To prove $2^n > n$ for $n \ge 1$ one might try $2^n > n^2$, but that fails at $n = 2, 3, 4$.
So test a strengthening on special cases before you try to prove it.

### Watch out

The first error is to strengthen without testing, as with $2^n > n^2$.
The second is to reject a stronger statement because it "must be harder"; the opening problem shows that this reasoning is wrong.
The third is to prove a stronger statement and forget to check that it implies the given one.
In the opening problem the check is one line, $2 - \frac{1}{n} < 2$, but you must write it.

### History

Pólya gave the inventor's paradox its own entry in the heuristic dictionary of *How to Solve It* (1945), where he observed that a plan with a larger aim can stand a better chance.
Automated theorem provers for induction include steps that generalize a goal before induction, because many goals cannot be proved by induction as stated.

### Try it

First, show by induction that $\sum_{k=1}^{n} \frac{1}{k(k + 1)} < 1$ for every $n \ge 1$.
A direct step gets stuck, so prove the equation $\sum_{k=1}^{n} \frac{1}{k(k + 1)} = 1 - \frac{1}{n + 1}$, whose step is $1 - \frac{1}{n + 1} + \frac{1}{(n + 1)(n + 2)} = 1 - \frac{1}{n + 2}$.

Second, who wins the take-away game with $30$ counters and moves of $1$, $2$ or $3$?
The losing positions are the multiples of $4$, and $30 = 4 \cdot 7 + 2$, so the first player wins by taking $2$.

## Explanations

### L1 human

Sometimes a bigger question is easier to answer than a small one.
Suppose two players take turns removing $1$, $2$ or $3$ counters from a pile of $21$, and whoever takes the last counter wins.
Working on $21$ alone is hard.
Asking "who wins with $1$, $2$, $3$, $4$, $5$ counters, and so on?" shows that the player to move loses exactly when the pile is a multiple of $4$.
That answers every pile at once, including $21$, and this surprise is the inventor's paradox.

### L2 human

We prove $\sum_{k=1}^{n} \frac{1}{k(k + 1)} < 1$ for every $n \ge 1$.
A direct induction is stuck: from "the sum up to $n$ is below $1$", adding $\frac{1}{(n + 1)(n + 2)}$ might push it over.
So we prove the exact statement
$$\sum_{k=1}^{n} \frac{1}{k(k + 1)} = 1 - \frac{1}{n + 1}.$$
Test it first: $n = 1$ gives $\frac{1}{2}$ on both sides, and $n = 2$ gives $\frac{2}{3}$ on both sides.
The step adds the next term:
$$1 - \frac{1}{n + 1} + \frac{1}{(n + 1)(n + 2)} = 1 - \frac{(n + 2) - 1}{(n + 1)(n + 2)} = 1 - \frac{1}{n + 2}.$$
Since $\frac{1}{n + 1} > 0$, the sum is below $1$.

This is the typical use: the inequality is the weak statement, and the equation is the strong statement that carries the induction.
Watch out: a strengthening must be true, which is why we tested it before the proof.

### L3 human

In automated theorem proving the paradox is a practical problem, because many goals cannot be proved by induction as stated.
Provers for induction therefore include generalization steps that replace a goal by a more general one, and the choice of that goal cannot be automated in general.
In human proofs, too, the choice of the stronger statement is often the main idea.

The paradox also explains why mathematicians value general theories: a general framework can turn many special results into exercises.
[[Abstraction and generalization|976RZZCT1H]] treats this effect for definitions and theories.
[[Specialization|FTBJX4G51S]] goes the other way, and it is the right move when the special case is the easier one.
