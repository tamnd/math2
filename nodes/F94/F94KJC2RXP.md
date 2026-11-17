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

Strengthening the induction hypothesis is a method for a claim $P(n)$ whose [[induction|0ASJVEFA9J]] step cannot be proved from $P(n)$ alone.
We choose a statement $Q(n)$ that implies $P(n)$ for each $n$, and we prove $Q(n)$ for all $n$ by induction instead.
The base case $Q(n_0)$ must be true, and the step from $Q(n)$ to $Q(n + 1)$ must be provable.
The method works because a [[stronger statement|KCK4AQ469Q]] gives a stronger hypothesis in the step, and this can outweigh the stronger conclusion that the step must reach.
The method matters because it turns many inductions that stall into short proofs, and finding the right $Q$ is often the main idea of the proof.

## Motivation

Take the claim that $\sum_{k=1}^n 1/k^2 < 2$ for every $n \ge 1$.
In the step we know only that the sum up to $n$ is less than $2$, and we add the positive number $1/(n+1)^2$.
A number below $2$ plus a positive number can be $2$ or more, so the step does not follow.
The trouble is that the hypothesis "less than $2$" gives no room for the new term.
The stronger claim $\sum_{k=1}^n 1/k^2 \le 2 - 1/n$ keeps a gap of $1/n$, and the new term fits into this gap.
So the stronger claim has an easy step, and it implies the weaker claim at once.

## Notation

1. We write $P(n)$ for the claim and $Q(n)$ for the strengthened claim. The condition "$Q(n)$ implies $P(n)$" must hold for each $n$.
2. Pólya calls this effect the inventor's paradox: a more general problem can be easier to solve than a special one.
3. Books also say "load the induction hypothesis" or "prove a more general statement".

## Remarks

### The steps of the method

1. Try the plain induction on $P(n)$, and find the place where the step fails.
2. Ask what the step needs: a sharper bound, an extra property, or a statement for all values of a second variable.
3. Write $Q(n)$ as $P(n)$ plus what the step needs.
4. Check that $Q(n)$ is true for small $n$, by computation. A false $Q$ cannot be proved.
5. Prove $Q(n_0)$ and the step from $Q(n)$ to $Q(n + 1)$.
6. Deduce $P(n)$ from $Q(n)$.

### Examples

1. [[The sum of 1/k² is at most 2 − 1/n|DFVCKA01PN]]: the bound $2 - 1/n$ replaces the bound $2$, and the step reduces to $1/(n + 1)^2 \le 1/(n(n + 1))$.
2. [[The product of (2k − 1)/(2k) is at most 1/√(3n + 1)|MC068WVGWS]]: the plain bound $1/\sqrt{3n}$ fails in the step, but the sharper bound $1/\sqrt{3n + 1}$ goes through.
3. The [[L-tromino tiling|EXRJ0JF2Q3]] of a $2^n \times 2^n$ board with one square removed: the claim for a removed corner square is too weak, because the step needs smaller boards with a square removed near the centre. The induction works for "any one square removed".
4. Exact formulas: $1 + 3 + \cdots + (2n - 1)$ is a perfect square. Induction on "is a perfect square" stalls, and induction on the exact value $n^2$ works.
5. The proof of [[strong induction|0KMVFSHFGZ]] from ordinary induction carries the claim "$P(k)$ for all $k < n$" instead of $P(n)$. This is the same idea.

### Non-examples

1. [[A direct induction on the bound 2 for the sum of 1/k²|MZXYW75TC3]]: the hypothesis $S_n < 2$ is used as it stands, and the step cannot be completed.
2. Replacing $P(n)$ by a weaker claim makes the step no easier. A weaker hypothesis gives less to work with.
3. The strengthened claim $\sum_{k=1}^n 1/k^2 \le 2 - 2/n$ is false already at $n = 1$, where it says $1 \le 0$. A strengthening that is false is not a proof method.

### Basic properties

1. If $Q(n)$ implies $P(n)$ for each $n$, and $Q(n)$ holds for each $n$, then $P(n)$ holds for each $n$. This is the whole logic of the method.
2. A strengthening cannot be too strong: it must be true. So the method needs a sharp guess, often found by computing small cases.
3. A stronger $Q$ makes the conclusion of the step harder and the hypothesis of the step easier. The method succeeds when the second effect wins.
4. Strong induction is ordinary induction applied to the strengthening $Q(n)$: "$P(k)$ holds for all $k \le n$".

### History

Pólya discusses the inventor's paradox in *How to Solve It*: a more general problem can be easier to solve than the special problem.
The bound $\sum_{k=1}^n 1/k^2 \le 2 - 1/n$ is a standard exercise in textbooks of proof, and the exact value of the infinite sum, $\pi^2/6$, is the answer to the [[Basel problem|0DMY75D6FV]].

### Common errors

1. The student strengthens the claim to a false statement. Then the base case or a small case fails. Always check small cases first.
2. The student proves $Q(n)$ but forgets to show that $Q(n)$ implies $P(n)$.
3. The student strengthens only the conclusion of the step and not the hypothesis. The induction must assume $Q(n)$, not $P(n)$.

## Explanations

### L1 human

Sometimes a small promise is hard to keep step by step, and a bigger promise is easier.
Suppose that we must show that a pile of sand never reaches $2$ kilograms, while we keep adding smaller and smaller spoonfuls.
Knowing only "less than $2$ so far" does not tell us that the next spoonful is safe.
If we know "at most $2$ kilograms minus the size of the last spoonful", then each new spoonful fits into the gap that is left.
So we prove the bigger promise, and the small promise follows from it.

### L2 human

We prove that $1 + 3 + 5 + \cdots + (2n - 1)$ is a perfect square for each $n \ge 1$.

1. Plain induction: suppose that $1 + 3 + \cdots + (2n - 1) = m^2$ for some integer $m$. Then the next sum is $m^2 + 2n + 1$.
2. We cannot say that $m^2 + 2n + 1$ is a square, because we know nothing linking $m$ and $n$. The step stalls.
3. Small cases: the sums for $n = 1, 2, 3, 4$ are $1, 4, 9, 16$. So we guess $Q(n)$: the sum equals $n^2$.
4. Base: for $n = 1$ the sum is $1 = 1^2$.
5. Step: if the sum up to $2n - 1$ is $n^2$, then the sum up to $2n + 1$ is $n^2 + 2n + 1 = (n + 1)^2$.
6. So $Q(n)$ holds for all $n \ge 1$, and $Q(n)$ implies the claim.

The typical use of the method is an inequality or a divisibility claim where the step needs a little more room than the claim gives.
A trap is to guess $Q$ without testing it: a false $Q$ wastes the whole proof.

### L3 human

The method reflects the fact that induction proves exactly the properties that are preserved by the successor step, and a property that is true need not be preserved.
Every true $P$ has a strengthening that is preserved, for example "$P(k)$ holds for all $k \le n$", but this one helps only when the step can use earlier cases.
Finding a preserved strengthening is the same task as finding an invariant.
In program verification, a loop invariant is a strengthened induction hypothesis for the number of iterations.
Proof assistants often fail on an induction until the user generalizes the goal.
In arithmetic with induction only for simple formulas, a needed strengthening may lie outside the allowed formulas; these questions belong to mathematical logic.
The related pages are [[double induction|AABX4YPKRR]], where the strengthening is "for all values of the second variable", and [[structural induction|12MQ2NJ29A]].
