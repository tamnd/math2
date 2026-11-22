---
tag: 2W5SMZWGYF
kind: example
name: A real root of x^5 - x - 1 by the intermediate value theorem
msc: ["00A35", "26A15"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [JZQVJ9XT63]
uses: [JZQVJ9XT63, 00KAFBR32E, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem
    locator: lead section
---

## Example

Statement: the equation $x^5 - x - 1 = 0$ has a real solution $c$ with $1 < c < 2$.
We give a [[non-constructive existence proof|JZQVJ9XT63]].

1. Let $f(x) = x^5 - x - 1$.
   Every polynomial is [[continuous|0X3WGX95FE]], so $f$ is continuous on $[1, 2]$.
2. Evaluate at the left end:
   $$f(1) = 1 - 1 - 1 = -1 < 0.$$
3. Evaluate at the right end:
   $$f(2) = 32 - 2 - 1 = 29 > 0.$$
4. The number $0$ lies strictly between $f(1)$ and $f(2)$.
   By the [[intermediate value theorem|00KAFBR32E]], there is a $c$ with $1 < c < 2$ and $f(c) = 0$.

The proof does not give $c$.
It shows only that some $c$ in the interval $(1, 2)$ is a root.

## Remarks

Here a non-constructive proof is the natural one, because the root has no formula of the usual kind.
By the [[Abel-Ruffini theorem|163A2WQQJX]] and Galois theory, the roots of $x^5 - x - 1$ cannot be written with $+$, $-$, $\times$, $\div$ and $n$-th roots, starting from integers.

You can still make the proof more informative by bisection: test the midpoint and keep the half where the sign changes.
$$f(1.5) \approx 5.09 > 0, \qquad f(1.25) \approx 0.80 > 0, \qquad f(1.125) \approx -0.32 < 0.$$
So the root lies in $(1, 1.5)$, then in $(1, 1.25)$, then in $(1.125, 1.25)$.
Each test halves the interval, and continuing gives $c \approx 1.1673$.
Check: $1.1673^5 \approx 2.1673$, and $2.1673 - 1.1673 - 1 = 0$.

Is $c$ the only real root?
The derivative $f'(x) = 5x^4 - 1$ is negative for $|x| < 5^{-1/4}$ and positive outside, so $f$ has a local maximum at $x = -5^{-1/4} \approx -0.669$, where $f \approx -0.46 < 0$.
Then $f$ falls to a local minimum at $x = 5^{-1/4}$, and after that it increases without bound.
So $f$ is negative on the whole interval $(-\infty, 5^{-1/4}]$, it crosses $0$ once after that, and $c$ is the only real root.

## Explanations

### L1 human

Draw the graph of $y = x^5 - x - 1$ without lifting the pencil.
At $x = 1$ the graph is below the $x$-axis, at height $-1$.
At $x = 2$ it is above the axis, at height $29$.
A curve drawn without lifting the pencil must cross the axis somewhere in between.
The crossing point is a solution, even though we do not know its exact value.

### L2 human

We use the same method to show that $\cos x = x$ has a solution.

1. Move everything to one side: let $g(x) = \cos x - x$, which is continuous on $[0, 1]$.
2. Evaluate: $g(0) = 1 > 0$.
3. Evaluate: $g(1) = \cos 1 - 1 < 0$, because $\cos 1 < 1$.
4. By the intermediate value theorem, $g(c) = 0$ for some $c$ in $(0, 1)$, so $\cos c = c$.

The typical use: move everything to one side, and find two points where the sign is different.
Watch out: the theorem needs continuity on the whole closed interval.
For $h(x) = \frac{1}{x}$ we have $h(-1) = -1 < 0$ and $h(1) = 1 > 0$, but $h$ has no zero, because it is not defined at $0$.
