# math2

This repository holds the content of Math 2.0. Math 2.0 is a versioned knowledge graph of mathematics. A person or a program can read it, run it, check it and move through it.

Each node is one file. A node is a concept, a definition, a statement, a conjecture, a problem, an example, a counterexample, an object, a proof, a computation or a topic. Each node has a permanent tag, its sources, its links to other nodes and a status. The build computes the status from the evidence. Formal statements and proofs use Lean 4 and Mathlib.

The toolchain that builds and checks this content is in [tamnd/math2-agent](https://github.com/tamnd/math2-agent).

Read the content as a wiki at https://tamnd.github.io/math2. Each node has a page for people and a copy for programs: Markdown, JSON and `llms.txt`. The wiki is rebuilt on each push to `main` and each night.

## Status

The project is at milestone M1. The repository has its first two nodes: the group concept and Lagrange's theorem. The wiki shows the spec, the plan and each node. The Lean package pins Lean v4.35.0 and Mathlib v4.35.0. It has the `@[m2 "TAG"]` attribute and one adapter. The adapter derives the form of Lagrange's theorem in node 3C53TD from the Mathlib theorem `Subgroup.card_subgroup_dvd_card`. The seed list `topics/curricula/seed.yaml` has 2,416 items in 14 courses of the first and second year. The seed nodes come from this list. Refer to the [milestones](https://github.com/tamnd/math2-agent/milestones) for the plan.

## The seed list

The file `topics/curricula/seed.yaml` lists the concepts, the definitions and the main statements of 14 courses, from logic and sets to probability. The courses and the items are in teaching order. An item that two courses teach is in the first of them only.

Each item has a name, a kind and at least one source. A source is an article of the English Wikipedia, with its Wikidata item, or a Mathlib list. 1,771 items have the Mathlib declaration that defines or states them, at the pinned Mathlib commit. An item without a declaration has no declaration in Mathlib that matches it. The field `node` gives the tag of the node for the item, when the node exists. The schema is `schema/curriculum.v1.json`.

## The skeletons

A skeleton is the list of the main concepts, definitions and named theorems of one top-level MSC2020 class. It is the file `topics/skeletons/NN.yaml`, where NN is the first two characters of the code, for example `topics/skeletons/20.yaml` for 20-XX. The items have the same fields as the items of the seed list. The schema is `schema/skeleton.v1.json`.

The coverage report gives C2 for each class with a skeleton (spec 18.1). C2 is the share of the items whose node is live and has at least one source. A person who works in the area reviews each change of a skeleton in its pull request.

The first 30 skeletons are drafts. They cover the classes 03, 05, 06, 11 to 18, 20, 22, 26, 28, 30, 34, 35, 37, 40, 46, 47, 51 to 55, 57, 60 and 68, with 6,812 items. 2,066 items have a Mathlib declaration. No person who works in these areas has reviewed them yet. Until a review, treat the C2 numbers of these classes as provisional. The other 33 classes have no skeleton yet.

## A node file

A node file is `nodes/<first two characters of the tag>/<tag>.md`. It has YAML front matter and a Markdown body. This example shows the form:

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

A new node has a provisional id until it merges, for example `~3fa94c01`. Before the merge, the mint workflow changes it to a tag and adds the tag to `registers/tags.reg`. CONTRIBUTING.md has the steps.

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

## Add a node

1. Install Go 1.27 or later. Then install the toolchain: `go install github.com/tamnd/math2-agent/cmd/m2@latest`.
2. Fork this repository, or make a branch if you can push to it.
3. Run `m2 new <kind>`, for example `m2 new statement`. It makes a file in `nodes/~/` with a provisional id. The 11 kinds are concept, definition, statement, conjecture, problem, example, counterexample, object, proof, computation and topic.
4. Write a value for each field that has the value `null`. Write the body under the headings. Use the example in "A node file". Write each sentence on one line.
5. Run `m2 fmt`, then `m2 check`. `m2 check` must report 0 findings.
6. Open a pull request. The `tags` check fails while the pull request has a provisional id. This is correct. A maintainer gives the tags before the merge. The other checks must pass.

CONTRIBUTING.md has the rules and the steps for the maintainer.

## Fidelity reviews

A fidelity review says that the Lean statement of a node says what its informal statement says. One review gives the binding F2, and E5 needs F2. The reviews are in `reviews/`, and `reviews/README.md` is the guide for reviewers. Each commit that changes `reviews/` must be signed.

## Check the content

You can check the node files with Python, PyYAML and jsonschema. You do not need the toolchain.

```sh
pip install --require-hashes -r .github/scripts/requirements.txt
python .github/scripts/check_nodes.py
python .github/scripts/check_curricula.py
python .github/scripts/check_reviews.py
```

`check_curricula.py` also checks the skeletons. With `--decls FILE`, it also reports each declaration that is not a line of FILE. Make the file from the `.ilean` files of the Lean build.

To build the Lean package, install [elan](https://github.com/leanprover/elan) and run these commands:

```sh
cd lean
lake exe cache get
lake build
```

The full audit is `m2 audit` from tamnd/math2-agent. Run it in the root of the repository. `m2 audit -changed` audits only the changes of your branch against `origin/main`. The check workflow runs `m2 audit -changed` on each pull request and the full audit on each push to `main`. The report goes to `reports/audit/`.

CI installs the `m2` version that `manifests/releases/next.yaml` pins. Move the pin in a pull request after each release of tamnd/math2-agent. Each day the audit workflow builds `main`, runs the full audit and opens a pull request when the report in `reports/audit/` changes.

## Releases

Releases use calendar versions, `YYYY.MM`, one each month. Each release pins one Lean stable release, one Mathlib tag, the container images, the model ids and the prompt versions. The first release is 2027.03. It gets a DOI and goes to Software Heritage and Zenodo.

Each week the bump workflow runs `m2 bump`. It moves `lean/` to the newest Mathlib release and opens a pull request with the report from `reports/bump/`. It also builds Mathlib `master` as an early warning. That build never becomes a pull request.

The release workflow cuts a release with `m2 release cut`:

1. The step `cut` builds `main`, writes the manifest, the levels and the notes of the release into `manifests/releases/`, and opens the pull request `release/NAME`. Then a second runner rebuilds the release with `m2 release verify` and adds the rebuild check to the pull request.
2. A person writes the summary of the notes and merges the pull request.
3. The step `tag` runs the full audit on `main`, and makes the tag and the GitHub release only when the audit passes. It builds the site of the release, checks it with `m2 site check`, and attaches the offline archive `math2-NAME-site.zip` to the GitHub release. Then the job `pages` publishes the same build of the site to https://tamnd.github.io/math2. To read a release with no network, unzip the archive and open `index.html` in a web browser.

The schedule runs the step `cut` on the first day of each month when the repository variable `M2_RELEASES` is `true`. With `dry-run`, the step makes no commit and no pull request, and the files go into an artefact of the run.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md). To decide on the proposals of `m2 align`, read [CURATION.md](CURATION.md). Each change is a pull request. The checks are the gate.

## Licence

This repository has three licence zones. [REUSE.toml](REUSE.toml) gives the licence for each path.

| Part | Licence |
|---|---|
| Prose in `nodes/`, `topics/` and `reviews/` | CC BY-SA 4.0 |
| Code in `lean/`, `compute/` and `.github/` | Apache-2.0 |
| Metadata in `manifests/`, `registers/`, `prov/` and `schema/` | CC0 1.0 |

Refer to [LICENCE](LICENCE) for the reasons.
