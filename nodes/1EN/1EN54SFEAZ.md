---
tag: 1EN54SFEAZ
kind: proof
name: Proof of Bézout's identity
msc: [11A05]
proves: 0DQVHMYAGA
uses: [02WF878BH1, 01BX15HSRR, 0CHQKZFK5S, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
---

## Proof

We show that the least positive integer of the form $ax + by$ is the [[greatest common divisor|02WF878BH1]].

1. Let $a$ and $b$ be integers and let $d = \gcd(a, b)$.
2. If $a = b = 0$, then $d = 0$ by convention, and $x = y = 0$ give $a x + b y = 0 = d$. From now on, $a$ and $b$ are not both $0$.
3. Then $1$ is a common divisor, so $d \ge 1$.
4. Let $S$ be the set of positive integers of the form $a x + b y$ with $x, y \in \Z$. It contains $a \cdot a + b \cdot b = a^2 + b^2 > 0$, so $S$ is nonempty.
5. By the [[well-ordering principle|01BX15HSRR]], $S$ has a least element $e$. Write $e = a x_0 + b y_0$ with $x_0, y_0 \in \Z$.
6. By the [[division algorithm|0CHQKZFK5S]], $a = e q + r$ with integers $q$, $r$ and $0 \le r < e$.
7. Then $r = a - q(a x_0 + b y_0) = a(1 - q x_0) + b(-q y_0)$, so $r$ has the form $ax + by$.
8. If $r > 0$, then $r \in S$ and $r < e$, which contradicts the choice of $e$. So $r = 0$, and $e$ [[divides|096PW7Q014]] $a$.
9. The same argument with $b$ in place of $a$ shows that $e \mid b$. So $e$ is a common divisor, and $e \le d$ because $d$ is the largest one.
10. Since $d \mid a$ and $d \mid b$, write $a = d a'$ and $b = d b'$ with integers $a'$, $b'$. Then $e = d(a' x_0 + b' y_0)$.
11. Here $e > 0$ and $d > 0$, so the integer $a' x_0 + b' y_0$ is positive. Hence it is at least $1$, and $e \ge d$.
12. By steps 9 and 11, $e = d$. So $a x_0 + b y_0 = d$, and $x = x_0$, $y = y_0$ are the required integers.

## Idea

The integers $ax + by$ form a set that is closed under subtracting multiples of each other. Its least positive element divides $a$ and $b$, because the remainder of a division stays in the set and is smaller. Every common divisor of $a$ and $b$ divides this element, so it is the greatest common divisor.
