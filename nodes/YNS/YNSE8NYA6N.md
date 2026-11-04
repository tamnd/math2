---
tag: YNSE8NYA6N
kind: proof
name: Proof of the integral of 1/x
msc: [26A36]
proves: 0K1N1Y4EGZ
uses: [0QD4E5JYPT, 07ZMX4ANJS, 07X1QA6BRW, 0RXX2PT1MQ, 0MH1WK89PP, 06SESV7GQY, 0XYAFCN0PT, 021WEM680W, 0J7PHRBNNS, 0044CPHJBV]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: Integration
---

## Proof

We find an antiderivative of $1/x$ on each half line and apply the fundamental theorem of calculus.

1. Let $f(x) = 1/x$ for $x \ne 0$. The function $x \mapsto x$ is differentiable and nonzero at each $x \ne 0$. By the [[reciprocal rule|0QD4E5JYPT]], $f$ is differentiable at each $x \ne 0$.
2. [[Differentiable functions are continuous|07ZMX4ANJS]], so $f$ is continuous on $(0, \infty)$ and on $(-\infty, 0)$.
3. Let $I$ be one of the open intervals $(0, \infty)$ or $(-\infty, 0)$. Let $F \colon I \to \R$ be differentiable with $F' = f$ on $I$. We claim that $\int_a^b \frac{dx}{x} = F(b) - F(a)$ for all $a, b \in I$.
4. Proof of the claim for $a < b$. The interval $[a, b]$ lies in $I$. By step 2, $f$ is [[Riemann integrable|06SESV7GQY]] on $[a, b]$. Also $F$ is differentiable on $I$, so it is continuous on $[a, b]$ by the result cited in step 2. The [[second fundamental theorem of calculus|0XYAFCN0PT]] gives $\int_a^b f = F(b) - F(a)$.
5. Proof of the claim for $a = b$ and $a > b$. By the convention for the [[definite integral|021WEM680W]], $\int_a^a f = 0 = F(a) - F(a)$. For $a > b$, $\int_a^b f = -\int_b^a f = -(F(a) - F(b)) = F(b) - F(a)$, by step 4.
6. Case $a, b > 0$. Take $I = (0, \infty)$ and $F = \ln$, the [[natural logarithm|0044CPHJBV]]. By the [[derivative of the logarithm|07X1QA6BRW]], $F' = f$ on $I$.
7. By steps 3 and 6, $\int_a^b \frac{dx}{x} = \ln b - \ln a$. By the [[logarithm of a quotient|0J7PHRBNNS]], this equals $\ln \frac{b}{a}$.
8. Case $a, b < 0$. Take $I = (-\infty, 0)$ and $F(x) = \ln(-x)$. Let $\varphi(x) = -x$. By the [[derivative of a polynomial|0MH1WK89PP]], $\varphi'(x) = -1$, and $\varphi$ maps $I$ into $(0, \infty)$.
9. By the [[chain rule|0RXX2PT1MQ]] and the derivative of the logarithm, $F$ is differentiable on $I$ and $F'(x) = \frac{1}{-x} \cdot (-1) = \frac{1}{x}$.
10. By steps 3 and 9, $\int_a^b \frac{dx}{x} = \ln(-b) - \ln(-a)$. Since $-a, -b > 0$, the logarithm of a quotient gives $\ln \frac{-b}{-a} = \ln \frac{b}{a}$.
11. For the last claim, let $x > 0$ and apply step 7 with $a = 1$ and $b = x$. This gives $\int_1^x \frac{dt}{t} = \ln \frac{x}{1} = \ln x$.

## Idea

On the positive half line, $\ln x$ has derivative $1/x$. On the negative half line, $\ln(-x)$ has derivative $1/x$ by the chain rule. The fundamental theorem of calculus then gives a difference of logarithms, which is the logarithm of the quotient $b/a$.
