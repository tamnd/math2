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
The statement is true.
A student hands in the following proof.

> (P1) Let $f \colon [0, 1] \to \mathbb{R}$ be continuous, and let $x \in [0, 1]$.
> (P2) By continuity at $x$ with $\varepsilon = 1$, there is $\delta_x > 0$ such that $\lvert f(y) - f(x) \rvert < 1$ for all $y \in [0, 1]$ with $\lvert y - x \rvert < \delta_x$.
> (P3) For these $y$ we get $\lvert f(y) \rvert < \lvert f(x) \rvert + 1$.
> (P4) So $f$ is bounded near each point, and hence $f$ is bounded on $[0, 1]$.

We check the proof by the method of [[checking a proof|4M98ZZNK0E]].

1. Line (P2) is the definition of continuity at $x$, applied with $\varepsilon = 1$. It is correct.
2. Line (P3) follows from the [[triangle inequality|03HF5PMY5T]]: $\lvert f(y) \rvert \le \lvert f(y) - f(x) \rvert + \lvert f(x) \rvert < 1 + \lvert f(x) \rvert$. It is correct.
3. The hypotheses are "$f$ is continuous" and "the domain is $[0, 1]$". The proof uses continuity in (P2), but no line uses that the domain is closed.
4. So we run the argument on a case where the domain is not closed and the conclusion fails. Take $g(x) = 1/x$ on $(0, 1]$, which is continuous there.
5. For $g$, line (P2) holds at each $x \in (0, 1]$, because $g$ is continuous at $x$. Line (P3) holds with the bound $1/x + 1$.
6. The first half of (P4), "bounded near each point", also holds for $g$. But $g$ is not bounded on $(0, 1]$, because $g(1/n) = n$ for each positive integer $n$.
7. So the step from "bounded near each point" to "bounded" fails for $g$. The same step must therefore use a property of $[0, 1]$ that $(0, 1]$ lacks, and the proof does not state it.
8. The verdict: the proof has a serious gap in (P4). The first three lines are correct.

## Remarks

1. The repair uses the [[Heine-Borel theorem|07PFYV65MB]]. The open intervals $(x - \delta_x, x + \delta_x)$, for $x \in [0, 1]$, cover $[0, 1]$, so finitely many of them, with centres $x_1, \dots, x_m$, already cover $[0, 1]$.
2. Then each $y \in [0, 1]$ lies in one of these intervals, and (P3) gives $\lvert f(y) \rvert < \max_i \lvert f(x_i) \rvert + 1$. This is a bound that does not depend on $y$.
3. The test case also shows why the repair is needed. If finitely many of the intervals covered $(0, 1]$ for $g$, then the same argument would bound $g$, which is false. So for $(0, 1]$ no finite family of these intervals covers the set.
4. The example shows the general rule of the method. An argument that would also prove a false statement contains an error. The error lies in a step that should use the missing hypothesis.

## Explanations

### L1 human

The claim is that a function with no jumps on the interval from $0$ to $1$, ends included, cannot grow without limit.
The student argues: near each point the function stays close to its value there, so it cannot grow without limit anywhere.
To check this, we try the same argument on $1/x$ on the interval from $0$ to $1$ with the end $0$ left out.
Each step of the argument still works for $1/x$, but $1/x$ grows without limit near $0$: at $x = 0.001$ it equals $1000$.
So the argument is missing something, namely a reason that uses the end point $0$.

### L2 human

The check has a fixed pattern, which applies to many proofs in analysis.

1. List the hypotheses: continuity, and the closed and bounded domain.
2. Find where each hypothesis is used: continuity in (P2), the domain nowhere.
3. Find a standard example where the unused hypothesis fails and the conclusion fails: $1/x$ on $(0, 1]$.
4. Run the proof on the example, and find the first false line: the second half of (P4).
5. Repair that line with a result that uses the hypothesis: the Heine-Borel theorem, or a bisection argument.

The typical use of this pattern is the check of a proof that passes from a local property to a global property.
A trap is to repair the gap by the words "by compactness" with no further step.
The repair must say which finite cover is used and how it gives one bound.
