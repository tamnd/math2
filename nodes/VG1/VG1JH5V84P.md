---
tag: VG1JH5V84P
kind: example
name: Handwaving about tangent lines of continuous functions
msc: ["00A35", "26A24"]
topics: [T6QQ749DM5]
audience: ug1
instance_of: [D8A1K052XV]
uses: [D8A1K052XV, 0X3WGX95FE, 0CQ9ZM383N, 01A0MK1730]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_function
    locator: Differentiability and continuity
  - url: https://en.wikipedia.org/wiki/Weierstrass_function
    locator: lead section
---

## Example

A student argues as follows.

1. Let $f$ be a [[continuous function|0X3WGX95FE]] on $\mathbb{R}$, and let $a \in \mathbb{R}$.
2. The graph of $f$ has no gaps.
3. If we zoom in at the point $(a, f(a))$, the graph looks more and more like a straight line.
4. That line is the tangent line, so $f$ is differentiable at $a$.

We check the argument.

1. Steps 1 and 2 are valid: a continuous function has no jumps.
2. Step 3 is handwaving. It replaces the definition of the derivative by a picture, and it gives no reason why the picture becomes a line.
3. The precise form of step 3 is: the difference quotient $\frac{f(a + h) - f(a)}{h}$ has a limit as $h \to 0$. Nothing in steps 1 and 2 gives this limit.
4. The conclusion is false. Let $f(x) = |x|$ and $a = 0$. Then $f$ is continuous, and $\frac{f(h) - f(0)}{h} = \frac{|h|}{h}$ is $1$ for $h > 0$ and $-1$ for $h < 0$.
5. So the difference quotient has no limit, and [[$|x|$ is not differentiable at $0$|0CQ9ZM383N]]. Zooming in at $0$ shows the same corner at every scale.

So the argument is an instance of [[handwaving|D8A1K052XV]]: the failing step is a picture with no proof.

## Remarks

The example shows that a picture of a "nice" graph hides the condition that a proof must check.
The failure is not limited to one point: the [[Weierstrass function|01A0MK1730]] is continuous on $\mathbb{R}$ and differentiable at no point.
If we add the hypothesis that $f$ is differentiable at $a$, step 4 becomes the definition of the tangent line, and the argument is correct but empty.

## Explanations

### L1 human

The graph of $|x|$ has the shape of a letter V.
It has no gaps, so it is continuous.
At the bottom point there is a sharp corner, and no single straight line touches the graph there in the way a tangent does.
However much we zoom in, the corner stays a corner.
So "no gaps" does not give "a tangent line at every point".

### L2 human

We test the claim on $f(x) = x^{1/3}$ at $a = 0$, a case where the graph does become a line when we zoom in.

1. The function $f$ is continuous on $\mathbb{R}$, as the inverse of the continuous increasing function $x \mapsto x^3$.
2. For $h \neq 0$, $\frac{f(h) - f(0)}{h} = \frac{h^{1/3}}{h} = h^{-2/3}$.
3. As $h \to 0$, $h^{-2/3} \to +\infty$, so the difference quotient has no finite limit.
4. So $f$ is not differentiable at $0$, although the graph has a tangent line there: the vertical line $x = 0$.

The typical use of this test is to compute the difference quotient whenever an argument says "the graph looks smooth".
A trap is to think that a vertical tangent line gives a derivative: a derivative is a finite slope.
