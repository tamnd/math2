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

Polish notation puts each connective in front of its arguments, and then no brackets are needed at all.
The connectives $\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$ become the letters $N$, $K$, $A$, $C$, $E$.
Each variable is a formula; if $\varphi$ is a formula, so is $N\varphi$; and if $\varphi$ and $\psi$ are formulas, so are $K\varphi\psi$, $A\varphi\psi$, $C\varphi\psi$ and $E\varphi\psi$.

We read the string $CCpqCNqNp$ with a counter.
The counter is the number of formulas we still need, so it starts at $1$.
A binary connective adds $1$, since it fills one need and opens two; $N$ adds $0$; a variable subtracts $1$.
Here are the values after each symbol:
$$\begin{array}{ccccccccc} C & C & p & q & C & N & q & N & p \\ 2 & 3 & 2 & 1 & 2 & 2 & 1 & 1 & 0 \end{array}$$

1. The counter reaches $0$ at the last symbol and not before, so the string is one complete formula.
2. The first $C$ is the main connective.
   Its first argument starts at the second symbol and ends at the fourth, where the counter first falls back to $1$; it is $Cpq$.
3. The rest, $CNqNp$, is the second argument: $C$ applied to $Nq$ and $Np$.
4. So the string is the formula $((p \to q) \to ((\neg q) \to (\neg p)))$, the law of [[contraposition|04T1CT7212]].

Now read $CpqC$.
The values are $2, 1, 0, 1$.
The counter reaches $0$ after the third symbol, before the end, so $Cpq$ is complete and the last $C$ is left over.
So $CpqC$ is not a formula.

## Remarks

The example shows that prefix order alone fixes the reading.
The counter test is general: a string over this alphabet is a formula exactly when the counter stays at $1$ or more before the last symbol and is $0$ after it.
The [[unique readability theorem|6KBJX91N7G]] states the same fact with weights, which are $1$ minus the counter values.

The saving is real.
The official form of the contraposition law has $5$ connectives, so it needs $10$ brackets and has $19$ symbols, while the Polish string has $9$.
Move the first $C$ to the end, and the string $CpqCNqNpC$ fails the test, because the counter reaches $0$ after the third symbol.

Watch out.
$NKpq$ is not $(\neg p) \land q$.
The $N$ applies to the whole formula $Kpq$ that follows it, so the string means $\neg (p \land q)$.

## Explanations

### L1 human

Polish notation writes the operation first and its parts after it.
So "$C$ $p$ $q$" means "if $p$ then $q$".
We can read such strings without brackets by counting how many parts we still need.
Each $C$ asks for two parts in place of one, each $N$ asks for one part in place of itself, and each letter fills one part.
The string is a complete formula when the last letter fills the last open part.

### L2 human

We turn $(p \land q) \lor (\neg r)$ into Polish notation.
The main connective is $\lor$, so the string starts with $A$.
The left part $(p \land q)$ becomes $Kpq$, and the right part $(\neg r)$ becomes $Nr$, so the result is $AKpqNr$.
Check with the counter:
$$\begin{array}{cccccc} A & K & p & q & N & r \\ 2 & 3 & 2 & 1 & 1 & 0 \end{array}$$
The counter first reaches $0$ at the last symbol, so the string is one complete formula.
Stack calculators and the internal forms of programs use the same prefix or postfix order, for the same reason: no brackets and a one-pass reading.
