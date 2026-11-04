---
tag: 9DM7JGR0K4
kind: proof
name: Proof that the complex numbers cannot be ordered
msc: [12J15]
proves: 01CJRJKDAA
uses: [010JCV9J4E, 07KBQCG9KV, 0316AYH1SC, 011C29Q1S1, 0FRSR10DWF, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Ordered_field
    locator: Orderability of fields
---

## Proof

We argue by contradiction.

1. Assume that $\le$ is a [[total order|0316AYH1SC]] on $\C$ that makes $\C$ an [[ordered field|010JCV9J4E]].
Its two axioms are: $a \le b$ implies $a + c \le b + c$, and $0 \le a$, $0 \le b$ imply $0 \le a b$.
2. Claim: for each $x \in \C$, we have $(-x)(-x) = x x$.
Write $x = p + q i$ with $p, q$ real. Then $-x = (-p) + (-q) i$.
The product rule for [[complex numbers|09FTAET5Z4]] gives $(-x)(-x) = (p^2 - q^2) + 2 p q \, i = x x$.
3. Claim: $0 \le x x$ for each $x \in \C$. Since the order is total, $0 \le x$ or $x \le 0$.
4. If $0 \le x$, then the second axiom with $a = b = x$ gives $0 \le x x$.
5. If $x \le 0$, the first axiom with $c = -x$ gives $0 \le -x$. The second axiom gives $0 \le (-x)(-x)$, which is $x x$ by step 2.
6. By step 3 with $x = 1$, we get $0 \le 1$.
7. By step 3 with $x = i$, we get $0 \le i^2$. By [[i squared is minus one|07KBQCG9KV]], this says $0 \le -1$.
8. Adding $1$ to both sides of $0 \le -1$ gives $1 \le 0$, by the first axiom.
9. A total order is a [[partial order|011C29Q1S1]], so it is antisymmetric. Steps 6 and 8 then give $0 = 1$.
10. But $0 \neq 1$ in $\C$, because $\C$ is a [[field|0FRSR10DWF]]. This contradiction shows that no such order exists.

## Idea

In any ordered field every square is nonnegative, so $1 = 1^2 \ge 0$.
In $\C$ the number $-1$ is also a square, namely $i^2$, so $-1 \ge 0$ as well.
These two facts force $0 = 1$, which is impossible.
