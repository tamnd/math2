---
tag: HW5E2DSZH3
kind: example
name: The word "but" in "the absolute value is continuous but not differentiable at 0"
msc: ["97E40", "26A24"]
topics: [WMY13MXY3W]
audience: ug1
instance_of: [12QQ51VK01]
uses: [12QQ51VK01, 0FFXKTKKQC, 0KRMJRDRZT, 0K57YG3BB8]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
---

## Example

Let $f \colon \mathbb{R} \to \mathbb{R}$ be the [[absolute value|0FFXKTKKQC]] function, $f(x) = |x|$.
Consider the statement "$f$ is continuous at $0$ but not differentiable at $0$".
In mathematical language, "$P$ but $Q$" has the same meaning as "$P$ and $Q$", as on the page [[connectives in mathematical language|12QQ51VK01]].
So the statement is the conjunction of $P$: "$f$ is continuous at $0$" and $Q$: "$f$ is not differentiable at $0$".
We check both parts.

1. Part $P$. Let $\varepsilon > 0$, and put $\delta = \varepsilon$. If $|x - 0| < \delta$, then $|f(x) - f(0)| = |x| < \varepsilon$. So $f$ is [[continuous at|0KRMJRDRZT]] $0$.
2. Part $Q$. For $h \neq 0$, the difference quotient is $\frac{f(h) - f(0)}{h} = \frac{|h|}{h}$.
3. For $h > 0$, the quotient is $1$. For $h < 0$, it is $-1$.
4. So the quotient takes the value $1$ at points $h$ as close to $0$ as we like, and also the value $-1$. It has no limit as $h \to 0$, and $f$ is not [[differentiable|0K57YG3BB8]] at $0$.
5. Both parts are true, so the conjunction is true, and the statement with "but" is true.

## Remarks

The word "but" tells the reader that the second part is unexpected after the first.
Many functions that a student meets are continuous and differentiable at the same points, so the contrast is useful to a reader.
The contrast does not change the truth value.
A proof of "$P$ but $Q$" proves $P$ and proves $Q$, as in steps 1 to 4.
The page [[absolute value is continuous but not differentiable at 0|0CQ9ZM383N]] treats the analysis of this example.

If we change the point $0$ to the point $1$, the statement "$f$ is continuous at $1$ but not differentiable at $1$" is false.
Near $1$, $f(x) = x$, so $f$ is differentiable at $1$ with derivative $1$, and part $Q$ fails.

## Explanations

### L1 human

The graph of $|x|$ is a V shape with its corner at $0$.
You can draw it without lifting the pen, so it is continuous.
At the corner, the graph has no single direction, so it has no slope there.
The sentence "it is continuous but has no slope at the corner" makes two claims, and both are true.
The word "but" only says that the second claim is a surprise.

### L2 human

We decide the truth value of "$g(x) = x^2$ is continuous at $0$ but not differentiable at $0$".

1. Rewrite "but" as "and": "$g$ is continuous at $0$, and $g$ is not differentiable at $0$".
2. The difference quotient of $g$ at $0$ is $\frac{h^2}{h} = h$ for $h \neq 0$, and $h \to 0$. So $g$ is differentiable at $0$, with $g'(0) = 0$.
3. So the second part is false.
4. A conjunction with a false part is false, so the statement is false.

The typical use is in the statements of counterexamples, which often have the form "$A$ but not $B$".
Such a statement shows that $A$ does not imply $B$.

A trap: a student may think that "but" weakens the first part.
It does not: a proof must still prove both parts.
