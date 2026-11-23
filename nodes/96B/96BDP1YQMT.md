---
tag: 96BDP1YQMT
kind: example
name: The pq-system
msc: ["03B22"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [439M8B4DY2]
uses: [439M8B4DY2, 1P6EP01HZF, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach
    locator: lead section
---

## Example

The pq-system is a [[formal system|439M8B4DY2]] whose rules only copy hyphens, yet whose theorems all look like true sums.
It comes from Hofstadter's book *Gödel, Escher, Bach*, and we use the following form of it.
Write $-^a$ for the [[string|1P6EP01HZF]] of $a$ hyphens.
The alphabet is $\{ p, q, - \}$, and every finite string over it is a formula.
The axioms are the strings
$$-^a \, p \, - \, q \, -^{a+1} \qquad (a \geq 1),$$
and the only rule is
$$\text{from } -^a \, p \, -^b \, q \, -^c \text{ infer } -^a \, p \, -^{b+1} \, q \, -^{c+1} \qquad (a, b, c \geq 1).$$

First we check that this is a formal system.

1. Every string is a formula, so the set of formulas is decidable.
2. A string is an axiom when it has the shape $-^a p - q -^c$ with $a \geq 1$ and $c = a + 1$, and counting hyphens decides this.
3. The rule has one premise, and counting the three blocks of hyphens in the premise and in the conclusion decides whether it applies.

Next we find all the theorems.
We claim that a string is a theorem exactly when it is $-^a p -^b q -^c$ with $a, b \geq 1$ and $c = a + b$.

1. Each axiom has this form, with $b = 1$ and $c = a + 1 = a + b$.
2. If the premise of the rule has $c = a + b$, then the conclusion has $c + 1 = a + (b + 1)$, so the rule keeps the form.
3. By induction on the length of derivations, every theorem has the form.
4. Conversely, for $a, b \geq 1$, the axiom $-^a p - q -^{a+1}$ followed by $b - 1$ uses of the rule derives $-^a p -^b q -^{a+b}$.

For example, $--p---q-----$ has $a = 2$, $b = 3$ and $c = 5$, and here is its derivation:
$$--p-q--- \quad \Longrightarrow \quad --p--q---- \quad \Longrightarrow \quad --p---q-----.$$
The first string is the axiom with $a = 2$, and each arrow is one use of the rule.
The string $--p--q---$ is not a theorem, because $2 + 2 \neq 3$.

## Remarks

### Syntax and semantics side by side

The rule never uses any meaning of $p$ and $q$.
Read $-^a$ as the number $a$, $p$ as "plus" and $q$ as "equals", and the theorems become exactly the true equations $a + b = c$ with $a, b \geq 1$.
So, for strings of the shape $-^a p -^b q -^c$, the system is [[sound|4A84VHDTHV]] and complete for this reading, in the sense of a proof system for a semantics.

The reading is not forced by the system.
Read $-^a p -^b q -^c$ as "$c$ minus $b$ equals $a$", and every theorem is again a true statement.
This is the difference between syntax, the rules on strings, and semantics, the meaning we give to them.

### Changing the axioms

If we allow $a = 0$ in the axioms, the theorems become the strings with $a \geq 0$, $b \geq 1$ and $c = a + b$, and the proof is the same.
If we drop the axioms with $a \geq 2$ and keep only $-p-q--$, the theorems are the strings $-p-^b q -^{b+1}$, which say $1 + b = b + 1$.
The reading as addition is still sound, but it is no longer complete, since $2 + 2 = 4$ has no derivation.

## Explanations

### L1 human

The pq-system writes numbers as rows of dashes, so three is ---.
You start from strings such as --p-q---, which you may read as "two plus one equals three".
The only rule adds one dash after p and one dash at the end, which turns "two plus one equals three" into "two plus two equals four".
The rule only copies dashes and knows nothing about addition.
Still, every string you can reach says something true about addition, and every true sum of positive numbers can be reached.

### L2 human

Is $---p--q-----$ a theorem?
The string has the shape $-^a p -^b q -^c$ with $a = 3$, $b = 2$ and $c = 5$.
Since $3 + 2 = 5$, the description of the theorems says yes.
A derivation confirms it: start from the axiom $---p-q----$ with $a = 3$, and apply the rule once.
This is the typical use of a description of all theorems: it replaces a search for derivations by a count.
Watch out: the reading as addition is not part of the system.
It is a semantics that we add, and the "minus" reading works just as well.
