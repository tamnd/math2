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

Let $X = (0, 1) \cup (2, 3)$, a subspace of $\mathbb{R}$.
Define $f \colon X \to \mathbb{R}$ by $f(x) = 0$ on $(0, 1)$ and $f(x) = 1$ on $(2, 3)$.
A student tries to prove that $f$ is constant by the [[open-closed argument|1JJCDJB7FM]], with $S = \{ x \in X : f(x) = f(\tfrac12) \}$.

1. $f$ is [[locally constant|N4GYVPPVX2]]: each point has the neighborhood $(0, 1)$ or $(2, 3)$, open in $X$, on which $f$ is constant.
2. Non-empty: $\tfrac12 \in S$.
3. Open: $S = (0, 1)$, which is open in $\mathbb{R}$ and so in $X$.
4. Closed: $X \setminus S = (2, 3)$ is open in $X$, so $S$ is closed in $X$.
5. So $S$ is a non-empty [[clopen set|DQ4E55T3BW]] of $X$, yet $S \neq X$, since $f(\tfrac52) = 1$.
6. The argument fails at its last step, which needs $X$ to be [[connected|0V032VWTHD]].
   Steps 3 and 4 show that $(0, 1)$ and $(2, 3)$ split $X$ into two disjoint non-empty open sets.

## Remarks

The three local facts are all true here, so the global conclusion comes from connectedness and from nothing else.
Step 4 shows a common surprise: $(0, 1)$ is closed in $X$ although it is not closed in $\mathbb{R}$.
Closedness in the open-closed argument always means closedness relative to $X$.

Join the two pieces, as in $X' = (0, 3)$, and every locally constant function becomes constant, by [[the example on connected spaces|4NTM65AY4F]].
In general a locally constant function is constant on each connected component and can take a different value on each.
The sign function $x / \lvert x \rvert$ on $\mathbb{R} \setminus \{0\}$ fails in the same way: its derivative is $0$ everywhere on its domain, and it is not constant.

## Explanations

### L1 human

Picture two islands with no bridge between them.
On the first island every house is red, and on the second every house is blue.
Near each house, all the houses have the same color.
But the whole country does not have one color, because the two islands do not touch.
The open-closed argument works only when the space is one piece.

### L2 human

We see the same failure in a derivative test.

1. Let $g(x) = \arctan x + \arctan(1/x)$ for $x \neq 0$.
2. For $x \neq 0$, $g'(x) = \frac{1}{1 + x^2} + \frac{1}{1 + 1/x^2} \cdot \left( -\frac{1}{x^2} \right) = \frac{1}{1 + x^2} - \frac{1}{x^2 + 1} = 0$.
3. So $g$ is locally constant on $\mathbb{R} \setminus \{0\}$, by the mean value theorem on small intervals.
4. But $g(1) = \frac{\pi}{4} + \frac{\pi}{4} = \frac{\pi}{2}$ and $g(-1) = -\frac{\pi}{2}$.
5. So $g$ equals $\frac{\pi}{2}$ on $(0, \infty)$ and $-\frac{\pi}{2}$ on $(-\infty, 0)$, one value on each component.

Before an open-closed proof, check that the domain is connected.
Watch out for the formula $\arctan x + \arctan(1/x) = \frac{\pi}{2}$ written for all $x \neq 0$: it is false for negative $x$.
