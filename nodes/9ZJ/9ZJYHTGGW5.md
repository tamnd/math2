---
tag: 9ZJYHTGGW5
kind: example
name: A zero derivative is necessary but not sufficient for a local extremum
msc: ["03B05", "26A24"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [09BJQQB3VS]
uses: [09BJQQB3VS, 0F405477F8, 0WFBH1Q3WC, 0K57YG3BB8]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_theorem_(stationary_points)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
---

## Example

At the top of a smooth hill the ground is flat, but a flat stretch of road need not be a top.
Let $f \colon (a, b) \to \mathbb{R}$ be a [[differentiable function|0K57YG3BB8]], and let $c \in (a, b)$.
The property is "$f$ has a [[local extremum|0WFBH1Q3WC]] at $c$", and the condition is "$f'(c) = 0$".
We check that the condition is [[necessary|09BJQQB3VS]] for the property, and that it is not sufficient.

1. Necessity: if $f$ has a local extremum at the interior point $c$, then $f'(c) = 0$.
   This is the theorem that the [[derivative vanishes at a local extremum|0F405477F8]].
2. To refute sufficiency, take $(a, b) = (-1, 1)$, $f(x) = x^3$ and $c = 0$.
3. The derivative is $f'(x) = 3x^2$, so $f'(0) = 0$, and the condition holds.
4. For $x < 0$ we have $f(x) = x^3 < 0 = f(0)$, and for $x > 0$ we have $f(x) > 0 = f(0)$.
5. So every interval around $0$ has values below $f(0)$ and values above $f(0)$, and $0$ is neither a local maximum nor a local minimum.
6. By steps 3 and 5, the condition holds and the property fails, so the condition is not sufficient.

## Remarks

### What the example shows

A necessary condition finds the candidates, and other tests decide among them.
To find the extrema of a differentiable function on an open interval, solve $f'(c) = 0$ and then test each solution.
Adding $f''(c) > 0$ to $f'(c) = 0$ gives a sufficient condition for a strict local minimum, for a twice differentiable $f$.

### Why each hypothesis is needed

Without differentiability, $f(x) = |x|$ has a minimum at $0$, and $f'(0)$ does not exist.
Without an interior point, $f(x) = x$ on $[0, 1]$ has a minimum at the endpoint $0$, and the one-sided derivative there is $1$.

### Watch out

Do not call every zero of $f'$ an extremum; $x^3$ at $0$ is the standard warning.

### Try it

Find the local extrema of $f(x) = x^3 - 3x$ on $\mathbb{R}$.
The derivative $3(x - 1)(x + 1)$ vanishes at $\pm 1$, and $f''(x) = 6x$ gives a local maximum at $-1$ and a local minimum at $1$.

## Explanations

### L1 human

At the top of a smooth hill the ground is flat for a moment.
So "the ground is flat here" is necessary for "this is the top of a hill".
It is not sufficient: a road that goes up, flattens for a moment, and goes up again has a flat point that is not a top.
The graph of $x^3$ at $0$ is such a road.

### L2 human

We find the local extrema of $f(x) = x^3 - 3x$ on $\mathbb{R}$.
The derivative is $f'(x) = 3x^2 - 3 = 3(x - 1)(x + 1)$.
By necessity, every local extremum is at $x = -1$ or $x = 1$, so the search shrinks to two points.
The second derivative is $f''(x) = 6x$, so $f''(-1) = -6 < 0$ and $f''(1) = 6 > 0$.
By the second derivative test, $f$ has a local maximum at $-1$ and a local minimum at $1$.
The last test is needed, because the necessary condition alone does not decide.
