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

A student meets "$\log 8$" in a calculus book, a chemistry book and an algorithms book, and gets three different numbers.
The sign $\log$ without a base is one of the standard [[conflicting conventions|CSFEP56A7D]].
We compute $\log 8$ under each reading.

1. In pure mathematics, $\log$ is the [[natural logarithm|04DXAFN2ES]], with base $e$.
   Since $8 = 2^3$,
   $$\log 8 = \ln 8 = 3 \ln 2 \approx 3 \cdot 0.6931 = 2.0794.$$
2. In school books, chemistry and engineering, $\log$ often has base $10$.
   Then $\log 8 = \log_{10} 8 \approx 0.9031$, because $10^{0.9031} \approx 8.000$.
3. In computer science, $\log$ often has base $2$.
   Then $\log 8 = \log_2 8 = 3$ exactly, because $2^3 = 8$.
4. The three values $2.0794$, $0.9031$ and $3$ differ, so the expression $\log 8$ alone does not fix a number.
5. The change of base rule $\log_b x = \frac{\ln x}{\ln b}$ connects them:
   $$\frac{\ln 8}{\ln 10} \approx \frac{2.0794}{2.3026} \approx 0.9031, \qquad \frac{\ln 8}{\ln 2} = \frac{3 \ln 2}{\ln 2} = 3.$$

## Remarks

The standard ISO 80000-2 avoids the conflict with three names: $\ln$ for base $e$, $\lg$ for base $10$ and $\operatorname{lb}$ for base $2$.
This site writes $\log$ for the natural logarithm, as Mathlib does, and $\log_b$ for every other base.
To tell which base a book uses, look for the derivative: $\frac{d}{dx} \log x = \frac{1}{x}$ holds only for base $e$.

Some statements do not depend on the base at all.
Since $\log_2 n = \frac{\ln n}{\ln 2}$, the two functions differ by the constant factor $\frac{1}{\ln 2} \approx 1.4427$.
So an estimate such as $O(\log n)$ in [[big O notation|0TGV80E6A4]] means the same in every base, and algorithm books write it with no base.

## Explanations

### L1 human

The logarithm asks: to which power must we raise the base to get the number?
With base $2$, we ask "$2$ to which power is $8$?", and the answer is $3$.
With base $10$, the answer is a bit less than $1$, since $10^1 = 10$ is already more than $8$.
So $\log 8$ has different values in different books, and we must know the base.

### L2 human

Check that the base does not change the statement $\log_2 n = O(\ln n)$, and that it does change an exponent.
For $n \ge 2$ the change of base rule gives
$$\log_2 n = \frac{1}{\ln 2} \ln n \approx 1.4427 \ln n \le 2 \ln n,$$
so $\log_2 n = O(\ln n)$.
In the other direction, $\ln n = (\ln 2) \log_2 n \le \log_2 n$, so $\ln n = O(\log_2 n)$.
Inside an exponent, though, the base matters:
$$2^{\log_2 n} = n, \qquad 2^{\ln n} = e^{(\ln 2)(\ln n)} = n^{\ln 2} \approx n^{0.693}.$$
Check: for $n = 8$, $2^{\ln 8} = 2^{2.0794} \approx 4.23$ and $8^{0.693} \approx 4.23$.
Watch out: a running time of $2^{\log n}$ is $n$ in one book and about $n^{0.693}$ in another.
