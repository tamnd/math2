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
A student argues as follows.

1. The function $f$ is [[continuous|0X3WGX95FE]] at each point $a \in (0, 1)$.
2. So for each $\varepsilon > 0$ we can choose $\delta > 0$ such that $|x - a| < \delta$ gives $|f(x) - f(a)| < \varepsilon$.
3. So $f$ is [[uniformly continuous|0M4JJT780X]] on $(0, 1)$.

We check the argument.

1. Step 1 is true. For $a \in (0, 1)$ and $\varepsilon > 0$, let $\delta = \min\left(\frac{a}{2}, \frac{\varepsilon a^2}{2}\right)$. If $|x - a| < \delta$ and $x \in (0, 1)$, then $x > \frac{a}{2}$, so $\left|\frac{1}{x} - \frac{1}{a}\right| = \frac{|x - a|}{xa} < \frac{\delta}{a^2/2} \le \varepsilon$.
2. The $\delta$ of step 1 depends on $a$, and it tends to $0$ as $a \to 0$.
3. Step 2 states continuity correctly, with "$\forall a \, \forall \varepsilon \, \exists \delta$". Uniform continuity needs "$\forall \varepsilon \, \exists \delta \, \forall a$", with one $\delta$ for all points.
4. So step 3 shifts the quantifier $\forall a$ past $\exists \delta$. This is the [[quantifier shift fallacy|CRW82NARQV]].
5. The conclusion is false. Take $\varepsilon = 1$ and any $\delta \in (0, 1)$. Let $a = \frac{\delta}{2}$ and $x = \frac{\delta}{4}$, both in $(0, 1)$.
6. Then $|x - a| = \frac{\delta}{4} < \delta$, but $|f(x) - f(a)| = \frac{4}{\delta} - \frac{2}{\delta} = \frac{2}{\delta} > 1$.
7. So no $\delta$ works for $\varepsilon = 1$ at all points, and $f$ is not uniformly continuous on $(0, 1)$.

## Remarks

The example shows the difference between "for each point a $\delta$" and "one $\delta$ for all points".
If the interval is changed to $[c, 1)$ with $0 < c < 1$, the choice $\delta = \varepsilon c^2$ works at every point, because $xa \ge c^2$ there.
Then $f$ is uniformly continuous, and the shift is valid on that interval.
The cause of the failure on $(0, 1)$ is the steep growth of $f$ near the missing end point $0$.

## Explanations

### L1 human

The graph of $\frac{1}{x}$ gets steeper and steeper as $x$ gets close to $0$.
Near $x = 0.5$, moving $x$ a little changes $\frac{1}{x}$ a little.
Near $x = 0.001$, the same small move changes $\frac{1}{x}$ by a lot.
So the size of a "safe" move depends on where we are, and no single size is safe everywhere.

### L2 human

We compute the largest $\delta$ that works at $a$ for $\varepsilon = 1$, approached from the left.

1. We need $\frac{1}{x} - \frac{1}{a} < 1$ for $a - \delta < x < a$. The left side increases as $x$ decreases.
2. So the condition is $\frac{1}{a - \delta} - \frac{1}{a} \le 1$, that is, $\frac{\delta}{a(a - \delta)} \le 1$.
3. This gives $\delta \le a^2 - a\delta$, so $\delta \le \frac{a^2}{1 + a}$.
4. At $a = 0.5$ this is $\frac{0.25}{1.5} \approx 0.167$, and at $a = 0.01$ it is $\frac{0.0001}{1.01} \approx 0.000099$.
5. The bound tends to $0$ as $a \to 0$, so no positive $\delta$ works for all $a$.

The typical use of this computation is to see how $\delta$ depends on the point before claiming a uniform statement.
A trap is to find a formula for $\delta$ in terms of $a$ and $\varepsilon$ and to forget that $a$ appears in it.
