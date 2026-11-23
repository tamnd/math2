---
tag: FJKE0AYXPA
kind: example
name: The Boolean function of exclusive or defined by a formula
msc: ["03B05", "06E30"]
topics: [JDK63589SA]
audience: ug1
instance_of: [H31CS3HK5P]
uses: [P0S056MDS7, 0X05GS525E, 0JMR2HM2N2]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_function
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
---

## Example

Every formula defines a function on rows of truth values, and "one or the other, but not both" is a good first case.
Let
$$\varphi = (p \lor q) \land \neg (p \land q).$$
We compute its [[Boolean function|0X05GS525E]] $F_\varphi \colon \{ 0, 1 \}^2 \to \{ 0, 1 \}$, where $F_\varphi(a, b)$ is the value of $\varphi$ under any valuation with $p = a$ and $q = b$.
The four rows are:
$$\begin{array}{cc|ccc|c} p & q & p \lor q & p \land q & \neg (p \land q) & \varphi \\ \hline 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 1 & 1 \\ 1 & 0 & 1 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 \end{array}$$

1. In the row $(0, 0)$ the first conjunct $p \lor q$ is $0$, so $\varphi = 0$.
2. In the rows $(0, 1)$ and $(1, 0)$ both conjuncts are $1$, so $\varphi = 1$.
3. In the row $(1, 1)$ the second conjunct $\neg (p \land q)$ is $0$, so $\varphi = 0$.

So $F_\varphi(a, b) = 1$ exactly when $a \neq b$.
This is exclusive or, also written $a \oplus b$.
A third variable $r$ has no effect, since it does not occur in $\varphi$.

## Remarks

The same function has many formulas.
The formula $\neg (p \leftrightarrow q)$ has the same table, so it is [[logically equivalent|0JMR2HM2N2]] to $\varphi$.
So is $(p \land \neg q) \lor (\neg p \land q)$, which we read off from the two rows with value $1$: the row $(1, 0)$ gives $p \land \neg q$, and the row $(0, 1)$ gives $\neg p \land q$.
There are $2^{2^2} = 16$ Boolean functions of two arguments, and exclusive or is one of them.

Drop the second conjunct and the function changes.
The formula $p \lor q$ alone has the value $1$ also in the row $(1, 1)$, so it defines inclusive or.

Watch out.
The English word "or" is often exclusive ("tea or coffee?"), but the logical $\lor$ is inclusive and gives $1$ in the row $(1, 1)$.

## Explanations

### L1 human

"Exclusive or" means "one or the other, but not both".
The formula says "$p$ or $q$, and not both $p$ and $q$".
When both letters are false, it is false.
When exactly one letter is true, it is true.
When both letters are true, "not both" fails, so it is false.

### L2 human

Exclusive or is the sum of two bits without the carry, which is why circuit designers care about it.
In arithmetic modulo $2$:
$$0 + 0 = 0, \qquad 0 + 1 = 1, \qquad 1 + 0 = 1, \qquad 1 + 1 = 0,$$
and this is the last column of the table above.
The carry is $p \land q$, which is $1$ only in the last row.
Check: the pair (carry, sum) in the row $(1, 1)$ is $(1, 0)$, the binary form of $2 = 1 + 1$.
So the formulas $p \land q$ and $\varphi$ together form a half adder.
