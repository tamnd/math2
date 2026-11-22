---
tag: F94KJC2RXP
kind: concept
name: Strengthening the induction hypothesis
aliases: [strengthening-the-inductive-hypothesis, loading-the-induction]
msc: ["00A35", "97E50"]
topics: [EEH2F76CYQ, G9JFJGY4TQ]
audience: ug1
uses: [0ASJVEFA9J, KCK4AQ469Q]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
  - url: https://en.wikipedia.org/wiki/Basel_problem
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 6
  - book: isbn:9780691164076
    locator: "Part III, Short dictionary of heuristic: Inventor's paradox"
---

## Summary

Sometimes an [[induction|0ASJVEFA9J]] stalls because the claim is too weak to feed its own step, and the cure is to prove more.
Here is the standard case: for every $n \ge 1$,
$$\sum_{k=1}^{n} \frac{1}{k^2} \le 2 - \frac1n, \quad \text{and so} \quad \sum_{k=1}^{n} \frac{1}{k^2} < 2.$$
Induction on "$< 2$" alone fails, because "below $2$" leaves no known room for the next term.
Induction on "$\le 2 - \tfrac1n$" works: the base case is $1 \le 1$, and the step needs only $\tfrac{1}{(n+1)^2} < \tfrac1n - \tfrac{1}{n+1}$, as [[the sum of $1/k^2$ is at most $2 - 1/n$|DFVCKA01PN]] shows in full.

In general, *strengthening the induction hypothesis* is the following method for a claim $P(n)$, $n \ge n_0$.
We choose a statement $Q(n)$ with $Q(n) \Rightarrow P(n)$ for each $n \ge n_0$, we prove $Q(n_0)$ and the step $Q(n) \Rightarrow Q(n + 1)$ for each $n \ge n_0$, and we conclude $Q(n)$, hence $P(n)$, for every $n \ge n_0$.
The method is valid because it is ordinary induction applied to $Q$, followed by one implication.

## Motivation

A [[stronger statement|KCK4AQ469Q]] is harder to reach and easier to use.
In an induction step it plays both roles: it is the hypothesis we use and the conclusion we must reach.
A stronger $Q$ makes the conclusion harder, but it also makes the hypothesis more informative, and the method succeeds when the second effect wins.
For the sum of $1/k^2$, the gap $\tfrac1n$ in the hypothesis is exactly the information that the step was missing.

The method is the usual repair when an induction step almost works.
It appears in bounds on sums and products, in tilings, in graph theory, and in computer science, where a loop invariant is a strengthened hypothesis about the number of iterations.
Finding the right $Q$ is often the main idea of a proof, and later methods such as [[double induction|AABX4YPKRR]] and [[structural induction|12MQ2NJ29A]] use the same move.

## Notation

We write $P(n)$ for the claim and $Q(n)$ for the strengthened claim, and the method needs $Q(n) \Rightarrow P(n)$ for each $n$.
Books also say "load the induction hypothesis", "generalize the claim" or "prove a more general statement".
Pólya calls the effect behind the method the inventor's paradox: a more ambitious problem can be easier to solve than the special one.

## Remarks

### How to find the stronger claim

The search for $Q$ follows a fixed routine.

1. Try plain induction on $P(n)$, and find the line where the step stalls.
2. Ask what that line needs: a sharper bound, an extra property, or a statement for all values of a second variable.
3. Write $Q(n)$ as $P(n)$ plus what the step needs.
4. Test $Q(n)$ on small $n$ by computation, because a false $Q$ cannot be proved.
5. Prove $Q(n_0)$ and the step, and then deduce $P(n)$ from $Q(n)$.

For the sum of $1/k^2$, step 1 stalls at "$S_n < 2$ plus a positive number", step 2 asks for a known gap below $2$, and step 4 confirms the guess $2 - \tfrac1n$ on the table $1 \le 1$, $\tfrac54 \le \tfrac32$, $\tfrac{49}{36} \le \tfrac53$.

### Three more strengthenings

A product works the same way as a sum.
For $P_n = \tfrac12 \cdot \tfrac34 \cdots \tfrac{2n-1}{2n}$, the claim $P_n < 1/\sqrt{3n}$ fails in its own step for every $n$, but the sharper $P_n \le 1/\sqrt{3n + 1}$ closes its step with a margin of exactly $n$, as [[the product of $(2k-1)/(2k)$|MC068WVGWS]] works out.

In the [[L-tromino tiling|EXRJ0JF2Q3]] of a $2^n \times 2^n$ board with one square removed, the strengthening is in the quantifier.
The claim "a corner square removed" is too weak, since the step produces quarters with a missing square near the center; the claim "any one square removed" carries itself.

