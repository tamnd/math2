---
tag: Z2R1JY1CHS
kind: statement
role: theorem
name: Morrey's inequality
msc: ["46E35", 26D10]
uses: [M4CEZ5K9HP, P101AX1ZSC, 012PBA0FMD, JQ9WXC729D, B03CA692K3, GZTT6FT18G, 2PVQY9PCT4]
about: [M4CEZ5K9HP, P101AX1ZSC]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_inequality
---

## Statement

Let $n \ge 1$, let $n < p \le \infty$, and let $\gamma = 1 - n/p$.
There is a constant $C = C(n, p)$ such that every continuously differentiable function $u \colon \R^n \to \R$ satisfies
$$\sup_{x \in \R^n} \abs{u(x)} + \sup_{x \ne y} \frac{\abs{u(x) - u(y)}}{\abs{x - y}^{\gamma}} \le C \norm{u}_{W^{1,p}(\R^n)}.$$
Consequently, each $u$ in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(\R^n)$ agrees almost everywhere with a function in the [[Hölder space|P101AX1ZSC]] $C^{0,\gamma}(\R^n)$.
The norm of this function in $C^{0,\gamma}(\R^n)$ is at most $C \norm{u}_{W^{1,p}(\R^n)}$.

## Remarks

The key step is the bound $\frac{1}{\abs{B}} \int_B \abs{u(y) - u(x)} \, dy \le C \int_B \frac{\abs{\nabla u(y)}}{\abs{x - y}^{n - 1}} \, dy$ for a ball $B$ centred at $x$.
By [[Hölder's inequality|JQ9WXC729D]], the kernel $\abs{x - y}^{1 - n}$ lies in $L^{p'}(B)$ exactly when $p > n$, and this gives a bound by $r^{1 - n/p} \norm{\nabla u}_{L^p}$ for the ball of radius $r$.
Comparing $u(x)$ and $u(y)$ with the average of $u$ on a ball containing both gives the [[Hölder continuity|012PBA0FMD]] bound.

The hypothesis $p > n$ is needed.
For $n = 2$ and $p = 2$, the function $\log \log (1/\abs{x})$, cut off away from the origin, lies in $W^{1,2}$ but is unbounded near $0$.

For a bounded open set $U$ with $C^1$ boundary, the same holds with $\R^n$ replaced by $U$ and $C$ depending also on $U$.
Together with the [[Sobolev inequality|B03CA692K3]] it forms the [[Sobolev embedding theorem|GZTT6FT18G]].

## Explanations

### L1 human

When the slope of a function is integrable to a high enough power, larger than the dimension, the function cannot jump or blow up.
It is then continuous, and even Hölder continuous with an exponent that measures how much $p$ exceeds $n$.
In one dimension any $p > 1$ is enough, which matches the fact that $\abs{u(x) - u(y)} \le \abs{x - y}^{1 - 1/p} \norm{u'}_{L^p}$ by Hölder's inequality.

### L2 human

Morrey's inequality is how one shows that weak solutions are continuous functions.
In dimension $n$, a function in $W^{k,p}$ with $kp > n$ is continuous, by combining Morrey's inequality with the Sobolev inequality for the lower derivatives.
This is the step that turns $L^2$ regularity results, such as those of [[elliptic regularity|2PVQY9PCT4]], into classical smoothness.
