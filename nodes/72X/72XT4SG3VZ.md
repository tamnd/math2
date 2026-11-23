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

We measure the [[derivation of p → p|S8M610SGM8]] in the Hilbert system L, a [[Frege system|J2BAR09TPF]], in two ways: by its number of lines and by its size.
The size of a formula is its number of variables and connectives, and parentheses are not counted.
Here is the proof, with the size of each line.

1. $p \to ((p \to p) \to p)$, by A1, of size $7$.
2. $(p \to ((p \to p) \to p)) \to ((p \to (p \to p)) \to (p \to p))$, by A2, of size $17$.
3. $(p \to (p \to p)) \to (p \to p)$, by modus ponens from lines 1 and 2, of size $9$.
4. $p \to (p \to p)$, by A1, of size $5$.
5. $p \to p$, by modus ponens from lines 4 and 3, of size $3$.

Add the sizes of the lines:
$$7 + 17 + 9 + 5 + 3 = 41.$$
So the proof has $5$ lines and size $41$.

Now put a formula $\varphi$ of size $s$ in place of $p$ everywhere.
The five lines become a proof of $\varphi \to \varphi$, because each axiom stays an axiom and each modus ponens step stays a step.
A line with $a$ copies of $p$ and $b$ arrows now has size $a s + b$, so the five sizes are $4s + 3$, $9s + 8$, $5s + 4$, $3s + 2$ and $2s + 1$.
Their sum is
$$(4 + 9 + 5 + 3 + 2) s + (3 + 8 + 4 + 2 + 1) = 23 s + 18.$$
Check: for $s = 1$ this gives $41$, the size above.

## Remarks

The number of lines does not depend on $\varphi$, but the size grows linearly in $\lvert \varphi \rvert$.
This is the gap between the two measures of a [[proof system|3V24CYWDT6]] whose proofs are lists of lines.
In general the size of a proof is at most its number of lines times the size of its largest line, and both factors matter.

What changes if a proof uses a formula many times inside one line?
Then the size can grow faster than the number of lines suggests.
In the proof of $\varphi \to \varphi$, line 2 holds $9$ copies of $\varphi$, so a long $\varphi$ makes line 2 the dominant cost.
Watch out: a lower bound on the number of lines is a weaker statement than the same lower bound on size, and a result must say which measure it bounds.

## Explanations

### L1 human

A proof can be measured by how many steps it has, or by how much ink it uses.
The proof of "$p$ implies $p$" has $5$ steps and uses $41$ symbols.
If $p$ is replaced by a long formula, the proof still has $5$ steps, but it uses far more ink.

### L2 human

We count line 2 for a formula $\varphi$ of size $s$.

1. Line 2 is $A \to B$ with $A = \varphi \to ((\varphi \to \varphi) \to \varphi)$.
2. $A$ has four copies of $\varphi$ and three arrows, so $\lvert A \rvert = 4s + 3$.
3. $B = (\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$ has five copies of $\varphi$ and four arrows, so $\lvert B \rvert = 5s + 4$.
4. With the middle arrow, $\lvert A \to B \rvert = (4s + 3) + 1 + (5s + 4) = 9s + 8$.

Counts of this kind are the typical tool in simulations, where each step of one proof is replaced by a fixed derivation under a substitution, as in the proof of [[Reckhow's theorem|YAHHWZ7XRH]].
