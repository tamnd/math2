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
We prove that $f$ is a bijection with the templates of [[proving injectivity and surjectivity|DD2P85Y8E9]].
The surjectivity half finds a solution of $f(x) = y$ without a formula for it.

1. Injectivity.
   Let $f(a) = f(b)$, so $a^3 - b^3 + a - b = 0$.
2. Use $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ to factor out $a - b$:
   $$(a - b)(a^2 + ab + b^2 + 1) = 0.$$
3. Complete the square to see that the second factor is positive:
   $$a^2 + ab + b^2 + 1 = \left(a + \frac{b}{2}\right)^2 + \frac{3}{4} b^2 + 1 \ge 1.$$
4. A product of real numbers is $0$ only when a factor is $0$, and the second factor is not $0$, so $a = b$.
   Hence $f$ is [[injective|09NWETVTNY]].
5. Surjectivity.
   Let $y \in \mathbb{R}$, and put $M = \lvert y \rvert + 1$.
6. The function $f$ is a polynomial, so it is [[continuous|0X3WGX95FE]] on $[-M, M]$.
7. At the right end, $f(M) = M^3 + M > M > \lvert y \rvert \ge y$, because $M^3 > 0$.
8. At the left end, $f(-M) = -M^3 - M < -M < -\lvert y \rvert \le y$.
9. So $f(-M) < y < f(M)$, and the [[intermediate value theorem|00KAFBR32E]] gives an $x \in [-M, M]$ with $f(x) = y$.
   Hence $f$ is [[surjective|01RVCMSN5N]], and with step 4 it is a bijection.

Check with numbers: $f(1) = 2$ and $f(2) = 10$, so the solution of $x^3 + x = 5$ lies between $1$ and $2$.
It is close to $1.516$, since
$$1.516^3 + 1.516 \approx 3.484 + 1.516 = 5.000.$$

## Remarks

The example shows that a surjectivity proof needs an element $x$, but not a formula for it.
An existence theorem can supply the element, and here the intermediate value theorem does.
The injectivity half has a second proof: $f'(x) = 3x^2 + 1 > 0$, so $f$ is strictly increasing, and a strictly increasing function is injective.

Change one sign and injectivity breaks.
For $g(x) = x^3 - x$, the factor in step 2 becomes $a^2 + ab + b^2 - 1$, which is $0$ at $a = 1$, $b = 0$, and indeed $g(-1) = g(0) = g(1) = 0$.
Surjectivity survives the change, by steps 5 to 9 with $M = \lvert y \rvert + 2$, as the L2 explanation checks.
So the two properties are independent of each other.

## Explanations

### L1 human

The rule "cube the number and add the number" gives $2$ for $1$, $10$ for $2$ and $-2$ for $-1$.
Bigger inputs always give bigger outputs, so two different inputs never share an output.
Every number is also an output, because the outputs move without jumps from very negative to very positive.
For the target $5$, the input lies between $1$ and $2$, where the outputs are $2$ and $10$.

### L2 human

We check the claims about $g(x) = x^3 - x$.

1. Compute $g(-1) = -1 + 1 = 0$, $g(0) = 0$ and $g(1) = 1 - 1 = 0$.
   Three different inputs share the output $0$, so $g$ is not injective.
2. For surjectivity, let $y \in \mathbb{R}$ and $M = \lvert y \rvert + 2$.
3. Since $M \ge 2$, we have $M^2 - 1 \ge 3$, so
   $$g(M) = M(M^2 - 1) \ge 3M > \lvert y \rvert \ge y.$$
4. The function $g$ is odd, so $g(-M) = -g(M) \le -3M < y$.
5. The intermediate value theorem gives an $x$ with $g(x) = y$, so $g$ is surjective.

The template applies to every polynomial of odd degree, which has no simple inverse formula in general.
Watch out: "every $y$ has a solution" does not give injectivity, and "different inputs give different outputs" does not give surjectivity.
