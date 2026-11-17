---
tag: NDYRDNFXRR
kind: example
name: Cauchy's sum theorem and the hidden lemma of uniform convergence
msc: ["00A35", "40A30"]
topics: [X1NSTVGDNQ]
audience: research
instance_of: [79P9CTRN0V]
uses: [79P9CTRN0V, 0GFGK40582, 08VZ57PT26, 0X9XT05JVC, VXV7M0QDH6]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: History
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: Method
---

## Example

Primitive conjecture: if each function $u_n \colon [0, 1] \to \mathbb{R}$ is continuous and the series $s(x) = \sum_{n=0}^{\infty} u_n(x)$ converges for each $x$, then $s$ is continuous.
This is the claim that Cauchy published in 1821.
We follow the [[method of proofs and refutations|79P9CTRN0V]].

1. Proof. Write $s_N = \sum_{n=0}^{N} u_n$, a finite sum of continuous functions, so $s_N$ is continuous. Fix $a \in [0, 1]$ and $\varepsilon > 0$. For $x$ near $a$,
$$|s(x) - s(a)| \leq |s(x) - s_N(x)| + |s_N(x) - s_N(a)| + |s_N(a) - s(a)|.$$
Choose $N$ so large that the third term is less than $\frac{\varepsilon}{3}$, and then $\delta > 0$ so that the second term is less than $\frac{\varepsilon}{3}$ for $|x - a| < \delta$.
The proof then says that the first term is also less than $\frac{\varepsilon}{3}$.
2. Global counterexample. Let $u_n(x) = x(1 - x)^n$. Each $u_n$ is a polynomial, so it is continuous.
3. The partial sums. For $0 < x \leq 1$ the geometric sum gives $s_N(x) = x \cdot \frac{1 - (1 - x)^{N + 1}}{1 - (1 - x)} = 1 - (1 - x)^{N + 1}$. For $x = 0$ each term is $0$, and the formula $1 - (1 - 0)^{N + 1} = 0$ also holds.
4. The sum. For $0 < x \leq 1$ we have $0 \leq 1 - x < 1$, so $(1 - x)^{N + 1} \to 0$ and $s(x) = 1$. For $x = 0$, $s(0) = 0$.
5. So $s$ is $0$ at $0$ and $1$ on $(0, 1]$. It is not continuous at $0$, and the conjecture is false.
6. Proof analysis. At $a = 0$ the first term of step 1 is $|s(x) - s_N(x)| = (1 - x)^{N + 1}$ for $x \in (0, 1]$. For a fixed $N$, this tends to $1$ as $x \to 0$, so no $\delta$ makes it less than $\frac{\varepsilon}{3}$ when $\varepsilon < 3$. The guilty lemma: "one $N$ makes $|s(x) - s_N(x)|$ small for all $x$ near $a$ at once."
7. Lemma-incorporation. The improved theorem adds the guilty lemma as a hypothesis: $\sup_{x \in [0, 1]} |s(x) - s_N(x)| \to 0$ as $N \to \infty$. This hypothesis is [[uniform convergence|08VZ57PT26]], and the improved theorem is the [[uniform limit theorem|0X9XT05JVC]].

## Remarks

The counterexample converges [[pointwise|0GFGK40582]] but not uniformly: $\sup_{x \in [0, 1]} (1 - x)^{N + 1} = 1$ for each $N$.
On an interval $[c, 1]$ with $c > 0$, the series converges uniformly, since $(1 - x)^{N + 1} \leq (1 - c)^{N + 1} \to 0$; so the sum is continuous there, as the improved theorem predicts.
The proof in step 1 is the [[epsilon over three argument|VXV7M0QDH6]], and the first of its three estimates is the place where uniformity is needed.
Abel's counterexample of 1826 was a Fourier series: $\sum_{n=1}^{\infty} (-1)^{n + 1} \frac{\sin nx}{n}$ equals $\frac{x}{2}$ for $-\pi < x < \pi$ and $0$ at $x = \pi$, so its sum jumps at $\pi$.
Seidel and Stokes found the hidden condition independently, and Weierstrass introduced the German name "gleichmäßig konvergent" for it.
Lakatos uses this history as a further case study of proof-generated concepts.

## Explanations

### L1 human

Cauchy believed that adding up infinitely many smooth, unbroken curves always gives an unbroken curve.
The sum of the curves $x(1 - x)^n$ is $1$ everywhere except at $x = 0$, where it is $0$: the sum jumps.
Cauchy's argument was right in every step but one.
That step assumed that the partial sums approach the total at the same speed everywhere.
Near $x = 0$ they approach it more and more slowly.
The repair is to ask for the same speed everywhere, and this condition is called uniform convergence.

### L2 human

We measure the failure of uniformity at a point near $0$.

1. Take $N = 10$ and $x = 0.01$. Then $s(x) - s_{10}(x) = (0.99)^{11} \approx 0.895$.
2. Take $N = 100$ and $x = 0.001$. Then $(0.999)^{101} \approx 0.904$.
3. For each $N$, the point $x = \frac{1}{N + 1}$ gives $\left(1 - \frac{1}{N + 1}\right)^{N + 1}$, which increases to $\frac{1}{e} \approx 0.368$ and is at least $\frac{1}{4}$ for $N \geq 1$.
4. So $\sup_x |s(x) - s_N(x)| \geq \frac{1}{4}$ for each $N \geq 1$, and the convergence is not uniform.

The typical use: to find the guilty lemma, compute the term of the proof that the counterexample makes large.

A trap: pointwise convergence at each point does not bound the error near the point; the proof must control a neighbourhood, not only the point.
