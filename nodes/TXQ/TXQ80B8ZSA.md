---
tag: TXQ80B8ZSA
kind: concept
name: Description logic
aliases: [description-logics, alc, terminological-logic, concept-language]
msc: ["03B70", "68T30", "03B45"]
topics: [CQM9SRN8PM]
audience: research
uses: [ERG3KAQWYF, 6BQ71KQ6QT, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: The description logic ALC
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: Decision problems
  - book: isbn:9780521695428
    locator: Baader et al., An Introduction to Description Logic
---

## Summary

A description logic is a logic for describing classes of objects and the relations between them, used to write and reason about ontologies.
The basic description logic $\mathcal{ALC}$ has concept names $A$, role names $r$, and concepts built by
$$C, D ::= A \mid \top \mid \bot \mid \neg C \mid C \sqcap D \mid C \sqcup D \mid \exists r.C \mid \forall r.C.$$
An interpretation $\mathcal{I} = (\Delta^{\mathcal{I}}, \cdot^{\mathcal{I}})$ has a nonempty domain, sets $A^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}}$ and relations $r^{\mathcal{I}} \subseteq \Delta^{\mathcal{I}} \times \Delta^{\mathcal{I}}$, and the Boolean constructors are read as set operations, with

1. $(\exists r.C)^{\mathcal{I}} = \set{d : \text{some } e \text{ with } (d, e) \in r^{\mathcal{I}} \text{ has } e \in C^{\mathcal{I}}}$;
2. $(\forall r.C)^{\mathcal{I}} = \set{d : \text{every } e \text{ with } (d, e) \in r^{\mathcal{I}} \text{ has } e \in C^{\mathcal{I}}}$.

A knowledge base is a pair of a TBox, a finite set of inclusions $C \sqsubseteq D$, and an ABox, a finite set of assertions $C(a)$ and $r(a, b)$ about named individuals.
Description logics matter because they are decidable fragments of [[first-order logic|086QKPF0A6]] with well-understood complexity, and they are the logical basis of the Web Ontology Language OWL.

## Motivation

Knowledge representation needs a language in which an expert can define terms, such as "a parent is a person with a child who is a person", and a machine can check the definitions.
Full first-order logic is undecidable, so a reasoner could not always answer.
Description logics keep only the variable-free constructs needed for classes and relations, and so they keep decidability.
The same constructs are the box and diamond of [[multimodal logic|ERG3KAQWYF]], so description logics inherit the methods of [[Kripke semantics|6BQ71KQ6QT]], tableaux and automata.

## Notation

1. $\mathcal{I} \models C \sqsubseteq D$ means $C^{\mathcal{I}} \subseteq D^{\mathcal{I}}$; $\mathcal{I} \models C(a)$ means $a^{\mathcal{I}} \in C^{\mathcal{I}}$; $\mathcal{I} \models r(a, b)$ means $(a^{\mathcal{I}}, b^{\mathcal{I}}) \in r^{\mathcal{I}}$.
2. $C \equiv D$ abbreviates the two inclusions $C \sqsubseteq D$ and $D \sqsubseteq C$.
3. $\mathcal{T} \models C \sqsubseteq D$ means that every model of the TBox $\mathcal{T}$ satisfies the inclusion; $\mathcal{K} \models C(a)$ is instance checking.
4. Letters added to $\mathcal{ALC}$ name extensions: $\mathcal{Q}$ for number restrictions such as ${\ge} 2\, r.C$, $\mathcal{I}$ for inverse roles, $\mathcal{O}$ for nominals, $\mathcal{S}$ for transitive roles.

## Remarks

### Examples

1. With $\mathcal{T} = \set{\mathsf{Parent} \equiv \mathsf{Person} \sqcap \exists \mathsf{hasChild}.\mathsf{Person}}$ and an ABox stating that Mary is a female person with a child Tom who is a person, the knowledge base entails $\mathsf{Parent}(\mathsf{mary})$, see [[a TBox and an ABox|YN1ZHN0085]].
2. The concept $\exists r.A \sqcap \forall r.B$ is subsumed by $\exists r.(A \sqcap B)$, which is the modal law $\Diamond p \wedge \Box q \to \Diamond(p \wedge q)$, see [[translating a concept|ZC9KDE68ER]].
3. The light description logic $\mathcal{EL}$, with only $\top$, $\sqcap$ and $\exists r.C$, has subsumption decidable in polynomial time, and it is used for large medical ontologies such as SNOMED CT.

