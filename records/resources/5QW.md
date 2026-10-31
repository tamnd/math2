---
records:
    - id: 5QWC1BNZD9
      kind: problem-set
      title: Kvant 2006, no. 2
      date: "2006"
      expressions:
        - key: e1
          kind: edition
          date: "2006"
          structure: 5QWC1BNZD9/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2006-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 5QWPNXQ32J
      kind: preprint
      title: Asymptotic approximation of sensitivities in finite dimensional continuous data assimilation with application to parameter estimation
      creators:
        - name: Joshua Newey
          role: author
        - name: Jared P. Whitehead
          role: author
      date: "2026-10-02"
      subjects:
        - system: arxiv
          code: math.DS
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-02"
          ids:
            arxiv: "2610.02686"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.02686"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
