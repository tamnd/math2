---
tag: NGNX2TXC7A
kind: example
name: An unsatisfiable set from modus ponens
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: QN7M1JCGT9
    note: every assignment that makes p and p → q true makes q true, so it makes ¬q false, and no assignment makes all three members true
uses: [H31CS3HK5P, 0NMG7W7Q11, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
    locator: Reduction of validity to satisfiability
---

## Example

"The alarm rings; if the alarm rings, the dog barks; the dog does not bark."
These three sentences cannot all be true, so the set is not [[satisfiable|QN7M1JCGT9]].
Let
$$\Gamma = \{ p, \; p \to q, \; \neg q \} .$$
We show that $\Gamma$ is unsatisfiable.

1. Suppose that a truth assignment $v$ satisfies $\Gamma$.
2. Then $v(p) = 1$, because $p \in \Gamma$.
3. Then $v(q) = 1$, because $\bar v(p \to q) = 1$, and an [[implication|0NMG7W7Q11]] with a true antecedent and a false consequent is false.
4. Then $\bar v(\neg q) = 0$ by the table of [[negation|029JBBF693]], so $v$ does not satisfy $\neg q$.
5. This contradicts step 1, so no assignment satisfies $\Gamma$.

Check: the four rows of $(p, q)$ are $(1, 1)$, which fails $\neg q$; $(1, 0)$, which fails $p \to q$; and $(0, 1)$ and $(0, 0)$, which fail $p$.

## Remarks

Each member alone is satisfiable, and so is each pair of members.
The pair $\{ p, \; p \to q \}$ holds under $v(p) = v(q) = 1$, the pair $\{ p, \; \neg q \}$ under $v(p) = 1$, $v(q) = 0$, and the pair $\{ p \to q, \; \neg q \}$ under $v(p) = v(q) = 0$.
So the failure lies only in the three members together.

The set is the premises $p$, $p \to q$ with the negated conclusion $\neg q$ added.
So its unsatisfiability is the same fact as $p, \; p \to q \models q$, which is [[modus ponens as a consequence|H8H9ZYZZEJ]].
In clause form the set is $\{ p \}$, $\{ \neg p, q \}$, $\{ \neg q \}$.
[[Resolution|ZDW6N1PGJ7]] on $p$ gives $\{ q \}$, and resolution of $\{ q \}$ with $\{ \neg q \}$ gives the empty clause.

Watch out.
A row of the table must make all members true at once to count.
A row that makes two of the three members true does not help.

Try it.
Is $\{ p, \; p \to q, \; q \to r, \; \neg r \}$ satisfiable?
No: $p$ forces $q = 1$, which forces $r = 1$, which clashes with $\neg r$.

## Explanations

### L1 human

"The alarm rings."
"If the alarm rings, the dog barks."
"The dog does not bark."
These three sentences cannot all be true: the first two make the dog bark, and the third says that it does not.

### L2 human

The set comes from a standard method.
To prove that a conclusion follows from premises, negate the conclusion, add it to the premises, and show that the result is unsatisfiable.
Here the premises are $p$ and $p \to q$, the conclusion is $q$, and the result is $\Gamma$.
Steps 1 to 5 of the example are the refutation.
Resolution provers, tableau provers and SAT solvers all prove consequences in this way.
