# Contributing to math2

## What you can contribute

1. A new node: a concept, a definition, a statement, a proof, an example or a problem.
2. A change to a node: a better statement, a source, a link or an explanation.
3. A formal binding: a link from a statement to a Lean declaration.
4. A fidelity review: a check that a formal statement says the same thing as its informal statement.
5. A report of an error.

## Add a node

1. Make a branch from `main`.
2. Run `m2 new <kind>`, for example `m2 new statement`. It makes the file `nodes/~/~<8 hex characters>.md`. The name is a provisional id, for example `~3fa94c01`. Do not choose a tag. A maintainer gives the tag before merge.
3. Write the front matter and the body. Each field that has the value `null` needs a value. Use the example in the README.
4. Write each sentence on one line. Do not break a sentence across lines.
5. Link to a new node of the same pull request with its provisional id, for example `[[a group|~3fa94c01]]`. Do not link to a provisional id of a different pull request.
6. Run `m2 fmt` and `m2 check`. `m2 check` must report 0 findings. If you do not have `m2`, run `python .github/scripts/check_nodes.py`. It must report 0 errors.
7. Open a pull request. The `tags` check fails while the pull request has provisional ids. This is correct. The other checks must pass.

Install `m2` with `go install github.com/tamnd/math2-agent/cmd/m2@latest`. It needs Go 1.27 or later.

## Give the tags before merge

A maintainer does these steps after the review and before the merge:

1. In the Actions tab, run the `mint` workflow. Give the number of the pull request.
2. The workflow runs `m2 mint`. It changes each provisional id in the pull request to a new tag. It changes the file name, the front matter, each link and each Lean attribute. It adds each new tag to `registers/tags.reg`.
3. The workflow pushes one commit with the new tags to the branch of the pull request. Then it runs the checks on that commit.
4. When the `tags` check and the other checks pass, merge the pull request.

If the pull request comes from a fork, the workflow cannot push to it. Then the maintainer runs `m2 mint` on the branch and pushes the commit. This needs "Allow edits by maintainers" on the pull request:

```sh
gh pr checkout <number>
m2 mint
git add -A nodes registers
git commit -m "Give tags to the provisional ids"
git push
```

### Why the tags are given this way

These are the reasons for this decision (spec 04.3 and rule T03).

1. A tag is permanent. Thus the repository gives a tag only to a node that merges. A pull request that does not merge does not use a tag.
2. The tags are given before the merge, and not after it. Thus `main` never has a provisional id, and no commit on `main` changes a tag.
3. The tags are in a commit on the branch of the pull request. Thus the reviewer and the checks see the final files before the merge.
4. A maintainer starts the workflow. Thus the workflow runs one time, after the review. It does not run on each push of the author.
5. The `tags` check is a required check. Thus a pull request with a provisional id cannot merge.

## Rules

1. Do not write a status level. The build computes it.
2. Do not copy text from a source that does not allow copies. Add a link and a locator. The LICENCE file names these sources.
3. Each node has one or more sources, unless it is a topic.
4. The statement section states one thing. Put a proof in a proof node. Put history in the history section.
5. Use only the LaTeX that KaTeX and MathJax can both show, and the macros in `macros/m2.sty`.
6. A link to another node is `[[text|TAG]]`. Do not link to a URL in the statement section.
7. Do not add `axiom` to the Lean package. A conditional result uses a named hypothesis in `lean/Math2/Hypotheses/`.
8. Do not use `sorry` or `native_decide` in the Lean package.
9. In the Explanations section, start each explanation with a level 3 heading that gives the level, L1 to L4, and the reader, `human` or `agent`. An example is `### L2 human`. Do not write text before the first heading. Audit rule B05 checks this.

## Propose a macro

1. Make sure that KaTeX and MathJax do not already have the macro, and that `macros/m2.sty` does not have it.
2. Add one `\newcommand` line to `macros/m2.sty`. Write the full definition on one line.
3. Add the same macro with the same expansion to `macros/m2.katex.json`.
4. Run `python -m unittest discover -s .github/scripts`. The test compares the two files.
5. In the pull request, give one node that needs the macro.

Do not change the expansion of a macro that nodes use. Add a new macro.

## Reviews

A fidelity review is a file in `reviews/`. You cannot review a binding that you wrote. A review is bound to the statement hash. If the statement changes, the review stops counting and the node goes back to the review queue.

## AI tools

You can use AI tools. You must say so in the pull request, and you must name the tool. You must check each statement, each source and each link yourself. You are responsible for the pull request, not the tool.

Agents open pull requests from a bot account. Each agent pull request links to its run record. A person reviews it before it merges.

## Licence of contributions

When you contribute, you agree that your contribution uses the licence of its path. The README has the table.
