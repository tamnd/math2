---
tag: RZK7Q1W36A
kind: proof
name: Proof of the integral of sine
msc: [26A36]
proves: 0GXCXCX3QN
uses: [0WB57D9488, 0V2DV29EGT, 00R4MWW532, 0Z9JB71BS0, 07ZMX4ANJS, 06SESV7GQY, 0XYAFCN0PT, 021WEM680W]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: Second part
---

## Proof

We use the antiderivative $-\cos$ of $\sin$.

1. Let $\sin$ and $\cos$ be the [[sine and cosine|0WB57D9488]], and let $F(x) = -\cos x$.
2. By the [[derivative of cosine|0V2DV29EGT]] and the [[constant multiple rule|0Z9JB71BS0]], $F$ is differentiable on $\R$ and $F'(x) = -(-\sin x) = \sin x$.
3. By the [[derivative of sine|00R4MWW532]], $\sin$ is differentiable on $\R$. [[Differentiable functions are continuous|07ZMX4ANJS]], so $\sin$ and $F$ are continuous on $\R$.
4. Assume $a < b$. By step 3, $\sin$ is [[Riemann integrable|06SESV7GQY]] on $[a, b]$. The [[second fundamental theorem of calculus|0XYAFCN0PT]] applies by steps 2 and 3. It gives $\int_a^b \sin x \, dx = F(b) - F(a) = \cos a - \cos b$.
5. Assume $a = b$. By the convention for the [[definite integral|021WEM680W]], the integral is $0 = \cos a - \cos a$.
6. Assume $a > b$. By the same convention and step 4 on $[b, a]$, $\int_a^b \sin x \, dx = -(\cos b - \cos a) = \cos a - \cos b$.
7. So $\int_a^b \sin x \, dx = \cos a - \cos b$ for all real $a$ and $b$.

## Idea

The derivative of $\cos$ is $-\sin$, so $-\cos$ is an antiderivative of $\sin$. The fundamental theorem of calculus turns the integral into $-\cos b - (-\cos a)$.
