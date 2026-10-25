# math2

This repository holds the content of Math 2.0. Math 2.0 is a versioned knowledge graph of mathematics. A person or a program can read it, run it, check it and move through it.

Each node is one file. A node is a concept, a definition, a statement, a conjecture, a problem, an example, a counterexample, an object, a proof, a computation or a topic. Each node has a permanent tag, its sources, its links to other nodes and a status. The build computes the status from the evidence. Formal statements and proofs use Lean 4 and Mathlib.

The toolchain that builds and checks this content is in [tamnd/math2-agent](https://github.com/tamnd/math2-agent).

## Status

The project is at milestone M0. The repository has no nodes yet. The Lean package pins Lean v4.35.0 and Mathlib v4.35.0. It has no declarations yet. Refer to the [milestones](https://github.com/tamnd/math2-agent/milestones) for the plan.

## A node file

A node file is `nodes/<first two characters of the tag>/<tag>.md`. It has YAML front matter and a Markdown body. The schema is not final until M0 closes. This example shows the planned form:

```markdown
---
tag: 7K3QX2
kind: statement
role: theorem
name: Lagrange's theorem
msc: [20D60]
uses: [1H8D2C, 6PQ0WZ]
proofs: [9TX3RB]
formal:
  - system: lean4
    library: mathlib
    decl: Subgroup.card_subgroup_dvd_card
    match: exact
sources:
  - book: "isbn:9780471433347"
    locator: "Section 3.2, Theorem 8"
same_as:
  wikidata: Q180967
---

## Statement

Let $G$ be a finite [[group|1A2B3C]] and let $H$ be a [[subgroup|1H8D2C]] of $G$. Then $|H|$ divides $|G|$.
```

## Identifiers

A tag has 6 characters of Crockford base32, for example `7K3QX2`. A tag does not change, and nobody uses it again for a different node. To remove a node, retire it. The retired tag points to the node that replaces it. Tags that start with `0` are the M1 seed.

A new node has a provisional id until it merges, for example `~3fa94c01`. The merge bot changes it to a tag.

The URI of a node is `m2://7K3QX2`. To refer to a node in a release, add the release, for example `m2://7K3QX2@2027.03`.

## Status levels

The build computes two levels for each statement. No person and no agent writes them.

| Evidence | Meaning |
|---|---|
| E5 kernel | The Lean kernel checks a proof of a bound formal statement. Independent checkers replay it. |
| E4 certified | A checked certificate from a computation proves it. |
| E3 refereed | A proof is in the refereed literature. |
| E2 standard | It is standard textbook mathematics. |
| E1 claimed | A preprint, a person or an agent claims it. Nobody has checked the claim. |
| E0 open | It is an open question. |
| E⊥ refuted | A counterexample or a proof of the negation exists. |

| Fidelity | Meaning |
|---|---|
| F0 | A formal statement is bound. Nobody has compared it with the informal statement. |
| F1 | The machine checks agree: back-translation, type checks, a critic and the checks for degenerate statements. |
| F2 | One person who is not the author reviewed this exact statement hash. |
| F3 | Two independent reviews agree, or a second independent formalization is proved equivalent. |

A review is bound to the hash of the informal statement and to the hash of the elaborated Lean type. If either hash changes, the review stops counting.

## Check the content

You can check the node files with Python, PyYAML and jsonschema. You do not need the toolchain.

```sh
pip install --require-hashes -r .github/scripts/requirements.txt
python .github/scripts/check_nodes.py
```

To build the Lean package, install [elan](https://github.com/leanprover/elan) and run these commands:

```sh
cd lean
lake exe cache get
lake build
```

The full audit is `m2 audit` from tamnd/math2-agent. It arrives in M1.

## Releases

Releases use calendar versions, `YYYY.MM`, one each month. Each release pins one Lean stable release, one Mathlib tag, the container images, the model ids and the prompt versions. The first release is 2027.03. It gets a DOI and goes to Software Heritage and Zenodo.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). Each change is a pull request. The checks are the gate.

## Licence

This repository has three licence zones. [REUSE.toml](REUSE.toml) gives the licence for each path.

| Part | Licence |
|---|---|
| Prose in `nodes/`, `topics/` and `reviews/` | CC BY-SA 4.0 |
| Code in `lean/`, `compute/` and `.github/` | Apache-2.0 |
| Metadata in `manifests/`, `registers/`, `prov/` and `schema/` | CC0 1.0 |

Refer to [LICENCE](LICENCE) for the reasons.
