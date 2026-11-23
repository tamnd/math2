---
tag: 7QDEKB8HC8
kind: example
name: Goldbach's conjecture as an equation of primitive recursive arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [WCXH72T8D8]
uses: [WCXH72T8D8, 330YAP9Y4Q, 063JNBSMJ0, 01826KMG2H, QQQRJA90EP, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: lead section
  - book: isbn:9780521857840
---

## Example

[[Goldbach's conjecture|063JNBSMJ0]] says that every even number greater than $2$ is the sum of two [[prime numbers|01826KMG2H]].
We write it as one equation $g(x) = 1$ of [[primitive recursive arithmetic|WCXH72T8D8]], with a free variable $x$ and no quantifiers.
The tool is that the [[primitive recursive relations|QQQRJA90EP]] are closed under $\neg$, $\land$, $\lor$ and the bounded quantifiers $\exists y \le x$ and $\forall y \le x$.
So each step below builds a primitive recursive relation, and each bound must lose no witness.

1. Divisibility.
   Let $\mathrm{Div}(d, x)$ be $\exists q \le x \, (d \cdot q = x)$.
   For $x \ge 1$, every $q$ with $d \cdot q = x$ has $d \ge 1$ and so $q \le x$, and for $x = 0$ the witness is $q = 0$.
2. Primality.
   Let $\mathrm{Prime}(p)$ be $2 \le p \land \forall d \le p \, (\mathrm{Div}(d, p) \to d = 1 \lor d = p)$.
   Every divisor of a number $p \ge 1$ is at most $p$, so the bound loses nothing.
3. Evenness.
   Let $\mathrm{Even}(x)$ be $\exists q \le x \, (q + q = x)$.
   A witness satisfies $q \le q + q = x$.
4. The Goldbach property.
   Let $G(x)$ be $\neg \mathrm{Even}(x) \lor x \le 2 \lor \exists p \le x \, \exists q \le x \, (\mathrm{Prime}(p) \land \mathrm{Prime}(q) \land p + q = x)$.
   If $p + q = x$, then $p \le x$ and $q \le x$, so the bounds lose nothing.
5. The function.
   Let $g$ be the characteristic function of $G$, with $g(x) = 1$ when $G(x)$ holds and $g(x) = 0$ otherwise.
   It is a [[primitive recursive function|5NVA2JRHPV]], so a function symbol of the [[definition|330YAP9Y4Q]] denotes it.
6. Correctness.
   For each $n$, $g(n) = 1$ exactly when $n$ is odd, or $n \le 2$, or $n$ is a sum of two primes.
   So $g(n) = 1$ for every $n$ exactly when Goldbach's conjecture is true.

So the free-variable formula $g(x) = 1$ of $\mathsf{PRA}$ expresses Goldbach's conjecture.

## Remarks

The conjecture has the form $\forall x \, \varphi(x)$ with $\varphi$ a bounded formula, so it is a $\Pi_1$ sentence.
Every $\Pi_1$ sentence gets a free-variable form in $\mathsf{PRA}$ by the same method.

For each numeral $\overline{n}$, $\mathsf{PRA}$ proves the true one of $g(\overline{n}) = 1$ and $g(\overline{n}) = 0$, by computing with the defining equations.
Suppose the conjecture fails at some $n$.
Then $\mathsf{PRA}$ proves $g(\overline{n}) = 0$, so it cannot also prove $g(x) = 1$, since substitution would give $g(\overline{n}) = 1$ and $\mathsf{PRA}$ is consistent.
Whether $\mathsf{PRA}$ proves $g(x) = 1$ is open, because the conjecture itself is open.

The method stops at one quantifier.
A sentence $\forall x \, \exists y \, \psi(x, y)$, such as "there is a prime above every number", needs a function that produces $y$ from $x$ before $\mathsf{PRA}$ can state it.

## Explanations

### L1 human

Goldbach's conjecture says that $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, and so on for every even number from $4$ on.
For one number, a computer can check the claim in finitely many steps, by trying all pairs of smaller numbers.
So there is a computable test $g$ that answers $1$ when the claim holds for $x$ and $0$ when it fails.
The conjecture says that the test answers $1$ for every number, and that is one equation with a variable.

### L2 human

We compute $g(10)$ from the definition.
First, $\mathrm{Even}(10)$ holds with the witness $q = 5$, and $10 \le 2$ is false, so the first two disjuncts of $G(10)$ fail.
Next, $3$ is prime, since the only $d \le 3$ with $\mathrm{Div}(d, 3)$ are $1$ and $3$.
In the same way $7$ is prime, since its only divisors up to $7$ are $1$ and $7$.
Since
$$3 + 7 = 10,$$
the third disjunct holds with $p = 3$ and $q = 7$, so $g(10) = 1$.

The typical use is to turn a statement of number theory into a free-variable formula, so that a finitist consistency or conservation argument applies to it.
Watch out for the bounds in steps 1 to 4.
An unbounded quantifier would make the relation only computably enumerable, and then $g$ need not be primitive recursive.
