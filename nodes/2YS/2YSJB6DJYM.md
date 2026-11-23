---
tag: 2YSJB6DJYM
kind: example
name: The Ackermann function is not a function of primitive recursive arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: WCXH72T8D8
    note: "No term of PRA denotes the Ackermann function, because every term of PRA denotes a primitive recursive function and the Ackermann function is not primitive recursive."
uses: [WCXH72T8D8, 330YAP9Y4Q, N470JF7ZJX, 97QF3KHSBY, 5NVA2JRHPV, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_recursive_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ackermann_function
    locator: lead section
---

## Example

The [[Ackermann function|N470JF7ZJX]] is computable, yet [[primitive recursive arithmetic|WCXH72T8D8]] has no name for it.
The function $A : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ is given by
$$A(0, n) = n + 1, \qquad A(m + 1, 0) = A(m, 1), \qquad A(m + 1, n + 1) = A(m, A(m + 1, n)).$$
We show that no term $t(x, y)$ of $\mathsf{PRA}$ has the value $A(m, n)$ at $x = m$ and $y = n$ for all $m$ and $n$.
The value of a term in $\mathfrak{N}$ is computed with the defining equations of its function symbols.

1. Every function symbol of the [[definition|330YAP9Y4Q]] denotes a [[primitive recursive function|5NVA2JRHPV]].
   We use [[structural induction|12MQ2NJ29A]] on the clauses that generate the symbols.
   The symbols $0$, $S$ and $\pi^n_i$ denote initial functions, and $\mathrm{Comp}$ and $\mathrm{Rec}$ denote composition and primitive recursion of the functions that their parts denote.
2. Every term $t(x_1, \ldots, x_k)$ denotes a primitive recursive function of $x_1, \ldots, x_k$.
   We use induction on terms: a variable $x_i$ denotes the projection $\pi^k_i$, and $f(t_1, \ldots, t_m)$ denotes a composition of primitive recursive functions.
3. The Ackermann function is not primitive recursive, by the [[theorem on the Ackermann function|97QF3KHSBY]].
4. Suppose a term $t(x, y)$ had the value $A(m, n)$ for all $m$ and $n$.
   By step 2, $A$ would be primitive recursive, which contradicts step 3.

So $\mathsf{PRA}$ has no term for the Ackermann function.

## Remarks

The example separates "computable" from "finitist" in the sense of [[Tait's thesis|WCXH72T8D8]].
It does not mean that $\mathsf{PRA}$ is silent about $A$.
The relation "$s$ codes a correct finite table of values of $A$ that ends with $A(m, n) = v$" is primitive recursive.
So for each true value $A(m, n) = v$ there is a code $s$ of a table, and $\mathsf{PRA}$ proves the equation saying that $s$ is such a table.

What $\mathsf{PRA}$ cannot do is state that $A$ is total.
That sentence has the form $\forall m \, \forall n \, \exists v \, \exists s \, (\ldots)$, and its free-variable form needs a term for the witness as a function of $m$ and $n$.
The same holds for $\mathsf{I}\Sigma_1$, whose provably total functions are exactly the primitive recursive functions.
[[Peano arithmetic|HACXBCM7SS]] proves that $A$ is total, by induction on $m$ for the formula $\forall n \, \exists v \, \exists s \, (\ldots)$.
That formula is $\Pi_2$, so the fragment $\mathsf{I}\Sigma_2$ already suffices.

If we fix $m$, the answer changes.
Each row $n \mapsto A(m, n)$ is primitive recursive, so each row has a term in $\mathsf{PRA}$, as L2 shows for the first rows.

## Explanations

### L1 human

The Ackermann function is a rule for computing numbers that soon grow faster than any rule built from repeated steps.
For example, $A(1, n) = n + 2$ and $A(2, n) = 2n + 3$, but $A(4, 2) = 2^{65536} - 3$ already has $19{,}729$ digits.
Every rule of primitive recursive arithmetic is built by "do this step $n$ times", and the shape of the repetition is fixed in advance.
The Ackermann function needs a new kind of repetition for each first argument, so the system has no name for it.

### L2 human

We show that the first three rows of $A$ are primitive recursive.
Row $0$ is $A(0, n) = n + 1$, the successor.
For row $1$, the equations give $A(1, 0) = A(0, 1) = 2$ and
$$A(1, n + 1) = A(0, A(1, n)) = A(1, n) + 1,$$
so $A(1, n) = n + 2$ by induction on $n$.
For row $2$, they give $A(2, 0) = A(1, 1) = 3$ and
$$A(2, n + 1) = A(1, A(2, n)) = A(2, n) + 2,$$
so $A(2, n) = 2n + 3$ by induction on $n$.
Check: $A(2, 1) = A(1, A(2, 0)) = A(1, 3) = 5 = 2 \cdot 1 + 3$.

In general, row $m + 1$ comes from row $m$ by one primitive recursion on $n$, so each row has a function symbol of $\mathsf{PRA}$.
Watch out: this does not make $A$ primitive recursive.
The definition of row $m + 1$ depends on $m$, and no single definition covers all rows at once.
