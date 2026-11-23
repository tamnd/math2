---
tag: YRZQ86RKYY
kind: example
name: Testing a boundedness argument on 1/x
msc: ["00A35", "26A15"]
topics: [STSM6PR7TX]
audience: ug2
instance_of: [4M98ZZNK0E]
uses: [4M98ZZNK0E, 0ATVXC3NCC, 0P27W9RW0G, 07PFYV65MB, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: lead section
---

## Example

The statement is the [[boundedness theorem|0ATVXC3NCC]] on $[0, 1]$: every [[continuous|0P27W9RW0G]] function $f \colon [0, 1] \to \mathbb{R}$ is bounded.
The statement is true, and a student hands in the following proof, which has a gap.

> (P1) Let $f \colon [0, 1] \to \mathbb{R}$ be continuous, and let $x \in [0, 1]$.
> (P2) By continuity at $x$ with $\varepsilon = 1$, there is $\delta_x > 0$ such that $\lvert f(y) - f(x) \rvert < 1$ for all $y \in [0, 1]$ with $\lvert y - x \rvert < \delta_x$.
> (P3) For these $y$ we get $\lvert f(y) \rvert < \lvert f(x) \rvert + 1$.
> (P4) So $f$ is bounded near each point, and hence $f$ is bounded on $[0, 1]$.

We check it by the method of [[checking a proof|4M98ZZNK0E]].
Line (P2) is the definition of continuity at $x$ with $\varepsilon = 1$, and line (P3) follows from the [[triangle inequality|03HF5PMY5T]], since $\lvert f(y) \rvert \le \lvert f(y) - f(x) \rvert + \lvert f(x) \rvert$.
The hypotheses are continuity and the domain $[0, 1]$, and continuity is used in (P2), but no line uses that the domain is closed.

So we run the argument where the domain is not closed and the conclusion fails: $g(x) = 1/x$ on $(0, 1]$, which is continuous there.
Line (P2) holds at each $x \in (0, 1]$, and (P3) holds with the bound $1/x + 1$.
The first half of (P4), "bounded near each point", also holds.
But $g$ is not bounded, since $g(1/n) = n$ for every positive integer $n$.
So the step from "bounded near each point" to "bounded" fails for $g$, and it must use some property of $[0, 1]$ that $(0, 1]$ lacks and that the proof never states.
The verdict: the first three lines are correct, and (P4) has a serious gap.

## Remarks

The repair uses the [[Heine-Borel theorem|07PFYV65MB]].
The open intervals $(x - \delta_x, x + \delta_x)$ for $x \in [0, 1]$ cover $[0, 1]$, so finitely many of them, with centers $x_1, \dots, x_m$, already cover it.
Every $y \in [0, 1]$ lies in one of these, and (P3) gives $\lvert f(y) \rvert < \max_i \lvert f(x_i) \rvert + 1$, a bound that does not depend on $y$.

The test case shows why the repair is needed.
If finitely many of the intervals covered $(0, 1]$ for $g$, the same argument would bound $g$, which is false, so no finite family of them covers $(0, 1]$.
In general, an argument that would also prove a false statement contains an error, and the error is in a step that should use the missing hypothesis.

## Explanations

### L1 human

The claim is that a function with no jumps on the interval from $0$ to $1$, ends included, cannot grow without limit.
The student argues that near each point the function stays close to its value there, so it cannot grow without limit anywhere.
To check this, we try the same argument on $1/x$ on the interval from $0$ to $1$ with the end $0$ left out.
Each step still works for $1/x$, but $1/x$ grows without limit near $0$: at $x = 0.001$ it equals $1000$.
So the argument is missing something, namely a reason that uses the end point $0$.

### L2 human

The check follows a pattern that fits many proofs in analysis.
List the hypotheses, here continuity and the closed bounded domain, and find where each is used: continuity in (P2), the domain nowhere.
Find a standard example where the unused hypothesis fails and the conclusion fails, here $1/x$ on $(0, 1]$.
Run the proof on it and find the first false line, here the second half of (P4).
Repair that line with a result that uses the hypothesis, such as the Heine-Borel theorem or a bisection argument.

The pattern suits any proof that passes from a local property to a global one.
Watch out: the words "by compactness" alone do not repair the gap, and the repair must say which finite cover is used and how it gives one bound.
