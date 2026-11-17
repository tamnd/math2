---
tag: MNS91DE23K
kind: example
name: Dividing x^2 = x by x loses a solution
msc: ["00A35", "97H30"]
topics: [958EF46EYJ]
audience: school
not_instance_of:
  - target: GQHHNV79PA
    note: dividing by x assumes x is not 0, so the argument shows only that the nonzero solutions equal 1, and the solution 0 is lost
uses: [GQHHNV79PA]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_fallacy
    locator: Division by zero
---

## Example

Claim: the equation $x^2 = x$ has the unique real solution $x = 1$.
A student writes this argument.

1. Let $x$ be a solution, so $x^2 = x$.
2. Divide both sides by $x$: $x = 1$.
3. Check: $1^2 = 1$. So $x = 1$ is the unique solution.

The claim is false, and the argument is not a valid [[proof of uniqueness|GQHHNV79PA]].
We check the condition that fails.

1. A uniqueness proof in the second form must show that every solution $x$ equals $1$.
2. Step 2 divides by $x$, which is allowed only if $x \neq 0$.
3. So the argument shows only: every solution with $x \neq 0$ equals $1$. The case $x = 0$ is not treated.
4. In that case $0^2 = 0$, so $x = 0$ is a second solution.

## Remarks

The correct solution factors instead of dividing.
$x^2 = x$ is equivalent to $x^2 - x = 0$, that is, $x(x - 1) = 0$.
A product of two real numbers is $0$ exactly when one factor is $0$, so the solutions are $x = 0$ and $x = 1$.

The same error appears whenever a variable expression is cancelled.
Cancelling $\sin x$ in $\sin x \cos x = \sin x$ loses the solutions with $\sin x = 0$, such as $x = 0$ and $x = \pi$.

## Explanations

### L1 human

Which numbers are equal to their own square?
The number $1$ works, since $1 \times 1 = 1$.
The number $0$ also works, since $0 \times 0 = 0$.
The student divided by $x$, and dividing by $0$ is not allowed.
So the student's method could not see the answer $0$.

### L2 human

We solve $x^3 = 4x$ without losing solutions.

1. Move all terms to one side: $x^3 - 4x = 0$.
2. Factor: $x(x - 2)(x + 2) = 0$.
3. A product is $0$ exactly when one factor is $0$. So $x = 0$, $x = 2$ or $x = -2$.
4. Each value satisfies the equation, and every solution is one of them.

The typical use: factor and use the zero product rule, so that each step is an equivalence.

A trap: dividing by $x$ at step 1 would give $x^2 = 4$ and the two solutions $\pm 2$, missing $x = 0$.
