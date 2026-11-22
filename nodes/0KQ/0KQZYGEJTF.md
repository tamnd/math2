---
tag: 0KQZYGEJTF
kind: definition
name: Signature of a quadratic form
msc: [15A63, "11E04"]
defines: 07EZA80NEH
topics: [6TSCEW8QMK]
audience: ug1
uses: [0HZNE5QZDJ, 0WFED3K3DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_signature
    locator: Definition
---

## Definition

Let $V$ be a real vector space of finite dimension $n$, and let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on $V$.
Choose a basis $(e_1, \dots, e_n)$ of $V$ in which $Q(x_1 e_1 + \cdots + x_n e_n) = a_1 x_1^2 + \cdots + a_n x_n^2$.
Let $p$, $q$ and $r$ be the numbers of indices $i$ with $a_i > 0$, with $a_i < 0$ and with $a_i = 0$.
The *signature* of $Q$ is the triple $(p, q, r)$.

## Remarks

Such a basis exists by [[the diagonalization theorem|0Z3FEWZ8HA]], and by [[Sylvester's law of inertia|0WFED3K3DQ]] the triple does not depend on the choice of the basis.
So the definition makes sense.

For example, $Q(x, y) = 2xy$ is $2s^2 - 2t^2$ in the basis $(1, 1), (1, -1)$, so its signature is $(1, 1, 0)$.
Check: $Q(s(1, 1) + t(1, -1)) = 2(s + t)(s - t) = 2s^2 - 2t^2$.

For a symmetric matrix $A$ of $Q$, the numbers $p$, $q$ and $r$ count the positive, negative and zero eigenvalues of $A$, with multiplicity.
The rank of $Q$ is $p + q$.
The Minkowski form $x_1^2 - x_2^2 - x_3^2 - x_4^2$ on $\mathbb{R}^4$ has $p = 1$, $q = 3$ and $r = 0$.

Watch out: conventions vary.
Some authors write only $(p, q)$, and others call the number $p - q$ the signature.

## Explanations

### L1 human

The signature counts the plus signs, the minus signs and the zeros in a real quadratic form, after you write it as a sum of squares.
Two real quadratic forms are equivalent exactly when they have the same signature, so the signature is all you need to classify them.
For example, $x^2 + 2xy = (x + y)^2 - y^2$ has signature $(1, 1, 0)$.
