---
tag: AAVBSD1CXQ
kind: statement
role: proposition
name: Axiom systems
sources:
  - wikipedia: en:81395508@r1360635402
    locator: Conditional logic, section Axiom systems
    note: adopted
    mention: wikipedia://en/81395508#LWH8
    sections: [Statement]
inventory: [5D8QBGANYP]
---

## Statement

Many conditional logics are given by Hilbert–style calculi extending classical propositional logic with a distinguished conditional connective $\mathbin{>}$. A typical system contains all propositional tautologies in the language with $\mathbin{>}$, is closed under modus ponens, and is further closed under some combination of structural rules and schematic principles for $\mathbin{>}$. This section summarizes some historically central systems and their axiomatizations.

A convenient starting point is Chellas's basic conditional logics **Ck** and **CK**, which correspond to the core selection function semantics for conditionals.

- **Ck** is the minimal system containing all propositional tautologies and closed under (MP) and (RCK). It may be viewed as a "hyperintensional" base system: it validates (RCK) but not (LLE).
- **CK** adds (LLE) to Ck. Equivalently, CK is the smallest logic containing all propositional tautologies and closed under (MP), (LLE) and (RCK). In CK, principles (LT), (RW) and (AND) are theorems, while stronger principles such as (ID), (OR), (CMon), (Rec), (RMon), (SM), (CS) and (CEM) are generally not validated.

CK is often taken as the conditional analogue of the normal modal logic K: it axiomatizes the basic variably strict semantics with arbitrary selection functions or similarity orderings, without extra frame conditions.

Building on CK, a family of stronger logics is obtained by adding further schemata. Égré and Rott highlight nine "salient" systems Ck, CK, B, SS, NP, V, VW, VC and C2, all normal in the above sense.

**B**

Burgess's system **B** is the smallest extension of CK in which (ID), (OR) and (CMon) hold; with (RCK) and (LLE) these also yield (AND), (CCut) and (Rec). In ordering semantics, B corresponds to models in which each world is equipped with a reflexive and transitive similarity preorder.

**V**

Lewis's logic **V** adds to B the principle (RMon). Semantically, this corresponds to strengthening the similarity ordering to a weak order (modular, total-preorder–like) at each evaluation world.

**VW**

System **VW** further extends V by validating (SM), so that every conditional implies the corresponding material conditional. This makes VW suitable as a weaker "counterfactual" logic that still preserves modus ponens in the usual way.

**VC**

Lewis's "official" logic of counterfactuals **VC** adds (CS) to VW. VC is thus the smallest normal logic extending V that validates both (SM) and (CS); in Lewis's sphere semantics this corresponds to total preorders with additional constraints ensuring that whenever both $A$ and $A\land B$ are possible, $A \land B$–worlds are among the closest $A$–worlds.

**C2**

Stalnaker's logic **C2** can be obtained from VC by replacing (CS) with the stronger (CEM). C2 is thus VC + (CEM), and it characterizes the simplified Stalnaker models in which each antecedent selects a unique closest antecedent world at every evaluation point.

**SS**

Pollock's system **SS** is obtained by adding (SM) and (CS) directly to B (rather than via V). It validates many of the same laws as VC but is based on partial, rather than total, similarity orderings.

**NP**

Delgrande's system **NP** is another extension of CK: like B it validates (ID), (AND), (OR) and (CCut), but instead of (CMon) it validates (RMon). This shows that the cautious and rational forms of monotonicity are independent over CK.

These systems all validate (LT) and (AND), differ on the status of (ID), (OR), (CCut), (CMon), (Rec), (RMon), (SM), (CS) and (CEM), and none validates full Monotonicity, Transitivity or Contraposition for $\mathbin{>}$.

An alternative but equivalent presentation of many of the above systems is widely used in the Lewis–Nute tradition, and is convenient when relating conditional logics directly to selection function semantics. In this type of axiomatization, one takes as primitive:

- all propositional tautologies in the language with $\mathbin{>}$;
- the rule (MP);
- one or both of the "replacement" rules

**(RCEC)** from $\varphi \leftrightarrow \psi$, infer $(\chi \mathbin{>} \varphi) \leftrightarrow (\chi \mathbin{>} \psi)$;

**(RCEA)** from $\varphi \leftrightarrow \psi$, infer $(\varphi \mathbin{>} \chi) \leftrightarrow (\psi \mathbin{>} \chi)$;

