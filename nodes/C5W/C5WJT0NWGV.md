---
tag: C5WJT0NWGV
kind: statement
role: theorem
name: Milstein method
msc: [65C30, 60H35]
uses: [B219G9SHJA, 22735FGJV6, 22T0NVC56P, 2J1RVQB0CM]
about: [B219G9SHJA]
sources:
  - url: https://en.wikipedia.org/wiki/Milstein_method
---

## Statement

Let $W$ be a one-dimensional [[Wiener process|22735FGJV6]], and consider the scalar Itô [[stochastic differential equation|B219G9SHJA]]
$$dX_t = a(X_t)\, dt + b(X_t)\, dW_t, \qquad X_0 = x_0 \in \R, \qquad 0 \le t \le T.$$
Assume that $a$ and $b$ are twice continuously differentiable with bounded first and second derivatives, and that $b b'$ is globally Lipschitz continuous.
Let $h = T/N$, $t_n = n h$ and $\Delta W_n = W_{t_{n+1}} - W_{t_n}$.
The Milstein method sets $Y_0 = x_0$ and
$$Y_{n+1} = Y_n + a(Y_n)\, h + b(Y_n)\, \Delta W_n + \tfrac12\, b(Y_n)\, b'(Y_n) \left( (\Delta W_n)^2 - h \right).$$
Then the method has strong order $1$: there is a constant $C$, independent of $N$, such that
$$\max_{0 \le n \le N} \left( \mathbb{E} \abs{X_{t_n} - Y_n}^2 \right)^{1/2} \le C h.$$

## Remarks

The scheme is the Itô–Taylor expansion of the solution over one step, cut after the terms of order $h$ in mean square.
Applying [[Itô's lemma|2J1RVQB0CM]] to $b(X_t)$ shows that the leading neglected term of the [[Euler–Maruyama method|22T0NVC56P]] is $b b' \int_{t_n}^{t_{n+1}} (W_s - W_{t_n})\, dW_s$, and this double integral equals $\frac12((\Delta W_n)^2 - h)$.
The Euler–Maruyama method omits this term and has strong order only $1/2$ when $b' \ne 0$; when $b$ is constant, both methods coincide.
Example: for geometric Brownian motion $dX = \mu X\, dt + \sigma X\, dW$, the method reads $Y_{n+1} = Y_n \left( 1 + \mu h + \sigma \Delta W_n + \frac{\sigma^2}{2} ((\Delta W_n)^2 - h) \right)$.
For systems driven by several Wiener processes, the analogous scheme needs the iterated integrals $\int\!\!\int dW^i\, dW^j$, which are not functions of the increments unless a commutativity condition holds.

## Explanations

### L1 human

Simulating a random differential equation step by step, the simplest method treats the noise strength as frozen over each step.
When the noise strength depends on the state, this ignores how the noise changes itself during the step.
Milstein's method adds one correction term for this effect, built from the square of the random increment.
With it, halving the step size halves the pathwise error, instead of reducing it only by a factor $\sqrt{2}$.

### L2 human

Strong order measures the error of individual paths and matters for multilevel Monte Carlo and for pathwise simulation.
Weak order measures the error of expectations, and there Euler–Maruyama and Milstein both have order $1$.
The extra term costs one derivative of $b$; derivative-free variants replace $b'$ by a difference quotient, as in stochastic Runge–Kutta methods.
