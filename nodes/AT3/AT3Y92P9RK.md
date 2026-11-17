---
tag: AT3Y92P9RK
kind: example
name: The value of log 8 under three conventions
msc: ["00A35", "26A09"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [CSFEP56A7D]
uses: [CSFEP56A7D, 04DXAFN2ES, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Logarithm
    locator: lead section
---

## Example

The expression $\log 8$ has three common readings.
We compute its value under each reading.

1. In pure mathematics, $\log$ is the [[natural logarithm|04DXAFN2ES]], with base $e$. Since $8 = 2^3$, $\log 8 = 3 \ln 2 \approx 3 \cdot 0.6931 = 2.0794$.
2. In school books and in engineering, $\log$ often has base $10$. Then $\log 8 = \log_{10} 8 \approx 0.9031$, because $10^{0.9031} \approx 8.000$.
3. In computer science, $\log$ often has base $2$. Then $\log 8 = \log_2 8 = 3$ exactly, because $2^3 = 8$.
4. The three values $2.0794$, $0.9031$ and $3$ differ, so the expression $\log 8$ alone does not fix a number.
5. The change of base rule $\log_b x = \frac{\ln x}{\ln b}$ connects them: $\frac{\ln 8}{\ln 10} \approx \frac{2.0794}{2.3026} \approx 0.9031$ and $\frac{\ln 8}{\ln 2} = \frac{3 \ln 2}{\ln 2} = 3$.

## Remarks

The international standard ISO 80000-2 avoids the conflict with three names: $\ln$ for base $e$, $\lg$ for base $10$ and $\operatorname{lb}$ for base $2$.
This site writes $\log$ for the natural logarithm, as Mathlib does, and $\log_b$ for every other base.
Some statements do not depend on the base.
For example, $\log_2 n = \frac{\ln n}{\ln 2}$, so $\log_2 n$ and $\ln n$ differ by the constant factor $\frac{1}{\ln 2} \approx 1.4427$, and an estimate such as $O(\log n)$ in [[big O notation|0TGV80E6A4]] means the same in every base.

## Explanations

### L1 human

The logarithm asks: to which power must we raise the base to get the number?
With base $2$, we ask "$2$ to which power is $8$?", and the answer is $3$.
With base $10$, the answer is a bit less than $1$, since $10^1 = 10$ is already more than $8$.
So $\log 8$ has different values in different books, and we must know the base.

### L2 human

We check that the choice of base does not change an asymptotic statement.

1. Let $f(n) = \log_2 n$ and $g(n) = \ln n$ for $n \ge 2$.
2. By the change of base rule, $f(n) = \frac{1}{\ln 2} \, g(n)$, and $\frac{1}{\ln 2} \approx 1.4427$.
3. So $f(n) \le 2 g(n)$ for all $n \ge 2$, which gives $f = O(g)$.
4. In the other direction, $g(n) = (\ln 2) f(n) \le f(n)$, which gives $g = O(f)$.

The typical use of this fact is in the analysis of algorithms, where authors write $O(n \log n)$ with no base.
A trap: the base does matter inside an exponent, since $2^{\log_2 n} = n$ but $2^{\ln n} = n^{\ln 2} \approx n^{0.693}$.
