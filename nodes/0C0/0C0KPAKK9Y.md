---
tag: 0C0KPAKK9Y
kind: counterexample
name: Separately continuous but not continuous function
msc: [26B05]
uses: [0JEJATBVD7, 0BJ6H85DRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_real_variables
    locator: Continuity and limit
---

## Counterexample

One could guess this: a function of two variables is continuous when it is continuous in each variable for each fixed value of the other variable.
This is false.
Let $f \colon \mathbb{R}^2 \to \mathbb{R}$ be given by $f(x, y) = \dfrac{xy}{x^2 + y^2}$ for $(x, y) \ne (0, 0)$ and $f(0, 0) = 0$.
For each fixed $b$, the function $x \mapsto f(x, b)$ is continuous on $\mathbb{R}$, and for each fixed $a$, the function $y \mapsto f(a, y)$ is continuous on $\mathbb{R}$.
But $f$ is not [[continuous|0JEJATBVD7]] at $(0, 0)$.

## Remarks

For $b \ne 0$, the function $x \mapsto f(x, b)$ is a quotient of polynomials with a denominator that is never $0$. For $b = 0$, it is the constant $0$. The same holds for the other variable.
On the line $y = x$ with $x \ne 0$, the value is $f(x, x) = 1/2$. So $f(x, x) \to 1/2 \ne f(0, 0)$ as $x \to 0$, by the [[test with different paths|0BJ6H85DRQ]].

## Explanations

### L1 human

Separate continuity checks only the two directions along the axes.
On both axes this function is $0$, so nothing goes wrong there.
On the diagonal it is $1/2$ everywhere except at the origin, so the function jumps there.
