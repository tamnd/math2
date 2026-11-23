---
tag: 4NTM65AY4F
kind: example
name: A locally constant function on a connected space is constant
msc: ["00A35", "54D05"]
topics: [MEKKHHQTKB]
audience: ug2
instance_of: [1JJCDJB7FM]
uses: [1JJCDJB7FM, N4GYVPPVX2, 0V032VWTHD, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_constant_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: lead section
---

## Example

Let $X$ be a non-empty [[connected space|0V032VWTHD]], let $Y$ be a set, and let $f \colon X \to Y$ be [[locally constant|N4GYVPPVX2]].
So each $x \in X$ has an open [[neighborhood|0ZCY0Z80B6]] $V_x$ on which $f$ takes only the value $f(x)$.
We prove by the [[open-closed argument|1JJCDJB7FM]] that $f$ is constant.

1. Fix $x_0 \in X$, and let $S = \{ x \in X : f(x) = f(x_0) \}$.
2. Non-empty: $x_0 \in S$.
3. Open: for $x \in S$, every $y \in V_x$ has $f(y) = f(x) = f(x_0)$, so $V_x \subseteq S$.
4. Closed: for $x \notin S$, every $y \in V_x$ has $f(y) = f(x) \neq f(x_0)$, so $V_x \subseteq X \setminus S$, and the complement of $S$ is open.
5. So $S$ is clopen, and a connected space has no clopen subsets except $\varnothing$ and $X$.
6. Since $S \neq \varnothing$, $S = X$, and $f$ is constant.

## Remarks

The proof uses no topology on $Y$, only the local constancy of $f$ and the connectedness of $X$.
The open step and the closed step use the same neighborhoods $V_x$, which is typical when the property is "equal to a fixed value".

Two common corollaries follow.
A continuous $g \colon X \to \mathbb{Z}$ is locally constant, since near $x$ continuity gives $\lvert g(y) - g(x) \rvert < \tfrac12$, so it is constant on a connected $X$.
On a connected open subset of $\mathbb{R}^n$, a differentiable function with zero gradient is locally constant by the [[mean value theorem|0BARQY52N5]] on small balls, and so constant.
On a disconnected space the conclusion fails, as [[the example on two intervals|87JHX7WQMR]] shows.

## Explanations

### L1 human

Suppose a map is painted so that the color does not change around any point.
If the map is one piece, with no gaps, then the whole map has one color.
Start from one point and look at all the points of the same color.
Near each of them the color stays the same, and near each point of another color it also stays the same.
So the regions of different colors cannot touch, and since the map is one piece, there is only one region.

### L2 human

We apply the example to the number of roots of a family of quadratics.

1. For $t \in (-1, 1)$, let $p_t(x) = x^2 - 2tx - 1$, with discriminant $4t^2 + 4 > 0$ and roots $r_\pm(t) = t \pm \sqrt{t^2 + 1}$.
2. Let $N(t)$ be the number of roots of $p_t$ in $(-2, 2)$.
3. A root can leave $(-2, 2)$ only through $\pm 2$, and $p_t(2) = 3 - 4t$ and $p_t(-2) = 3 + 4t$ are positive for $\lvert t \rvert < \tfrac34$.
4. On $(-\tfrac34, \tfrac34)$ the roots move continuously and never equal $\pm 2$, so $N$ is locally constant, and the interval is connected, so $N$ is constant.
5. At $t = 0$ the roots are $\pm 1$, so $N(t) = 2$ for all $\lvert t \rvert < \tfrac34$.

The method shows that an integer invariant, such as a number of roots, a degree or an index, does not change along a connected family.
Watch out: step 3 is essential, since at $t = \tfrac34$ the root $r_+$ reaches $2$, and for $t$ slightly above $\tfrac34$, $N(t) = 1$.
