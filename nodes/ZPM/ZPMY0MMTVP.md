---
tag: ZPMY0MMTVP
kind: example
name: Symmetry, transitivity and congruence from the Hilbert equality axioms
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [Y90Z13AXY8]
uses: [Y90Z13AXY8, N95HV0VWSM, 05006AJ7DZ, 0Y0MQYST0M, VKSK35Y52Z]
sources:
  - url: https://en.wikipedia.org/wiki/Equality_(mathematics)
    locator: Derivations of basic properties
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Example

We work in Enderton's [[Hilbert-style predicate calculus|N95HV0VWSM]].
Its logical axioms are all generalizations of six groups of formulas, and its only rule is [[modus ponens|0Y0MQYST0M]] (MP).
We use group 1 ([[tautology|05006AJ7DZ]] instances), group 2 ($\forall x\,\varphi \to \varphi[t/x]$ with $t$ substitutable for $x$), and the two [[equality rules|Y90Z13AXY8]]:

- Axiom 5: $x = x$.
- Axiom 6: $x = y \to (\alpha \to \alpha')$, with $\alpha$ atomic and $\alpha'$ obtained from $\alpha$ by replacing $x$ at zero or more places by $y$.

The variables $x$ and $y$ in Axiom 6 are arbitrary, so the schema also has instances with other variables, such as $y = z \to (\alpha \to \alpha')$.

**Symmetry:** $\vdash_{\mathsf{H}} x = y \to y = x$.

1. $x = y \to (x = x \to y = x)$. Axiom 6 with $\alpha$ the formula $x = x$; replacing the first occurrence of $x$ by $y$ gives $\alpha' = (y = x)$.
2. $(x = y \to (x = x \to y = x)) \to (x = x \to (x = y \to y = x))$. Axiom 1: an instance of the tautology $(A \to (B \to C)) \to (B \to (A \to C))$.
3. $x = x \to (x = y \to y = x)$. MP from 1 and 2.
4. $x = x$. Axiom 5.
5. $x = y \to y = x$. MP from 4 and 3.

**Transitivity:** $\vdash_{\mathsf{H}} x = y \to (y = z \to x = z)$.

1. $y = z \to (x = y \to x = z)$. Axiom 6 with the variables $y, z$ in the roles of $x, y$, and $\alpha$ the formula $x = y$; replacing the occurrence of $y$ by $z$ gives $\alpha' = (x = z)$.
2. $(y = z \to (x = y \to x = z)) \to (x = y \to (y = z \to x = z))$. Axiom 1: the same tautology as in step 2 of the symmetry proof.
3. $x = y \to (y = z \to x = z)$. MP from 1 and 2.

**Congruence for a unary function symbol $f$:** $\vdash_{\mathsf{H}} x = y \to f(x) = f(y)$.

1. $\forall x\,(x = x)$. A generalization of Axiom 5, so a logical axiom.
2. $\forall x\,(x = x) \to f(x) = f(x)$. Axiom 2 with $t = f(x)$; the term is substitutable, since $x = x$ has no quantifier.
3. $f(x) = f(x)$. MP from 1 and 2.
4. $x = y \to (f(x) = f(x) \to f(x) = f(y))$. Axiom 6 with $\alpha$ the formula $f(x) = f(x)$; replacing the occurrence of $x$ on the right side by $y$ gives $f(x) = f(y)$.
5. $(x = y \to (f(x) = f(x) \to f(x) = f(y))) \to (f(x) = f(x) \to (x = y \to f(x) = f(y)))$. Axiom 1, the same tautology again.
6. $f(x) = f(x) \to (x = y \to f(x) = f(y))$. MP from 4 and 5.
7. $x = y \to f(x) = f(y)$. MP from 3 and 6.

## Remarks

The [[generalization theorem|VKSK35Y52Z]] turns each result into a closed theorem, for example $\vdash_{\mathsf{H}} \forall x\,\forall y\,(x = y \to y = x)$, because the derivations use no hypotheses.
Transitivity needs only one instance of Axiom 6; it does not use symmetry.
The congruence proof needs Axiom 2, because Axiom 5 gives $x = x$ only for variables and not for the term $f(x)$.

In Mendelson's variant the axioms are $\forall x\,(x = x)$ and $x = y \to (\varphi(x,x) \to \varphi(x,y))$ for all formulas, and there is a rule of generalization.
The derivations are the same, except that $x = x$ is obtained from $\forall x\,(x = x)$ by the instantiation axiom.

For a binary function symbol $g$, two such derivations, one for each argument, and transitivity give $x_1 = y_1 \to (x_2 = y_2 \to g(x_1, x_2) = g(y_1, y_2))$.
The first one gives $g(x_1, x_2) = g(y_1, x_2)$, and the second one gives $g(y_1, x_2) = g(y_1, y_2)$.

## Explanations

### L1 human

The two basic rules are "everything equals itself" and "equals can replace equals".
To see that $a = b$ gives $b = a$, start from the true statement "$a = a$".
Replace the first $a$ by $b$, which is allowed because $a = b$.
The result is "$b = a$".
Transitivity works in the same way: from "$a = b$" and "$b = c$", replace $b$ by $c$ in the first statement and get "$a = c$".

### L2 human

The pattern of each derivation is the same.

1. Choose an atomic formula $\alpha$ that is already provable, and a place in it to replace a variable.
2. Write the instance of Axiom 6 for that choice.
3. Use the tautology $(A \to (B \to C)) \to (B \to (A \to C))$ to swap the two antecedents.
4. Discharge the provable antecedent $\alpha$ by modus ponens.

The typical use is in any theory with equality, where these derived facts are used without comment.
A trap is to replace all occurrences at once.
In step 1 of the symmetry proof, replacing both occurrences of $x$ in $x = x$ gives only $y = y$, which proves nothing.
