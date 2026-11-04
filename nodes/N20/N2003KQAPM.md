---
tag: N2003KQAPM
kind: statement
role: proposition
name: Formula level
sources:
  - wikipedia: en:1974007@r1305487255
    locator: Independence-friendly logic, section Model-theoretic properties > Formula level
    note: adopted
    mention: wikipedia://en/1974007#0XFD
    sections: [Statement]
inventory: [WJZ74WPV9H]
---

## Statement

The notion of satisfiability by a team has the following properties:

- Downward closure: if $\mathcal M,X\models^\pm \varphi$ and $Y\subseteq X$, then $\mathcal M,Y\models^\pm \varphi$.
- Consistency: $\mathcal M,X\models^+ \varphi$ and $\mathcal M,X\models^- \varphi$ if and only if $X=\emptyset$.
- Non-locality: there are $\mathcal M,X,\varphi$ such that $\mathcal M,X\models \varphi\not\Leftrightarrow M,X_{\upharpoonright \mbox{Free}(\varphi)}\models \varphi$.

Since IF formulas are satisfied by teams and formulas of classical logics are satisfied by assignments, there is no obvious intertranslation between IF formulas and formulas of some classical logic system. However, there is a translation procedure of IF formulas into *sentences* of *relational* $\Sigma_1^1$ (actually, one distinct translation $\tau_{U,R}$ for each finite $U\supseteq \mbox{Free}(\varphi)$ and for each choice of a predicate symbol $R$ of arity $card(U)$). In this kind of translation, an extra n-ary predicate symbol $R$ is used to represent an n-variable team $X$. This is motivated by the fact that, once an ordering $v_1\dots v_n$ of the variables of $dom(X)$ has been fixed, it is possible to associate a relation $Rel_{v_1\dots v_n}(X) = \{(s(v_1),\dots,s(v_n)) | s\in X\}$ to the team $X$. With this conventions, an IF formula is related to its translation thus:

$$\mathcal M,X\models \varphi \Leftrightarrow (\mathcal M,Rel_{v_1\dots v_n}(X))\models \tau_{dom(X),R}(\varphi)$$

where $(M,Rel_{v_1\dots v_n}(X))$ is the expansion of $\mathcal M$ that assigns $Rel_{v_1\dots v_n}(X)$ as interpretation for the predicate $R$.

Through this correlation, it is possible to say that, on a structure $\mathcal M$, an IF formula $\varphi$ of n free variables *defines* a family of n-ary relations over $\mathcal M$ (the family of the relations $Rel_{v_1\dots v_n}(X)$ such that $\mathcal M,X\models\varphi$).

In 2009, Kontinen and Väänänen, showed, by means of a partial inverse translation procedure, that the families of relations that are definable by IF logic are exactly those that are nonempty, downward closed and definable in relational $\Sigma_1^1$ with an extra predicate $R$ (or, equivalently, nonempty and definable by a $\Sigma_1^1$ sentence in which $R$ occurs only negatively).
