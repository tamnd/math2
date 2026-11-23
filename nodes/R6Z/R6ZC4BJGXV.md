---
tag: R6ZC4BJGXV
kind: object
name: Fast-growing hierarchy
aliases: [wainer-hierarchy, extended-grzegorczyk-hierarchy, schwichtenberg-wainer-hierarchy]
msc: ["03D20", "03F30"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [KT50SMH3EC, 6GD30FGYDZ, VB6YXF761M, KAEDCQ8RM6, KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: The Wainer hierarchy
  - url: https://en.wikipedia.org/wiki/Fast-growing_hierarchy
    locator: Points of interest
---

## Description

The fast-growing hierarchy is a ladder of functions $f_\alpha : \mathbb{N} \to \mathbb{N}$, one for each ordinal $\alpha \le \varepsilon_0$, in which each rung iterates the rung below it.
It is a ruler for growth: a theory of arithmetic is measured by how high up the ladder it proves functions total.

The bottom rung adds one, and each next rung applies the previous rung $x$ times to $x$.
Then
$$f_0(3) = 4, \qquad f_1(3) = f_0(f_0(f_0(3))) = 6, \qquad f_2(3) = f_1(f_1(f_1(3))) = f_1(f_1(6)) = f_1(12) = 24.$$
So $f_1$ doubles and $f_2(x) = x \cdot 2^x$.

**The convention.**
Write $g^x$ for the $x$-fold iterate of a function $g$, with $g^0(x) = x$.
We use the base case $f_0(x) = x + 1$ and the iteration count $x$, as in the Wainer hierarchy:
$$f_0(x) = x + 1, \qquad f_{\alpha + 1}(x) = f_\alpha^x(x), \qquad f_\lambda(x) = f_{\lambda[x]}(x) \text{ for a limit } \lambda.$$
The recursion on $\alpha$ is well founded because $\lambda[x] < \lambda$.

**The fundamental sequences.**
The limit clause needs, for each limit ordinal $\lambda \le \varepsilon_0$, a [[fundamental sequence|VB6YXF761M]] $\lambda[0] < \lambda[1] < \cdots$ with supremum $\lambda$.
Every $\alpha < \varepsilon_0$ has a [[Cantor normal form|6GD30FGYDZ]] $\alpha = \omega^{\alpha_1} + \cdots + \omega^{\alpha_k}$ with $\alpha_1 \ge \cdots \ge \alpha_k$, and $\alpha$ is a limit exactly when $k \ge 1$ and $\alpha_k > 0$.
For such $\alpha$, write $\gamma = \omega^{\alpha_1} + \cdots + \omega^{\alpha_{k-1}}$, and use the standard sequences:

1. if $\alpha_k = \beta + 1$, then $\alpha[x] = \gamma + \omega^\beta \cdot x$;
2. if $\alpha_k$ is a limit, then $\alpha[x] = \gamma + \omega^{\alpha_k[x]}$;
3. for [[epsilon nought|KT50SMH3EC]], $\varepsilon_0[0] = 0$ and $\varepsilon_0[x+1] = \omega^{\varepsilon_0[x]}$.

So $\omega[x] = x$, $(\omega^2)[x] = \omega \cdot x$, $(\omega^\omega)[x] = \omega^x$, and $\varepsilon_0[1] = 1$, $\varepsilon_0[2] = \omega$, $\varepsilon_0[3] = \omega^\omega$.

## Remarks

### The finite rungs

Each finite rung comes from the one before by a short induction on the number of iterations.
Each application of $f_0$ adds $1$, so $x$ applications add $x$:
$$f_1(x) = f_0^x(x) = x + x = 2x.$$
Each application of $f_1$ doubles, so $x$ applications multiply by $2^x$:
$$f_2(x) = f_1^x(x) = x \cdot 2^x.$$
So $f_2(0), f_2(1), \dots, f_2(4)$ are $0, 2, 8, 24, 64$.
The next rung is already a tower of powers:
$$f_3(2) = f_2(f_2(2)) = f_2(8) = 8 \cdot 2^8 = 2048.$$
Check: $f_2(2) = 2 \cdot 4 = 8$ and $2^8 = 256$, so $8 \cdot 256 = 2048$.

### The first infinite rung

At $\omega$ the hierarchy diagonalizes: $f_\omega(x) = f_{\omega[x]}(x) = f_x(x)$.
So $f_\omega(0) = f_0(0) = 1$, $f_\omega(1) = f_1(1) = 2$ and $f_\omega(2) = f_2(2) = 8$.
The next value is
$$f_\omega(3) = f_3(3) = f_2(f_2(f_2(3))) = f_2(f_2(24)) = f_2(3 \cdot 2^{27}) = 3 \cdot 2^{402653211}.$$
Here $f_2(24) = 24 \cdot 2^{24} = 3 \cdot 2^{27}$, and $3 \cdot 2^{27} + 27 = 402653211$.
The same number is the length of the [[Goodstein sequence|XQMNJF241J]] of $4$, plus $2$.
The function $f_\omega$ grows like the [[Ackermann function|N470JF7ZJX]], and it eventually dominates every [[primitive recursive function|5NVA2JRHPV]].

At the top, $f_{\varepsilon_0}(0) = f_0(0) = 1$, $f_{\varepsilon_0}(1) = f_1(1) = 2$ and $f_{\varepsilon_0}(2) = f_\omega(2) = 8$.
Then $f_{\varepsilon_0}(3) = f_{\omega^\omega}(3) = f_{\omega^3}(3)$, a number far too large to write down.

### How the rungs compare

The basic facts about growth hold for the standard fundamental sequences.
Every $f_\alpha$ is total and [[computable|KZSB5E471K]], because the recursion on $\alpha$ terminates.
If $\alpha < \beta$, then $f_\beta$ eventually dominates $f_\alpha$: $f_\alpha(x) < f_\beta(x)$ for all large enough $x$.
Each primitive recursive function is dominated by some $f_n$ with $n$ finite, and this is why $f_\omega$ is not primitive recursive.

The level $\varepsilon_0$ is the boundary for [[Peano arithmetic|MPSCREYC3M]].
Each $f_\alpha$ with $\alpha < \varepsilon_0$ is [[provably total|Z742YPHPNS]] in $\mathsf{PA}$.
Conversely, Wainer and Schwichtenberg proved that every function that $\mathsf{PA}$ proves total is eventually dominated by some $f_\alpha$ with $\alpha < \varepsilon_0$.
So $f_{\varepsilon_0}$ is [[not provably total in PA|Z2JK9QHKWF]].

### The theory and the stronger theory

$\mathsf{PA}$ does not prove that $f_{\varepsilon_0}$ is total, but $\mathsf{ZFC}$ proves it by transfinite recursion.
$\mathsf{PA}$ plus [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ also proves it.
The induction runs over $\alpha \le \varepsilon_0$ for the formula "$f_\alpha$ is total", with an ordinary induction on the number of iterations at successor steps.

### Other conventions

Books do not agree on the definition, so always check the base case and the sequences.
Some authors iterate $x + 1$ times, with $f_{\alpha+1}(x) = f_\alpha^{x+1}(x)$.
Then $f_1(x) = 2x + 1$ and $f_2(x) = 2^{x+1}(x + 1) - 1$, since $k$ applications of $x \mapsto 2x + 1$ send $x$ to $2^k(x + 1) - 1$.
Others start with $\varepsilon_0[0] = 1$, so that $\varepsilon_0[2] = \omega^\omega$.
Then $f_{\varepsilon_0}(2) = f_{\omega^\omega}(2) = f_{\omega + 2}(2)$, which is larger than $f_8(8)$, since $f_{\omega+1}(2) = f_\omega(8) = f_8(8)$.
The domination facts survive these changes below $\varepsilon_0$, but single values do not.

### Relation to other hierarchies

The [[Hardy hierarchy|X8RKXQASR9]] unfolds the iterations into one countdown, and $f_\alpha = H_{\omega^\alpha}$ for every $\alpha < \varepsilon_0$.
It measures the lengths of Goodstein sequences and hydra battles.
The [[slow-growing hierarchy|VDF6R9EVJ2]] grows much more slowly: $g_{\varepsilon_0}$ is a finite tower and is dominated by $f_4$.

### Watch out

The small values say nothing about growth.
Since $f_{\varepsilon_0}(2) = f_2(2) = 8$, a table of the first three values cannot tell $f_{\varepsilon_0}$ from $f_2$.
Domination is a statement about all large arguments.

"Not provably total in $\mathsf{PA}$" does not mean "not computable".
The function $f_{\varepsilon_0}$ is computable, and $\mathsf{ZFC}$ proves that it is total.

### History

Martin Löb and Stanley Wainer introduced the hierarchy around 1970, and it is also called the Schwichtenberg-Wainer hierarchy.
Its finite levels $f_n$ correspond to the levels of the Grzegorczyk hierarchy of primitive recursive functions.

### Try it

First, compute $f_2(5)$.
The answer is $5 \cdot 2^5 = 160$.

Second, compute $f_{\omega + 1}(1)$.
The answer is $f_\omega^1(1) = f_\omega(1) = f_1(1) = 2$.

## Explanations

### L1 human

The fast-growing hierarchy is a ladder of functions, and each rung grows much faster than the one below.
The first rung adds one, the next rung doubles, and the next one multiplies by a power of two.
For example the third rung sends $3$ to $24$, and the fourth rung sends $2$ to $2048$.
After all the finite rungs come rungs labeled by infinite ordinals, which mix the earlier rungs.
The rung labeled $\varepsilon_0$ grows so fast that ordinary arithmetic cannot prove that it always gives an answer.

### L2 human

We compute $f_{\varepsilon_0}(2)$ from the definitions, and then one value of $f_3$.
First unfold the fundamental sequence of $\varepsilon_0$:
$$\varepsilon_0[2] = \omega^{\varepsilon_0[1]} = \omega^{\omega^{\varepsilon_0[0]}} = \omega^{\omega^0} = \omega.$$
So $f_{\varepsilon_0}(2) = f_\omega(2) = f_{\omega[2]}(2) = f_2(2) = 8$.
Next, $f_3(2) = f_2^2(2) = f_2(f_2(2)) = f_2(8) = 2048$.
This shows the typical use of the hierarchy as a ruler.
To show that a theory does not prove "$\forall x\, \exists y\, \varphi(x, y)$", show that the least $y$ escapes every $f_\alpha$ with $\alpha$ below the ordinal of the theory.

### L3 human

The hierarchy turns ordinals into growth rates.
For a theory with an [[ordinal analysis|C5E5TG8PGP]], the provably total functions are usually those dominated by some $f_\alpha$ with $\alpha$ below its [[proof-theoretic ordinal|C72RBH0CDR]].
For $\mathsf{PA}$ this ordinal is $\varepsilon_0$, the ordinal of [[Gentzen's consistency proof|QPV0HNP22S]] of 1936.
It is the boundary in the [[Paris-Harrington theorem|509ZWA0R26]] and in [[Goodstein's theorem|XQMNJF241J]].
Beyond $\varepsilon_0$ the fundamental sequences come from ordinal notations such as the [[Veblen function|6QFEVWKE25]], and the values then depend much more on the choice of notation.
