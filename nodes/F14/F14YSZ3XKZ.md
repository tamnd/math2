---
tag: F14YSZ3XKZ
kind: example
name: Robinson arithmetic is not negation complete
msc: ["03F30", "03C62"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: 319P85G2C1
    note: "Q proves neither the sentence for all x, 0 + x = x, nor its negation."
uses: [319P85G2C1, 3K1AKGXF8A, TT8MXRTVBM, 4A84VHDTHV, WP27CABPA4]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: Metamathematics
  - book: isbn:9780521857840
---

## Example

[[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ proves $0 + \underline{5} = \underline{5}$, and the same for every other numeral, but it does not prove the general law $\forall x \, (0 + x = x)$.
It does not refute the law either.
So $\mathsf{Q}$ is not [[negation complete|319P85G2C1]], and we can see this with two models, without the incompleteness theorems.
We use the seven [[axioms|TT8MXRTVBM]] of $\mathsf{Q}$:
$$\begin{aligned} &(1)\ Sx \ne 0, \quad (2)\ Sx = Sy \to x = y, \quad (3)\ x \ne 0 \to \exists y \, (x = Sy), \\ &(4)\ x + 0 = x, \quad (5)\ x + Sy = S(x + y), \quad (6)\ x \cdot 0 = 0, \quad (7)\ x \cdot Sy = x \cdot y + x. \end{aligned}$$
If the language also has $<$, we interpret it by its defining axiom, and nothing below changes.

### The model

Let $M$ have domain $\mathbb{N} \cup \{ a, b \}$, with two new elements $a \ne b$.
On $\mathbb{N}$ the operations are the usual ones, and below $n$ ranges over $\mathbb{N}$ and $x$ over all of $M$.
Successor fixes the new elements: $Sa = a$ and $Sb = b$.
Adding a new element on the right swaps it: $x + a = b$ and $x + b = a$ for every $x$.
Adding a number on the right changes nothing: $a + n = a$ and $b + n = b$.
For products, $x \cdot 0 = 0$ for every $x$, and $0 \cdot a = 0 \cdot b = 0$.
For $n \ge 1$, $a \cdot n = b$, $b \cdot n = a$ and $n \cdot a = n \cdot b = a$.
Finally $a \cdot a = b$, $b \cdot a = a$, $a \cdot b = b$ and $b \cdot b = a$.

### The check

1. Axioms 1 to 3: $S$ is injective on $M$, $0$ is not a value of $S$, and every $x \ne 0$ is a value, since $a = Sa$ and $b = Sb$.
2. Axiom 4: $n + 0 = n$, $a + 0 = a$ and $b + 0 = b$.
3. Axiom 5 with $y = n$: for $x \in \mathbb{N}$ it is ordinary arithmetic.
   For $x = a$, both sides are $a$, since $a + (n + 1) = a$ and $S(a + n) = Sa = a$; the case $x = b$ is the same.
4. Axiom 5 with $y = a$: the left side is $x + Sa = x + a = b$, and the right side is $S(x + a) = Sb = b$.
   The case $y = b$ is the same with $a$ and $b$ exchanged.
5. Axiom 6 holds by the first rule for products.
6. Axiom 7 with $y = n$: for $x = a$ the left side is $a \cdot (n + 1) = b$, and the right side is $a \cdot n + a = b$, because anything plus $a$ is $b$.
   For $x = b$ both sides are $a$ in the same way.
7. Axiom 7 with $y = a$: since $Sa = a$, it reads $x \cdot a = x \cdot a + x$.
   For $x = 0$ this is $0 = 0 + 0$; for $x = n \ge 1$ it is $a = a + n$; for $x = a$ it is $b = b + a$; for $x = b$ it is $a = a + b$.
   All four hold.
8. Axiom 7 with $y = b$ reads $x \cdot b = x \cdot b + x$, and the four cases give $0 = 0 + 0$, $a = a + n$, $b = b + a$ and $a = a + b$.

So $M$ is a model of $\mathsf{Q}$, and in $M$ we have $0 + a = b \ne a$.

### The conclusion

Since $M \models \neg \forall x \, (0 + x = x)$, [[soundness|4A84VHDTHV]] gives $\mathsf{Q} \nvdash \forall x \, (0 + x = x)$.
The [[standard model|WP27CABPA4]] $\mathbb{N}$ is also a model of $\mathsf{Q}$, and it satisfies the law, so soundness gives $\mathsf{Q} \nvdash \neg \forall x \, (0 + x = x)$.

## Remarks

The failure needs a non-standard element.
For each numeral, $\mathsf{Q}$ proves $0 + \underline{n} = \underline{n}$ by $n$ uses of axiom 5 after one use of axiom 4, so no model of $\mathsf{Q}$ can break the law at a standard number.

The sentence is independent of $\mathsf{Q}$ only because $\mathsf{Q}$ has no induction.
Peano arithmetic proves $\forall x \, (0 + x = x)$ by induction on $x$, using axioms 4 and 5 for the base case and the step.
In $M$ addition is also not commutative, since $a + 0 = a$ but $0 + a = b$.
So the same model shows that $\mathsf{Q}$ does not prove the commutative law of addition.

## Explanations

### L1 human

Robinson arithmetic has the rules for adding and multiplying, but no rule of induction.
So it can check $0 + 5 = 5$ step by step, but it cannot prove "$0 + x = x$ for every $x$".
A strange number system with two extra elements obeys all the rules and breaks this law.
The ordinary numbers obey the law, so the rules cannot refute it either.

### L2 human

The method has three steps, and it works for any theory.
First, build a model of the theory in which the sentence fails; here $M$, with $0 + a = b$.
Second, find a model in which it holds; here $\mathbb{N}$.
Third, apply soundness twice: the theory proves neither the sentence nor its negation.
This is the typical way to show that $\mathsf{Q}$ is weak, and why $\mathsf{PA}$ adds the induction schema.
Watch out: $\mathsf{Q}$ is still strong on closed terms, since it proves every true equation between numerals, such as $0 + \underline{5} = \underline{5}$.
