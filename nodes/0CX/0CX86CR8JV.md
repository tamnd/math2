---
tag: 0CX86CR8JV
kind: concept
name: Integrating factor for a non-exact equation
msc: [34A05]
specializes: [07DJAZW32T]
uses: [0EC7AGJ0PX, 0MSCQNFTM8, 07DJAZW32T]
sources:
  - url: https://en.wikipedia.org/wiki/Integrating_factor
    locator: Use
---

## Summary

Let $M\, dx + N\, dy = 0$ be an equation that is not [[exact|0EC7AGJ0PX]] on an open set $D$.
An integrating factor for it is a nowhere zero differentiable function $\mu$ on $D$ such that $\mu M\, dx + \mu N\, dy = 0$ is exact.
On a rectangle, with $M$, $N$ and $\mu$ of class $C^1$, the [[test for exactness|0MSCQNFTM8]] makes this condition $(\mu M)_y = (\mu N)_x$.
The two equations have the same solutions, because $\mu$ has no zero.

## Remarks

If $(M_y - N_x)/N$ is a function $g(x)$ of $x$ only, then $\mu(x) = e^{\int g(x)\, dx}$ is an integrating factor.
If $(N_x - M_y)/M$ is a function $h(y)$ of $y$ only, then $\mu(y) = e^{\int h(y)\, dy}$ is an integrating factor.
The [[integrating factor|01THH3Y3YP]] of a linear first-order equation is the first case: $y' + p y - q = 0$ has $M = p y - q$, $N = 1$ and $(M_y - N_x)/N = p$.

## Explanations

### L1 human

Some equations are not exact, but they become exact after multiplication by a good function.
In general, it is hard to find this function.
In two common cases, the factor depends on one variable only, and a simple integral gives it.
