---
tag: VEVN4JA38E
kind: example
name: With the series definition of sine the derivative proof of sin x / x is not circular
msc: ["00A35", "97I40"]
topics: [T6QQ749DM5]
audience: ug1
not_instance_of:
  - target: JPHE53PABT
    note: the proof uses sin' = cos, which is proved by term-by-term differentiation of the series, without the limit of sin x / x
uses: [JPHE53PABT, 0WB57D9488, 002X7EK91H, 00R4MWW532, 01QSSKS5C1]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Series and polynomials
  - url: https://en.wikipedia.org/wiki/Differentiation_of_trigonometric_functions
    locator: Limit of sin(θ)/θ as θ tends to 0
---

## Example

Suppose that a course defines [[sine and cosine|0WB57D9488]] by their power series:
$$\sin x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k}}{(2k)!}.$$
The course then proves the [[limit of $\frac{\sin x}{x}$|01QSSKS5C1]] by the [[proof as a derivative at $0$|NB6TE89WR1]].
We check that this proof is not [[circular|JPHE53PABT]].

1. The proof uses $\sin'(0) = \cos 0 = 1$, from the [[derivative of sine|00R4MWW532]].
2. In this course, $\sin' = \cos$ comes from the theorem that [[power series are differentiable term by term|002X7EK91H]] inside the radius of convergence, which is infinite here.
3. The term-by-term derivative of $\frac{(-1)^k x^{2k+1}}{(2k+1)!}$ is $\frac{(-1)^k x^{2k}}{(2k)!}$, the $k$-th term of the cosine series.
4. The theorem on power series is proved from estimates on series, and it does not mention sine. So the derivative of sine does not depend on the limit.
5. So the chain "series, then $\sin' = \cos$, then the limit" has no cycle, and the proof is correct.

A second proof in the same course needs no derivative.
For $x \neq 0$, $\frac{\sin x}{x} = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k}}{(2k+1)!}$, a power series with value $1$ at $x = 0$.
A power series is continuous inside its radius of convergence, so the limit at $0$ is the value $1$.

## Remarks

The example is the correct counterpart of the [[circular L'Hôpital computation|XFD21N14W4]].
The two arguments use the same formula $\sin' = \cos$; they differ in the definition of sine and so in the proof of that formula.
The cost of the series definition is elsewhere: the course must prove that the series sine has period $2\pi$ and describes the unit circle, and these proofs are longer than the geometric ones.

## Explanations

### L1 human

Whether an argument goes in a circle depends on where we start.
If sine is defined by a formula with infinitely many terms, then its slope can be found from the formula directly.
With that slope known, the limit of $\frac{\sin x}{x}$ follows in one line.
Nothing in this chain uses the limit before it is proved.

### L2 human

We compute $\frac{\sin x}{x}$ at $x = 0.1$ from the series, to see the limit at work.

1. The series gives $\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots$.
2. At $x = 0.1$: $1 - \frac{0.01}{6} + \frac{0.0001}{120} \approx 1 - 0.0016667 + 0.0000008 = 0.9983341$.
3. The remaining terms are smaller than $\frac{0.1^6}{5040} < 10^{-9}$ in absolute value, because the series alternates with decreasing terms.
4. So $\frac{\sin 0.1}{0.1} \approx 0.998334$, close to the limit $1$.

The typical use of the series definition is in analysis courses that build the elementary functions from power series.
A trap is to mix the two developments: to use the series for $\sin' = \cos$ and the geometric picture for $\sin^2 + \cos^2 = 1$ without proving that the two definitions agree.
