---
tag: 3WGZ1AR5E0
kind: example
name: Maximum is not a Sheffer function
msc: ["08A40"]
topics: [WZP584JQ06]
audience: research
not_instance_of:
  - target: 1K829SJG3K
    note: every term in max is idempotent, so no constant and no negation is generated
uses: [6KFS240R42]
sources:
  - url: https://en.wikipedia.org/wiki/Sheffer_stroke
---

## Example

Let $V = \set{0, \dots, m - 1}$ with $m \ge 2$, and consider $\max$ on $V$.

1. Claim: every term $t(x_1, \dots, x_n)$ in $\max$ satisfies $t(a, \dots, a) = a$ for all $a \in V$. We use structural induction on $t$.
2. A variable $x_i$ gives $a$ at $(a, \dots, a)$.
3. If $t = \max(t_1, t_2)$ and both $t_i$ give $a$, then $t$ gives $\max(a, a) = a$.
4. The [[Sheffer function|6KFS240R42]] property needs the operation $g(x) = S x = x + 1 \bmod m$ as a term.
5. But $g(0) = 1 \ne 0$, so $g$ is not idempotent, and by step 1 it is not a term in $\max$.

So $\max$ is not a Sheffer function on $V$.

## Remarks

1. The same argument shows that $\min$ is not a Sheffer function, and that $\set{\max, \min}$ is not complete.
2. Adding the shift "$+1 \bmod m$" after $\max$ gives Webb's function, which is a Sheffer function.
3. Every idempotent operation fails for the same reason; a Sheffer function must move some constant tuple.

## Explanations

### L1 human

If all inputs are equal, the maximum returns that same value.
Any formula built from maximum does the same.
So it can never turn $0$ into $1$, and it cannot build every table.

### L2 human

1. Find a property that the operation has, here "equal inputs give the same output".
2. Show that composition keeps the property.
3. Exhibit an operation without the property.

The typical use is this preservation argument for incompleteness.
A trap: the property must survive composition; "takes all values" does not, so it cannot replace idempotence here.
