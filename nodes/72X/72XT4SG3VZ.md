---
tag: 72XT4SG3VZ
kind: example
name: Lines and size of a proof of p → p in L
msc: ["03F20", "03B05"]
topics: [CBAF7J051K]
audience: research
instance_of: [J2BAR09TPF]
uses: [S8M610SGM8, ET1HPME8VV, 3V24CYWDT6]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Proof example in P2
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

We measure the [[derivation of $p \to p$|S8M610SGM8]] in the Hilbert system L, a [[Frege system|J2BAR09TPF]].
The size of a formula is its number of variables and connectives; parentheses are not counted.
The proof has five lines.

1. $p \to ((p \to p) \to p)$, by A1. Size $7$.
2. $(p \to ((p \to p) \to p)) \to ((p \to (p \to p)) \to (p \to p))$, by A2. Size $17$.
3. $(p \to (p \to p)) \to (p \to p)$, by modus ponens from lines 1 and 2. Size $9$.
4. $p \to (p \to p)$, by A1. Size $5$.
5. $p \to p$, by modus ponens from lines 4 and 3. Size $3$.

So the proof has $5$ lines and size $7 + 17 + 9 + 5 + 3 = 41$.

Now replace $p$ by a formula $\varphi$ of size $s$.
The five lines become a proof of $\varphi \to \varphi$, with sizes $4s + 3$, $9s + 8$, $5s + 4$, $3s + 2$ and $2s + 1$.
For $s = 1$ these are the sizes above.
So the proof of $\varphi \to \varphi$ has $5$ lines for every $\varphi$, and its size is $23 s + 18$.

## Remarks

The number of lines does not depend on $\varphi$, but the size grows linearly in $\abs{\varphi}$.
This is the difference between the two measures of a [[proof system|3V24CYWDT6]].
For Frege systems, the size of a proof is at most the number of lines times the size of its largest line.
A proof with few lines can still have large size, as the proof of $\varphi \to \varphi$ shows for a long $\varphi$.

## Explanations

### L1 human

A proof can be measured by how many steps it has, or by how much ink it uses.
The proof of "$p$ implies $p$" has $5$ steps and uses $41$ symbols.
If $p$ is replaced by a long formula, the proof still has $5$ steps, but it uses more ink.

### L2 human

We count line 2 for a formula $\varphi$ of size $s$.

1. Line 2 is $A \to B$ with $A = \varphi \to ((\varphi \to \varphi) \to \varphi)$.
2. $A$ has four copies of $\varphi$ and three arrows, so $\abs{A} = 4 s + 3$.
3. $B = (\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$ has five copies of $\varphi$ and four arrows, so $\abs{B} = 5 s + 4$.
4. So $\abs{A \to B} = (4 s + 3) + 1 + (5 s + 4) = 9 s + 8$.

The typical use of such counts is in simulations, where one proof is replaced by a fixed derivation with a substitution.
A trap: the line count of a proof system can be small while the size is large, so each lower bound must name its measure.
