---
tag: AN5RQ78DD8
kind: example
name: A function that scales like a square but is not a quadratic form
msc: ["15A63"]
topics: [6TSCEW8QMK]
audience: ug1
not_instance_of:
  - target: 0RBQS1JJCR
    note: the function scales like a square but is not a homogeneous polynomial of degree 2, so it has no polar form that is bilinear
uses: [0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Example

Define $Q \colon \mathbb{R}^2 \to \mathbb{R}$ by $Q(0, 0) = 0$ and
$$Q(x, y) = \frac{x^4}{x^2 + y^2} \qquad \text{for } (x, y) \ne (0, 0).$$
We show that $Q$ satisfies the first condition of a [[quadratic form|0HZNE5QZDJ]] but not the second.

1. Scaling for $a \ne 0$ and $(x, y) \ne (0, 0)$. The numerator picks up $a^4$ and the denominator picks up $a^2$:
$$Q(ax, ay) = \frac{a^4 x^4}{a^2 (x^2 + y^2)} = a^2 Q(x, y).$$
2. Scaling when $a = 0$ or $(x, y) = (0, 0)$. Both sides are $0$. So $Q(av) = a^2 Q(v)$ for all $a$ and $v$.
3. The polar map. Let $b(u, v) = Q(u + v) - Q(u) - Q(v)$, and take $u = (1, 0)$, so that $Q(u) = 1$.
4. For $v = (0, 1)$ we get $Q(v) = 0$ and $Q(1, 1) = \tfrac{1}{2}$, so $b(u, v) = \tfrac{1}{2} - 1 - 0 = -\tfrac{1}{2}$.
5. For $2v = (0, 2)$ we get $Q(2v) = 0$ and $Q(1, 2) = \tfrac{1}{5}$, so $b(u, 2v) = \tfrac{1}{5} - 1 - 0 = -\tfrac{4}{5}$.
6. A bilinear $b$ would give $b(u, 2v) = 2 b(u, v) = -1$. Since $-\tfrac{4}{5} \ne -1$, the map $b$ is not bilinear.

So the second condition fails, and $Q$ is not a quadratic form.

## Remarks

The scaling rule $Q(av) = a^2 Q(v)$ alone does not define quadratic forms.
A function on $\mathbb{R}^2$ with this scaling is fixed by its values on the unit circle, and those values can be any function of the angle $\theta$.
A quadratic form $ax^2 + bxy + cy^2$ allows only the functions $a \cos^2\theta + b \cos\theta \sin\theta + c \sin^2\theta$ on the circle.
Here $Q(\cos\theta, \sin\theta) = \cos^4\theta$, which is not of that type: it would need $a = 1$ from $\theta = 0$, $c = 0$ from $\theta = \pi/2$, and then $\theta = \pi/4$ gives $\tfrac{1}{4} = \tfrac{1}{2} + \tfrac{b}{2}$, so $b = -\tfrac{1}{2}$, while $\theta = -\pi/4$ gives $\tfrac{1}{4} = \tfrac{1}{2} - \tfrac{b}{2}$, so $b = \tfrac{1}{2}$.

The bilinearity of the polar form is the condition that forces a polynomial of degree $2$.
If you change the example to $Q(x, y) = x^2$, which agrees with it on the $x$-axis, the polar form becomes $2xx'$, which is bilinear.

## Explanations

### L1 human

When you double the input, this function multiplies its output by four, just as a square does.
But it is a fraction, not a polynomial, so it is not a quadratic form.
The polar test finds the difference with two numbers, $-\tfrac{1}{2}$ and $-\tfrac{4}{5}$, where a quadratic form would give $-\tfrac{1}{2}$ and $-1$.

### L2 human

To test a candidate quadratic form, check both conditions.
First check $Q(av) = a^2 Q(v)$.
Then compute $b(u, v)$ for a few chosen vectors, and test $b(u, 2v) = 2 b(u, v)$ and $b(u, v + w) = b(u, v) + b(u, w)$.
Watch out: the second test needs specific vectors, as in steps 4 and 5, because a general argument with symbols can hide the failure.
