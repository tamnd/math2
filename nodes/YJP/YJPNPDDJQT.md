---
tag: YJPNPDDJQT
kind: example
name: A deduction with a captured variable
msc: ["03B10"]
topics: [TTCRX3NFNY]
audience: ug2
not_instance_of:
  - target: N95HV0VWSM
    note: the second line is not an instance of the instantiation axiom, because the term y is not substitutable for x, so the list is not a deduction
uses: [2B00FE6K5W, NCDZ969V7X, 983GZBQYT4]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
---

## Example

We work in the [[Hilbert-style predicate calculus|2B00FE6K5W]] $\mathsf{H}$, for the language with equality and no other symbols.
Let $\Gamma = \{ \forall x\, \neg \forall y\,(x = y) \}$.
The hypothesis says that for each $x$ some $y$ differs from $x$, so it says that the domain has at least two elements.
Consider the following list of three formulas.

$$\begin{array}{rll} \text{(i)} & \forall x\, \neg \forall y\,(x = y) & \text{member of } \Gamma \\ \text{(ii)} & \forall x\, \neg \forall y\,(x = y) \to \neg \forall y\,(y = y) & \text{claimed: group 2 with } t = y \\ \text{(iii)} & \neg \forall y\,(y = y) & \text{modus ponens, (i) and (ii)} \end{array}$$

We check that the list is not a deduction.

1. Group 2 contains $\forall x\, \varphi \to \varphi[t/x]$ only when $t$ is substitutable for $x$ in $\varphi$.
   Here $\varphi = \neg \forall y\,(x = y)$ and $t = y$.
2. The only free occurrence of $x$ in $\varphi$ lies inside the scope of $\forall y$.
3. Replacing it by $y$ gives $\neg \forall y\,(y = y)$, where the new $y$ is bound by $\forall y$.
   So $y$ is not substitutable for $x$ in $\varphi$, in the sense of [[substitution|NCDZ969V7X]], and line (ii) is not in group 2.
4. Line (ii) is not a tautology either.
   Its prime formulas are $\forall x\, \neg \forall y\,(x = y)$ and $\forall y\,(y = y)$, and making both true makes line (ii) false.
5. Line (ii) is not in groups 3 to 6.
   Its consequent is a negation, and its antecedent is neither an equation nor of the form $\forall x\,(\varphi \to \psi)$.
6. Line (ii) is not a generalization of any axiom, since its main symbol is $\to$, not $\forall$.
7. Line (ii) is not in $\Gamma$, and it cannot come from modus ponens, since only one line precedes it.
   So the list is not a deduction.

The list is also unsound, which shows why the rule forbids it.

8. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{ 0, 1 \}$, where $=$ means identity.
9. For $x = 0$ the formula $\forall y\,(0 = y)$ is false, because $0 \neq 1$.
   For $x = 1$ it is false, because $1 \neq 0$.
   So $\mathcal{M} \models \forall x\, \neg \forall y\,(x = y)$, and $\mathcal{M}$ satisfies $\Gamma$.
10. The formula $\forall y\,(y = y)$ is true in $\mathcal{M}$, so line (iii) is false in $\mathcal{M}$.
11. So line (ii) is false in $\mathcal{M}$: its antecedent is true and its consequent is false.

## Remarks

### The correct move

The right way to instantiate is to rename the bound variable first.
The formula $\forall x\, \neg \forall z\,(x = z)$ means the same as the hypothesis, and $y$ is substitutable for $x$ in $\neg \forall z\,(x = z)$.
The instance $\neg \forall z\,(y = z)$ says that some element differs from $y$, which is true in $\mathcal{M}$ for both values of $y$.

### What changes with a constant

Replace the hypothesis by $\forall x\, \neg (x = c)$ with a constant symbol $c$.
The same move now gives $\neg (c = c)$, and this time no capture happens.
The constant $c$ is substitutable, the instance is a real axiom, and $\Gamma$ is inconsistent, as it should be, since $c$ names an element that equals itself.

## Explanations

### L1 human

The hypothesis says: "for every person $x$, not everybody is $x$".
Plugging the name $y$ into a sentence that already uses $y$ for "everybody" changes the meaning.
The result says "not everybody is themselves", which is absurd.
The rule of the calculus forbids this plug-in, so the absurd line cannot be deduced.

### L2 human

To check a claimed instance of $\forall x\, \varphi \to \varphi[t/x]$, do three things.
First, find the free occurrences of $x$ in $\varphi$.
Second, list the quantifiers in whose scope each of them lies.
Third, check that no variable of $t$ is bound by one of these quantifiers.
Here the second step finds $\forall y$, and the third step fails because $t = y$.
The usual fix is to rename the bound variable, which gives an equivalent formula.
Watch out: the check is needed even for one-letter terms, since the term $y$ already fails it.
