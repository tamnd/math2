---
tag: 2BZ4WGH7C3
kind: example
name: For 1/x on (0, 1) the delta of continuity depends on the point
msc: ["00A35", "26A15"]
topics: [T6QQ749DM5]
audience: ug1
instance_of: [CRW82NARQV]
uses: [CRW82NARQV, 0X3WGX95FE, 0M4JJT780X]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Examples and nonexamples
---

## Example

Let $f(x) = \frac{1}{x}$ on the interval $(0, 1)$.
Here is a student's argument; one step is wrong, so find it before reading on.

1. The function $f$ is [[continuous|0X3WGX95FE]] at each point $a \in (0, 1)$.
2. So for each $\varepsilon > 0$ we can choose $\delta > 0$ such that $|x - a| < \delta$ gives $|f(x) - f(a)| < \varepsilon$.
3. So $f$ is [[uniformly continuous|0M4JJT780X]] on $(0, 1)$.

Steps 1 and 2 are true, and step 3 is false.
Step 1 holds with $\delta = \min\left(\frac{a}{2}, \frac{\varepsilon a^2}{2}\right)$: if $|x - a| < \delta$, then $x > \frac{a}{2}$, so $\left|\frac{1}{x} - \frac{1}{a}\right| = \frac{|x - a|}{xa} < \frac{\delta}{a^2/2} \le \varepsilon$.
This $\delta$ depends on $a$, and it shrinks to $0$ as $a \to 0$.
Step 2 is continuity, "$\forall a \, \forall \varepsilon \, \exists \delta$", while uniform continuity says "$\forall \varepsilon \, \exists \delta \, \forall a$", one $\delta$ for every point.
So step 3 moves $\forall a$ past $\exists \delta$, which is the [[quantifier shift fallacy|CRW82NARQV]].

The correct statement is that $f$ is continuous on $(0, 1)$ but not uniformly continuous, and we prove the second half.

1. Take $\varepsilon = 1$ and suppose that some $\delta > 0$ works at every point.
2. A smaller $\delta$ then works too, so we may assume $\delta < 1$.
3. Let $a = \frac{\delta}{2}$ and $x = \frac{\delta}{4}$, both in $(0, 1)$, so $|x - a| = \frac{\delta}{4} < \delta$.
4. But $|f(x) - f(a)| = \frac{4}{\delta} - \frac{2}{\delta} = \frac{2}{\delta} > 1$, a contradiction.

## Remarks

On a shorter interval $[c, 1)$ with $0 < c < 1$ the shift becomes true.
There $xa \ge c^2$, so $\delta = \varepsilon c^2$ works at every point, and $f$ is uniformly continuous.
So the failure on $(0, 1)$ comes from the steep growth of $f$ near the missing end point $0$.

## Explanations

### L1 human

The graph of $\frac{1}{x}$ gets steeper and steeper as $x$ gets close to $0$.
Near $x = 0.5$, a small move of $x$ changes $\frac{1}{x}$ a little.
Near $x = 0.001$, the same small move changes $\frac{1}{x}$ a lot.
So the size of a safe move depends on where we stand, and no single size is safe everywhere.

### L2 human

We compute the largest $\delta$ that works at $a$ for $\varepsilon = 1$.
Points to the left of $a$ are the binding ones, because $\frac{1}{x} - \frac{1}{a}$ grows as $x$ decreases.
So we need $\frac{1}{a - \delta} - \frac{1}{a} \le 1$, that is, $\frac{\delta}{a(a - \delta)} \le 1$.
This rearranges to $\delta \le a^2 - a\delta$, that is, $\delta \le \frac{a^2}{1 + a}$.
At $a = 0.5$ the bound is $\frac{0.25}{1.5} \approx 0.167$, and at $a = 0.01$ it is $\frac{0.0001}{1.01} \approx 0.000099$.
The bound tends to $0$ as $a \to 0$, so no positive $\delta$ works at every point.

The typical use of this computation is to see how $\delta$ depends on the point before claiming a uniform statement.
Watch out for a formula for $\delta$ in terms of $a$ and $\varepsilon$ whose $a$ is then forgotten.
