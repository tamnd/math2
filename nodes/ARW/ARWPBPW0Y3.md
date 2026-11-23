---
tag: ARWPBPW0Y3
kind: example
name: The intermediate value theorem needs a rigorous proof
msc: ["00A35", "26A15"]
topics: [1BTHSHST4M]
audience: ug1
instance_of: [E1PE9R8DBB]
uses: [E1PE9R8DBB, 00KAFBR32E, 0AXWET80YW, 0DZGSDHD92, P54346XMQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Proof
---

## Example

The [[intermediate value theorem|00KAFBR32E]] says that if $f \colon [a, b] \to \mathbb{R}$ is continuous and $y$ lies between $f(a)$ and $f(b)$, then $f(c) = y$ for some $c \in [a, b]$.
The picture argument says that the graph is an unbroken curve from one height to another, so it must pass through each height in between.
We show that the picture argument is not [[rigorous|E1PE9R8DBB]], and we find the property that a rigorous proof must use.

1. We run the picture argument on the rational numbers $\mathbb{Q}$ in place of $\mathbb{R}$. Let $g(x) = x^2 - 2$ for rational $x$ with $1 \le x \le 2$.
2. The function $g$ is continuous on these rational numbers. It is a polynomial, and the epsilon-delta proof of continuity for polynomials uses only the arithmetic of the numbers.
3. We compute the end values: $g(1) = 1 - 2 = -1 < 0$ and $g(2) = 4 - 2 = 2 > 0$.
4. Suppose that $g(c) = 0$ for a rational $c$. Then $c^2 = 2$.
5. No rational number has square $2$, because $\sqrt{2}$ is [[irrational|0DZGSDHD92]]. This contradicts step 4, so $g$ has no rational zero.
6. So the statement "a continuous function that changes sign has a zero" fails over $\mathbb{Q}$. The graph over $\mathbb{Q}$ looks the same as the graph over $\mathbb{R}$, so the picture cannot be the reason that the theorem holds over $\mathbb{R}$.
7. The difference between $\mathbb{Q}$ and $\mathbb{R}$ is the [[completeness axiom|0AXWET80YW]]: each nonempty set of real numbers with an upper bound has a least upper bound. The set $\{x \in \mathbb{Q} : x > 0, \ x^2 < 2\}$ has upper bounds in $\mathbb{Q}$ but no least one, as the L2 explanation checks.
8. [[The rigorous proof|P54346XMQQ]] takes $c$ to be the least upper bound of the set of points where $f(x) < y$. It uses completeness at this one step, and it uses continuity to show both $f(c) \ge y$ and $f(c) \le y$.

## Remarks

The example shows the main use of rigor: it finds the hypothesis on which a result depends.
The picture hides the completeness of $\mathbb{R}$, and the rigorous proof names it.
This is also why the theorem fails for functions on $\mathbb{Q}$ and holds for real functions on every closed interval.

The example also marks a change in the standard of proof.
Earlier authors took the result as evident and gave no proof.
Bernard Bolzano published a proof in 1817, and Augustin-Louis Cauchy gave a proof in his *Cours d'analyse* of 1821.
A full construction of the real numbers, from which completeness follows as a theorem, came later in the 19th century, for example with [[Dedekind cuts|0G3RRM41X9]].

What changes if we change the function?
For $h(x) = x^2 - 4$ on the rational interval $[1, 3]$, the zero $x = 2$ is rational, so the conclusion holds.
One rational example can satisfy the conclusion by luck, and only a proof shows which functions must satisfy it.

## Explanations

### L1 human

Draw a line with a pen from a point below a river to a point above it, without lifting the pen.
It seems that the line must cross the river.
Mathematicians wanted to know why this is true, and not only that it looks true.
They found that it depends on the number line having no holes.
A number line made only of fractions has holes, for example at the square root of $2$.
A curve on such a line can pass a hole without any break that we can see, so the crossing can fail.
The rigorous proof uses exactly the fact that the real number line has no holes.

### L2 human

We check the claim of step 7 for the set $A = \{x \in \mathbb{Q} : x > 0, \ x^2 < 2\}$.

1. The set $A$ is nonempty, since $1 \in A$, and $2$ is an upper bound, since $x \ge 2$ gives $x^2 \ge 4$.
2. Let $u$ be a rational upper bound of $A$. Then $u \ge 1 > 0$, since $1 \in A$, and $u^2 \neq 2$, since $\sqrt{2}$ is irrational.
3. Put $v = (2u + 2)/(u + 2)$, a rational number. Then $v - u = (2 - u^2)/(u + 2)$.
4. Also $v^2 - 2 = \big((2u + 2)^2 - 2(u + 2)^2\big)/(u + 2)^2 = 2(u^2 - 2)/(u + 2)^2$.
5. If $u^2 < 2$, then step 3 gives $v > u$ and step 4 gives $v^2 < 2$, so $v \in A$ and $v > u$. This contradicts that $u$ is an upper bound, so $u^2 > 2$.
6. Since $u^2 > 2$, step 3 gives $v < u$ and step 4 gives $v^2 > 2$.
7. Each $x \in A$ has $x^2 < 2 < v^2$, so $x < v$. Thus $v$ is a smaller rational upper bound, and $A$ has no least rational upper bound.

Check with $u = 2$: $v = 6/4 = 1.5$, and $1.5^2 = 2.25 > 2$, so $1.5$ is a smaller upper bound.

The typical use of the check is to show that a theorem of analysis needs completeness.
Watch out for the belief that the theorem fails over $\mathbb{Q}$ because $g$ is not continuous there.
The function is continuous, and the failure comes from the holes in $\mathbb{Q}$.
