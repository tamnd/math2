---
tag: ZSJCMR4A04
kind: statement
role: proposition
name: Quantitative Ryser conjecture
sources:
  - wikipedia: en:82859189@r1369844038
    locator: Ryser's conjecture on circulant Hadamard matrices, section Quantitative Ryser conjecture
    note: adopted
    mention: wikipedia://en/82859189#G14P
    sections: [Statement]
inventory: [2RGTKVQ7XP]
---

## Statement

In 2024, Stefan Steinerberger proposed the quantitative Ryser conjecture, a strengthened form of the circulant Hadamard conjecture. It asserts that there is an absolute constant $\varepsilon_0>0$ such that, for every $n>4$ and every Littlewood polynomial

$$P(z)=\sum_{k=0}^{n-1}a_kz^k,\qquad a_k\in\{-1,1\},$$

one has

$$\max_{0\leq j<n} \left| \left|P\!\left(e^{2\pi i j/n}\right)\right|-\sqrt n \right| \geq\varepsilon_0 n^{1/4}.$$

Steinerberger called this formulation *ultra-flat at roots of unity*.

If $A=\operatorname{circ}(a_0,\ldots,a_{n-1})$, its singular values are the numbers $|P(e^{2\pi i j/n})|$. Thus the conjecture is equivalently the spectral-gap assertion

$$\max_{1\leq j\leq n} \left|\sigma_j(A)-\sqrt n\right| \geq\varepsilon_0n^{1/4},$$

where $\sigma_1(A),\ldots,\sigma_n(A)$ are the singular values of $A$. The ordinary Ryser conjecture says only that the left-hand side is nonzero; the quantitative version predicts a universal gap of order $n^{1/4}$.

The exponent $1/4$ would be optimal up to logarithmic factors. When $n$ is prime, probabilistic modifications of the [[Legendre symbol|01J8AMV9RS]] give circulant sign matrices satisfying

$$\max_{0\leq j<n} \left| \left|P\!\left(e^{2\pi i j/n}\right)\right|-\sqrt n \right| =O\!\left(n^{1/4}\sqrt{\log n}\right).$$

Consequently, the power of $n$ in the conjectured lower bound cannot in general be increased beyond $1/4$.