- and the rule

**(RCK)** as above.

In this setting, the Lewis systems V, VW, VC and Stalnaker's C2 can be described as the smallest conditional logics containing all tautologies, closed under (MP), (RCEC) and (RCK), and containing all substitution instances of appropriate sets of schemata such as:

**ID** $\varphi \mathbin{>} \varphi$;

**MP/SM** $(\varphi \mathbin{>} \psi) \to (\varphi \to \psi)$;

**MOD** $(\neg \varphi \mathbin{>} \varphi) \to (\psi \mathbin{>} \varphi)$;

**CSO** $((\varphi \mathbin{>} \psi)\land(\psi \mathbin{>} \varphi)) \to ((\varphi \mathbin{>} \chi) \leftrightarrow (\psi \mathbin{>} \chi))$;

**CV** $((\varphi \mathbin{>} \psi)\land\neg(\varphi \mathbin{>} \neg \chi)) \to ((\varphi \land \chi) \mathbin{>} \psi)$;

**CS** $(\varphi \land \psi) \to (\varphi \mathbin{>} \psi)$;

**CEM** $(\varphi \mathbin{>} \psi) \lor (\varphi \mathbin{>} \neg \psi)$.

For example, one standard presentation takes:

- **V** as the smallest logic with (RCEC), (RCK) and schemata ID, MOD, CSO, CV;
- **VW** as V + (SM);
- **VC** as VW + (CS);
- **C2** as VC with (CS) replaced by (CEM).

These axiomatizations are equivalent to the ones described via the Table 6 schemata above and are often used in proof theory and automated reasoning for conditional logics.

In artificial intelligence and nonmonotonic reasoning it is common to work, not directly with a connective $\mathbin{>}$, but with a defeasible consequence relation $\vdash_{\!\sim}$ intended to capture defaults of the form "normally, if $A$ then $B$". Kraus, Lehmann and Magidor axiomatized three central such systems, now known as C, P and R. 

These systems are given by rules on $\vdash_{\!\sim}$ such as:

- **(ID<sub>~</sub>)** Identity: $A \vdash_{\!\sim} A$.
- **(LLE<sub>~</sub>)** Left logical equivalence: if $\vDash A \equiv B$ and $A \vdash_{\!\sim} C$, then $B \vdash_{\!\sim} C$.
- **(RW<sub>~</sub>)** Right weakening: if $\vDash C \to D$ and $A \vdash_{\!\sim} C$, then $A \vdash_{\!\sim} D$.
- **(CCut<sub>~</sub>)** Cautious cut: from $A \vdash_{\!\sim} B$ and $A \land B \vdash_{\!\sim} C$, infer $A \vdash_{\!\sim} C$.
- **(CMon<sub>~</sub>)** Cautious monotonicity: from $A \vdash_{\!\sim} B$ and $A \vdash_{\!\sim} C$, infer $A \land B \vdash_{\!\sim} C$.
- **(AND<sub>~</sub>)** And: from $A \vdash_{\!\sim} B$ and $A \vdash_{\!\sim} C$, infer $A \vdash_{\!\sim} (B \land C)$.
- **(OR<sub>~</sub>)** Or: from $A \vdash_{\!\sim} C$ and $B \vdash_{\!\sim} C$, infer $A \lor B \vdash_{\!\sim} C$.
- **(RMon<sub>~</sub>)** Rational monotonicity: from $A \vdash_{\!\sim} C$ and not $A \vdash_{\!\sim} \neg B$, infer $A \land B \vdash_{\!\sim} C$.

On this basis one defines:

- System **C** (cumulative): the smallest relation satisfying (ID<sub>~</sub>), (LLE<sub>~</sub>), (RW<sub>~</sub>), (CCut<sub>~</sub>) and (CMon<sub>~</sub>) (and hence (AND<sub>~</sub>)).
- System **P** (preferential): C plus (OR<sub>~</sub>); it is sound and complete for preferential models and corresponds to the "flat" ($L_1$) fragment of several conditional logics such as B and VC.
- System **R** (rational): P plus (RMon<sub>~</sub>); it is complete for ranked (totally ordered) preferential models.

Via translations of the form "$A \mathbin{>} B$ is accepted iff $A \vdash_{\!\sim} B$", these nonmonotonic systems can be seen as providing the flat fragments of many of the selection–function conditional logics described above, linking conditional logic to AGM belief revision and default reasoning.
