---
tag: 74MM1MKBG8
kind: proof
name: Proof of the integral of the exponential function
msc: [26A36]
proves: 06D0EWR2DV
uses: [0RMVS7RXZX, 0EX9GFJ0B3, 07ZMX4ANJS, 06SESV7GQY, 0XYAFCN0PT, 021WEM680W]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: Second part
---

## Proof

We use that the exponential function is an antiderivative of itself.

1. Let $F = \exp$, the [[exponential function|0RMVS7RXZX]], and write $e^x = \exp(x)$.
2. By [[the derivative of exp|0EX9GFJ0B3]], $F$ is differentiable on $\R$ and $F' = F$.
3. [[Differentiable functions are continuous|07ZMX4ANJS]], so $F$ is continuous on $\R$.
4. Assume $a < b$. By step 3, $F$ is [[Riemann integrable|06SESV7GQY]] on $[a, b]$. By steps 2 and 3, the [[second fundamental theorem of calculus|0XYAFCN0PT]] applies to $F$ with $F' = F$. It gives $\int_a^b e^x \, dx = e^b - e^a$.
5. Assume $a = b$. By the convention for the [[definite integral|021WEM680W]], $\int_a^a e^x \, dx = 0 = e^a - e^a$.
6. Assume $a > b$. By the same convention and step 4 on $[b, a]$, $\int_a^b e^x \, dx = -(e^a - e^b) = e^b - e^a$.
7. So $\int_a^b e^x \, dx = e^b - e^a$ for all real $a$ and $b$.

## Idea

The exponential function is its own derivative, so it is its own antiderivative. The fundamental theorem of calculus then evaluates the integral as a difference of two values of $e^x$.
