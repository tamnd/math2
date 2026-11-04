---
tag: V5JFWF2SH8
kind: statement
role: theorem
name: Class existence theorem
sources:
  - wikipedia: en:528491@r1330985339
    locator: Von Neumann–Bernays–Gödel set theory, section Axiomatization of NBG > Class existence theorem
    note: adopted
    mention: wikipedia://en/528491#C6WF
    sections: [Statement]
inventory: [ZYYKV7ZQPJ]
---

## Statement

The theorem's proof will be done in two steps:

1. Transformation rules are used to transform the given formula $\phi$ into an equivalent formula that simplifies the [[inductive|0ASJVEFA9J]] part of the proof. For example, the only logical symbols in the transformed formula are $\neg$, $\land$, and $\exists$, so the induction handles logical symbols with just three cases.
1. The class existence theorem is proved inductively for transformed formulas. Guided by the structure of the transformed formula, the class existence axioms are used to produce the unique class of $n$-tuples satisfying the formula.

**Transformation rules.thin** In rules 1 and 2 below, $\Delta$ and $\Gamma$ denote set or class variables. These two rules eliminate all occurrences of class variables before an $\in$ and all occurrences of equality. Each time rule 1 or 2 is applied to a subformula, $i$ is chosen so that $z_i$ differs from the other variables in the current formula. The three rules are repeated until there are no subformulas to which they can be applied. This produces a formula that is built only with $\neg$, $\land$, $\exists$, $\in$, set variables, and class variables $Y_k$ where $Y_k$ does not appear before an $\in$.

1. $\,Y_k \in \Gamma$ is transformed into $\exists z_i(z_i = Y_k \,\land\, z_i \in \Gamma).$
1. Extensionality is used to transform $\Delta = \Gamma$ into $\forall z_i(z_i \in \Delta \iff z_i \in \Gamma).$
1. Logical identities are used to transform subformulas containing $\lor, \implies, \iff,$ and $\forall$ to subformulas that only use $\neg, \land,$ and $\exists.$

**Transformation rules: bound variables.thin** Consider the composite function formula of example 1 with its free set variables replaced by $x_1$ and $x_2$: $\exists t[(x_1, t) \in F \,\land\, (t, x_2) \in G].$ The inductive proof will remove $\exists t$, which produces the formula $(x_1, t) \in F \land (t, x_2) \in G.$ However, since the class existence theorem is stated for subscripted variables, this formula does not have the form expected by the induction hypothesis. This problem is solved by replacing the variable $t$ with $x_3.$ Bound variables within nested quantifiers are handled by increasing the subscript by one for each successive quantifier. This leads to rule 4, which must be applied after the other rules since rules 1 and 2 produce quantified variables.

1. If a formula contains no free set variables other than $x_1, \dots, x_n,$ then bound variables that are nested within $q$ quantifiers are replaced with $x_{n+q}$. These variables have *(quantifier) nesting depth* $q$.

{| class="wikitable"

\|- style="text-align: left; vertical-align: top; style="background: white" |**Example 2:** thinRule 4 is applied to the formula $\phi(x_1)$ that defines the class consisting of all sets of the form $\{\emptyset, \{\emptyset, \dots\}, \dots\}.$ That is, sets that contain at least $\emptyset$ and a set containing $\emptyset$ — for example, $\{\emptyset, \{\emptyset, a, b, c\}, d, e\}$ where $a, b, c, d,$ and $e$ are sets.

$$\begin{aligned} \phi(x_1) \,&=\, \exists u\;\,[\,u \in x_1 \,\land\, \neg\exists v\;\,(\;v\, \in \,u\,)] \,\land\, \,\exists w\;\bigl(w \in x_1 \,\land\, \exists y\;\,[(\;y\, \in w \;\land\; \neg\exists z\;\,(\;z\, \in \,y\,)]\bigr) \\ \phi_r(x_1) \, &=\, \exists x_2[x_2 \!\in\! x_1 \,\land\, \neg\exists x_3(x_3 \!\in\! x_2)] \,\land\, \,\exists x_2\bigl(x_2 \!\in\! x_1 \,\land\, \exists x_3[(x_3 \!\in\! x_2 \,\land\, \neg\exists x_4(x_4 \!\in\! x_3)]\bigr) \end{aligned}$$

Since $x_1$ is the only free variable, $n = 1.$ The quantified variable $x_3$ appears twice in $x_3 \in x_2$ at nesting depth 2. Its subscript is 3 because $n+q = 1+2 = 3.$ If two quantifier scopes are at the same nesting depth, they are either identical or disjoint. The two occurrences of $x_3$ are in disjoint quantifier scopes, so they do not interact with each other. |}
