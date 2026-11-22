---
tag: SQS8CTP3EX
kind: proof
name: Proof of the first consequences of the vector space axioms
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 5E4VBC0A4H
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [05EGHEQZAW, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - book: isbn:9783031410253
    locator: Section 1B
---

## Proof

We derive the seven parts in order from the axioms 1 to 8 of the [[definition|05EGHEQZAW]] and the rules of the [[field|04C5ZBG1WT]] $F$, and each part may use the earlier ones.
By axiom 2 we may also write $0 + v = v$ and $(-v) + v = 0$.

1. Part 1. Let $u + w = v + w$. Add $-w$ on the right of both sides, so $(u + w) + (-w) = (v + w) + (-w)$.
2. By axiom 1 the left side is $u + (w + (-w))$, which is $u + 0 = u$ by axioms 4 and 3. In the same way the right side is $v$, so $u = v$.
3. Part 2. Let $v + z = v$. By axiom 3 also $v + 0 = v$, so $z + v = 0 + v$ by axiom 2, and part 1 gives $z = 0$.
4. Part 3. Let $v + w = 0$. By axiom 4 also $v + (-v) = 0$, so $w + v = (-v) + v$ by axiom 2, and part 1 gives $w = -v$.
5. Part 4. In $F$ we have $0 + 0 = 0$, so axiom 8 gives
$$0v = (0 + 0)v = 0v + 0v.$$
6. This equation has the form $x + z = x$ with $x = z = 0v$, so part 2 gives $0v = 0$.
7. Part 5. By axiom 3, $0 + 0 = 0$ in $V$, so axiom 7 gives $a0 = a(0 + 0) = a0 + a0$, and part 2 gives $a0 = 0$.
8. Part 6. By axioms 6 and 8 and the rule $1 + (-1) = 0$ in $F$,
$$v + (-1)v = 1v + (-1)v = (1 + (-1))v = 0v,$$
and $0v = 0$ by part 4.
9. So $v + (-1)v = 0$, and part 3 with $w = (-1)v$ gives $(-1)v = -v$.
10. Part 7. Let $av = 0$. If $a = 0$ there is nothing to prove, so assume $a \ne 0$.
11. Since $F$ is a field, $a$ has an inverse $a^{-1}$ in $F$. By axioms 6 and 5,
$$v = 1v = (a^{-1} a)v = a^{-1}(av) = a^{-1} 0,$$
and $a^{-1} 0 = 0$ by part 5, so $v = 0$.

This proves all seven parts.

## Idea

The trick for parts 4 and 5 is to write $0$ as $0 + 0$.
Multiplying gives an equation $x = x + x$, and cancellation leaves $x = 0$.
Part 6 shows that $(-1)v$ has the defining property of $-v$, and part 3 says that only one vector has that property.
Part 7 divides by $a$, which is the one place where we need $F$ to be a field and not just a ring.

## Variants

Parts 1 to 3 hold in every group, and many books prove them there first and quote them.
Some books prove part 4 by adding $-(0v)$ to both sides of $0v = 0v + 0v$, which is the argument of part 1 written out inside part 4.
The same pattern proves $0 \cdot r = 0$ in every ring, with the distributive law of the ring in place of axiom 8.
