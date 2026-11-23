---
tag: WT1CMRARAY
kind: example
name: Translation is not continuous in L-infinity
msc: ["00A35", "46E30"]
topics: [MEKKHHQTKB]
audience: grad
not_instance_of:
  - target: J2J35J3055
    note: the continuous functions with compact support are not dense in L-infinity, so the claim does not pass from them to all bounded functions
uses: [J2J35J3055, EPP5T6MSD5, SASP14MA1Z, WPC2XRMB9Y, 0RCQZ36MME]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
    locator: lead section
---

## Example

Let $f = \mathbf{1}_{[0, 1]}$, the [[indicator function|0RCQZ36MME]] of $[0, 1]$, as an element of [[$L^\infty(\mathbb{R})$|SASP14MA1Z]], whose norm is the [[essential supremum|WPC2XRMB9Y]].
We show that $\lVert \tau_h f - f \rVert_\infty = 1$ for $0 < \lvert h \rvert < 1$, so translation is not continuous at $f$.
Then we find where the [[density argument|J2J35J3055]] of [[the case p < infinity|EPP5T6MSD5]] breaks.

1. Let $0 < h < 1$, so $\tau_h f(x) = f(x - h) = \mathbf{1}_{[h, 1 + h]}(x)$.
2. For $x \in [0, h)$, $f(x) = 1$ and $\tau_h f(x) = 0$, and this set has measure $h > 0$, so the essential supremum of $\lvert \tau_h f - f \rvert$ is at least $1$.
3. A difference of two indicators takes only the values $-1$, $0$ and $1$, so $\lVert \tau_h f - f \rVert_\infty = 1$.
4. For $-1 < h < 0$, the same computation on $(1 + h, 1]$ gives $1$ again, so the norm does not tend to $0$.

The first ingredient of the density argument still holds.
For $g \in C_c(\mathbb{R})$, uniform continuity gives $\lVert \tau_h g - g \rVert_\infty = \sup_x \lvert g(x - h) - g(x) \rvert \to 0$.
The second ingredient fails: no continuous $g$ has $\lVert f - g \rVert_\infty < \frac12$.

5. Suppose $g$ is continuous and $c = \lVert f - g \rVert_\infty < \frac12$.
6. Then $\lvert g(x) \rvert \le c$ for almost every $x \in (-1, 0)$, where $f = 0$, and by continuity $g(0) \le c$.
7. Also $g(x) \ge 1 - c$ for almost every $x \in (0, 1)$, where $f = 1$, so $g(0) \ge 1 - c$.
8. Then $1 - c \le c$, so $c \ge \frac12$, a contradiction.

So $C_c(\mathbb{R})$ is not dense in $L^\infty(\mathbb{R})$, and the density argument fails at its second ingredient.

## Remarks

The example shows that "the class is dense" cannot be dropped.
The special case holds, the bound $\lVert \tau_h u \rVert_\infty = \lVert u \rVert_\infty$ holds, and the conclusion is still false.
The closure of $C_c(\mathbb{R})$ in $L^\infty(\mathbb{R})$ is $C_0(\mathbb{R})$, the continuous functions that tend to $0$ at infinity, and on this closed subspace translation is continuous.
For a bounded uniformly continuous $f$, $\lVert \tau_h f - f \rVert_\infty \to 0$ as well; the jumps of $\mathbf{1}_{[0, 1]}$ at $0$ and $1$ are what break continuity.

For $p < \infty$ the same $f$ behaves well.
The difference $\tau_h f - f$ is nonzero on a set of measure $2 \lvert h \rvert$ when $\lvert h \rvert < 1$, so $\lVert \tau_h f - f \rVert_p = (2 \lvert h \rvert)^{1/p} \to 0$.

## Explanations

### L1 human

Take a step: a function that is $1$ on an interval and $0$ outside it.
Slide it a little to the right.
The $L^\infty$ norm looks at the largest gap between the old and the new graph.
Near the jump, one graph is at height $1$ and the other at height $0$, so the largest gap is $1$, however small the slide.
The $L^1$ norm looks at the area between the graphs, and that area is small for a small slide.

### L2 human

We compare the two norms for $h = 0.1$.

1. $\tau_{0.1} f = \mathbf{1}_{[0.1, 1.1]}$, and $f = \mathbf{1}_{[0, 1]}$.
2. The two functions differ on $[0, 0.1)$ and on $(1, 1.1]$, by $1$ in absolute value.
3. So $\lVert \tau_{0.1} f - f \rVert_1 = 0.1 + 0.1 = 0.2 = 2 \cdot 0.1$.
4. And $\lVert \tau_{0.1} f - f \rVert_\infty = 1$, by steps 2 and 3 of the example.

Before a density argument, check that the class is dense in the norm of the claim.
Watch out: continuous functions are dense in $L^p$ for $p < \infty$, but not in $L^\infty$.
