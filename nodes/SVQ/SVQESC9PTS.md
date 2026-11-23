---
tag: SVQESC9PTS
kind: example
name: The Riemann-Lebesgue lemma by a density argument
msc: ["00A35", "42A38"]
topics: [MEKKHHQTKB]
audience: grad
instance_of: [J2J35J3055]
uses: [J2J35J3055, WVKDC011KP, DWJF7ABPR1, 0AJXYH4DDQ, B6RYM7QTYZ, 0RCQZ36MME]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Lebesgue_lemma
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Lp_space
    locator: lead section
---

## Example

For $f \in L^1(\mathbb{R})$ and $\xi \in \mathbb{R}$, the Fourier transform is the [[Lebesgue integral|DWJF7ABPR1]]
$$\hat f(\xi) = \int_{\mathbb{R}} f(x) \, e^{-2\pi i x \xi} \, dx.$$
We prove the [[Riemann-Lebesgue lemma|WVKDC011KP]] in dimension one, $\hat f(\xi) \to 0$ as $\lvert \xi \rvert \to \infty$, by a [[density argument|J2J35J3055]] with the [[step functions|0AJXYH4DDQ]] as the dense class.

1. Let $f = \mathbf{1}_{[a, b]}$ be the [[indicator function|0RCQZ36MME]] of an interval with $a < b$, and let $\xi \neq 0$.
   Then
   $$\hat f(\xi) = \int_a^b e^{-2\pi i x \xi} \, dx = \frac{e^{-2\pi i b \xi} - e^{-2\pi i a \xi}}{-2\pi i \xi}.$$
2. Each exponential has absolute value $1$, so the numerator has absolute value at most $2$, and $\lvert \hat f(\xi) \rvert \le \frac{1}{\pi \lvert \xi \rvert}$.
3. A step function $s = \sum_{k=1}^{m} c_k \mathbf{1}_{[a_k, b_k]}$ has $\hat s(\xi) = \sum_k c_k \widehat{\mathbf{1}_{[a_k, b_k]}}(\xi)$, since the integral is linear.
4. By step 2, $\lvert \hat s(\xi) \rvert \le \frac{1}{\pi \lvert \xi \rvert} \sum_k \lvert c_k \rvert$, so the lemma holds on the dense class.
5. The property survives limits: for $f, g \in L^1(\mathbb{R})$ and every $\xi$, $\lvert \hat f(\xi) - \hat g(\xi) \rvert \le \int \lvert f - g \rvert = \lVert f - g \rVert_1$.
6. Let $f \in L^1(\mathbb{R})$ and $\varepsilon > 0$.
   Step functions are dense in $L^1(\mathbb{R})$, through the [[simple functions|B6RYM7QTYZ]], so there is a step function $s$ with $\lVert f - s \rVert_1 < \varepsilon / 2$.
7. By step 4, there is $R > 0$ with $\lvert \hat s(\xi) \rvert < \varepsilon / 2$ for every $\lvert \xi \rvert > R$.
8. For $\lvert \xi \rvert > R$, steps 5 and 7 give $\lvert \hat f(\xi) \rvert \le \lvert \hat f(\xi) - \hat s(\xi) \rvert + \lvert \hat s(\xi) \rvert < \varepsilon$.

Check: for $f = \mathbf{1}_{[-1/2, 1/2]}$, step 1 gives $\hat f(\xi) = \frac{\sin(\pi \xi)}{\pi \xi}$.
At $\xi = 10.5$, $\sin(10.5\pi) = 1$, so $\hat f(10.5) = \frac{1}{10.5 \pi} \approx 0.0303$, which equals the bound of step 2, so that bound is sharp.

## Remarks

Step 5 is the estimate that makes the method work.
The map $f \mapsto \hat f$ is linear and $\sup_\xi \lvert \hat f(\xi) \rvert \le \lVert f \rVert_1$, so a small change of $f$ in $L^1$ gives a small change of $\hat f$ at every $\xi$ at once.
The proof gives no rate of decay for a general $f$; only the dense class has the rate $1 / \lvert \xi \rvert$.

Other dense classes work too.
With $C_c^1(\mathbb{R})$, an integration by parts gives $\hat g(\xi) = \frac{1}{2\pi i \xi} \widehat{g'}(\xi)$, which tends to $0$.
The same three steps (compute on a dense class, find a uniform bound, approximate) prove the version for Fourier coefficients of an integrable function on $[0, 1]$.

## Explanations

### L1 human

A Fourier transform measures how much a function oscillates at each frequency.
For a block shape, the integral against a fast wave nearly cancels, because the positive and negative parts of the wave balance out.
A general function is not a block, but it is very close to a staircase of blocks.
The cancellation for the staircase, plus a small error, shows that the transform of the general function also goes to zero.

### L2 human

We compute the bound of step 4 for a concrete step function.

1. Let $s = 3 \cdot \mathbf{1}_{[0, 1]} - \mathbf{1}_{[1, 4]}$.
2. Step 4 gives $\lvert \hat s(\xi) \rvert \le \frac{3 + 1}{\pi \lvert \xi \rvert} = \frac{4}{\pi \lvert \xi \rvert}$.
3. For $\lvert \hat s(\xi) \rvert < 0.01$ it suffices that $\lvert \xi \rvert > \frac{400}{\pi} \approx 127.3$.
4. So $R = 128$ works in step 7 when $\varepsilon / 2 = 0.01$.

The pattern applies to any limit statement about a linear functional, such as an integral against an oscillating kernel.
Watch out: $R$ depends on the step function $s$, and $s$ depends on $\varepsilon$, so choose $s$ first.
