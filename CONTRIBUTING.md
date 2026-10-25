# Contributing to math2

## What you can contribute

1. A new node: a concept, a definition, a statement, a proof, an example or a problem.
2. A change to a node: a better statement, a source, a link or an explanation.
3. A formal binding: a link from a statement to a Lean declaration.
4. A fidelity review: a check that a formal statement says the same thing as its informal statement.
5. A report of an error.

## Add a node

1. Make a branch from `main`.
2. Make the file `nodes/~/~<8 hex characters>.md`. The name is a provisional id, for example `~3fa94c01`. Do not choose a tag. The merge bot gives the tag.
3. Write the front matter and the body. Use the example in the README.
4. Write each sentence on one line. Do not break a sentence across lines.
5. Run `python .github/scripts/check_nodes.py`. It must report 0 errors.
6. Open a pull request.

When `m2` has a release, use `m2 new <kind>` for step 2 and `m2 check` for step 5.

## Rules

1. Do not write a status level. The build computes it.
2. Do not copy text from a source that does not allow copies. Add a link and a locator. The LICENCE file names these sources.
3. Each node has one or more sources, unless it is a topic.
4. The statement section states one thing. Put a proof in a proof node. Put history in the history section.
5. Use only the LaTeX that KaTeX and MathJax can both show.
6. A link to another node is `[[text|TAG]]`. Do not link to a URL in the statement section.
7. Do not add `axiom` to the Lean package. A conditional result uses a named hypothesis in `lean/Math2/Hypotheses/`.
8. Do not use `sorry` or `native_decide` in the Lean package.

## Reviews

A fidelity review is a file in `reviews/`. You cannot review a binding that you wrote. A review is bound to the statement hash. If the statement changes, the review stops counting and the node goes back to the review queue.

## AI tools

You can use AI tools. You must say so in the pull request, and you must name the tool. You must check each statement, each source and each link yourself. You are responsible for the pull request, not the tool.

Agents open pull requests from a bot account. Each agent pull request links to its run record. A person reviews it before it merges.

## Licence of contributions

When you contribute, you agree that your contribution uses the licence of its path. The README has the table.
