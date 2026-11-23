---
tag: EPP5T6MSD5
kind: example
name: Continuity of translation in Lp by a density argument
msc: ["00A35", "46E30"]
topics: [MEKKHHQTKB]
audience: grad
instance_of: [J2J35J3055]
uses: [J2J35J3055, VXV7M0QDH6, SASP14MA1Z, 06B8BNJCD6, N4QZS912MT, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dense_set
    locator: lead section
---

## Example

Let $1 \le p < \infty$, let $f \in L^p(\mathbb{R})$, and write $\tau_h f(x) = f(x - h)$.
We prove that $\lVert \tau_h f - f \rVert_p \to 0$ as $h \to 0$, by a [[density argument|J2J35J3055]] in [[$L^p(\mathbb{R})$|SASP14MA1Z]].
The dense class is $C_c(\mathbb{R})$, the continuous functions that vanish outside a bounded interval, which is dense in $L^p(\mathbb{R})$ for $1 \le p < \infty$.

First the claim on the dense class.
Let $g \in C_c(\mathbb{R})$ with $g(x) = 0$ for $\lvert x \rvert > R$, and let $\eta > 0$.
By the [[Heine-Cantor theorem|06B8BNJCD6]] on $[-R - 1, R + 1]$, and since $g$ vanishes outside $[-R, R]$, $g$ is uniformly continuous on $\mathbb{R}$.
So there is $\delta$ with $0 < \delta \le 1$ such that $\lvert g(x - h) - g(x) \rvert < \eta$ for every $x$ and every $\lvert h \rvert < \delta$.
For such $h$, the function $\tau_h g - g$ vanishes outside $[-R - 1, R + 1]$, an interval of length $2R + 2$.
Hence $\lVert \tau_h g - g \rVert_p \le \eta (2R + 2)^{1/p}$, and since $\eta$ was arbitrary, $\lVert \tau_h g - g \rVert_p \to 0$.

Then the passage to all of $L^p$.

1. Let $\varepsilon > 0$, and by density fix $g \in C_c(\mathbb{R})$ with $\lVert f - g \rVert_p < \varepsilon / 3$.
2. [[Lebesgue measure|2Z2QVWZ262]] is invariant under translation, so $\lVert \tau_h u \rVert_p = \lVert u \rVert_p$ for every $u \in L^p$.
   With $u = f - g$, this gives $\lVert \tau_h f - \tau_h g \rVert_p < \varepsilon / 3$.
3. By the claim on the dense class, there is $\delta' > 0$ with $\lVert \tau_h g - g \rVert_p < \varepsilon / 3$ for $\lvert h \rvert < \delta'$.
4. For $\lvert h \rvert < \delta'$, the [[Minkowski inequality|N4QZS912MT]] gives
   $$\lVert \tau_h f - f \rVert_p \le \lVert \tau_h f - \tau_h g \rVert_p + \lVert \tau_h g - g \rVert_p + \lVert g - f \rVert_p < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

## Remarks

Steps 7 to 10 are an [[epsilon over three argument|VXV7M0QDH6]]: the outer terms are small by density, and the middle term is small by the special case.
Step 8 supplies the bound that every density argument needs: each $\tau_h$ is an isometry of $L^p$, so the approximation error does not grow under translation.

The hypothesis $p < \infty$ enters only through the density of $C_c(\mathbb{R})$.
For $p = \infty$ that density fails, and so does the claim, as [[translation is not continuous in L-infinity|WT1CMRARAY]] shows.
The same proof works in $\mathbb{R}^n$ with $C_c(\mathbb{R}^n)$, and on the circle with continuous periodic functions.
The result is the main step in proving that the convolution of $f \in L^p$ with an [[approximate identity|CDYXTW3PJF]] converges to $f$ in $L^p$.

## Explanations

### L1 human

Take the graph of a function and slide it a little to the right.
If the graph is a smooth hill, the slid graph is almost the same as the old one, and the area between them is small.
A general function can be very rough, so this is not clear for it.
But each rough function is close to a smooth hill shape.
Slide the hill and add the two small errors of the approximation, and the total difference is still small.

### L2 human

We compute $\lVert \tau_h g - g \rVert_1$ for a concrete function in $C_c(\mathbb{R})$.

1. Let $g(x) = \max(0, 1 - \lvert x \rvert)$, the tent function on $[-1, 1]$.
2. The function $g$ is Lipschitz with constant $1$, so $\lvert g(x - h) - g(x) \rvert \le \lvert h \rvert$ for every $x$.
3. For $\lvert h \rvert \le 1$, the difference vanishes outside $[-2, 2]$, an interval of length $4$.
4. So $\lVert \tau_h g - g \rVert_1 \le 4 \lvert h \rvert$, which tends to $0$ as $h \to 0$.

The pattern passes a continuity property of a group action, here translation, from nice functions to all of $L^p$.
Watch out: $g$ must be fixed before $h$ is chosen, or step 3 gives no single $\delta'$.
