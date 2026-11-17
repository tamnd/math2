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
We use the fact that $C_c(\mathbb{R})$, the continuous functions that vanish outside a bounded interval, is dense in $L^p(\mathbb{R})$ for $1 \le p < \infty$.

1. Let $g \in C_c(\mathbb{R})$ with $g(x) = 0$ for $\lvert x \rvert > R$. Let $\eta > 0$.
2. The function $g$ is continuous and vanishes outside the compact set $[-R, R]$, so $g$ is uniformly continuous on $\mathbb{R}$, by the [[Heine-Cantor theorem|06B8BNJCD6]] on $[-R - 1, R + 1]$.
3. So there is $\delta$ with $0 < \delta \le 1$ such that $\lvert g(x - h) - g(x) \rvert < \eta$ for each $x$ and each $\lvert h \rvert < \delta$.
4. For $\lvert h \rvert < \delta \le 1$, the function $\tau_h g - g$ vanishes outside $[-R - 1, R + 1]$, an interval of length $2R + 2$.
5. Hence $\lVert \tau_h g - g \rVert_p^p = \int_{-R-1}^{R+1} \lvert g(x - h) - g(x) \rvert^p \, dx \le \eta^p (2R + 2)$. So $\lVert \tau_h g - g \rVert_p \le \eta (2R + 2)^{1/p}$.
6. Since $\eta$ was arbitrary, $\lVert \tau_h g - g \rVert_p \to 0$. The claim holds on the dense class $C_c(\mathbb{R})$.
7. Now let $f \in L^p(\mathbb{R})$ and $\varepsilon > 0$. Choose $g \in C_c(\mathbb{R})$ with $\lVert f - g \rVert_p < \varepsilon / 3$, by density.
8. [[Lebesgue measure|2Z2QVWZ262]] is invariant under translation, so $\lVert \tau_h u \rVert_p = \lVert u \rVert_p$ for each $u \in L^p$. With $u = f - g$, this gives $\lVert \tau_h f - \tau_h g \rVert_p = \lVert f - g \rVert_p < \varepsilon / 3$.
9. By step 6, there is $\delta' > 0$ with $\lVert \tau_h g - g \rVert_p < \varepsilon / 3$ for $\lvert h \rvert < \delta'$.
10. For $\lvert h \rvert < \delta'$, the [[Minkowski inequality|N4QZS912MT]] gives
$$\lVert \tau_h f - f \rVert_p \le \lVert \tau_h f - \tau_h g \rVert_p + \lVert \tau_h g - g \rVert_p + \lVert g - f \rVert_p < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
11. So $\lVert \tau_h f - f \rVert_p \to 0$ as $h \to 0$.

## Remarks

1. Steps 7 to 10 are an [[epsilon over three argument|VXV7M0QDH6]]: the first and the third terms are small by density, and the middle term is small by the special case.
2. Step 8 is where the argument uses a uniform bound: each $\tau_h$ is an isometry of $L^p$, so the error of the approximation does not grow under translation.
3. The hypothesis $p < \infty$ enters only through the density of $C_c(\mathbb{R})$. For $p = \infty$ this density fails, and the claim fails too, as shown in [[translation is not continuous in L-infinity|WT1CMRARAY]].
4. The same proof works in $\mathbb{R}^n$ with $C_c(\mathbb{R}^n)$, and on the circle with continuous periodic functions.
5. The result is used to prove that the convolution of $f \in L^p$ with an [[approximate identity|CDYXTW3PJF]] converges to $f$ in $L^p$.

## Explanations

### L1 human

Take the graph of a function and slide it a little to the right.
If the graph is a smooth hill, the slid graph is almost the same as the old one, and the area between the two graphs is small.
A general function can be very rough, so this is not clear for it.
But each rough function is close to a smooth hill shape.
Slide the hill, and add the two small errors of the approximation: the total difference is still small.

### L2 human

We compute $\lVert \tau_h g - g \rVert_1$ for a concrete function in $C_c(\mathbb{R})$.

1. Let $g(x) = \max(0, 1 - \lvert x \rvert)$, the tent function on $[-1, 1]$. It is continuous and vanishes for $\lvert x \rvert \ge 1$.
2. The function $g$ is Lipschitz with constant $1$, so $\lvert g(x - h) - g(x) \rvert \le \lvert h \rvert$ for each $x$.
3. For $\lvert h \rvert \le 1$, the difference vanishes outside $[-2, 2]$, an interval of length $4$.
4. So $\lVert \tau_h g - g \rVert_1 \le 4 \lvert h \rvert$, which tends to $0$ as $h \to 0$.

The typical use of the pattern is to pass a continuity property of a group action (here translation) from nice functions to all of $L^p$.
A trap is to approximate $f$ by a $g$ that depends on $h$: the function $g$ must be fixed before $h$ is chosen, or step 9 gives no single $\delta'$.
