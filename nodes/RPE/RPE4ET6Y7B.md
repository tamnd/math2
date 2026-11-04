---
tag: RPE4ET6Y7B
kind: proof
name: Proof of Wilson's theorem by pairing inverses
msc: [11A07]
proves: 03KGGKTB2E
uses: [0SN0MAEKYX, 0TPW25CBN6, 096PW7Q014, 02WF878BH1, 0M67FWZWPQ, 00GXTQMY8Z, 0CHQKZFK5S, 051VYKA1EX, 09RDZZGJZ9, 072D5G4SK6]
methods: [0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson%27s_theorem
    locator: Elementary proof
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]]. If $p = 2$, then $(p - 1)! = 1$, and $2$ [[divides|096PW7Q014]] $1 - (-1) = 2$. So $(p - 1)! \equiv -1 \pmod p$. From now on let $p \ge 3$.
2. Let $R = \{ 1, 2, \dots, p - 1 \}$. Each $a \in R$ satisfies $p \nmid a$, so the [[greatest common divisor|02WF878BH1]] $\gcd(a, p)$ is a positive divisor of $p$ other than $p$. Thus $\gcd(a, p) = 1$.
3. Let $a \in R$. By step 2 and the [[existence of inverses modulo n|0M67FWZWPQ]], $a$ has a [[modular multiplicative inverse|00GXTQMY8Z]] $x$, so $a x \equiv 1 \pmod p$.
4. By the [[division algorithm|0CHQKZFK5S]], $x = q p + a'$ with $0 \le a' < p$. Then $a a' \equiv a x \equiv 1 \pmod p$. Since $a \cdot 0 = 0 \not\equiv 1 \pmod p$, we get $a' \ne 0$, so $a' \in R$.
5. If $b \in R$ and $a b \equiv 1 \pmod p$, then $a b \equiv a a' \pmod p$. By [[cancellation|09RDZZGJZ9]] with $\gcd(a, p) = 1$, $b \equiv a' \pmod p$. Both lie in $R$, so $b = a'$.
6. So each $a \in R$ has exactly one $a' \in R$ with $a a' \equiv 1 \pmod p$. Since $a' a \equiv 1 \pmod p$, step 5 applied to $a'$ gives $(a')' = a$.
7. Let $a \in R$. Then $a' = a$ if and only if $a^2 \equiv 1 \pmod p$, that is, $p \mid (a - 1)(a + 1)$.
8. By [[Euclid's lemma|051VYKA1EX]], this holds if and only if $p \mid a - 1$ or $p \mid a + 1$. Since $0 \le a - 1 \le p - 2$ and $2 \le a + 1 \le p$, this means $a = 1$ or $a = p - 1$.
9. Let $T = \{ 2, 3, \dots, p - 2 \}$, which is empty when $p = 3$. Let $a \in T$. If $a' = 1$, then $a \equiv a a' \equiv 1 \pmod p$, so $a = 1$. If $a' = p - 1$, then $-a \equiv a a' \equiv 1$, so $a = p - 1$. Both contradict $a \in T$.
10. So $a \mapsto a'$ maps $T$ to $T$. By steps 6 and 8, it is its own inverse and has no fixed point in $T$.
11. Hence $T$ splits into disjoint pairs $\{ a, a' \}$ with $a \ne a'$. Each pair has product $a a' \equiv 1 \pmod p$.
12. By [[compatibility with multiplication|072D5G4SK6]], $(p - 2)! = 1 \cdot \prod_{a \in T} a \equiv 1 \pmod p$. This also holds when $T$ is empty.
13. Then $(p - 1)! = (p - 1) \cdot (p - 2)! \equiv (-1) \cdot 1 = -1 \pmod p$, by compatibility with multiplication and $p - 1 \equiv -1 \pmod p$.

## Idea

Modulo a prime, every nonzero residue has a unique inverse. Only $1$ and $-1$ are their own inverses, so all the other factors of $(p - 1)!$ cancel in pairs. What remains is $1 \cdot (p - 1) \equiv -1$.
