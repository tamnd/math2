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

Let $V = \{0, \dots, m - 1\}$ with $m \ge 2$, and consider the operation $\max$ on $V$.
We show that it is not a [[Sheffer function|6KFS240R42]].

1. We claim that every term $t(x_1, \dots, x_n)$ in $\max$ satisfies $t(a, \dots, a) = a$ for all $a \in V$.
   We prove it by induction on the build of $t$.
2. A variable $x_i$ takes the value $a$ at $(a, \dots, a)$, so the claim holds for variables.
3. Let $t = \max(t_1, t_2)$, where $t_1$ and $t_2$ both take the value $a$ at $(a, \dots, a)$.
   Then $t$ takes the value $\max(a, a) = a$ there, so the claim holds for $t$.
4. A Sheffer function would generate the shift $g(x) = x + 1 \bmod m$.
5. But $g(0) = 1 \ne 0$, so $g$ fails the property of step 1, and it is not a term in $\max$.

So $\max$ is not a Sheffer function on $V$.

## Remarks

The argument uses one property, "equal inputs give back the same value", and checks that composition keeps it.
The same argument shows that $\min$ is not a Sheffer function, and that even the pair $\{\max, \min\}$ is not complete.
Every idempotent operation fails in the same way, so a Sheffer function must move at least one constant tuple $(a, \dots, a)$.

A small change repairs the failure.
Adding the shift after $\max$ gives Webb's function $\max(x, y) + 1 \bmod m$, which moves every constant tuple, and it is a Sheffer function by [[Webb's theorem|EPSBDVPKJP]].
So the step up, and the wrap-around from $m - 1$ to $0$, carry all the extra power.

## Explanations

### L1 human

If all inputs are equal, the maximum returns that same value.
Any formula built from the maximum does the same.
So it can never turn $0$ into $1$, and it cannot build every table.

### L2 human

The proof is a preservation argument, and it has three moves.
First find a property that the operation has, here "equal inputs give the same output".
Then show that composition keeps the property, as in steps 2 and 3.
Finally exhibit an operation without the property, here the shift.
This is the standard way to prove that a set of operations is incomplete.
Watch out: the property must survive composition.
"Takes all values" does not: exclusive or on $\{0, 1\}$ takes both values, but its composite $x \oplus x$ is the constant $0$.