### Non-examples

1. The concept "has at least two $r$-successors", ${\ge} 2\, r.\top$, is not expressible in $\mathcal{ALC}$, see [[number restrictions are not ALC concepts|5KQCT1HMC3]].
2. A first-order formula with two free variables, such as $r(x, y) \wedge r(y, x)$, is not a concept: concepts denote sets, not relations.

### Basic properties

1. Schild's correspondence: $\mathcal{ALC}$ concepts are the formulas of the multimodal logic $\mathsf{K}_n$, with one modality per role, and interpretations are Kripke models, see [[the correspondence theorem|G8BHVS9715]].
2. Concept satisfiability in $\mathcal{ALC}$ without a TBox is [[PSPACE-complete|JWC9CE07Q2]] (Schmidt-Schauß and Smolka, 1991).
3. Satisfiability with respect to a general TBox is [[EXPTIME|T9G5S33CA0]]-complete.
4. Subsumption reduces to satisfiability: $\mathcal{T} \models C \sqsubseteq D$ iff $C \sqcap \neg D$ is unsatisfiable with respect to $\mathcal{T}$.
5. Concepts are invariant under [[bisimulation|7T740SFHHV]], and $\mathcal{ALC}$ has the tree model property and the finite model property.
6. Every $\mathcal{ALC}$ concept is equivalent to a formula of the two-variable guarded fragment of first-order logic, by the [[standard translation|YW6YGBMVQY]].

### History

Description logics grew out of the semantic networks and frame languages of the 1970s, through the system KL-ONE of Brachman.
Early names were terminological logics and concept languages.
Schmidt-Schauß and Smolka introduced $\mathcal{ALC}$ ("attributive language with complements") in 1991 and proved its satisfiability problem PSPACE-complete.
In the same year Schild showed that $\mathcal{ALC}$ is a notational variant of multimodal $\mathsf{K}$.
The description logic $\mathcal{SROIQ}$ is the logical basis of OWL 2 DL.

### Common errors

1. Reading an ABox under the closed world assumption. A knowledge base that does not entail $C(a)$ does not entail $\neg C(a)$ either.
2. Reading $\forall r.C$ as requiring an $r$-successor. An object with no $r$-successors belongs to $\forall r.C$ for every $C$.
3. Assuming that distinct names denote distinct objects. $\mathcal{ALC}$ does not impose the unique name assumption unless it is added.

## Explanations

### L1 human

A description logic is a precise language for definitions such as "a parent is a person who has a child".
It talks about kinds of things, like "person", and about relations, like "has child".
A computer can then check whether one kind is always included in another.
For example, it can check that every mother is a parent, once both are defined.

### L2 human

We check that $\mathsf{Mother} \sqsubseteq \mathsf{Parent}$ follows from the TBox $\mathsf{Parent} \equiv \mathsf{Person} \sqcap \exists \mathsf{hasChild}.\mathsf{Person}$ and $\mathsf{Mother} \equiv \mathsf{Parent} \sqcap \mathsf{Female}$.

1. Let $\mathcal{I}$ be a model of the TBox and $d \in \mathsf{Mother}^{\mathcal{I}}$.
2. By the second definition, $d \in \mathsf{Parent}^{\mathcal{I}}$.
3. So $\mathsf{Mother}^{\mathcal{I}} \subseteq \mathsf{Parent}^{\mathcal{I}}$ in every model.

The typical use is to classify an ontology: compute all subsumptions between named concepts.
A trap: a subsumption that holds in one model need not follow from the TBox; it must hold in every model.

### L3 human

Under Schild's correspondence, a TBox inclusion $C \sqsubseteq D$ is the global modal axiom $\tau(C) \to \tau(D)$, which is why general TBoxes raise satisfiability from PSPACE to EXPTIME, as global consequence does for $\mathsf{K}$.
Inverse roles correspond to converse modalities and tense logic, nominals to hybrid logic, and transitive roles to $\mathsf{K4}$ modalities.
Query answering over ontologies, with conjunctive queries in place of concepts, connects description logic with database theory.
