---
tag: 5MWBX5QWGJ
kind: proof
name: Proof that Z/nZ is a field if and only if n is prime
msc: [11A07]
proves: 0NV6E43P4A
uses: [01N3AYAA6N, 0QA8CHH8MG, 0SN0MAEKYX, 0N3ADXHNTQ, 02WF878BH1, 0DQVHMYAGA, 0GYGHKX834]
sources:
  - url: https://proofwiki.org/wiki/Ring_of_Integers_Modulo_Prime_is_Field
  - url: https://proofwiki.org/wiki/Ring_of_Integers_Modulo_Composite_is_not_Integral_Domain
---

## Proof

1. Let $n \ge 2$ be an integer. Write $\overline{a}$ for the class of an integer $a$ in the ring $\Z/n\Z$ of [[integers modulo n|01N3AYAA6N]].
2. The ring $\Z/n\Z$ is a [[commutative ring|0GYGHKX834]], because the operations on classes come from the commutative operations on $\Z$.
3. We have $\overline{a} = \overline{0}$ if and only if $n \mid a$. In particular, $\overline{1} \neq \overline{0}$, since $n \ge 2$ does not divide $1$.
4. First suppose that $n$ is not a [[prime number|0SN0MAEKYX]]. Since $n \ge 2$, $n$ is [[composite|0N3ADXHNTQ]]. So $n$ has a positive divisor $a$ with $a \neq 1$ and $a \neq n$. Put $b = n / a$. Then $1 < a < n$, and so $1 < b < n$.
5. By step 3, $\overline{a} \neq \overline{0}$ and $\overline{b} \neq \overline{0}$, since $0 < a, b < n$. But $\overline{a} \cdot \overline{b} = \overline{n} = \overline{0}$.
6. Suppose that $\overline{a}$ had an inverse $\overline{c}$, so that $\overline{c} \cdot \overline{a} = \overline{1}$. Then $\overline{b} = \overline{c} \cdot \overline{a} \cdot \overline{b} = \overline{c} \cdot \overline{0} = \overline{0}$.
7. This contradicts step 5. So $\overline{a}$ is a nonzero element without inverse, and $\Z/n\Z$ is not a [[field|0QA8CHH8MG]].
8. Now suppose that $n = p$ is a prime number. By steps 2 and 3, it remains to show that every nonzero class has an inverse.
9. Let $\overline{a} \neq \overline{0}$, so $p \nmid a$ by step 3. Let $d = \gcd(a, p)$ be the [[greatest common divisor|02WF878BH1]].
10. Since $d$ is a positive divisor of the prime $p$, $d = 1$ or $d = p$. Since $d \mid a$ and $p \nmid a$, $d \neq p$. So $d = 1$.
11. By [[Bézout's identity|0DQVHMYAGA]], there are integers $x, y$ with $a x + p y = 1$.
12. Passing to classes, $\overline{a} \cdot \overline{x} + \overline{p} \cdot \overline{y} = \overline{1}$. Since $\overline{p} = \overline{0}$, this gives $\overline{a} \cdot \overline{x} = \overline{1}$.
13. So $\overline{x}$ is an inverse of $\overline{a}$, and $\Z/p\Z$ is a field.
14. By steps 7 and 13, $\Z/n\Z$ is a field if and only if $n$ is prime.

## Idea

A factorization $n = a b$ gives two nonzero classes with product zero, and such a class cannot be invertible. For a prime $p$, any $a$ not divisible by $p$ is coprime to $p$. Bézout's identity then writes $1$ as $a x$ plus a multiple of $p$, so $x$ inverts $a$ modulo $p$.
