---
tag: GQHHNV79PA
kind: concept
name: Proof of uniqueness
aliases: [uniqueness-proof, existence-and-uniqueness-proof]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [ACSC75R7R5, 0QAJHFGZZJ, 0B94TKFQJX, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Summary

A proof of uniqueness shows that there cannot be two different objects with a given property.
It is what gives you the right to say "the" identity, "the" inverse or "the" solution.

Here is a small one: a [[group|28PKCPYA2V]] has only one identity element.
Suppose $e$ and $e'$ are both identities, so $eg = ge = g$ and $e'g = ge' = g$ for every $g$.
Then
$$e = ee' = e',$$
where the first equality uses that $e'$ is an identity and the second uses that $e$ is one.
So any two identities are equal; see [[uniqueness of the identity element|GDBV09GFYB]] and [[the identity element of a group is unique|9BA5AWWYD9]].

In general, a *proof of uniqueness* for a property $P$ shows that at most one object has $P$.
It has two standard forms.
The first form assumes that $x$ and $y$ both satisfy $P$ and proves $x = y$.
The second form takes a known object $a$ with $P(a)$ and proves that every $x$ with $P(x)$ equals $a$.
A statement of [[existence and uniqueness|ACSC75R7R5]], "there is exactly one $x$ with $P(x)$", needs two separate proofs: one of existence and one of uniqueness.

## Motivation

Uniqueness lets you name things.
Once a group has exactly one identity element, you can call it the identity and write $e$ or $1$ for it.
Once a function has exactly one inverse, the notation $f^{-1}$ means something definite.
For an equation, uniqueness means that the solution you found is the only one, so you missed none.

In analysis, uniqueness theorems for limits and for solutions of differential equations make the objects well defined.
A limit would be useless if a sequence could converge to two numbers at once.
Without uniqueness, every later use of an object would have to say which of several objects it means.

## Notation

"There is a unique $x$ such that $P(x)$" is written $\exists! x \, P(x)$, with the [[uniqueness quantifier|0QAJHFGZZJ]].
A proof is usually split into two labeled parts, "Existence." and "Uniqueness."
The uniqueness part often begins "Suppose that $x$ and $y$ both satisfy $P$."
In Lean, `∃! x, P x` unfolds to `∃ x, P x ∧ ∀ y, P y → y = x`.
The lemma `ExistsUnique.intro` builds such a proof from a witness and a uniqueness proof, and `ExistsUnique.unique` turns a proof of `∃! x, P x` and two proofs `P y₁` and `P y₂` into `y₁ = y₂`.

## Remarks

### Why the method is valid

The statement $\exists! x \, P(x)$ has two standard unfoldings:
$$\exists x \, P(x) \;\land\; \forall x \, \forall y \, \big(P(x) \land P(y) \Rightarrow x = y\big),$$
$$\exists x \, \big(P(x) \land \forall y \, (P(y) \Rightarrow y = x)\big).$$
The first form of the proof matches the second conjunct of the first unfolding, and the second form matches the inner part of the second unfolding.
Both unfoldings are equivalent, so either form of the proof, together with an existence proof, proves "exactly one".

The two halves are independent.
The equation $x^2 = 4$ has a real solution but not a unique one, and $x^2 = -1$ has at most one real solution because it has none.
So a uniqueness proof alone never shows that an object exists.

### The first form at work

The group identity above is the first form: two objects, one chain of equalities.
The inverse of a group element works the same way.
If $b$ and $c$ are both [[inverses|0ZNZH0EXFX]] of $a$, so $ba = ab = e$ and $ca = ac = e$, then
$$b = be = b(ac) = (ba)c = ec = c.$$
Each step uses one fact: the identity, $ac = e$, associativity, $ba = e$ and the identity again.

The same form solves congruences.
In [[the congruence 3x = 1 modulo 7|VY92J0VMG6]], two solutions $x$ and $y$ in $\{0, \dots, 6\}$ give $7 \mid 3(x - y)$, so $7 \mid x - y$, and $|x - y| \le 6$ forces $x = y$.
The [[division algorithm|0CHQKZFK5S]] has a unique quotient and remainder by the same pattern: if $a = bq + r = bq' + r'$ with $0 \le r, r' < b$, then $b \mid r - r'$ and $|r - r'| < b$, so $r = r'$ and then $q = q'$.

### The second form at work

The second form is natural when a solution is already known.
[[The exponential function is the only solution of f' = f with f(0) = 1|17X7D2YD39]]: any such $f$ is compared with $e^x$ through $g(x) = f(x) e^{-x}$, whose derivative is $0$, so $g$ is the constant $g(0) = 1$.
Two [[greatest common divisors are equal|GZHZVV87T0]] because each divides the other and both are positive.
In this form you need the existence part first, since the known object $a$ is the thing you compare with.

### When to choose it

Use the first form when the property gives you equations that you can combine, as in algebra: subtract the two equations, or chain them as in $e = ee' = e'$.
Use the second form when an explicit solution is known and you can measure how far any other candidate is from it.
In algebra and in category theory, the honest statement is often uniqueness "up to isomorphism": any two objects with the property are isomorphic, and they need not be equal.

### What is not a uniqueness proof

[[Dividing x^2 = x by x loses a solution|MNS91DE23K]]: the argument divides by $x$, so it shows only that every nonzero solution equals $1$, and it misses $x = 0$.
Finding one solution and stopping is not a proof of uniqueness either.
The equation $x^2 = 4$ has the solution $x = 2$, and "the solution is $2$" is false, since $x = -2$ also works.

### Watch out

The first trap is to prove one half and claim both.
"I found $x = 5$" is existence, and "two solutions are equal" is uniqueness; each needs its own argument.

The second trap is to divide by an expression that can be $0$, which can remove solutions, as in $x^2 = x$.

The third trap, in the first form, is to choose $y$ as a specific object.
Both $x$ and $y$ must be arbitrary objects with the property, or the proof covers only the pairs you chose.

### Writing it up

Label the two parts "Existence." and "Uniqueness." and prove them in that order.
Begin the uniqueness part with the full assumption: "Suppose $x$ and $y$ both satisfy $P$."
End it with "$x = y$", and then state the result in the words of the theorem: "so there is exactly one such $x$".
A uniqueness theorem then justifies a [[definite description|PD2R4XT79Q]] "the $x$ such that $P(x)$".

### History

Bertrand Russell's theory of descriptions, of 1905, analyzes a phrase "the $x$ such that $P(x)$" as the claim that exactly one $x$ satisfies $P$, together with a statement about that $x$.
The symbol $\exists!$ for unique existence is now standard in logic and in mathematical writing.

### Try it

First, prove that $2x + 3 = 11$ has exactly one real solution.
Existence: $x = 4$ gives $8 + 3 = 11$; uniqueness: if $2x + 3 = 11$ and $2y + 3 = 11$, then $2x = 2y$, so $x = y$.

Second, prove that a function $f \colon A \to B$ has at most one two-sided inverse.
If $g$ and $h$ are both inverses, then $g = g \circ \operatorname{id}_B = g \circ (f \circ h) = (g \circ f) \circ h = \operatorname{id}_A \circ h = h$.

## Explanations

### L1 human

"There is exactly one" says two things.
First, there is at least one.
Second, there are not two different ones.
For example, there is exactly one whole number between $4$ and $6$.
There is at least one, namely $5$.
And any whole number between $4$ and $6$ is $5$, so there are not two different ones.

### L2 human

Let us prove that for real numbers $a \ne 0$ and $b$, the equation $ax + b = 0$ has exactly one real solution.
For existence, take $x_0 = -\frac{b}{a}$, which is defined because $a \ne 0$, and check
$$a x_0 + b = -b + b = 0.$$
For uniqueness, suppose $x$ and $y$ are real numbers with $ax + b = 0$ and $ay + b = 0$.
Subtract the two equations:
$$a(x - y) = 0.$$
Since $a \ne 0$, we can divide by $a$, so $x - y = 0$ and $x = y$.
Check: for $3x + 6 = 0$ the formula gives $x_0 = -2$, and $3 \cdot (-2) + 6 = 0$.
The typical use: subtract the two equations that $x$ and $y$ satisfy, and show that the difference is $0$.
The step that divides by $a$ needs $a \ne 0$; for $a = 0$ and $b = 0$ every real number is a solution, and uniqueness fails.

### L3 human

In first-order logic with equality, $\exists! x \, P(x)$ is an abbreviation, and the two forms of the proof correspond to its two equivalent unfoldings.
Universal properties in category theory define objects by the unique existence of morphisms, and the standard argument that two such objects are isomorphic is a uniqueness proof of the second form.
In homotopy type theory, unique existence becomes contractibility of the type of pairs $(x, p)$ with $p : P(x)$, which makes "unique up to a unique isomorphism" the basic notion.
Uniqueness theorems for differential equations, such as the Picard-Lindelöf theorem, follow the pattern of the exponential example: two solutions are compared, and their difference is shown to vanish.
More patterns for goals of this kind are in the topic [[proof patterns for common goals|MEKKHHQTKB]].
