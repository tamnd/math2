---
tag: MJ6FMPYEF2
kind: example
name: Reading a formula in Polish notation
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
instance_of: [TT7WT5HPN9]
uses: [TFDYXS3K1N]
sources:
  - url: https://en.wikipedia.org/wiki/Polish_notation
    locator: Polish notation for logic
  - url: https://en.wikipedia.org/wiki/Polish_notation
    locator: History
---

## Example

In Polish notation the connectives $\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$ are the letters $N$, $K$, $A$, $C$, $E$, and each connective comes before its arguments.
So the formulas are given by the rules: each variable is a formula; if $\varphi$ is a formula, then $N\varphi$ is one; if $\varphi$ and $\psi$ are formulas, then $K\varphi\psi$, $A\varphi\psi$, $C\varphi\psi$ and $E\varphi\psi$ are formulas.
We read the string $CCpqCNqNp$ with a counter.
The counter is the number of formulas that we still need, so it starts at $1$.
A binary connective adds $1$ (it uses one need and makes two), $N$ adds $0$, and a variable subtracts $1$.

1. The values after each of the $9$ symbols are $2, 3, 2, 1, 2, 2, 1, 1, 0$.
2. The counter reaches $0$ at the last symbol and not before it, so the string is one complete formula.
3. The first $C$ is the main connective, and its first argument starts at position $2$.
4. The second $C$ starts the formula $Cpq$, which ends at position $4$, where the counter first falls to $1$.
5. The rest, $CNqNp$, is the second argument: $C$ applied to $Nq$ and $Np$.
6. So the string is the formula $((p \to q) \to ((\neg q) \to (\neg p)))$, the law of [[contraposition|04T1CT7212]].

Now we read the string $CpqC$.

7. The values after each symbol are $2, 1, 0, 1$.
8. The counter reaches $0$ after the third symbol, before the end; so $Cpq$ is a complete formula and the last $C$ is left over.
9. So $CpqC$ is not a formula.

## Remarks

The example shows that prefix notation needs no brackets: the order of the symbols alone fixes the reading.
The counter test is general: a string over this alphabet is a formula in Polish notation if and only if the counter stays at $1$ or more before the last symbol and is $0$ after the last symbol.
The [[unique readability theorem|6KBJX91N7G]] states the same fact with weights, which are the counter values subtracted from $1$.
In the string $CCpqCNqNp$ the official formula needs $10$ brackets and the Polish string needs none, so the Polish string has $9$ symbols instead of $19$.
If we move the first $C$ to the end, the string $CpqCNqNpC$ fails the test, because the counter reaches $0$ after the third symbol.

## Explanations

### L1 human

Polish notation writes the operation first and its parts after it.
So "$C$ $p$ $q$" means "if $p$ then $q$".
We can read such strings without brackets by counting how many parts we still need.
Each $C$ asks for two more parts, each $N$ asks for one part in place of itself, and each letter fills one part.
The string is a complete formula when the last letter fills the last open part.

### L2 human

We turn the formula $(p \land q) \lor (\neg r)$ into Polish notation and check it.

1. The main connective is $\lor$, so the string starts with $A$.
2. The left part $(p \land q)$ becomes $Kpq$.
3. The right part $(\neg r)$ becomes $Nr$.
4. So the string is $AKpqNr$.
5. The counter values are $2, 3, 2, 1, 1, 0$, so the string is one complete formula.

The typical use of the notation is in machines: stack calculators and the internal form of programs use prefix or postfix order.
A trap is to read $NKpq$ as $(\neg p) \land q$; the $N$ applies to the whole formula $Kpq$, so the string means $\neg (p \land q)$.