An exact value can be a strengthening of a vague claim.
Induction on "$1 + 3 + \cdots + (2n - 1)$ is a perfect square" stalls, while induction on "it equals $n^2$" is the short proof of [[the sum of the first $n$ odd numbers|QSWRESJAZ4]].
The proof of [[strong induction|0KMVFSHFGZ]] from ordinary induction is a fourth case: it carries "$P(k)$ for every $k < n$" instead of $P(n)$.

### What it is not

A [[direct induction on the bound 2|MZXYW75TC3]] uses the claim itself as its hypothesis, so it is not the method, and its step cannot be completed.
Weakening the claim is not the method either: a weaker hypothesis gives less to work with, so the step only gets harder.
A strengthening must also be true, so $\sum_{k=1}^n 1/k^2 \le 2 - \tfrac2n$ is no help: at $n = 1$ it says $1 \le 0$.

### Watch out

The first error is a false $Q$.
It looks strong enough for the step, but the base case or a small case fails, so always test $Q$ on a table first.
The second error is to prove $Q(n)$ and forget the last implication $Q(n) \Rightarrow P(n)$; with $2 - \tfrac1n$ it uses $\tfrac1n > 0$, and that line must be written.
The third error is to strengthen only the conclusion of the step and still assume $P(n)$.
The induction must assume $Q(n)$; otherwise the step is harder than before.

### History

Pólya describes the inventor's paradox in *How to Solve It*: the more general problem may be the easier one to solve.
The exact value of $\sum_{k \ge 1} 1/k^2$, which is $\pi^2/6$, is the answer to the [[Basel problem|0DMY75D6FV]], and the bound $2$ from the strengthened induction is a standard first estimate of it.

### Try it

First, plain induction on $\sum_{k=1}^n \tfrac{1}{k(k+1)} < 1$ stalls; which stronger claim works?
The exact value $1 - \tfrac{1}{n+1}$ works, since $1 - \tfrac{1}{n+1} + \tfrac{1}{(n+1)(n+2)} = 1 - \tfrac{1}{n+2}$.

Second, the claim $S_n \le 2 - \tfrac{1}{n+1}$ for $S_n = \sum_{k=1}^n 1/k^2$ is true, since it follows from $S_n \le 2 - \tfrac1n$; can induction prove it directly?
No: the step would need $\tfrac{1}{(n+1)^2} \le \tfrac{1}{n+1} - \tfrac{1}{n+2} = \tfrac{1}{(n+1)(n+2)}$, which is false, so a strengthening must be strong enough, not only true.

## Explanations

### L1 human

Sometimes a small promise is hard to keep step by step, and a bigger promise is easier.
Suppose we must show that a pile of sand never reaches $2$ kilograms while we keep adding smaller and smaller spoonfuls.
Knowing only "less than $2$ so far" does not tell us that the next spoonful is safe.
If we know "at most $2$ kilograms minus the size of the last spoonful", then each new spoonful fits into the gap that is left.
So we prove the bigger promise, and the small promise follows from it.

### L2 human

We prove that $1 + 3 + 5 + \cdots + (2n - 1)$ is a perfect square for each $n \ge 1$.
Try plain induction first: suppose the sum up to $2n - 1$ is $m^2$ for some integer $m$.
The next sum is $m^2 + 2n + 1$, and we know nothing that links $m$ and $n$, so we cannot say that it is a square.

The step stalls for lack of information, so we compute small cases: the sums for $n = 1, 2, 3, 4$ are $1, 4, 9, 16$.
That suggests $Q(n)$: the sum equals $n^2$.
The base case is $1 = 1^2$, and the step is
$$n^2 + (2n + 1) = (n + 1)^2.$$
So $Q(n)$ holds for every $n \ge 1$, and $Q(n)$ implies the claim, with $m = n$.

The method is the standard move for an inequality or a divisibility claim whose step needs a little more than the claim gives.
Watch out: guess $Q$ from a table and test it before you start, because a false $Q$ wastes the whole proof.

### L3 human

Induction proves exactly the properties that the successor step preserves, and a true property need not be preserved.
Every true $P$ has a preserved strengthening, for example "$P(k)$ for all $k \le n$", but that one helps only when the step can use earlier cases.
In general, finding a preserved strengthening is the same task as finding an invariant, and in program verification a loop invariant is a strengthened induction hypothesis on the number of iterations.

Proof assistants make the point sharp: an induction in Lean often fails until the user generalizes the goal, for example by reverting a variable so that the hypothesis holds for all its values.
In arithmetic where induction is allowed only for simple formulas, the needed strengthening may lie outside the allowed class; such questions belong to mathematical logic.
Among the induction methods, [[double induction|AABX4YPKRR]] strengthens to "for all values of the second variable", and [[forward-backward induction|QC9FKGZH1V]] and [[induction on size|B2D8PTFNN1]] often need a loaded hypothesis too.
