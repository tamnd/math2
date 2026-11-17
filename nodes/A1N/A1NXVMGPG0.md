---
tag: A1NXVMGPG0
kind: example
name: Euler's evaluation of the Basel sum as plausible reasoning
msc: ["00A35", "11M06"]
topics: [DME0TPC348]
audience: ug2
instance_of: [8DHD3H1CJ9]
uses: [8DHD3H1CJ9, 0DMY75D6FV, 0XCYA4YERS]
sources:
  - url: https://en.wikipedia.org/wiki/Basel_problem
    locator: Euler's approach
  - url: https://en.wikipedia.org/wiki/Mathematics_and_Plausible_Reasoning
    locator: lead section
---

## Example

The [[Basel problem|0DMY75D6FV]] asks for the value of $\sum_{n=1}^{\infty} 1/n^2$.
Leonhard Euler found the value $\pi^2/6$ by an argument that was not a proof in his time.
We follow the argument as [[plausible reasoning|8DHD3H1CJ9]]: an analogy gives a conjecture, and checks of consequences make it more credible.

1. A fact about polynomials. If $p$ is a polynomial of degree $m$ with $p(0) = 1$ and with the nonzero roots $a_1, \ldots, a_m$, then $p(x) = (1 - x/a_1)(1 - x/a_2) \cdots (1 - x/a_m)$. Both sides have the same roots and the same value at $0$.
2. The coefficient of $x$ in this product is $-(1/a_1 + \cdots + 1/a_m)$. It comes from choosing the term $-x/a_i$ in one factor and $1$ in all others.
3. The function. The power series of the sine gives $\dfrac{\sin x}{x} = 1 - \dfrac{x^2}{6} + \dfrac{x^4}{120} - \cdots$, with the value $1$ at $x = 0$. Its zeros are $\pm \pi, \pm 2\pi, \pm 3\pi, \ldots$.
4. The analogy. Euler treated $\sin x / x$ as a polynomial of infinite degree. Step 1 then suggests $\dfrac{\sin x}{x} = \prod_{n=1}^{\infty} \left(1 - \dfrac{x}{n\pi}\right)\left(1 + \dfrac{x}{n\pi}\right) = \prod_{n=1}^{\infty} \left(1 - \dfrac{x^2}{n^2\pi^2}\right)$.
5. The conjecture. The coefficient of $x^2$ on the left is $-1/6$, by step 3. On the right it is $-\sum_{n} 1/(n^2\pi^2)$, as in step 2. Equal coefficients give $\sum_{n=1}^{\infty} 1/n^2 = \pi^2/6$.
6. Check 1, a numerical consequence. The partial sum up to $n = 1000$ is $1.643934\ldots$, and the tail beyond $1000$ is about $1/1000$. The total $1.644934\ldots$ agrees with $\pi^2/6 = 1.6449340668\ldots$.
7. Check 2, a new consequence of the same analogy. The coefficient of $x^4$ gives $\sum_{m < n} 1/(m^2 n^2) = \pi^4/120$. With $\left(\sum 1/n^2\right)^2 = \sum 1/n^4 + 2\sum_{m<n} 1/(m^2n^2)$, this predicts $\sum 1/n^4 = \pi^4/36 - \pi^4/60 = \pi^4/90 = 1.0823232\ldots$. A numerical sum agrees.
8. Check 3, a consequence of a different kind. Put $x = \pi/2$ in step 4: $\dfrac{2}{\pi} = \prod_{n=1}^{\infty}\left(1 - \dfrac{1}{4n^2}\right)$. This is the [[Wallis product|0XCYA4YERS]], which was already proved.
9. Weighing. Each check is a verified consequence of the analogy, so the analogy and its conclusion become more credible. Check 3 has the most weight: it is a known theorem, and it is of a different kind from the numerical checks.

## Remarks

The argument of step 4 is not valid as it stands.
The function $e^x \sin x / x$ has the same zeros and the same value at $0$, but it is a different function.
So "same zeros and same value at $0$" does not determine an infinite product, and the analogy with polynomials needs a theorem to become a proof.
The [[Weierstrass factorization theorem|11VC51YHQJ]] and the growth of the sine supply that theorem today, and Euler himself gave other proofs later.

If we compare the coefficients of $x^6$, the same method predicts $\sum 1/n^6 = \pi^6/945$, which is also true.
A different analogy can fail: step 4 used all the zeros, and an argument that misses a zero gives a wrong product.

## Explanations

### L1 human

Euler wanted the exact value of $1 + \frac14 + \frac19 + \frac1{16} + \cdots$.
He guessed it with an idea that was not fully justified: he treated the sine function like a very long polynomial.
The idea gave the answer $\pi^2/6$, which is about $1.645$.
He then tested the idea in other ways: adding many terms on paper, and getting a famous old formula for $\pi$ from it.
Every test agreed, so he became confident, even before a full proof existed.

### L2 human

We repeat check 2 in detail.

1. The coefficient of $x^4$ in $\sin x / x$ is $1/120$, from $\sin x = x - x^3/6 + x^5/120 - \cdots$.
2. In $\prod_n (1 - x^2/(n^2\pi^2))$, a term $x^4$ comes from choosing $-x^2/(m^2\pi^2)$ and $-x^2/(n^2\pi^2)$ in two different factors, $m < n$. So the coefficient is $\sum_{m<n} 1/(m^2 n^2 \pi^4)$.
3. Equal coefficients give $\sum_{m<n} 1/(m^2n^2) = \pi^4/120$.
4. Squaring the sum of step 5: $(\pi^2/6)^2 = \sum 1/n^4 + 2 \cdot \pi^4/120$.
5. So $\sum 1/n^4 = \pi^4/36 - \pi^4/60 = \pi^4/90$.
6. Numerically, $\pi^4/90 = 1.0823232337\ldots$, and the sum of $1/n^4$ for $n \leq 10^5$ gives the same digits.

The typical use: a heuristic that gives one result also gives others, and checking those others tests the heuristic.
A trap: the checks raise confidence in the method, but they do not repair the gap in step 4.
