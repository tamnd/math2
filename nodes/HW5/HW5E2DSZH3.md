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
Calculus books say: "$f$ is continuous at $0$ but not differentiable at $0$".
In mathematical language "$P$ but $Q$" means "$P$ and $Q$", as [[connectives in mathematical language|12QQ51VK01]] explains.
So the sentence is the conjunction of $P$, "$f$ is continuous at $0$", and $Q$, "$f$ is not differentiable at $0$", and we check both parts.

1. Part $P$.
   Let $\varepsilon > 0$ and put $\delta = \varepsilon$.
   If $|x - 0| < \delta$, then $|f(x) - f(0)| = |x| < \varepsilon$, so $f$ is [[continuous at|0KRMJRDRZT]] $0$.
2. Part $Q$.
   For $h \ne 0$ the difference quotient is
   $$\frac{f(h) - f(0)}{h} = \frac{|h|}{h}.$$
3. For $h > 0$ the quotient is $1$, and for $h < 0$ it is $-1$.
4. So the quotient takes the value $1$ at points $h$ as close to $0$ as we like, and also the value $-1$.
   It has no limit as $h \to 0$, and $f$ is not [[differentiable|0K57YG3BB8]] at $0$.
5. Both parts are true, so the conjunction is true, and the sentence with "but" is true.

## Remarks

The word "but" warns the reader that the second part is unexpected after the first.
Most functions that a student meets are differentiable wherever they are continuous, so the warning helps.
It does not change the truth value, and a proof of "$P$ but $Q$" proves $P$ and proves $Q$, as steps 1 to 4 do.
The analysis of the example is on [[absolute value is continuous but not differentiable at 0|0CQ9ZM383N]].

Move the point from $0$ to $1$ and the sentence becomes false.
Near $1$ we have $f(x) = x$, so $f$ is differentiable at $1$ with derivative $1$, and part $Q$ fails.

## Explanations

### L1 human

The graph of $|x|$ is a V shape with its corner at $0$.
You can draw it without lifting the pen, so it is continuous.
At the corner the graph has no single direction, so it has no slope there.
The sentence "it is continuous but has no slope at the corner" makes two claims, and both are true.
The word "but" only says that the second claim is a surprise.

### L2 human

Decide whether "$g(x) = x^2$ is continuous at $0$ but not differentiable at $0$" is true.
First rewrite "but" as "and": "$g$ is continuous at $0$, and $g$ is not differentiable at $0$".
The difference quotient of $g$ at $0$ is
$$\frac{g(h) - g(0)}{h} = \frac{h^2}{h} = h \qquad (h \ne 0),$$
and $h \to 0$, so $g$ is differentiable at $0$ with $g'(0) = 0$.
So the second part is false, and a conjunction with a false part is false.

Statements of the form "$A$ but not $B$" are the usual way to announce a counterexample, since one such object shows that $A$ does not imply $B$.
Watch out: "but" does not weaken the first part, and a proof must still prove both.
