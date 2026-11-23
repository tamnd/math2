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

We want
$$I = \int_0^{2\pi} \frac{dx}{2 + \cos x}.$$
A standard [[auxiliary element|8TKKRAXKFN]] for integrals of rational functions of $\sin x$ and $\cos x$ is the new variable $t = \tan \frac{x}{2}$, the [[tangent half-angle substitution|0W8ETY2AZ6]].
We first follow the naive computation and see where the new variable misleads.

1. With $t = \tan \frac{x}{2}$ we have $\cos x = \frac{1 - t^2}{1 + t^2}$ and $dx = \frac{2 \, dt}{1 + t^2}$.
2. Then
   $$2 + \cos x = \frac{2 + 2t^2 + 1 - t^2}{1 + t^2} = \frac{3 + t^2}{1 + t^2},$$
   and the integrand becomes $\frac{2}{3 + t^2}$.
3. The limits change to $\tan 0 = 0$ and $\tan \pi = 0$.
4. The naive result is $\int_0^0 \frac{2 \, dt}{3 + t^2} = 0$.

The result $0$ is false.
Since $2 + \cos x \le 3$, the integrand is at least $\frac{1}{3}$, so $I \ge \frac{2\pi}{3} > 0$.
We find the error and the correct value.

1. The rule of [[integration by substitution|0D37QFPEZE]] needs the new variable to be a differentiable function of $x$ on the whole interval.
2. The function $\tan \frac{x}{2}$ is not defined at $x = \pi$, inside $[0, 2\pi]$.
   As $x$ rises to $\pi$, $t$ tends to $+\infty$, and just after $\pi$ it comes back from $-\infty$.
3. So we split the interval at $\pi$.
   On $[0, \pi)$ the variable $t$ runs over $[0, \infty)$, and on $(\pi, 2\pi]$ it runs over $(-\infty, 0]$.
4. An antiderivative of $\frac{2}{3 + t^2}$ is $\frac{2}{\sqrt{3}} \arctan \frac{t}{\sqrt{3}}$, so each half gives
   $$\int_0^\infty \frac{2 \, dt}{3 + t^2} = \int_{-\infty}^0 \frac{2 \, dt}{3 + t^2} = \frac{2}{\sqrt{3}} \cdot \frac{\pi}{2} = \frac{\pi}{\sqrt{3}}.$$
5. Adding the halves, $I = \frac{2\pi}{\sqrt{3}} \approx 3.6276$.

Check: the midpoint rule with $200\,000$ subintervals gives $3.62760$, in agreement.

## Remarks

The auxiliary variable was a good idea used outside the region where it is defined.
An auxiliary element brings its own conditions, and you must check them before you use it.
The same error appears if you evaluate the antiderivative $F(x) = \frac{2}{\sqrt{3}} \arctan\left(\frac{1}{\sqrt{3}} \tan \frac{x}{2}\right)$ at $0$ and $2\pi$.
That function drops by $\frac{2\pi}{\sqrt{3}}$ at $x = \pi$, so it is not an antiderivative on all of $[0, 2\pi]$.

On an interval inside $(-\pi, \pi)$ the substitution is valid.
For example, $t$ runs from $0$ to $1$ as $x$ runs from $0$ to $\frac{\pi}{2}$, so
$$\int_0^{\pi/2} \frac{dx}{2 + \cos x} = \frac{2}{\sqrt{3}} \arctan \frac{1}{\sqrt{3}} = \frac{2}{\sqrt{3}} \cdot \frac{\pi}{6} = \frac{\pi}{3\sqrt{3}}.$$

## Explanations

### L1 human

The function we integrate is always positive, so its integral must be positive.
A clever change of variable gave the answer $0$, which is impossible.
The new variable, $\tan \frac{x}{2}$, breaks down in the middle of the interval, at $x = \pi$, where it shoots off to infinity and comes back from minus infinity.
The helper that we added was not valid on the whole interval, and that caused the wrong answer.

### L2 human

Before you use a new variable $t = g(x)$, test it on the interval of the problem.
Check that $g$ is defined and continuously differentiable on the whole interval.
For $g(x) = \tan \frac{x}{2}$ on $[0, 2\pi]$ this fails at $x = \pi$, so you split the interval there and treat each piece separately, as above.
Then check the answer against a rough bound.
Since $1 \le 2 + \cos x \le 3$, the integral lies between $\frac{2\pi}{3} \approx 2.09$ and $2\pi \approx 6.28$, and $\frac{2\pi}{\sqrt{3}} \approx 3.63$ lies in this range.

The half-angle variable turns a trigonometric integrand into a rational one, which is why it is a standard helper.
Equal limits after a substitution, as in step 3 of the naive computation, are a warning that the new variable has passed through a point where it is not defined.
