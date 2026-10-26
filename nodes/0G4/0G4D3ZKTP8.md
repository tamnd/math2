---
tag: 0G4D3ZKTP8
kind: example
name: Sum of the reciprocals of the factorials
msc: [40A05]
instance_of: [0AF7X08PCR]
uses: [0MVCFMW7S4, 0QNY6ZBXPN, 0RMVS7RXZX]
sources:
  - url: https://en.wikipedia.org/wiki/E_(mathematical_constant)
    locator: Definitions
---

## Example

The series
$$\sum_{n=0}^{\infty} \frac{1}{n!} = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \cdots$$
converges, and its sum is the number [[e|0MVCFMW7S4]] $\approx 2.71828$.

## Remarks

The series converges by the [[ratio test|0QNY6ZBXPN]], since the ratio of consecutive terms is $1/(n+1) \to 0$.
It is the value at $x = 1$ of the power series $\sum x^n / n!$ of the [[exponential function|0RMVS7RXZX]].
The series converges fast. The tail after the term $1/N!$ is less than $1/(N! \, N)$.

## Explanations

### L1 human

The terms shrink very fast, because $n!$ grows fast.
Only a few terms give a good value of $e$: the first five terms already give $2.708$.
