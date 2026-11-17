---
tag: YYC7CRH6M4
kind: example
name: An auxiliary variable that breaks the integral of 1/(2 + cos x) over a full period
msc: ["00A35", "26A42"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: 8TKKRAXKFN
    note: the auxiliary variable t = tan(x/2) is not defined at x = π, so the substitution is not valid on [0, 2π], and the naive computation gives 0 instead of 2π/√3
uses: [8TKKRAXKFN, 0W8ETY2AZ6, 0D37QFPEZE]
sources:
  - url: https://en.wikipedia.org/wiki/Tangent_half-angle_substitution
    locator: lead section
---

## Example

Problem: compute
$$I = \int_0^{2\pi} \frac{dx}{2 + \cos x}.$$
A standard [[auxiliary element|8TKKRAXKFN]] for integrals of rational functions of $\sin x$ and $\cos x$ is the new variable $t = \tan \frac{x}{2}$, the [[tangent half-angle substitution|0W8ETY2AZ6]].
We follow the naive computation and see where the auxiliary variable misleads.

1. With $t = \tan \frac{x}{2}$, we have $\cos x = \frac{1 - t^2}{1 + t^2}$ and $dx = \frac{2 \, dt}{1 + t^2}$.
2. Then $2 + \cos x = \frac{2 + 2t^2 + 1 - t^2}{1 + t^2} = \frac{3 + t^2}{1 + t^2}$, and the integrand becomes $\frac{2}{3 + t^2}$.
3. The new limits: $x = 0$ gives $t = \tan 0 = 0$, and $x = 2\pi$ gives $t = \tan \pi = 0$.
4. The naive result is $\int_0^0 \frac{2 \, dt}{3 + t^2} = 0$.

The result $0$ is false.
The integrand $\frac{1}{2 + \cos x}$ is positive, and since $2 + \cos x \leq 3$, it is at least $\frac{1}{3}$.
So $I \geq \frac{2\pi}{3} > 0$.

We find the error and the correct value.

1. The rule of [[integration by substitution|0D37QFPEZE]] needs the new variable to be a differentiable function of $x$ on the whole interval.
2. The function $\tan \frac{x}{2}$ is not defined at $x = \pi$, which lies inside $[0, 2\pi]$. As $x$ increases to $\pi$, $t$ tends to $+\infty$; just after $\pi$, $t$ comes from $-\infty$.
3. Split the interval at $\pi$. On $[0, \pi)$ the variable $t$ runs over $[0, \infty)$, and on $(\pi, 2\pi]$ it runs over $(-\infty, 0]$.
4. An antiderivative of $\frac{2}{3 + t^2}$ is $\frac{2}{\sqrt{3}} \arctan \frac{t}{\sqrt{3}}$.
5. So $\int_0^\infty \frac{2 \, dt}{3 + t^2} = \frac{2}{\sqrt{3}} \cdot \frac{\pi}{2} = \frac{\pi}{\sqrt{3}}$, and $\int_{-\infty}^0 \frac{2 \, dt}{3 + t^2} = \frac{\pi}{\sqrt{3}}$ in the same way.
6. So $I = \frac{2\pi}{\sqrt{3}} \approx 3.628$.

A numerical check with the midpoint rule and $200\,000$ subintervals gives $3.62760$, which agrees with $\frac{2\pi}{\sqrt{3}} \approx 3.62760$.

## Remarks

The auxiliary variable was a good idea, but it was used outside the region where it is defined.
An auxiliary element brings its own conditions, and they must be checked before it is used.
The same error appears when the antiderivative $F(x) = \frac{2}{\sqrt{3}} \arctan\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)$ is evaluated at $0$ and $2\pi$: $F$ jumps by $\frac{2\pi}{\sqrt{3}}$ at $x = \pi$, so it is not an antiderivative on all of $[0, 2\pi]$.

On an interval inside $(-\pi, \pi)$, the substitution is valid.
For example, $\int_0^{\pi/2} \frac{dx}{2 + \cos x} = \frac{2}{\sqrt{3}} \arctan \frac{1}{\sqrt{3}} = \frac{\pi}{3\sqrt{3}}$.

## Explanations

### L1 human

The function we integrate is always positive, so its integral must be positive.
A clever change of variable gave the answer $0$, which is impossible.
The new variable, $\tan \frac{x}{2}$, breaks down in the middle of the interval, at $x = \pi$.
There it shoots off to infinity and comes back from minus infinity.
The helper that we added was not valid on the whole interval, and that caused the wrong answer.

### L2 human

We test a proposed auxiliary variable before we use it.

1. Write the new variable as a function $t = g(x)$ on the interval of the problem.
2. Check that $g$ is defined and continuously differentiable on the whole interval. For $g(x) = \tan \frac{x}{2}$ on $[0, 2\pi]$, this fails at $x = \pi$.
3. If it fails, split the interval at the bad points and treat each piece separately, as above.
4. Check the answer with a rough bound: here $\frac{2\pi}{3} \leq I \leq 2\pi$, since $1 \leq 2 + \cos x \leq 3$, and $\frac{2\pi}{\sqrt{3}} \approx 3.628$ lies in this range.

The typical use: the half-angle variable turns a trigonometric integrand into a rational function.

A trap: equal limits after a substitution, as in step 3 of the naive computation, are a warning that the new variable has passed through a singular point.
