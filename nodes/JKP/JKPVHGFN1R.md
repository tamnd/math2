---
tag: JKPVHGFN1R
kind: example
name: The epsilon over three argument fails for x^n on [0, 1]
msc: ["00A35", "40A30"]
topics: [MEKKHHQTKB]
audience: ug2
not_instance_of:
  - target: VXV7M0QDH6
    note: the convergence is only pointwise, so no single index makes the two outer terms small at all points near 1
uses: [VXV7M0QDH6, 056FSKG32J, 0YSRR1JTKZ, 0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pointwise_convergence
    locator: lead section
---

## Example

Let $f_n(x) = x^n$ on $[0, 1]$.
The sequence converges [[pointwise|056FSKG32J]] to $f$, where $f(x) = 0$ for $0 \le x < 1$ and $f(1) = 1$.
Each $f_n$ is continuous, yet $f$ is not [[continuous at|0EEE2CZB2A]] $1$, as [[x^n converges pointwise but not uniformly on [0, 1]|0YSRR1JTKZ]] proves.
We try the [[epsilon over three argument|VXV7M0QDH6]] at $c = 1$ with $\varepsilon = \frac12$, and find the step where it breaks.

1. The chain is $\lvert f(x) - f(1) \rvert \le \lvert f(x) - f_N(x) \rvert + \lvert f_N(x) - f_N(1) \rvert + \lvert f_N(1) - f(1) \rvert$.
2. The third term is $\lvert 1 - 1 \rvert = 0$ for every $N$.
3. For $0 \le x < 1$ the first term is $x^N$ and the middle term is $1 - x^N$.
4. So the first two terms add up to exactly $1$ at each $x < 1$, for each $N$, and they cannot both be less than $\frac16$.
5. The method needs one $N$ with $x^N < \frac16$ at all $x$ near $1$.
   For each fixed $N$, $x^N \to 1$ as $x \to 1$, so no such $N$ exists, and this is the step that breaks.
6. At a single point an index exists, but it depends on the point.
   The smallest $N$ with $x^N < \frac16$ is $18$ for $x = 0.9$, $179$ for $x = 0.99$ and $1791$ for $x = 0.999$.
7. If $N$ is chosen after $x$, the function in the middle term is not fixed, and the $\delta$ from the continuity of $f_N$ depends on $x$, which is not a valid choice.

So the argument is not an instance of the method, and its conclusion is false: $\lvert f(x) - f(1) \rvert = 1$ for every $x < 1$.

## Remarks

The failure is local.
On $[0, b]$ with $b < 1$, $\sup_{0 \le x \le b} x^n = b^n \to 0$, so the convergence is uniform there.
At each point $c < 1$ the method works on the neighborhood $[0, b]$ with $c < b < 1$, and $f$ is continuous at $c$.
The method needs uniform convergence only near the point.

The broken step is the choice of $N$, not the triangle inequality.
The inequality of step 1 is true, but its right side is never small.
The same test applies to any pointwise limit: compute $\sup_x \lvert f_N(x) - f(x) \rvert$ over $x$ near the point, and if it does not tend to $0$, no single $N$ makes the outer terms small.

## Explanations

### L1 human

The functions $x^n$ are a bridge from $f(x)$ to $f(1)$ that does not hold.
For $x$ a little below $1$, the power $x^n$ is close to $0$ only when $n$ is very large, and how large depends on how close $x$ is to $1$.
For any fixed $n$, the points close enough to $1$ have $x^n$ close to $1$, far from the limit value $0$.
So one function of the sequence cannot be close to the limit at all the points the argument needs.

### L2 human

We test the step "choose $N$" with the numbers of step 6.

1. For $x = 0.9$ we need $N \ge 18$, since $0.9^{17} \approx 0.1668$ and $0.9^{18} \approx 0.150$.
2. Fix $N = 18$.
   At $x = 0.99$ the first term is $0.99^{18} \approx 0.835$, far above $\frac16$.
3. Each larger $N$ fails in the same way at a point closer to $1$: for $N = 1791$, the point $x = 0.9999$ gives $x^N \approx 0.836$.

Use this test to decide whether the epsilon over three argument applies to a pointwise limit.
Watch out: checking the outer terms only at $c$ hides the failure, because $f_N(1) = f(1)$ for every $N$, and the problem shows only at the nearby points $x$.
