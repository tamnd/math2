---
tag: 40JPQXGYXQ
kind: statement
role: proposition
name: The Routh criterion
sources:
  - wikipedia: en:16187387@r1339524459
    locator: Derivation of the Routh array, section The Routh criterion
    note: adopted
    mention: wikipedia://en/16187387#4LA5
    sections: [Statement]
inventory: [G649D94KYD]
---

## Statement

To derive Routh's criterion, first we'll use a different notation to differentiate between the even and odd terms of $f(x)$:

$$f(x) = a_0x^n + b_0x^{n-1} + a_1x^{n-2} + b_1x^{n-3} + \cdots \quad (20)$$

Now we have:

$$\begin{aligned} f(j\omega) & = a_0(j\omega)^n+b_0(j\omega)^{n-1}+a_1(j\omega)^{n-2}+b_1(j\omega)^{n-3}+\cdots & {} \quad (21)\\ & = a_0(j\omega)^n+a_1(j\omega)^{n-2}+a_2(j\omega)^{n-4}+\cdots & {} \quad (22)\\ & + b_0(j\omega)^{n-1}+b_1(j\omega)^{n-3}+b_2(j\omega)^{n-5}+\cdots \\ \end{aligned}$$

Therefore, if $n$ is even,

$$\begin{aligned} f(j\omega) & = (-1)^{n/2}\big[a_0\omega^n-a_1\omega^{n-2}+a_2\omega^{n-4}-\cdots \big] & {} \quad (23)\\ & + j(-1)^{(n/2)-1}\big[b_0\omega^{n-1}-b_1\omega^{n-3}+b_2\omega^{n-5}-\cdots \big] & {} \\ \end{aligned}$$

and if $n$ is odd:

$$\begin{aligned} f(j\omega) & = j(-1)^{(n-1)/2}\big[a_0\omega^n-a_1\omega^{n-2}+a_2\omega^{n-4}-\cdots \big] & {} \quad (24)\\ & + (-1)^{(n-1)/2}\big[b_0\omega^{n-1}-b_1\omega^{n-3}+b_2\omega^{n-5}-\cdots \big] & {}\\ \end{aligned}$$

Now observe that if $n$ is an odd integer, then by (3) $N+P$ is odd. If $N+P$ is an odd integer, then $N-P$ is odd as well. Similarly, this same argument shows that when $n$ is even, $N-P$ will be even. Equation (15) shows that if $N-P$ is even, $\theta$ is an integer multiple of $\pi$. Therefore, $\tan(\theta)$ is defined for $n$ even, and is thus the proper index to use when n is even, and similarly $\tan(\theta') = \tan(\theta+\pi) = -\cot(\theta)$ is defined for $n$ odd, making it the proper index in this latter case.

Thus, from (6) and (23), for $n$ even:

$$\Delta = I_{-\infty}^{+\infty}\frac{-\mathfrak{Im}[f(x)]}{\mathfrak{Re}[f(x)]}= I_{-\infty}^{+\infty}\frac{b_0\omega^{n-1}-b_1\omega^{n-3}+\cdots}{a_0\omega^n-a_1\omega^{n-2}+\ldots} \quad (25)$$

and from (19) and (24), for $n$ odd:

$$\Delta = I_{-\infty}^{+\infty}\frac{\mathfrak{Re}[f(x)]}{\mathfrak{Im}[f(x)]}= I_{-\infty}^{+\infty}\frac{b_0\omega^{n-1}-b_1\omega^{n-3}+\ldots}{a_0\omega^n-a_1\omega^{n-2}+\ldots} \quad (26)$$

Lo and behold we are evaluating the same Cauchy index for both: $\Delta = I_{-\infty}^{+\infty}\frac{b_0\omega^{n-1}-b_1\omega^{n-3}+\ldots}{a_0\omega^n-a_1\omega^{n-2}+\ldots} \quad (27)$
