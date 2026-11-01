---
tag: KDT3E0VE0K
kind: statement
role: theorem
name: Jordan decomposition of a function of bounded variation
msc: [26A45, 26A48]
uses: [A8251BHCMP, 8QA5DEWNYD, 0WFF6AZPBP]
about: [A8251BHCMP]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_variation
---

## Statement

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
Then $f$ has [[bounded variation|A8251BHCMP]] on $[a, b]$ if and only if there are nondecreasing functions $g, h \colon [a, b] \to \R$ with $f = g - h$.
Moreover, when $f$ has bounded variation, one can take $g(x) = V_a^x(f)$ and $h(x) = V_a^x(f) - f(x)$, where $V_a^x(f)$ is the [[total variation|8QA5DEWNYD]] of $f$ on $[a, x]$ and $V_a^a(f) = 0$.

## Remarks

A nondecreasing function has bounded variation, and a difference of two functions of bounded variation has bounded variation, which gives one direction.
For the other direction, $g(x) = V_a^x(f)$ is nondecreasing because variation is additive over adjacent intervals.
For $x < y$ one has $f(y) - f(x) \le \abs{f(y) - f(x)} \le V_x^y(f) = g(y) - g(x)$, so $h = g - f$ is nondecreasing too.
For example, $f(x) = \sin x$ on $[0, 2\pi]$ is the difference of $g(x) = V_0^x(\sin)$ and $g - \sin$.
The decomposition is not unique: one may add the same nondecreasing function to $g$ and to $h$.

## Explanations

### L1 human

A function of bounded variation may go up and down, but it can always be split into a part that only goes up and a part that only goes down.
This reduces many questions about such functions to [[monotone functions|0WFF6AZPBP]], which are much easier to handle.

### L2 human

With the decomposition, results about monotone functions pass to functions of bounded variation.
By [[Lebesgue's theorem on monotone functions|1Y4N1DDQNR]], a function of bounded variation is differentiable almost everywhere.
It also has one-sided limits at every point and at most countably many discontinuities.
The theorem is the one-variable model of the Jordan decomposition of a signed measure.
