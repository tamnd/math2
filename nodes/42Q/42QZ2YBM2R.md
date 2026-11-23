---
tag: 42QZ2YBM2R
kind: example
name: A filtration of the successor model on the natural numbers
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [6ZZSHAKG5F]
uses: [6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV, G8VGTW9P4F]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M}$ with these parts:
$$W = \mathbb{N}, \quad R = \{ (n, n + 1) : n \in \mathbb{N} \}, \quad V(p) = \{ n : n \text{ even} \}.$$
Take $\Sigma = \{ p, \square p \}$, which is closed under subformulas.
We build the smallest and the largest [[filtration|6ZZSHAKG5F]] of $\mathfrak{M}$ through $\Sigma$.

### The classes

The formula $\square p$ is true at $n$ exactly when $n + 1$ is even, that is, when $n$ is odd.
So the even numbers make $p$ true and $\square p$ false, and the odd numbers make $p$ false and $\square p$ true.
Two worlds are identified when they agree on $\Sigma$, so there are two classes: $E$, the even numbers, and $O$, the odd numbers.
The valuation of the quotient is $V^f(p) = \{ E \}$.

### The smallest filtration

The smallest filtration has $[w] R^s [v]$ when some $w' \sim w$ and $v' \sim v$ have $w' R v'$.
The arrows $n \to n + 1$ go from an even number to an odd one or from an odd number to an even one, so $R^s = \{ (E, O), (O, E) \}$.

### The largest filtration

The largest filtration has $[w] R^l [v]$ when every $\square\varphi \in \Sigma$ true at $w$ has $\varphi$ true at $v$, and the only boxed formula in $\Sigma$ is $\square p$.
$E$ makes $\square p$ false, so the condition is empty, and $E$ sees both $E$ and $O$.
$O$ makes $\square p$ true, so $O$ sees only classes where $p$ holds, which means $E$.
So $R^l = \{ (E, E), (E, O), (O, E) \}$.

### Check

In $R^s$, $E$ sees only $O$, where $p$ is false, so $\square p$ is false at $E$, and $O$ sees only $E$, so $\square p$ is true at $O$.
In $R^l$, $E$ sees $O$, so $\square p$ is false at $E$, and $O$ sees only $E$, so $\square p$ is true at $O$.
Both match the values in $\mathfrak{M}$, as the [[filtration theorem|T99DK51S0W]] promises.
The infinite model has collapsed to 2 worlds, below the bound $2^{\lvert \Sigma \rvert} = 4$.

## Remarks

### What the quotient keeps

A filtration keeps exactly the information about $\Sigma$, and here it turns an infinite model into a finite one.
The two filtrations differ only by the loop $(E, E)$, and both satisfy the filtration theorem.
The quotient is not a copy of $\mathfrak{M}$: in $R^s$ the world $E$ lies on a cycle of length 2, while $\mathbb{N}$ has no cycles.

### Watch out

Formulas outside $\Sigma$ can change their truth value.
The formula $\square\square p$ is true at $0$ in $\mathfrak{M}$, since $\square p$ is true at $1$.
With $R^l$, $\square\square p$ is false at $E$, since $E R^l E$ and $\square p$ is false at $E$.
This does not contradict the theorem, because $\square\square p \notin \Sigma$.

### A degenerate variant

If we take $V(p) = \mathbb{N}$, then all worlds agree on $\Sigma$, the quotient has one world, and the smallest filtration is a single loop.

## Explanations

### L1 human

Picture the days $0, 1, 2, \dots$, with rain on even days.
We care about only two questions: "does it rain today?" and "does it rain tomorrow?"
Every even day answers "yes, no", and every odd day answers "no, yes".
So we merge all even days into one day and all odd days into another.
The result is a picture with two days that take turns, and it answers both questions correctly.

### L2 human

Take the world $3$ of $\mathfrak{M}$, which is odd, so $[3] = O$.
In $\mathfrak{M}$, $\square p$ is true at $3$, since $4$ is even.
In both filtrations, $O$ sees only $E$, where $p$ is true, so $\square p$ is true at $O$.
So $\square p$ has the same value at $3$ and at $[3]$, as the filtration theorem says.
The typical use of filtration is to prove the finite model property: a formula that fails in some model fails in a finite model.
