---
tag: 8M9ZFDR4DH
kind: statement
role: theorem
name: The deduction theorem in predicate logic
sources:
  - wikipedia: en:480010@r1320842012
    locator: Deduction theorem, section The deduction theorem in predicate logic
    note: adopted
    mention: wikipedia://en/480010#Y3DL
    sections: [Statement]
inventory: [TGSPJ68GEB]
---

## Statement

The deduction theorem is also valid in [[first-order logic|086QKPF0A6]] in the following form:

- If *T* is a theory and *F*, *G* are formulas with *F* closed, and $T \cup \{ F \} \vdash G$, then $T \vdash F \rightarrow G$.

Here, the symbol $\vdash$ means "is a syntactical consequence of." We indicate below how the proof of this deduction theorem differs from that of the deduction theorem in propositional calculus.

In the most common versions of the notion of formal proof, there are, in addition to the axiom schemes of propositional calculus (or the understanding that all tautologies of propositional calculus are to be taken as axiom schemes in their own right), [[quantifier axioms|086QKPF0A6]], and in addition to [[modus ponens|0Y0MQYST0M]], one additional rule of inference, known as the rule of *generalization*: "From *K*, infer ∀*vK*."

In order to convert a proof of *G* from *T*∪{*F*} to one of *F*→*G* from *T*, one deals with steps of the proof of *G* that are axioms or result from application of modus ponens in the same way as for proofs in propositional logic. Steps that result from application of the rule of generalization are dealt with via the following quantifier axiom (valid whenever the variable *v* is not free in formula *H*):

- (∀*v*(*H*→*K*))→(*H*→∀*vK*).

Since in our case *F* is assumed to be closed, we can take *H* to be *F*. This axiom allows one to deduce *F*→∀*vK* from *F*→*K* and generalization, which is just what is needed whenever the rule of generalization is applied to some *K* in the proof of *G*.

In first-order logic, the restriction of that F be a closed formula can be relaxed given that the free variables in F have not been varied in the deduction of G from $T \cup \{ F \}$. In the case that a free variable v in F has been varied in the deduction, we write $T \cup \{ F \} \vdash^v G$ (the superscript in the turnstile indicating that v has been varied) and the corresponding form of the deduction theorem is $T \vdash (\forall vF) \rightarrow G$.
