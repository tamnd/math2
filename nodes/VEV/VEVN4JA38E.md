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

An analysis course defines [[sine and cosine|0WB57D9488]] by their power series:
$$\sin x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k+1}}{(2k+1)!}, \qquad \cos x = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k}}{(2k)!}.$$
It then proves the [[limit of $\frac{\sin x}{x}$|01QSSKS5C1]] by the [[proof as a derivative at $0$|NB6TE89WR1]]: the limit is $\sin'(0) = \cos 0 = 1$.
In a geometric course this argument is [[circular|JPHE53PABT]], but here it is a proof, and we check why.

1. The proof uses $\sin'(0) = \cos 0 = 1$, from the [[derivative of sine|00R4MWW532]].
2. In this course, $\sin' = \cos$ comes from the theorem that [[power series are differentiable term by term|002X7EK91H]] inside the radius of convergence, which is infinite here.
3. Term by term, the derivative of $\frac{(-1)^k x^{2k+1}}{(2k+1)!}$ is $\frac{(-1)^k x^{2k}}{(2k)!}$, the term number $k$ of the cosine series.
4. The theorem on power series is proved from estimates on series, and it never mentions sine, so the derivative of sine does not depend on the limit.
5. So the chain "series, then $\sin' = \cos$, then the limit" has no cycle.

A second proof in the same course needs no derivative at all.
For $x \neq 0$, divide the series by $x$:
$$\frac{\sin x}{x} = \sum_{k=0}^{\infty} \frac{(-1)^k x^{2k}}{(2k+1)!}.$$
The right side is a power series with value $1$ at $x = 0$, and a power series is continuous inside its radius of convergence, so the limit at $0$ is $1$.

## Remarks

The example is the correct twin of the [[circular L'Hôpital computation|XFD21N14W4]].
Both arguments use the formula $\sin' = \cos$; they differ in the definition of sine and so in the proof of that formula.
The series definition pays elsewhere: the course must prove that the series sine has period $2\pi$ and traces the unit circle, and those proofs are longer than the geometric ones.

## Explanations

### L1 human

Whether an argument runs in a circle depends on where you start.
If sine is defined by a formula with infinitely many terms, its slope can be read from the formula directly.
With that slope known, the limit of $\frac{\sin x}{x}$ follows in one line.
Nothing in this chain uses the limit before it is proved.

### L2 human

We compute $\frac{\sin x}{x}$ at $x = 0.1$ from the series, to watch the limit at work.
The series gives $\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots$, so at $x = 0.1$:
$$1 - \frac{0.01}{6} + \frac{0.0001}{120} \approx 1 - 0.0016667 + 0.0000008 = 0.9983341.$$
The series alternates with decreasing terms, so the error is at most the next term, $\frac{0.1^6}{5040} < 10^{-9}$.
So $\frac{\sin 0.1}{0.1} \approx 0.998334$, already close to the limit $1$.

The typical use of the series definition is in analysis courses that build the elementary functions from power series.
Watch out for mixing the two developments: using the series for $\sin' = \cos$ and the circle picture for $\sin^2 + \cos^2 = 1$ needs a proof that the two definitions agree.
