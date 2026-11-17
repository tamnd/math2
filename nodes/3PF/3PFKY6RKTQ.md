---
tag: 3PFKY6RKTQ
kind: example
name: The function x^3 + x is a bijection of the real numbers
msc: ["00A35", "26A06"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [DD2P85Y8E9]
uses: [DD2P85Y8E9, 09NWETVTNY, 01RVCMSN5N, 00KAFBR32E, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: lead section
---

## Example

Define $f \colon \mathbb{R} \to \mathbb{R}$ by $f(x) = x^3 + x$.
We prove that $f$ is a bijection with the patterns of [[proving injectivity and surjectivity|DD2P85Y8E9]].
The surjectivity half shows a pattern without an explicit inverse.

1. Injectivity. Let $a, b \in \mathbb{R}$ with $f(a) = f(b)$. Then $a^3 + a = b^3 + b$, so $a^3 - b^3 + a - b = 0$.
2. We factor, with $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$: the equation becomes $(a - b)(a^2 + ab + b^2 + 1) = 0$.
3. Complete the square: $a^2 + ab + b^2 = \left(a + \tfrac{b}{2}\right)^2 + \tfrac{3}{4} b^2 \ge 0$. So $a^2 + ab + b^2 + 1 \ge 1 > 0$.
4. A product of two real numbers is zero only if a factor is zero. The second factor is positive, so $a - b = 0$ and $a = b$. Hence $f$ is [[injective|09NWETVTNY]].
5. Surjectivity. Let $y \in \mathbb{R}$. The equation $x^3 + x = y$ is a cubic equation, and we do not solve it by a formula.
6. The function $f$ is a polynomial, so it is [[continuous|0X3WGX95FE]] on $\mathbb{R}$.
7. Let $M = \lvert y \rvert + 1$. Then $f(M) = M^3 + M > M > y$, because $M^3 > 0$ and $M > \lvert y \rvert \ge y$.
8. In the same way $f(-M) = -M^3 - M < -M < y$, because $-M < -\lvert y \rvert \le y$.
9. So $f(-M) < y < f(M)$. By the [[intermediate value theorem|00KAFBR32E]] on $[-M, M]$, there is an $x$ with $f(x) = y$. Hence $f$ is [[surjective|01RVCMSN5N]].
10. Steps 4 and 9 show that $f$ is a bijection.

A check with numbers: $f(1) = 2$ and $f(2) = 10$, so the solution of $x^3 + x = 5$ lies between $1$ and $2$.
It is near $1.516$, since $1.516^3 + 1.516 \approx 3.484 + 1.516 = 5.000$.

## Remarks

1. The example shows that a surjectivity proof needs an element $x$, but not a formula for it. An existence theorem can supply the element.
2. The injectivity half can also use monotonicity. The derivative $f'(x) = 3x^2 + 1$ is positive, so $f$ is strictly increasing, and a strictly increasing function is injective.
3. If we change the function to $g(x) = x^3 - x$, injectivity fails: $g(-1) = g(0) = g(1) = 0$. In step 2 the second factor becomes $a^2 + ab + b^2 - 1$, which can be zero, for example at $a = 1$ and $b = 0$.
4. The function $g(x) = x^3 - x$ is still surjective, by the same steps 6 to 9 with $M = \lvert y \rvert + 2$. So the two properties are independent.

## Explanations

### L1 human

The rule "cube the number and add the number" gives $2$ for $1$, $10$ for $2$, and $-2$ for $-1$.
Bigger inputs always give bigger outputs, so two different inputs never give the same output.
Every number is also reached as an output, because the outputs move without jumps from very negative to very positive.
For the target $5$, the input lies between $1$ and $2$, since the outputs there are $2$ and $10$.

### L2 human

We check Remarks 3 and 4 in detail, for $g(x) = x^3 - x$.

1. $g(-1) = -1 + 1 = 0$, $g(0) = 0$ and $g(1) = 1 - 1 = 0$.
2. So three different inputs give the value $0$, and $g$ is not injective.
3. For the target $y = 0$, each of these inputs is a solution, so surjectivity at $y = 0$ holds.
4. For a general $y$, take $M = \lvert y \rvert + 2$. Then $g(M) = M(M^2 - 1) \ge 3M > y$, because $M \ge 2$ gives $M^2 - 1 \ge 3$.
5. In the same way $g(-M) \le -3M < y$, and the intermediate value theorem gives a solution.

The typical use of the pattern is a function given by a formula that has no simple inverse, such as a polynomial of odd degree.
A trap is to think that "every $y$ has a solution" gives injectivity, or that "different inputs give different outputs" gives surjectivity.
