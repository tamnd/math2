---
tag: 87JHX7WQMR
kind: example
name: A locally constant function on a disconnected set need not be constant
msc: ["00A35", "54D05"]
topics: [MEKKHHQTKB]
audience: ug2
not_instance_of:
  - target: 1JJCDJB7FM
    note: the set where the property holds is non-empty, open and closed, but the space is not connected, so the argument gives no conclusion
uses: [1JJCDJB7FM, N4GYVPPVX2, 0V032VWTHD, DQ4E55T3BW]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Locally_constant_function
    locator: lead section
---

## Example

Let $X = (0, 1) \cup (2, 3)$, with the topology of a subspace of $\mathbb{R}$.
Define $f \colon X \to \mathbb{R}$ by $f(x) = 0$ for $x \in (0, 1)$ and $f(x) = 1$ for $x \in (2, 3)$.
A student tries to prove that $f$ is constant by the [[open-closed argument|1JJCDJB7FM]], with $S = \{ x \in X : f(x) = f(\tfrac12) \}$.

1. $f$ is [[locally constant|N4GYVPPVX2]]: a point $x \in (0, 1)$ has the neighbourhood $(0, 1)$, and a point $x \in (2, 3)$ has the neighbourhood $(2, 3)$. Both sets are open in $X$, and $f$ is constant on each.
2. Non-empty: $\tfrac12 \in S$.
3. Open: $S = (0, 1)$, and $(0, 1)$ is open in $\mathbb{R}$, so it is open in $X$.
4. Closed: $X \setminus S = (2, 3)$ is open in $X$, so $S$ is closed in $X$.
5. So $S$ is a non-empty [[clopen set|DQ4E55T3BW]] of $X$. But $S \neq X$, because $f(\tfrac52) = 1 \neq 0$.
6. The argument fails at its last step. That step needs $X$ to be [[connected|0V032VWTHD]], and $X$ is not connected: steps 3 and 4 show that $(0, 1)$ and $(2, 3)$ split $X$ into two disjoint non-empty open sets.

## Remarks

1. The three local facts (non-empty, open, closed) are all true here. The example shows that the global conclusion comes from connectedness, not from the local facts.
2. Step 4 shows a common surprise: $(0, 1)$ is closed in $X$ although it is not closed in $\mathbb{R}$. Closedness in the open-closed argument is always closedness relative to the space $X$.
3. If we join the two intervals, for example $X' = (0, 3)$, then a locally constant function on $X'$ is constant, by [[the example on connected spaces|4NTM65AY4F]].
4. The same failure occurs for the function $\operatorname{sgn}(x) = x / \lvert x \rvert$ on $\mathbb{R} \setminus \{0\}$. Its derivative is $0$ at every point of its domain, and it is not constant.
5. In general, a locally constant function is constant on each connected component, and it can take a different value on each component.

## Explanations

### L1 human

Picture two islands with no bridge between them.
On the first island every house is painted red, and on the second island every house is painted blue.
Near each house all the houses have the same colour.
But the whole country does not have one colour, because the two islands do not touch.
The open-closed argument works only when the space is one piece.

### L2 human

We see the same failure in a derivative test.

1. Let $g(x) = \arctan x + \arctan(1/x)$ for $x \neq 0$.
2. For $x \neq 0$, $g'(x) = \frac{1}{1 + x^2} + \frac{1}{1 + 1/x^2} \cdot \left( -\frac{1}{x^2} \right) = \frac{1}{1 + x^2} - \frac{1}{x^2 + 1} = 0$.
3. So $g$ is locally constant on $\mathbb{R} \setminus \{0\}$, by the mean value theorem on small intervals.
4. At $x = 1$, $g(1) = \frac{\pi}{4} + \frac{\pi}{4} = \frac{\pi}{2}$. At $x = -1$, $g(-1) = -\frac{\pi}{4} - \frac{\pi}{4} = -\frac{\pi}{2}$.
5. So $g$ is not constant. It equals $\frac{\pi}{2}$ on $(0, \infty)$ and $-\frac{\pi}{2}$ on $(-\infty, 0)$, one value on each component.

The typical use of this non-example is a check before a proof: verify that the domain is connected.
A trap is the formula $\arctan x + \arctan(1/x) = \frac{\pi}{2}$, written for all $x \neq 0$, which is false for negative $x$.
