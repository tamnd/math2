---
tag: 4D9HP5TS6W
kind: example
name: Minkowski question-mark function
msc: [26A30, 11A55]
instance_of: [P5AWRD2793]
uses: [0BK6JBK58W, 05GZ11PWRY]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%27s_question-mark_function
---

## Example

Every irrational $x \in (0, 1)$ has a unique infinite [[continued fraction|0BK6JBK58W]] expansion $x = [0; a_1, a_2, a_3, \dots]$ with positive integers $a_k$.
The question-mark function $? \colon [0, 1] \to [0, 1]$ is defined at such $x$ by
$$?(x) = 2 \sum_{k=1}^{\infty} (-1)^{k+1} \, 2^{-(a_1 + a_2 + \cdots + a_k)}.$$
For a rational $x = [0; a_1, \dots, a_n]$ the same formula with a finite sum is used, and $?(0) = 0$.
The value does not depend on which of the two finite expansions of a rational is chosen.
For example, $\frac12 = [0; 2] = [0; 1, 1]$ gives $2 \cdot 2^{-2} = \frac12$ and $2(2^{-1} - 2^{-2}) = \frac12$.

Some values: $?(1) = 1$, $?(\frac13) = 2 \cdot 2^{-3} = \frac14$, and for $x = [0; 1, 1, 1, \dots] = (\sqrt5 - 1)/2$ the geometric series gives $?(x) = 2 \cdot \frac{1/2}{1 + 1/2} = \frac23$.

The function $?$ is continuous and strictly increasing, so it is a [[homeomorphism|05GZ11PWRY]] of $[0, 1]$ onto itself.
Its derivative exists and equals $0$ at almost every point of $[0, 1]$.
So $?$ is a [[singular function|P5AWRD2793]].
Unlike the [[Cantor function|NPBYYK63FE]], it is strictly increasing, so it is constant on no interval.

The function maps the rationals of $[0, 1]$ onto the dyadic rationals $m/2^n$ of $[0, 1]$.
It maps the quadratic irrationals of $(0, 1)$ onto the rationals that are not dyadic.

## Explanations

### L1 human

The question-mark function reads the continued fraction of a number and turns it into a binary expansion: each partial quotient becomes a run of equal binary digits.
The first run has length $a_1 - 1$, and the $k$-th run has length $a_k$ for $k \ge 2$.
It is a continuous, strictly increasing function that still has slope zero almost everywhere.
This shows that a function can climb steadily from $0$ to $1$ while being flat in the sense of derivatives almost everywhere.
