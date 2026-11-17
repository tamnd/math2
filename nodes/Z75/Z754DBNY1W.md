---
tag: Z754DBNY1W
kind: example
name: Bar recursion along a continuous functional
msc: ["03F10", "03D65"]
topics: [8XY7JYZKFW]
audience: research
instance_of: [8CCG6F2FAT]
uses: [8CCG6F2FAT, 0M4JJT780X, P2WS16HKD7]
sources:
  - url: https://en.wikipedia.org/wiki/Bar_recursion
    locator: Technical definition
---

## Example

Let $Y(\alpha) = \alpha(\alpha(0)) + 1$ on sequences of numbers.
$Y$ is continuous: its value depends only on $\alpha(0)$ and on $\alpha(\alpha(0))$.
We find the lengths at which the [[bar recursion|8CCG6F2FAT]] stops along each sequence $\alpha$, that is, the least $k$ with $Y(\widehat{\bar \alpha k}) < k$.
Let $a = \alpha(0)$ and $b = \alpha(1)$, and let $s = \bar \alpha k$.

1. $k = 0$: $\hat s$ is the zero sequence, so $Y(\hat s) = 0 + 1 = 1$, and $1 < 0$ fails.
2. $k = 1$: $\hat s = a, 0, 0, \ldots$. If $a = 0$, then $\hat s(a) = a = 0$; if $a \ge 1$, then $\hat s(a) = 0$. So $Y(\hat s) = 1$ and $1 < 1$ fails.
3. $k = 2$ and $a \ne 1$: $\hat s(a) = 0$, since $a = 0$ gives $\hat s(0) = 0$ and $a \ge 2$ lies beyond $s$. So $Y(\hat s) = 1 < 2$, and the recursion stops.
4. $k \ge 2$ and $a = 1$: $\hat s(1) = b$, so $Y(\hat s) = b + 1$, and the condition is $b + 1 < k$.
5. So for $a = 1$ the recursion stops at $k = \max(2, b + 2)$.

So the recursion stops at length $2$ if $\alpha(0) \ne 1$, and at length $\max(2, \alpha(1) + 2)$ if $\alpha(0) = 1$.

## Remarks

The stopping length is not the modulus of [[continuity|0M4JJT780X]] of $Y$ at $\alpha$.
For $a = 5$, $Y(\alpha)$ depends on $\alpha(5)$, so the modulus at $\alpha$ is $6$, but the recursion stops at length $2$.
The zero extension decides there: $\hat s(5) = 0$, and the test $1 < 2$ passes without reading $\alpha(5)$.
For $a = 1$ and $b = 9$, the modulus is $2$, but the recursion runs to length $11$, because the condition also needs $|s| > Y(\alpha)$.
So the stopping point can come before or after the modulus.

## Explanations

### L1 human

The judge $Y$ reads the first entry $a$ of the list, then reads entry number $a$, and adds $1$.
Missing entries count as $0$.
If $a$ is not $1$, then entry $a$ is $0$ or missing at length $2$, so the judge answers $1$ and the list of length $2$ is long enough.
If $a = 1$, the judge reads entry $1$, say $b$, and the list must grow until it has more than $b + 1$ entries.

### L2 human

We run three sequences.

1. $\alpha = 0, 7, 7, \ldots$: here $a = 0$, so the recursion stops at length $2$.
2. $\alpha = 1, 0, 3, \ldots$: here $a = 1$ and $b = 0$, so it stops at $\max(2, 2) = 2$.
3. $\alpha = 1, 4, \ldots$: here $b = 4$, so it stops at length $6$.

The typical use is to see the stopping condition of bar recursion at work on a functional that reads values at data-dependent places.
A trap is to stop when $Y$ has read all the entries it needs; the condition $Y(\hat s) < |s|$ is a different test.
