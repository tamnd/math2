---
records:
    - id: 8DA16QRB71
      kind: problem-set
      title: Kvant 2025, no. 2
      date: "2025"
      expressions:
        - key: e1
          kind: edition
          date: "2025"
          structure: 8DA16QRB71/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2025-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 8DATR785BJ
      kind: preprint
      title: Note on extensions of the beta function
      creators:
        - name: Mehar Chand
          role: author
      date: "2017-04-17"
      msc:
        - code: 26-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.CA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2017-04-17"
          ids:
            arxiv: "1704.08191"
            zbl_id: "900313824"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "1704.08191"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "1704.08191"
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "900313824"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
