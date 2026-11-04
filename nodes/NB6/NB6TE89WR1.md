---
tag: NB6TE89WR1
kind: proof
name: Proof that sin x / x tends to 1 as a derivative at 0
msc: [33B10]
proves: 01QSSKS5C1
uses: [0F1WR9C83K, 00R4MWW532, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/Sinc_function
    locator: Properties
---

## Proof

1. From the [[defining series|0WB57D9488]], $\sin 0 = 0$, since every term vanishes at $0$. Also $\cos 0 = 1$, since only the first term of the cosine series is nonzero.
2. For $x \ne 0$, $\frac{\sin x}{x} = \frac{\sin(0 + x) - \sin 0}{x}$. This is the difference quotient of $\sin$ at $0$ with increment $x$.
3. By the [[derivative of sine|00R4MWW532]], $\sin$ is differentiable at $0$ with $\sin'(0) = \cos 0 = 1$.
4. By the [[definition of the derivative|0F1WR9C83K]], the difference quotient in step 2 tends to $\sin'(0)$ as $x \to 0$.
5. So $\lim_{x \to 0} \frac{\sin x}{x} = 1$.

## Idea

Since $\sin 0 = 0$, the quotient $\frac{\sin x}{x}$ is exactly the slope of the secant of $\sin$ from $0$ to $x$. As $x \to 0$ this slope tends to the slope of the tangent at $0$, which is $\cos 0 = 1$.
