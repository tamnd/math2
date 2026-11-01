---
tag: D0ZXXEYNK8
kind: definition
name: Euler–Maruyama method
msc: [65C30, 60H35, 60H10]
defines: 22T0NVC56P
uses: [22735FGJV6, 0JARTXX4XP, 05AQE0QR0D, D48DR46B97]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
---

## Definition

Let $T > 0$, let $x_0 \in \R$, and let $a, b \colon [0, T] \times \R \to \R$ be functions.
Consider the stochastic differential equation $dX_t = a(t, X_t) \, dt + b(t, X_t) \, dB_t$ with $X_0 = x_0$, where $B$ is a [[Brownian motion|22735FGJV6]].
Let $N \ge 1$, let $\Delta t = T / N$, and let $t_n = n \, \Delta t$ for $0 \le n \le N$.
The *Euler–Maruyama approximation* is the sequence $(Y_n)_{0 \le n \le N}$ with $Y_0 = x_0$ and
$$Y_{n+1} = Y_n + a(t_n, Y_n) \, \Delta t + b(t_n, Y_n) \, \Delta B_n, \quad \Delta B_n = B_{t_{n+1}} - B_{t_n}.$$

## Remarks

The increments $\Delta B_n$ are independent and [[normal|05AQE0QR0D]] with mean $0$ and variance $\Delta t$.
In a simulation one takes $\Delta B_n = \sqrt{\Delta t} \, Z_n$ with independent standard normal $Z_n$.
Example: for [[geometric Brownian motion|D48DR46B97]], $a(t, x) = \mu x$ and $b(t, x) = \sigma x$, so $Y_{n+1} = Y_n (1 + \mu \Delta t + \sigma \Delta B_n)$.
Non-example: the update $Y_{n+1} = Y_n + a(t_n, Y_n) \Delta t + b(t_n, Y_n) \Delta t \, Z_n$ uses noise of size $\Delta t$ instead of $\sqrt{\Delta t}$, so its noise vanishes in the limit.
If $b = 0$, the scheme is the [[Euler method|0JARTXX4XP]] for the ordinary equation $x' = a(t, x)$.
Assume that $a$ and $b$ are Lipschitz in $x$ uniformly in $t$, grow at most linearly, and are Hölder continuous of exponent $1/2$ in $t$.
Then $E\abs{X_T - Y_N} \le C \sqrt{\Delta t}$ for a constant $C$.
