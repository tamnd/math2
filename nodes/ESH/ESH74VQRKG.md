---
tag: ESH74VQRKG
kind: example
name: Asking for a rational closed form of the harmonic numbers
msc: ["00A35", "11B83"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: Y896GWYF8A
    note: the question is posed by analogy together with the form of its expected answer, and no answer of that form exists, so the posed problem has the answer "impossible"
uses: [Y896GWYF8A, 0NANDX7V02, 0E9M24KS9J, 05S2GSPMGA, 0XDK9CGYKJ, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_number
    locator: lead section
---

## Example

The sums $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$ and $1^2 + 2^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$ have closed forms that are polynomials in $n$.
A student changes the exponent from $1$ to $-1$ and poses a question by analogy.
Find a closed form for the [[harmonic number|0NANDX7V02]] $H_n = 1 + \frac{1}{2} + \dots + \frac{1}{n}$, as a polynomial or a quotient of polynomials in $n$.

The student first fits a line through the first values $H_1 = 1$ and $H_2 = \frac{3}{2}$, which gives $p(n) = \frac{n + 1}{2}$.
It predicts $p(3) = 2$, but $H_3 = \frac{11}{6}$, so the line fails.
Higher degrees fail in the same way, and the failures suggest that the expected answer does not exist.
We prove that it does not.

1. Suppose that $H_n = R(n)$ for each integer $n \ge 1$, where $R = \frac{P}{Q}$ is a [[rational function|0XDK9CGYKJ]] with polynomials $P$ and $Q$.
2. The [[harmonic series diverges|0E9M24KS9J]], so $H_n \to \infty$.
   A rational function that tends to infinity along the integers has $\deg P > \deg Q$.
3. Then $\frac{R(n)}{n} = \frac{P(n)}{n Q(n)}$ with $\deg P \ge \deg (nQ)$.
   So $\frac{R(n)}{n}$ tends to a nonzero constant or to $\pm\infty$, and it does not tend to $0$.
4. On the other hand, [[the harmonic numbers grow like the logarithm|05S2GSPMGA]].
   For $k \ge 2$ we have $\frac{1}{k} \le \int_{k-1}^{k} \frac{dx}{x}$, so $H_n \le 1 + \ln n$, where $\ln$ is the [[natural logarithm|04DXAFN2ES]].
5. So $0 < \frac{H_n}{n} \le \frac{1 + \ln n}{n} \to 0$, which contradicts step 3.
6. Hence no rational function $R$ has $R(n) = H_n$ for each $n \ge 1$.

The posing went wrong, and we name the condition that failed.
[[Problem posing|Y896GWYF8A]] asks for a new problem with content that you can attack, and it lets the answer take whatever form it has.
Here the variant came with the form of its answer, copied from the original by [[analogy|7KDT0R1HF2]].
The change from exponent $1$ to exponent $-1$ changes the growth from a power of $n$ to $\ln n$, and a rational function cannot grow like a logarithm.
A better question drops the expected form and asks how fast $H_n$ grows.
Its answer is $H_n = \ln n + \gamma + o(1)$, with Euler's constant $\gamma \approx 0.5772$.

## Remarks

The values show the logarithmic growth: $H_{10} \approx 2.929$ against $\ln 10 \approx 2.303$, $H_{100} \approx 5.187$ against $\ln 100 \approx 4.605$, and $H_{1000} \approx 7.485$ against $\ln 1000 \approx 6.908$.
The differences $0.626$, $0.582$ and $0.578$ approach $\gamma$.

The sums $1^k + 2^k + \dots + n^k$ for integers $k \ge 0$ are polynomials in $n$ of degree $k + 1$, and this is the pattern that the analogy copied.
Negative exponents break it: for $k = -1$ the sum grows like $\ln n$, and for $k \le -2$ it converges, with limit $\zeta(-k)$.
The negative result is itself an answer, since it shows that $H_n$ is a new function that the earlier ones cannot express.

## Explanations

### L1 human

We know a short formula for $1 + 2 + 3 + \dots + n$, which is $\frac{n(n + 1)}{2}$.
So it is natural to ask for a short formula of the same kind for $1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n}$.
But no such formula exists.
This sum grows very slowly, like the logarithm of $n$, and fractions made of powers of $n$ cannot grow that way.
The question was a good one to ask, but it assumed the kind of answer it would get.
The better question is how fast the sum grows, and it has a clear answer.

### L2 human

We test the analogy on small values before we try to prove anything.
The first values are $H_1 = 1$, $H_2 = \frac{3}{2}$, $H_3 = \frac{11}{6}$ and $H_4 = \frac{25}{12}$.
The denominators grow, and $H_{10} = \frac{7381}{2520}$, where $2520$ is the least common multiple of $1, 2, \dots, 10$.
A polynomial that takes rational values at the integers $1, \dots, d + 1$ has rational coefficients, so its values at integers have bounded denominators.
The growing denominators of $H_n$ therefore rule out every polynomial.
They do not rule out a rational function, whose values can have growing denominators, and the growth argument above is needed for that.
When you pose a variant by analogy, pose the question without fixing the form of the answer, and test small cases first.
Watch out: a pattern in the first few values, such as denominators that look like $2$, $6$ and $12$, can mislead, since $H_4 = \frac{25}{12}$ already breaks the guess $n(n + 1)$.
