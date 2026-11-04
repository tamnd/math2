---
tag: HSXN8T7CVS
kind: proof
name: Proof of the derivative of tangent by the quotient rule
msc: [33B10, 26A24]
proves: 0SAMR34WXC
uses: [06T0HS14PP, 0BS0NJPKVE, 00R4MWW532, 0V2DV29EGT, 03H7WZ4T3K, 07ZMX4ANJS]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: From the quotient rule
---

## Proof

1. Let $a$ be real with $\cos a \ne 0$. By the [[definition of tangent|06T0HS14PP]], $\tan x = \frac{\sin x}{\cos x}$ wherever $\cos x \ne 0$.
2. By the [[derivative of cosine|0V2DV29EGT]], $\cos$ is differentiable, hence [[continuous|07ZMX4ANJS]]. So there is an open interval $I$ containing $a$ on which $\cos x \ne 0$.
3. On $I$, $\tan = \frac{\sin}{\cos}$ is a quotient of two functions that are differentiable at $a$, by the [[derivative of sine|00R4MWW532]] and the derivative of cosine.
4. By the [[quotient rule|0BS0NJPKVE]], $\tan$ is differentiable at $a$, and $\tan'(a) = \frac{\cos a \cdot \cos a - \sin a \cdot (-\sin a)}{\cos^2 a} = \frac{\cos^2 a + \sin^2 a}{\cos^2 a}$.
5. By the [[Pythagorean identity|03H7WZ4T3K]], the numerator is $1$. So $\tan'(a) = \frac{1}{\cos^2 a}$.
6. Splitting the fraction in step 4 instead gives $\tan'(a) = 1 + \frac{\sin^2 a}{\cos^2 a} = 1 + \tan^2 a$.
7. So $\tan$ is differentiable at every $a$ with $\cos a \ne 0$, and $\tan'(a) = \frac{1}{\cos^2 a} = 1 + \tan^2 a$.

## Idea

Tangent is sine over cosine, so the quotient rule applies wherever cosine is not zero. The numerator becomes $\cos^2 + \sin^2$, which is $1$ by the Pythagorean identity. Dividing it term by term instead gives the form $1 + \tan^2$.
