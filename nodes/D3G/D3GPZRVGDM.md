---
tag: D3GPZRVGDM
kind: example
name: The square function is continuous but not uniformly continuous on R
msc: ["03B10", "26A15"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [0FYQMKFE77]
uses: [0FYQMKFE77, 0X3WGX95FE, 0M4JJT780X]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let $f \colon \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$.
Let $C(a, \varepsilon, \delta)$ be the predicate $\forall x \in \mathbb{R} \; \bigl( |x - a| < \delta \to |x^2 - a^2| < \varepsilon \bigr)$.
[[Continuity|0X3WGX95FE]] on $\mathbb{R}$ is $\forall a \; \forall \varepsilon > 0 \; \exists \delta > 0 \; C(a, \varepsilon, \delta)$.
[[Uniform continuity|0M4JJT780X]] is $\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall a \; C(a, \varepsilon, \delta)$.
We show that the first statement is true and the second is false.

1. Continuity: let $a \in \mathbb{R}$ and $\varepsilon > 0$, and put $\delta = \min\bigl(1, \frac{\varepsilon}{2|a| + 1}\bigr)$, which depends on $a$ and $\varepsilon$.
2. Let $|x - a| < \delta$.
   Then $|x - a| < 1$, so by the triangle inequality $|x + a| \leq |x - a| + 2|a| < 1 + 2|a|$.
3. So $|x^2 - a^2| = |x - a| \, |x + a| < \delta (2|a| + 1) \leq \varepsilon$.
   This proves $C(a, \varepsilon, \delta)$, so $f$ is continuous.
4. Uniform continuity fails: take $\varepsilon = 1$, and let $\delta > 0$ be arbitrary.
   We find $a$ and $x$ with $|x - a| < \delta$ and $|x^2 - a^2| \geq 1$.
5. Put $a = \frac{1}{\delta}$ and $x = a + \frac{\delta}{2}$, so that $|x - a| = \frac{\delta}{2} < \delta$.
6. Then $x^2 - a^2 = (x - a)(x + a) = \frac{\delta}{2} \bigl( \frac{2}{\delta} + \frac{\delta}{2} \bigr) = 1 + \frac{\delta^2}{4} > 1$.
7. So no $\delta$ works for all $a$ when $\varepsilon = 1$, and $f$ is not uniformly continuous on $\mathbb{R}$.

## Remarks

The order $\forall a \, \forall \varepsilon \, \exists \delta$ is weaker than the order $\forall \varepsilon \, \exists \delta \, \forall a$.
The $\delta$ of step 1 shrinks as $|a|$ grows, and step 5 uses this: for large $a$ the graph is steep, and a fixed $\delta$ is too large.
On the interval $[0, 1]$ the order can be exchanged, because $|x^2 - a^2| = |x - a| \, |x + a| \leq 2 |x - a|$ there, so $\delta = \frac{\varepsilon}{2}$ works for all $a \in [0, 1]$.
This agrees with the theorem that [[continuous functions on a closed bounded interval are uniformly continuous|0W0TZDRF9C]].
Concluding uniform continuity from continuity is an instance of the [[quantifier shift fallacy|CRW82NARQV]].

## Explanations

### L1 human

The graph of $x^2$ gets steeper and steeper as $x$ grows.
Near $x = 1$, moving $x$ by $0.1$ changes $x^2$ by about $0.2$.
Near $x = 100$, the same move of $0.1$ changes $x^2$ by about $20$.
So the allowed distance depends on where we are on the graph.
No single distance works everywhere at once.

### L2 human

To decide whether a function is uniformly continuous, ask whether the $\delta$ of continuity can be chosen without the point $a$.
First compute $|f(x) - f(a)|$ and factor out $|x - a|$: here $|x^2 - a^2| = |x - a| \, |x + a|$.
Then look at the other factor: here $|x + a|$ is about $2|a|$, so it has no bound on $\mathbb{R}$.
An unbounded factor suggests that $\delta$ must depend on $a$, and a pair of points as in steps 5 and 6 confirms it.
For $f(x) = 3x + 1$ the other factor is the constant $3$, and $\delta = \frac{\varepsilon}{3}$ works for every $a$, so $f$ is uniformly continuous.
Watch out: a proof of continuity with a formula for $\delta$ that contains $a$ does not show uniform continuity.
