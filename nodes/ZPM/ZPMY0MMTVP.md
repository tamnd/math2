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

We derive $x = y \to y = x$ in Enderton's [[Hilbert-style predicate calculus|N95HV0VWSM]] $\mathsf{H}$, and then transitivity and the congruence law for a function symbol.
The logical axioms of $\mathsf{H}$ are all generalizations of six groups of formulas, and its only rule is [[modus ponens|0Y0MQYST0M]] (MP).
We use group 1, the [[tautology|05006AJ7DZ]] instances, and group 2, the formulas $\forall x\, \varphi \to \varphi[t/x]$ with $t$ substitutable for $x$.
We also use the two groups of [[equality axioms|Y90Z13AXY8]].
Group 5 is $x = x$.
Group 6 is $x = y \to (\alpha \to \alpha')$, with $\alpha$ atomic and $\alpha'$ obtained from $\alpha$ by replacing $x$ at zero or more places by $y$.
The variables $x$ and $y$ in group 6 are arbitrary, so the schema also has instances with other variables, such as $y = z \to (\alpha \to \alpha')$.
All three derivations use the tautology
$$\text{(Swap)} \quad (A \to (B \to C)) \to (B \to (A \to C)).$$

**Symmetry:** $\vdash_{\mathsf{H}} x = y \to y = x$.
$$\begin{array}{rll} 1. & x = y \to (x = x \to y = x) & \text{group 6} \\ 2. & (x = y \to (x = x \to y = x)) \to (x = x \to (x = y \to y = x)) & \text{group 1, Swap} \\ 3. & x = x \to (x = y \to y = x) & \text{MP, 1 and 2} \\ 4. & x = x & \text{group 5} \\ 5. & x = y \to y = x & \text{MP, 4 and 3} \end{array}$$
Check: in line 1, $\alpha$ is $x = x$, and replacing only the first $x$ by $y$ gives $\alpha' = (y = x)$.

**Transitivity:** $\vdash_{\mathsf{H}} x = y \to (y = z \to x = z)$.
$$\begin{array}{rll} 1. & y = z \to (x = y \to x = z) & \text{group 6} \\ 2. & (y = z \to (x = y \to x = z)) \to (x = y \to (y = z \to x = z)) & \text{group 1, Swap} \\ 3. & x = y \to (y = z \to x = z) & \text{MP, 1 and 2} \end{array}$$
Check: line 1 is group 6 with $y$ and $z$ in the roles of $x$ and $y$, with $\alpha$ the formula $x = y$ and $\alpha' = (x = z)$.

**Congruence for a unary function symbol $f$:** $\vdash_{\mathsf{H}} x = y \to f(x) = f(y)$.
$$\begin{array}{rll} 1. & \forall x\,(x = x) & \text{generalization of group 5} \\ 2. & \forall x\,(x = x) \to f(x) = f(x) & \text{group 2, } t = f(x) \\ 3. & f(x) = f(x) & \text{MP, 1 and 2} \\ 4. & x = y \to (f(x) = f(x) \to f(x) = f(y)) & \text{group 6} \\ 5. & (x = y \to (f(x) = f(x) \to f(x) = f(y))) \to (f(x) = f(x) \to (x = y \to f(x) = f(y))) & \text{group 1, Swap} \\ 6. & f(x) = f(x) \to (x = y \to f(x) = f(y)) & \text{MP, 4 and 5} \\ 7. & x = y \to f(x) = f(y) & \text{MP, 3 and 6} \end{array}$$
Check: in line 2 the term $f(x)$ is substitutable, since $x = x$ has no quantifier.
In line 4, $\alpha$ is $f(x) = f(x)$, and only the $x$ on the right side is replaced by $y$.

## Remarks

### Closed forms

The derivations use no hypotheses, so the [[generalization theorem|VKSK35Y52Z]] turns each result into a closed theorem.
For example, $\vdash_{\mathsf{H}} \forall x\, \forall y\,(x = y \to y = x)$.

### What each derivation needs

Transitivity needs only one instance of group 6, and it does not use symmetry.
The congruence proof needs group 2, because group 5 gives $x = x$ only for variables and not for the term $f(x)$.

### Mendelson's variant

In Mendelson's variant the axioms are $\forall x\,(x = x)$ and $x = y \to (\varphi(x, x) \to \varphi(x, y))$ for all formulas, and there is a rule of generalization.
The derivations are the same, except that $x = x$ comes from $\forall x\,(x = x)$ by the instantiation axiom.

### Functions of two arguments

For a binary function symbol $g$, two derivations of the same kind, one for each argument, give $x_1 = y_1 \to g(x_1, x_2) = g(y_1, x_2)$ and $x_2 = y_2 \to g(y_1, x_2) = g(y_1, y_2)$.
Transitivity joins them into $x_1 = y_1 \to (x_2 = y_2 \to g(x_1, x_2) = g(y_1, y_2))$.

## Explanations

### L1 human

The two basic rules are "everything equals itself" and "equals can replace equals".
To see that $a = b$ gives $b = a$, start from the true statement "$a = a$".
Replace the first $a$ by $b$, which is allowed because $a = b$.
The result is "$b = a$".
Transitivity works in the same way: from "$a = b$" and "$b = c$", replace $b$ by $c$ in the first statement and get "$a = c$".

### L2 human

Each derivation follows one pattern.
First choose an atomic formula $\alpha$ that is already provable, and a place in it where a variable is replaced.
Then write the instance of group 6 for that choice.
Next use the tautology Swap to exchange the two antecedents.
Last, discharge the provable antecedent $\alpha$ by modus ponens.
The typical use is in any theory with equality, where these derived facts are used without comment.
Watch out: do not replace all occurrences at once.
In line 1 of the symmetry proof, replacing both occurrences of $x$ in $x = x$ gives only $y = y$, which proves nothing.
