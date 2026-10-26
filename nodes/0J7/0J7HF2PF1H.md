---
tag: 0J7HF2PF1H
kind: definition
name: Picard–Lindelöf hypotheses
msc: [34A12]
defines: 0QXM0A9878
uses: [055VVSN00V, 075VBY4K4X]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Theorem
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Optimization of the solution's interval
---

## Definition

Let $t_{\min} \le t_0 \le t_{\max}$ be real numbers, let $J = [t_{\min}, t_{\max}]$, let $x_0 \in \mathbb{R}^n$, and let $a, L, K \ge 0$.
Let $B = \{x \in \mathbb{R}^n : \|x - x_0\| \le a\}$, and let $f : J \times \mathbb{R}^n \to \mathbb{R}^n$ be a function.
The function $f$ satisfies the Picard–Lindelöf hypotheses at $(t_0, x_0)$ with constants $a, L, K$ if these four conditions hold.
(1) For each $t \in J$, the map $x \mapsto f(t, x)$ is $K$-Lipschitz on $B$ ([[Lipschitz condition|055VVSN00V]]).
(2) For each $x \in B$, the map $t \mapsto f(t, x)$ is continuous on $J$.
(3) For each $t \in J$ and $x \in B$, $\|f(t, x)\| \le L$.
(4) $L \cdot \max(t_{\max} - t_0,\ t_0 - t_{\min}) \le a$.

## Remarks

Conditions (1) and (2) together imply that $f$ is continuous on $J \times B$.
Condition (4) makes the time interval short enough. A curve that starts at $x_0$ with speed at most $L$ cannot leave $B$ during the time interval $J$.
Under these hypotheses, the [[Picard–Lindelöf theorem|0P6KRD5B7A]] gives a unique solution of $x' = f(t, x)$, $x(t_0) = x_0$ on $J$.
A [[$C^1$ vector field satisfies these hypotheses|03Z9V0Y78A]] on a small time interval.

## Explanations

### L1 human


These are the conditions that make the proof of existence and uniqueness work.
The field must be continuous in time, Lipschitz in space and bounded near the start point.
The time interval must be so short that the solution stays in the region where we control the field.
