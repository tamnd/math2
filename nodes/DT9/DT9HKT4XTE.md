---
tag: DT9HKT4XTE
kind: proof
name: Proof of the derivative of arctangent
msc: [33B10, 26A24]
proves: 05P4B4Q22V
uses: [065XW2V6C3, 06T0HS14PP, 0SAMR34WXC, 07ZMX4ANJS, 07J5X2T1ZX, 0W766JAPSN, 0M0RZ3HSB0]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Differentiating the inverse tangent function
---

## Proof

We apply the rule for the derivative of an inverse function to the tangent on $(-\pi/2, \pi/2)$.

1. Let $I = (-\pi/2, \pi/2)$, and let $T \colon I \to \R$ be the restriction of the [[tangent function|06T0HS14PP]] to $I$.
2. No point of $I$ has the form $\frac{\pi}{2} + k\pi$ with $k \in \Z$. So $\cos y \ne 0$ for all $y \in I$, and $T$ is defined on all of $I$.
3. By the [[derivative of tangent|0SAMR34WXC]], $T$ is differentiable at each $y \in I$, with $T'(y) = 1 + \tan^2 y$.
4. By step 3, $T$ is continuous on $I$, since [[differentiable functions are continuous|07ZMX4ANJS]].
5. For each $y \in I$, step 3 gives $T'(y) = 1 + \tan^2 y \ge 1 > 0$.
6. By steps 4 and 5, $T$ is strictly increasing on $I$, since [[a function with positive derivative is strictly increasing|07J5X2T1ZX]].
7. By the definition of the [[arctangent|065XW2V6C3]], each real $x$ has exactly one $y \in I$ with $T(y) = x$, namely $y = \arctan x$.
8. So $T \colon I \to \R$ is a bijection, and its [[inverse function|0W766JAPSN]] is $T^{-1} = \arctan$.
9. Fix a real number $x$, and let $a = \arctan x \in I$. Then $T(a) = x$, and $T'(a) = 1 + \tan^2 a = 1 + x^2 \ne 0$.
10. The interval $I$ is open, and $T$ is continuous and strictly monotone on it by steps 4 and 6. So the [[derivative of an inverse function|0M0RZ3HSB0]] applies at $a$.
11. It gives that $\arctan = T^{-1}$ is differentiable at $x = T(a)$, with
$$\arctan'(x) = \frac{1}{T'(a)} = \frac{1}{1 + x^2}.$$
12. Since $x$ was an arbitrary real number, $\arctan$ is differentiable on $\R$ with $\frac{d}{dx} \arctan x = \frac{1}{1 + x^2}$.

## Idea

The arctangent undoes the tangent on $(-\pi/2, \pi/2)$, so its slope at $x$ is the reciprocal of the slope of $\tan$ at $\arctan x$. That slope is $1 + \tan^2 y$, and $\tan y = x$ there. So the answer depends on $x$ alone: $\frac{1}{1 + x^2}$.
