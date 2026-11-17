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
We use the fact that the [[primitive recursive relations|QQQRJA90EP]] are closed under $\neg$, $\land$, $\lor$ and bounded quantifiers $\exists y \le x$ and $\forall y \le x$.

1. Divisibility. Let $\mathrm{Div}(d, x)$ be $\exists q \le x \, (d \cdot q = x)$. The relation $d \cdot q = x$ is primitive recursive, and the bounded quantifier keeps it primitive recursive. For $x \ge 1$, every $q$ with $d \cdot q = x$ satisfies $q \le x$; for $x = 0$ the witness is $q = 0$. So the bound loses no witnesses.
2. Primality. Let $\mathrm{Prime}(p)$ be $2 \le p \land \forall d \le p \, (\mathrm{Div}(d, p) \to d = 1 \lor d = p)$. Every divisor of $p \ge 1$ is at most $p$, so the bound loses nothing, and the relation is primitive recursive.
3. Evenness. Let $\mathrm{Even}(x)$ be $\exists q \le x \, (q + q = x)$. A witness $q$ satisfies $q \le q + q = x$, so the bound loses nothing.
4. The Goldbach property. Let $G(x)$ be $\neg \mathrm{Even}(x) \lor x \le 2 \lor \exists p \le x \, \exists q \le x \, (\mathrm{Prime}(p) \land \mathrm{Prime}(q) \land p + q = x)$. If $p + q = x$, then $p \le x$ and $q \le x$, so the bounds lose nothing. By steps 1 to 3 and the closure properties, $G$ is primitive recursive.
5. The function. Let $g$ be the characteristic function of $G$: $g(x) = 1$ if $G(x)$ holds and $g(x) = 0$ otherwise. It is a [[primitive recursive function|5NVA2JRHPV]], so some function symbol of the [[definition|330YAP9Y4Q]] has $g$ as its value in $\mathfrak{N}$.
6. Correctness. For each $n$, $g(n) = 1$ if and only if $n$ is odd, or $n \le 2$, or $n$ is a sum of two primes. So $g(n) = 1$ for all $n$ if and only if Goldbach's conjecture is true.

So the formula $g(x) = 1$ of $\mathsf{PRA}$ expresses Goldbach's conjecture.

## Remarks

The conjecture has the logical form $\forall x \, \varphi(x)$ with $\varphi$ a $\Delta_0$ formula, that is, it is a $\Pi_1$ sentence.
Every $\Pi_1$ sentence has a free-variable form in $\mathsf{PRA}$ by the same method.
For each numeral $\overline{n}$, $\mathsf{PRA}$ proves the true one of $g(\overline{n}) = 1$ and $g(\overline{n}) = 0$, by computing with the defining equations.
So if the conjecture is false, with a counterexample $n$, then $\mathsf{PRA}$ proves $g(\overline{n}) = 0$, and the substitution rule shows that $\mathsf{PRA}$ refutes $g(x) = 1$.
Contrapositively, if $\mathsf{PRA}$ does not refute $g(x) = 1$, then the conjecture is true.
Whether $\mathsf{PRA}$ proves $g(x) = 1$ is open, since the conjecture itself is open.
A statement of the form $\forall x \, \exists y \, \psi(x, y)$, such as "there are infinitely many primes", needs a function that produces $y$ from $x$ before $\mathsf{PRA}$ can state it.

## Explanations

### L1 human

Goldbach's conjecture says that $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$, and so on for every even number from $4$ on.
For a single number, a computer can check the claim in finitely many steps, by trying all pairs of smaller numbers.
So there is a computable test $g$ that answers $1$ ("the claim holds for $x$") or $0$.
The conjecture says that the test answers $1$ for every number, and this is one equation with a variable.

### L2 human

We compute $g(10)$ with the definition.

1. $\mathrm{Even}(10)$ holds with the witness $q = 5$.
2. $10 \le 2$ is false.
3. $\mathrm{Prime}(3)$ holds: the only $d \le 3$ with $\mathrm{Div}(d, 3)$ are $d = 1$ and $d = 3$.
4. $\mathrm{Prime}(7)$ holds: the only $d \le 7$ with $\mathrm{Div}(d, 7)$ are $d = 1$ and $d = 7$.
5. $3 + 7 = 10$, so the third disjunct of $G(10)$ holds, and $g(10) = 1$.

The typical use is to transfer a number-theoretic statement into a free-variable formula, so that a finitist consistency or conservation argument applies to it.
A trap is to forget the bounds in steps 1 to 4: an unbounded quantifier would make the relation only computably enumerable, not primitive recursive.
